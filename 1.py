#!/usr/bin/env python3
# rebrand.py — ری‌برندینگ jellyfin-web → padzanij-web

import os
import re
from pathlib import Path

# —————————————————————————————————————————————
# تنظیمات
EXCLUDE_DIRS = {'.git', 'node_modules', 'dist', 'build', '__pycache__'}
TEXT_EXTS = {'.js', '.jsx', '.ts', '.tsx', '.html', '.md', '.json', '.mjs'}

# —————————————————————————————————————————————
# الگوهای regex
PAT_UPPER = re.compile(r'(?<!@)Jellyfin')
PAT_LOWER = re.compile(r'(?<!@)jellyfin')

def should_skip(path: Path) -> bool:
    """
    اگر مسیر شامل یکی از فولدرهای EXCLUDE_DIRS باشه، نادیده گرفته بشه.
    """
    # path.resolve().parts برمی‌گردونه لیستی از رشته‌ها
    return any(part in EXCLUDE_DIRS for part in path.resolve().parts)

# —————————————————————————————————————————————
# ۱) تغییر نام فایل‌ها و پوشه‌ها
print("🔄 مرحله ۱: تغییر نام فایل‌ها و پوشه‌ها …")
for root, dirs, files in os.walk('.', topdown=False):
    root_path = Path(root)
    if should_skip(root_path):
        continue

    # تغییر نام فایل‌ها
    for fname in files:
        if 'jellyfin' in fname:
            src = root_path / fname
            dst = root_path / fname.replace('jellyfin', 'padzanij')
            print(f"  ✏️  {src} → {dst}")
            src.rename(dst)

    # تغییر نام پوشه‌ها
    for dname in dirs:
        if dname in EXCLUDE_DIRS or 'jellyfin' not in dname:
            continue
        src = root_path / dname
        dst = root_path / dname.replace('jellyfin', 'padzanij')
        print(f"  📂  {src} → {dst}")
        src.rename(dst)


# —————————————————————————————————————————————
# ۲) ویرایش درون فایل‌های متنی
print("🔄 مرحله ۲: ویرایش محتوای درون فایل‌ها …")
for root, dirs, files in os.walk('.', topdown=True):
    root_path = Path(root)
    # حذف پوشه‌های exclude از پیمایش
    dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

    for fname in files:
        path = root_path / fname
        if path.suffix.lower() not in TEXT_EXTS:
            continue

        text = path.read_text(encoding='utf-8')
        new_text = PAT_UPPER.sub('Padzanij', text)
        new_text = PAT_LOWER.sub('padzanij', new_text)

        if new_text != text:
            print(f"  📝 ویرایش {path}")
            path.write_text(new_text, encoding='utf-8')

print("✅ تمام شد! حالا:\n  1. `npm install` و `npm run build` رو اجرا کن\n  2. تست کن که همه چیز اوکی باشه\n  3. کامیت و پوش:\n     git add . && git commit -m \"Rebrand jellyfin-web to padzanij-web\" && git push")
