param(
 [string]$ApplicationPath = 'D:\topst-imager\dist\TOPST Imager.exe',
 [string]$OutputDirectory = (Join-Path $PSScriptRoot '..\Assets\Quick Guide\TOPST Imager'),
 [string]$LabelsPath = (Join-Path $PSScriptRoot 'topst-imager-ui-labels.json'),
 [string[]]$Locales = @('en','kr','jp','zh','zh-TW','th','de'),
 [string]$RawDirectory = ''
)
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName UIAutomationClient
Add-Type -AssemblyName UIAutomationTypes
Add-Type -AssemblyName System.Drawing
Add-Type -AssemblyName System.Windows.Forms
Add-Type @'
using System;
using System.Runtime.InteropServices;
public class ImagerCaptureNative {
 [StructLayout(LayoutKind.Sequential)] public struct RECT { public int Left,Top,Right,Bottom; }
 [StructLayout(LayoutKind.Sequential)] public struct POINT { public int X,Y; }
 [DllImport("user32.dll")] public static extern bool SetProcessDPIAware();
 [DllImport("user32.dll")] public static extern bool PrintWindow(IntPtr h, IntPtr dc, uint flags);
 [DllImport("user32.dll")] public static extern bool ShowWindow(IntPtr h,int cmd);
 [DllImport("user32.dll")] public static extern bool SetWindowPos(IntPtr h,IntPtr after,int x,int y,int w,int ht,uint flags);
 [DllImport("user32.dll")] public static extern bool GetClientRect(IntPtr h,out RECT r);
 [DllImport("user32.dll")] public static extern bool ClientToScreen(IntPtr h,ref POINT p);
 [DllImport("user32.dll")] public static extern bool SetForegroundWindow(IntPtr h);
 [DllImport("user32.dll")] public static extern bool MoveWindow(IntPtr h,int x,int y,int w,int ht,bool repaint);
 [DllImport("user32.dll")] public static extern bool SetCursorPos(int x,int y);
 [DllImport("user32.dll")] public static extern void mouse_event(uint f,uint x,uint y,uint d,UIntPtr extra);
}
'@
[ImagerCaptureNative]::SetProcessDPIAware() | Out-Null
function Click($x,$y) {
 $r=New-Object ImagerCaptureNative+RECT
 [ImagerCaptureNative]::GetClientRect($script:window,[ref]$r)|Out-Null
 $p=New-Object ImagerCaptureNative+POINT
 $p.X=[int]($x*$r.Right/910); $p.Y=[int]($y*$r.Bottom/610)
 [ImagerCaptureNative]::ClientToScreen($script:window,[ref]$p)|Out-Null
 [ImagerCaptureNative]::SetCursorPos($p.X,$p.Y)|Out-Null
 [ImagerCaptureNative]::mouse_event(2,0,0,0,[UIntPtr]::Zero)
 [ImagerCaptureNative]::mouse_event(4,0,0,0,[UIntPtr]::Zero)
 Start-Sleep -Milliseconds 400
}
function Capture($path, $boxes) {
 $r=New-Object ImagerCaptureNative+RECT
 [ImagerCaptureNative]::GetClientRect($script:window,[ref]$r)|Out-Null
 $p=New-Object ImagerCaptureNative+POINT
 [ImagerCaptureNative]::ClientToScreen($script:window,[ref]$p)|Out-Null
 [ImagerCaptureNative]::SetCursorPos(0,0)|Out-Null
 Start-Sleep -Milliseconds 250
 $bmp=New-Object Drawing.Bitmap($r.Right,$r.Bottom)
 $g=[Drawing.Graphics]::FromImage($bmp)
 $dc=$g.GetHdc()
 $ok=[ImagerCaptureNative]::PrintWindow($script:window,$dc,3)
 $g.ReleaseHdc($dc)
 if(-not $ok){throw "PrintWindow failed"}
 if($RawDirectory){
  $rawLocale=Join-Path $RawDirectory $script:locale
  New-Item -ItemType Directory -Path $rawLocale -Force|Out-Null
  $bmp.Save((Join-Path $rawLocale (Split-Path $path -Leaf)),[Drawing.Imaging.ImageFormat]::Png)
 }
 $g.SmoothingMode=[Drawing.Drawing2D.SmoothingMode]::AntiAlias
 $pen=New-Object Drawing.Pen([Drawing.Color]::FromArgb(229,57,53),3)
 $red=New-Object Drawing.SolidBrush([Drawing.Color]::FromArgb(229,57,53))
 $font=New-Object Drawing.Font('Arial',13,[Drawing.FontStyle]::Bold)
 $format=New-Object Drawing.StringFormat
 $format.Alignment=[Drawing.StringAlignment]::Center
 $format.LineAlignment=[Drawing.StringAlignment]::Center
 foreach($box in $boxes){$g.DrawRectangle($pen,[single]$box.x,[single]$box.y,[single]$box.w,[single]$box.h)}
 # Draw badges after every rectangle so highlight lines cannot obscure digits.
 foreach($box in $boxes){
  $badge=New-Object Drawing.RectangleF(([single]$box.x-15),([single]$box.y-15),30,30)
  $g.FillEllipse($red,$badge)
  $g.DrawString([string]$box.n,$font,[Drawing.Brushes]::White,$badge,$format)
 }
 $bmp.Save($path,[Drawing.Imaging.ImageFormat]::Png)
 $pen.Dispose();$red.Dispose();$font.Dispose();$format.Dispose()
 $g.Dispose();$bmp.Dispose()
}


function Button($key) {
 $text=$script:labels.$key
 if(-not $text){throw "Missing translation key $key"}
 $root=[Windows.Automation.AutomationElement]::FromHandle($script:window)
 $elements=$root.FindAll([Windows.Automation.TreeScope]::Descendants,[Windows.Automation.Condition]::TrueCondition)
 foreach($element in $elements){
  $name=$element.Current.Name
  if(($name -eq $text -or $name.StartsWith($text+' ')) -and $element.Current.BoundingRectangle.Width -gt 0){return $element}
 }
 throw "Visible control not found: $key ($text)"
}
function Box($x,$y,$w,$h,$n){return @{x=$x;y=$y;w=$w;h=$h;n=$n}}
function ButtonBox($key,$n) {
 $r=(Button $key).Current.BoundingRectangle
 $origin=New-Object ImagerCaptureNative+POINT
 [ImagerCaptureNative]::ClientToScreen($script:window,[ref]$origin)|Out-Null
 $padding=2
 if($script:locale -eq 'de' -and $key -eq 'driverComplete'){$padding=12}
 return (Box ($r.X-$origin.X-$padding) ($r.Y-$origin.Y-2) ($r.Width+2*$padding) ($r.Height+4) $n)
}
function ClickButton($key) {
 $b=ButtonBox $key 0
 Click ($b.x+$b.w/2) ($b.y+$b.h/2)
}
function SaveScreen($name,$boxes) {
 $path=Join-Path $script:localeOutput ("TOPST Imager $name.png")
 Capture $path $boxes
 Write-Output "$script:locale / $name"
}
$allLabels=Get-Content -Raw -Encoding UTF8 $LabelsPath|ConvertFrom-Json
$registryPath='HKCU:\Software\Telechips\TOPST Imager\ui'
$previous=(Get-ItemProperty -Path $registryPath -Name language -ErrorAction SilentlyContinue).language
$env:QT_QUICK_BACKEND='software'
$app=$null
try {
 foreach($entry in @(@('en','en'),@('kr','ko'),@('jp','ja'),@('zh','zh'),@('zh-TW','tw'),@('th','th'),@('de','de'))) {
  if($entry[0] -notin $Locales){continue}
  $script:locale=$entry[0]; $appLanguage=$entry[1]
  $script:labels=$allLabels.$appLanguage
  New-Item -Path $registryPath -Force|Out-Null
  Set-ItemProperty -Path $registryPath -Name language -Value $appLanguage
  $script:localeOutput=Join-Path $OutputDirectory $script:locale
  New-Item -ItemType Directory -Path $script:localeOutput -Force|Out-Null
  $app=Start-Process -FilePath $ApplicationPath -WorkingDirectory (Split-Path $ApplicationPath) -PassThru
  Start-Sleep -Seconds 3
  $app.Refresh();$script:window=$app.MainWindowHandle
  if($script:window -eq 0){throw 'TOPST Imager window not found'}
  [ImagerCaptureNative]::ShowWindow($script:window,9)|Out-Null
  [ImagerCaptureNative]::SetWindowPos($script:window,[IntPtr](-1),40,40,926,649,0x40)|Out-Null
  [ImagerCaptureNative]::SetForegroundWindow($script:window)|Out-Null
  Start-Sleep -Milliseconds 500
  ClickButton 'options'
  SaveScreen 'App Options' @((Box 290 210 330 42 1),(ButtonBox 'openUserGuide' 2),(ButtonBox 'askCommunity' 3),(ButtonBox 'save' 4))
  ClickButton 'cancel'
  Click 500 140
  SaveScreen 'Board Selection' @((Box 330 102 530 88 1),(ButtonBox 'next' 2))
  ClickButton 'next'
  Click 500 130
  SaveScreen 'OS Selection' @((Box 330 102 530 72 1),(Box 330 340 530 52 2),(ButtonBox 'next' 3))
  ClickButton 'next'
  Click 500 150
  SaveScreen 'Version Selection' @((Box 330 102 530 108 1),(ButtonBox 'write' 2))
  ClickButton 'write'
  SaveScreen 'eMMC Erase Warning' @((Box 250 359 190 44 1),(Box 446 359 214 44 2))
  Click 550 380
  SaveScreen 'D3-G Driver Installation' @((ButtonBox 'installDriver' 1),(ButtonBox 'driverComplete' 2))
  # This only advances the guide; never run the driver installer or flash button.
  ClickButton 'driverComplete'
  SaveScreen 'D3-G Boot Mode' @((Box 344 170 500 87 1),(ButtonBox 'checkAgain' 2),(ButtonBox 'startFlash' 3))
  $app.CloseMainWindow()|Out-Null
  if(-not $app.WaitForExit(4000)){$app.Kill();$app.WaitForExit()}
  $app=$null
 }
} finally {
 if($app -and -not $app.HasExited){$app.CloseMainWindow()|Out-Null;if(-not $app.WaitForExit(2000)){$app.Kill()}}
 if($null -ne $previous){Set-ItemProperty -Path $registryPath -Name language -Value $previous}
 elseif(Test-Path $registryPath){Remove-ItemProperty -Path $registryPath -Name language -ErrorAction SilentlyContinue}
}
