#!/usr/bin/env python3
"""Capture the real Linux app through X11, without installing drivers or flashing.

Requires libX11, libXtst, and ImageMagick (import/convert).
Use --library-dir or --font-config for a temporary runtime/font setup.
All app settings, logs, and caches are isolated in --work-dir.
"""
import argparse
import ctypes as C
import os
from pathlib import Path
import re
import subprocess
import tempfile
import time

LOCALES = {'en': 'en', 'kr': 'ko', 'jp': 'ja', 'zh': 'zh',
           'zh-TW': 'tw', 'th': 'th', 'de': 'de'}


class X11:
    def __init__(self):
        self.x = C.CDLL('libX11.so.6')
        self.xt = C.CDLL('libXtst.so.6')
        self.x.XOpenDisplay.argtypes = [C.c_char_p]
        self.x.XOpenDisplay.restype = C.c_void_p
        self.d = self.x.XOpenDisplay(None)
        if not self.d:
            raise RuntimeError('Cannot connect to the X11 display.')
        self.x.XDefaultRootWindow.argtypes = [C.c_void_p]
        self.x.XDefaultRootWindow.restype = C.c_ulong
        self.root = self.x.XDefaultRootWindow(self.d)
        self.x.XTranslateCoordinates.argtypes = [C.c_void_p, C.c_ulong, C.c_ulong,
            C.c_int, C.c_int, C.POINTER(C.c_int), C.POINTER(C.c_int), C.POINTER(C.c_ulong)]
        self.x.XSetInputFocus.argtypes = [C.c_void_p, C.c_ulong, C.c_int, C.c_ulong]
        self.x.XRaiseWindow.argtypes = [C.c_void_p, C.c_ulong]
        self.x.XFlush.argtypes = [C.c_void_p]
        self.x.XCloseDisplay.argtypes = [C.c_void_p]
        self.x.XStringToKeysym.argtypes = [C.c_char_p]
        self.x.XStringToKeysym.restype = C.c_ulong
        self.x.XKeysymToKeycode.argtypes = [C.c_void_p, C.c_ulong]
        self.x.XKeysymToKeycode.restype = C.c_ubyte
        self.xt.XTestFakeKeyEvent.argtypes = [C.c_void_p, C.c_uint, C.c_int, C.c_ulong]
        self.xt.XTestFakeMotionEvent.argtypes = [C.c_void_p, C.c_int, C.c_int, C.c_int, C.c_ulong]
        self.xt.XTestFakeButtonEvent.argtypes = [C.c_void_p, C.c_uint, C.c_int, C.c_ulong]
        self.window = None

    def find_window(self, process):
        for _ in range(60):
            if process.poll() is not None:
                raise RuntimeError('Linux app exited before opening a window; inspect its capture log.')
            tree = subprocess.check_output(['xwininfo', '-root', '-tree'], text=True)
            for handle in re.findall(r'(0x[0-9a-f]+) "TOPST Imager v[^"\n]+"', tree):
                pid = subprocess.check_output(['xprop', '-id', handle, '_NET_WM_PID'], text=True)
                if re.search(r'=\s*' + str(process.pid) + r'\s*$', pid):
                    self.window = int(handle, 16)
                    time.sleep(1.2)
                    return
            time.sleep(.25)
        raise RuntimeError('Linux app window did not appear.')

    def click(self, x, y):
        self.x.XRaiseWindow(self.d, self.window)
        self.x.XSetInputFocus(self.d, self.window, 2, 0)
        xx, yy, child = C.c_int(), C.c_int(), C.c_ulong()
        self.x.XTranslateCoordinates(self.d, self.window, self.root, 0, 0,
                                    C.byref(xx), C.byref(yy), C.byref(child))
        self.xt.XTestFakeMotionEvent(self.d, -1, xx.value+x, yy.value+y, 0)
        self.xt.XTestFakeButtonEvent(self.d, 1, 1, 0)
        self.xt.XTestFakeButtonEvent(self.d, 1, 0, 0)
        self.x.XFlush(self.d)
        time.sleep(.6)

    def key(self, name):
        symbol = self.x.XStringToKeysym(name.encode())
        code = self.x.XKeysymToKeycode(self.d, symbol)
        self.xt.XTestFakeKeyEvent(self.d, code, 1, 0)
        self.xt.XTestFakeKeyEvent(self.d, code, 0, 0)
        self.x.XFlush(self.d)
        time.sleep(.2)

    def capture(self, raw):
        self.xt.XTestFakeMotionEvent(self.d, -1, 0, 0, 0)
        self.x.XFlush(self.d)
        time.sleep(.25)
        subprocess.run(['import', '-window', hex(self.window), str(raw)], check=True)


def color_bounds(raw, color, crop):
    x, y, w, h = crop
    geometry = '{}x{}+{}+{}'.format(w, h, x, y)
    result = subprocess.check_output(['convert', str(raw), '-crop', geometry,
        '+repage', '-alpha', 'off', '-fill', 'black', '+opaque', color,
        '-fill', 'white', '-opaque', color, '-morphology', 'Open', 'Square:2',
        '-trim', '-format', '%X %Y %w %h', 'info:'], text=True)
    dx, dy, width, height = map(int, result.split())
    if width < 70 or height < 20:
        raise RuntimeError('Expected a visible app control in '+str(raw)+': '+result)
    return x+dx, y+dy, width, height


def border_rows(raw, x, width, start, stop, minimum):
    # Read actual screenshot pixels only; the underlying UI is never redrawn.
    pixels = subprocess.check_output(['convert', str(raw), '-alpha', 'off',
        '-depth', '8', 'rgb:-'])
    stride = 910*3
    rows = []
    for y in range(start, stop):
        row = pixels[y*stride+x*3:y*stride+(x+width)*3]
        count = sum(row[i:i+3] == b'\xe5\xe5\xe5' for i in range(0,len(row),3))
        if count >= minimum:
            rows.append(y)
    if not rows:
        raise RuntimeError('Expected a bordered app control in '+str(raw))
    return rows


def annotate(raw, destination, boxes):
    if raw.name == 'TOPST Imager eMMC Erase Warning.png':
        # Read the actual dialog button bounds, which vary with translated text.
        bounds = subprocess.check_output(['convert', str(raw), '-alpha', 'off',
            '-fill', 'white', '+opaque', '#0078d4', '-fill', 'black', '-opaque',
            '#0078d4', '-trim', '-format', '%X %Y %w %h', 'info:'], text=True)
        cx, cy, cw, ch = map(int, bounds.split())
        if not (240 < cx < 670 and 300 < cy < 430 and cw > 100 and ch > 25):
            raise RuntimeError('Expected a real eMMC confirmation dialog: '+bounds)
        boxes = [(250,cy-2,cx-258,ch+4,1),(cx-2,cy-2,cw+4,ch+4,2)]
    if raw.name == 'TOPST Imager D3-G Boot Mode.png':
        sx, sy, sw, sh = color_bounds(raw, '#E8E8E8', (450,300,300,170))
        sx, sy, sw, sh = sx-1, sy-1, sw+2, sh+2
        cx = sx-118
        boxes = [(346,168,498,85,1),
                 (cx-2,sy-2,114,sh+4,2,cx-18,sy+sh//2),
                 (sx-2,sy-2,sw+4,sh+4,3,sx+sw+18,sy+sh//2)]
    if raw.name in ['TOPST Imager Custom FAI Image.png', 'TOPST Imager Custom ROM Image.png']:
        rows = border_rows(raw,344,503,150,420,400)
        top, bottom = rows[0], rows[-1]
        bx, by, bw, bh = color_bounds(raw, '#0078D4', (480,top+95,230,100))
        boxes = [(344,top,502,bottom-top,1),
                 (bx-2,by-2,bw+4,bh+4,2,bx-18,by+bh//2)]
    if raw.name == 'TOPST Imager VCP-G Boot Mode and COM Port.png':
        cx, cy, cw, ch = color_bounds(raw, '#E0E0E0', (340,270,510,130))
        rows = border_rows(raw,510,171,cy+ch+10,480,100)
        py, ph = rows[0], rows[-1]-rows[0]+1
        boxes = [(346,168,498,85,1), (cx-2,cy-2,cw+4,ch+4,2),
                 (cx+cw+4,cy-2,92,ch+4,3,cx+cw+112,cy+ch//2),
                 (490 if 'de' in raw.parts else 508,py-2,210 if 'de' in raw.parts else 174,ph+4,4,460,py+ph//2)]
    if raw.name == 'TOPST Imager AI-G Ethernet Setup.png':
        cx, cy, cw, ch = color_bounds(raw, '#E0E0E0', (340,160,510,120))
        boxes = [(cx-2,cy-2,cw+4,ch+4,1), (346,cy+ch+4,498,68,2),
                 (740,cy-2,104,ch+4,3,860,cy+ch//2)]
    args = ['convert', str(raw), '-stroke', '#e53935', '-strokewidth', '3', '-fill', 'none']
    for x, y, w, h, n, *badge in boxes:
        args += ['-draw', 'rectangle {},{} {},{}'.format(x, y, x+w, y+h)]
    # Render badges after every frame so red lines cannot obscure the digits.
    for x, y, w, h, n, *badge in boxes:
        bx, by = badge or [x, y]
        args += ['-stroke', 'none', '-fill', '#e53935', '-draw',
                 'circle {},{} {},{}'.format(bx, by, bx+15, by),
                 '-font', 'DejaVu-Sans-Bold', '-pointsize', '18', '-fill', 'white',
                 '-draw', "text {},{} '{}'".format(bx-6, by+6, n)]
    subprocess.run(args + [str(destination)], check=True)


def capture_locale(args, ui, work, locale):
    isolated = work / locale
    config = isolated / 'config' / 'Telechips'
    config.mkdir(parents=True, exist_ok=True)
    (config / 'TOPST Imager.conf').write_text('[ui]\nlanguage='+LOCALES[locale]+'\n')
    env = dict(os.environ, QT_QPA_PLATFORM='xcb', QT_QUICK_BACKEND='software',
               XDG_CONFIG_HOME=str(isolated/'config'), XDG_DATA_HOME=str(isolated/'data'),
               XDG_CACHE_HOME=str(isolated/'cache'))
    if args.library_dir:
        env['LD_LIBRARY_PATH'] = str(args.library_dir) + os.pathsep + env.get('LD_LIBRARY_PATH', '')
    if args.font_config:
        env['FONTCONFIG_FILE'] = str(args.font_config)
    output = args.output / locale / 'Linux'
    output.mkdir(parents=True, exist_ok=True)
    raw_dir = isolated / 'raw'
    raw_dir.mkdir(exist_ok=True)
    with (isolated/'app.log').open('w') as log:
        process = subprocess.Popen([str(args.app)], cwd=str(args.app.parent), env=env,
                                   stdout=log, stderr=subprocess.STDOUT)
        try:
            ui.find_window(process)
            def click(x, y): ui.click(x, y)
            def back(): click(710, 550)
            def next_page(): click(820, 550)
            def save(name, boxes):
                filename = 'TOPST Imager '+name+'.png'
                raw = raw_dir/filename
                ui.capture(raw)
                annotate(raw, output/filename, boxes)
                print(locale+' / Linux / '+name, flush=True)
            # Official D3-G image selection and its Linux boot guide.
            click(500, 140)
            save('Board Selection', [(330,100,530,88,1),(768,528,104,44,2)])
            next_page(); click(500,130)
            save('OS Selection', [(330,98,530,72,1),(330,332,530,58,2),(768,528,104,44,3)])
            next_page(); click(500,140)
            save('Version Selection', [(330,98,530,108,1),(768,528,104,44,2)])
            next_page()
            save('eMMC Erase Warning', [(250,353,190,44,1),(446,353,214,44,2)])
            click(550,375)
            save('D3-G Boot Mode', [(346,168,498,85,1),(469,385,114,38,2),(587,385,134,38,3)])
            # Return from setup without starting a download or flash operation.
            click(820,550); back()
            click(500,350); next_page()
            save('Custom FAI Image', [(344,171,502,179,1),(508,276,174,44,2,490,298)])
            back(); back()
            click(500,325); next_page(); click(500,205); next_page()
            save('Custom ROM Image', [(344,171,502,179,1),(508,276,174,44,2,490,298)])
            back(); click(500,130); next_page(); click(500,140); next_page(); click(550,375)
            save('VCP-G Boot Mode and COM Port', [(346,168,498,85,1),(346,312,404,38,2),(752,312,92,38,3),(508,374,174,38,4)])
            click(820,550); back(); back()
            click(500,230); next_page(); click(500,130); next_page(); click(500,140)
            next_page(); click(550,375)
            # Select eth0 in this WSL environment without changing network settings.
            click(500,210); ui.key('e'); ui.key('Return')
            save('AI-G Ethernet Setup', [(346,190,390,44,1),(346,236,498,68,2),(740,190,104,44,3)])
        finally:
            # Only terminate the process created by this capture job.
            process.terminate()
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--app', type=Path, default=Path('/home/ben/topst-imager/build/linux/topst-imager'))
    parser.add_argument('--output', type=Path,
        default=Path(__file__).resolve().parents[1]/'Assets/Quick Guide/TOPST Imager')
    parser.add_argument('--work-dir', type=Path)
    parser.add_argument('--library-dir', type=Path)
    parser.add_argument('--font-config', type=Path)
    parser.add_argument('--locales', nargs='+', choices=list(LOCALES), default=list(LOCALES))
    args = parser.parse_args()
    args.app = args.app.resolve()
    if not args.app.is_file():
        parser.error('Linux app binary does not exist: '+str(args.app))
    work = args.work_dir or Path(tempfile.mkdtemp(prefix='topst-linux-capture-'))
    work.mkdir(parents=True, exist_ok=True)
    ui = X11()
    try:
        for locale in args.locales:
            capture_locale(args, ui, work, locale)
    finally:
        ui.x.XCloseDisplay(ui.d)


if __name__ == '__main__':
    main()
