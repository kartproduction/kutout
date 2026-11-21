# ✂️ Kutout – Free Background Remover

**Kutout** removes image backgrounds in seconds. Free, no sign-up, and your photos never leave your device.

- 🌐 **Use online:** https://kartproduction.github.io/Kutout/
- 📱 **Android app:** [Download the latest APK](https://github.com/kartproduction/Kutout/releases/latest/download/Kutout.apk)
- 🍎 **iPhone:** open the website in Safari → Share → Add to Home Screen

## Features
- Touch-up brushes (erase/restore), before/after slider, paste support, batch processing
- Photo backgrounds with move/zoom, gradients, shadow and sticker outline
- Text layers (fonts, colors, shadow, behind-subject) for poster making
- Export PNG/JPG, crop to subject, Passport / Instagram / A4 poster sizes

## Old list
- AI background removal that runs fully on your device
- Transparent, solid color, gradient or your own photo as the background
- Download as PNG
- Works in any modern browser and as an Android app

## Install the APK
1. Download `Kutout.apk` from the link above.
2. Open it and allow "Install from unknown sources" if Android asks.

## For developers
1. Push these files to `main`. GitHub Pages serves `index.html`.
2. Settings → Actions → General → Workflow permissions → **Read and write**.
3. Actions → **Build APK** → Run workflow. It publishes `Kutout.apk` to Releases.

Built with [Capacitor](https://capacitorjs.com) and [@imgly/background-removal](https://github.com/imgly/background-removal-js).

## License
Copyright © 2026 Kart Production. The code is licensed under the **GNU AGPL-3.0** (see `LICENSE`). Any copy or modified version must stay open source under the same license, keep this copyright notice, and link to the source. See `NOTICE.txt` for the full terms.

The names **Kutout**, **Kart Production**, **Kasign**, **Kartory**, **Kalendar by Kasign**, **Kauncher**, **The Change Voice** and **Hope For A Change**, and their logos, may not be used for other projects without written permission. Forks must use a different name and branding.

Background removal powered by @imgly/background-removal (AGPL-3.0, © IMG.LY GmbH).

## Permanent signing key
Add secrets `KEYSTORE_BASE64`, `KEYSTORE_PASSWORD`, `KEY_ALIAS` (Settings → Secrets and variables → Actions). Builds then sign the APK and `Kutout.aab` (for Google Play) with the same key, so new versions install over old ones.

## Poster tools
Templates (Sale, Night event, Minimal, Birthday, YouTube), text layers with Google Fonts (online) and device fonts, logo/sticker layers, and **Save project / Open project** (`.json`) to keep editing later.
