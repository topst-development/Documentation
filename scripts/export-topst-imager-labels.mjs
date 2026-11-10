// Export the exact UI strings used by the application for capture and Docs checks.
// Usage: node scripts/export-topst-imager-labels.mjs /path/to/qml/Translations.js
import fs from 'node:fs';
import vm from 'node:vm';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const source = process.argv[2];
if (!source) throw new Error('Pass the app qml/Translations.js path.');
const context = vm.createContext({});
vm.runInContext(fs.readFileSync(source, 'utf8').replace(/^\.pragma library\s*$/m, ''), context);
const keys = [
  'options', 'openUserGuide', 'askCommunity', 'language', 'save', 'cancel',
  'next', 'back', 'selected', 'useCustom', 'write', 'flash', 'flashing',
  'complete', 'installDriver', 'driverComplete', 'checkAgain', 'startFlash',
  'download', 'extract', 'confirm', 'configurePermissions', 'onlineDownload',
  'minimum', 'spaceRequired', 'release', 'findFai', 'findRom', 'customImage', 'refresh',
];
const labels = {};
for (const language of ['ko', 'en', 'ja', 'zh', 'tw', 'th', 'de']) {
  labels[language] = {};
  for (const key of keys) {
    const label = context.text(language, key);
    if (!label || label === key) throw new Error(`Missing translation: ${language}/${key}`);
    labels[language][key] = label;
  }
}
const destination = path.join(path.dirname(fileURLToPath(import.meta.url)), 'topst-imager-ui-labels.json');
fs.writeFileSync(destination, JSON.stringify(labels, null, 2) + '\n');
console.log(destination);
