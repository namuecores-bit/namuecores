#!/usr/bin/env python3
"""
Downloads 폴더의 파일들을 확장자별로 하위 폴더로 이동합니다.

- *.jpg, *.jpeg -> images
- *.csv, *.xlsx -> data
- *.txt, *.doc, *.pdf -> docs
- *.zip -> archive

대상 폴더가 없으면 생성합니다.
"""

from pathlib import Path
import shutil

DOWNLOADS = Path(r"C:\Users\student\Downloads")

EXT_MAP = {
    "jpg": "images",
    "jpeg": "images",
    "csv": "data",
    "xlsx": "data",
    "txt": "docs",
    "doc": "docs",
    "pdf": "docs",
    "zip": "archive",
}

def ensure_unique(target: Path) -> Path:
    if not target.exists():
        return target
    stem = target.stem
    suffix = target.suffix
    parent = target.parent
    i = 1
    while True:
        new_name = f"{stem}_{i}{suffix}"
        new_target = parent / new_name
        if not new_target.exists():
            return new_target
        i += 1

def organize(dry_run: bool = False):
    if not DOWNLOADS.exists():
        print(f"다운로드 폴더가 없습니다: {DOWNLOADS}")
        return []

    moved = []
    for p in DOWNLOADS.iterdir():
        if not p.is_file():
            continue
        ext = p.suffix.lower().lstrip('.')
        folder = EXT_MAP.get(ext)
        if not folder:
            continue
        dest_dir = DOWNLOADS / folder
        dest_dir.mkdir(parents=True, exist_ok=True)
        target = dest_dir / p.name
        target = ensure_unique(target)
        if dry_run:
            print(f"[DRY] {p.name} -> {target}")
        else:
            shutil.move(str(p), str(target))
            moved.append((p.name, str(target)))
            print(f"Moved: {p.name} -> {target}")

    print(f"\n완료: 총 {len(moved)}개 파일 이동됨.")
    return moved


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Organize Downloads files by extension")
    parser.add_argument("--dry-run", action="store_true", help="시뮬레이션 모드 (파일을 실제로 이동하지 않음)")
    args = parser.parse_args()
    organize(dry_run=args.dry_run)
