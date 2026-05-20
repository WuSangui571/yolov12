#!/usr/bin/env python3
"""Prepare RS-STOD split files for Ultralytics YOLO training.

The dataset already contains COCO train/val JSON files and a flat YOLO export:
RS-STOD/yolo/images/*.jpg and RS-STOD/yolo/labels/*.txt. Ultralytics can train
from txt image lists, so this script writes RS-STOD/train.txt and RS-STOD/val.txt
using the official COCO split while reusing the existing YOLO labels.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Iterable

CLASS_NAMES = {
    0: "Small Vehicle",
    1: "Large Vehicle",
    2: "Ship",
    3: "Airplane",
    4: "Storage Tank",
}


def load_coco_images(annotation_file: Path) -> list[str]:
    data = json.loads(annotation_file.read_text(encoding="utf-8"))
    return [Path(img["file_name"]).name for img in data["images"]]


def write_split(dataset_root: Path, split: str, names: Iterable[str]) -> None:
    lines = [f"./yolo/images/{name.replace(chr(92), '/')}" for name in sorted(names)]
    (dataset_root / f"{split}.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")


def validate_labels(dataset_root: Path) -> dict:
    image_dir = dataset_root / "yolo" / "images"
    label_dir = dataset_root / "yolo" / "labels"
    images = {p.stem for p in image_dir.glob("*.jpg")}
    labels = {p.stem for p in label_dir.glob("*.txt")}

    class_counts: Counter[int] = Counter()
    bad_labels: list[dict] = []
    boxes = 0
    for label_file in sorted(label_dir.glob("*.txt")):
        for line_no, line in enumerate(label_file.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            parts = line.split()
            if len(parts) != 5:
                bad_labels.append({"file": str(label_file), "line": line_no, "reason": "field_count", "value": line})
                continue
            try:
                cls = int(float(parts[0]))
                coords = [float(v) for v in parts[1:]]
            except ValueError:
                bad_labels.append({"file": str(label_file), "line": line_no, "reason": "parse", "value": line})
                continue
            if cls not in CLASS_NAMES or any(v < 0.0 or v > 1.0 for v in coords):
                bad_labels.append({"file": str(label_file), "line": line_no, "reason": "range", "value": line})
                continue
            class_counts[cls] += 1
            boxes += 1

    return {
        "images": len(images),
        "labels": len(labels),
        "boxes": boxes,
        "class_counts": {CLASS_NAMES[k]: class_counts[k] for k in sorted(CLASS_NAMES)},
        "images_without_labels": sorted(images - labels),
        "labels_without_images": sorted(labels - images),
        "bad_labels": bad_labels,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Prepare RS-STOD YOLO split txt files.")
    parser.add_argument("--root", default="RS-STOD", help="RS-STOD dataset root")
    args = parser.parse_args()

    root = Path(args.root)
    ann_dir = root / "coco" / "annotations"
    train_names = load_coco_images(ann_dir / "train.json")
    val_names = load_coco_images(ann_dir / "val.json")

    image_dir = root / "yolo" / "images"
    label_dir = root / "yolo" / "labels"
    missing = []
    for name in train_names + val_names:
        stem = Path(name).stem
        if not (image_dir / name).exists():
            missing.append(f"image:{name}")
        if not (label_dir / f"{stem}.txt").exists():
            missing.append(f"label:{stem}.txt")
    if missing:
        sample = ", ".join(missing[:10])
        raise FileNotFoundError(f"Missing YOLO files for COCO split ({len(missing)} total): {sample}")

    write_split(root, "train", train_names)
    write_split(root, "val", val_names)

    summary = validate_labels(root)
    summary.update(
        {
            "train_images": len(train_names),
            "val_images": len(val_names),
            "classes": CLASS_NAMES,
            "split_files": [str(root / "train.txt"), str(root / "val.txt")],
        }
    )
    (root / "rs_stod_summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
