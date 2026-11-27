#!/usr/bin/env bash
# Builds the offline files into www/: the AI model (www/models) and the background-removal library (www/vendor/rb.js).
# If anything here fails, the site and app still work: they fall back to loading these from the internet.
set -e
mkdir -p www/models www/vendor
npm i --no-save @imgly/background-removal@1.5.5 @imgly/background-removal-data@1.5.5 esbuild
cp -r node_modules/@imgly/background-removal-data/dist/. www/models/
echo "export { removeBackground } from '@imgly/background-removal';" > rb-entry.mjs
npx esbuild rb-entry.mjs --bundle --format=esm --platform=browser --minify --outfile=www/vendor/rb.js
ls -la www/models | head -5
echo "Offline files ready"
