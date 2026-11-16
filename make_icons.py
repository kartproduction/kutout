"""Builds Android launcher icons from assets/*.png into the generated android project.
Fails loudly if anything is missing, so the build never silently ships the default icon."""
import os, sys
from PIL import Image, ImageDraw

RES = 'android/app/src/main/res'
for f in ('icon-only', 'icon-foreground', 'icon-background'):
    if not os.path.exists(f'assets/{f}.png'):
        sys.exit(f'MISSING assets/{f}.png - upload the assets folder')
if not os.path.isdir(RES):
    sys.exit('android project not found - run after "npx cap add android"')

full = Image.open('assets/icon-only.png').convert('RGBA')
fg = Image.open('assets/icon-foreground.png').convert('RGBA')
bg = Image.open('assets/icon-background.png').convert('RGBA')

def shaped(im, size, circle=False):
    im = im.resize((size, size), Image.LANCZOS).convert('RGBA')
    m = Image.new('L', (size * 4, size * 4), 0)
    d = ImageDraw.Draw(m)
    if circle: d.ellipse([0, 0, size * 4 - 1, size * 4 - 1], fill=255)
    else: d.rounded_rectangle([0, 0, size * 4 - 1, size * 4 - 1], radius=int(size * 4 * .22), fill=255)
    im.putalpha(m.resize((size, size), Image.LANCZOS))
    return im

legacy = {'mdpi': 48, 'hdpi': 72, 'xhdpi': 96, 'xxhdpi': 144, 'xxxhdpi': 192}
adaptive = {'mdpi': 108, 'hdpi': 162, 'xhdpi': 216, 'xxhdpi': 324, 'xxxhdpi': 432}
for dpi in legacy:
    d = f'{RES}/mipmap-{dpi}'
    os.makedirs(d, exist_ok=True)
    shaped(full, legacy[dpi]).save(f'{d}/ic_launcher.png')
    shaped(full, legacy[dpi], True).save(f'{d}/ic_launcher_round.png')
    fg.resize((adaptive[dpi],) * 2, Image.LANCZOS).save(f'{d}/ic_launcher_foreground.png')
    bg.resize((adaptive[dpi],) * 2, Image.LANCZOS).save(f'{d}/ic_launcher_background.png')

xml = '''<?xml version="1.0" encoding="utf-8"?>
<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">
    <background android:drawable="@mipmap/ic_launcher_background"/>
    <foreground android:drawable="@mipmap/ic_launcher_foreground"/>
</adaptive-icon>
'''
os.makedirs(f'{RES}/mipmap-anydpi-v26', exist_ok=True)
for n in ('ic_launcher', 'ic_launcher_round'):
    open(f'{RES}/mipmap-anydpi-v26/{n}.xml', 'w').write(xml)

# remove the default Capacitor vector icon layers so nothing can fall back to them
for p in (f'{RES}/drawable-v24/ic_launcher_foreground.xml', f'{RES}/drawable/ic_launcher_background.xml'):
    if os.path.exists(p): os.remove(p)
print('Kutout icons written to', RES)
