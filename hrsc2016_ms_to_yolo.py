from __future__ import annotations

import argparse
import os
import shutil
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Iterable

SPLITS = ("train", "val", "test")
CLASS_NAMES = {0: "ship"}


def _safe_float(text: str | None, default: float = 0.0) -> float:
    return float(text) if text is not None else default


def _safe_int(text: str | None, default: int = 0) -> int:
    return int(float(text)) if text is not None else default


def _link_or_copy(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        return
    try:
        os.link(src, dst)
    except OSError:
        shutil.copy2(src, dst)


def _convert_box(width: int, height: int, xmin: float, ymin: float, xmax: float, ymax: float) -> tuple[float, float, float, float]:
    x_center = ((xmin + xmax) / 2.0) / width
    y_center = ((ymin + ymax) / 2.0) / height
    box_width = (xmax - xmin) / width
    box_height = (ymax - ymin) / height
    return x_center, y_center, box_width, box_height


def _parse_annotation(xml_file: Path) -> tuple[int, int, list[str]]:
    root = ET.parse(xml_file).getroot()
    size = root.find("size")
    if size is None:
        raise ValueError(f"Missing <size> in {xml_file}")

    width = _safe_int(size.findtext("width"))
    height = _safe_int(size.findtext("height"))
    if width <= 0 or height <= 0:
        raise ValueError(f"Invalid image size in {xml_file}")

    lines: list[str] = []
    for obj in root.findall("object"):
        difficult = _safe_int(obj.findtext("difficult"))
        if difficult not in (0, 1):
            difficult = 0

        bndbox = obj.find("bndbox")
        if bndbox is None:
            continue

        xmin = _safe_float(bndbox.findtext("xmin"))
        ymin = _safe_float(bndbox.findtext("ymin"))
        xmax = _safe_float(bndbox.findtext("xmax"))
        ymax = _safe_float(bndbox.findtext("ymax"))
        if xmax <= xmin or ymax <= ymin:
            continue

        x_center, y_center, box_width, box_height = _convert_box(width, height, xmin, ymin, xmax, ymax)
        lines.append(f"0 {x_center:.6f} {y_center:.6f} {box_width:.6f} {box_height:.6f}")

    return width, height, lines


def _read_split_ids(split_file: Path) -> list[str]:
    return [line.strip() for line in split_file.read_text(encoding="utf-8").splitlines() if line.strip()]


def convert_hrsc2016_ms(dataset_root: str | Path, splits: Iterable[str] = SPLITS) -> dict[str, int]:
    dataset_root = Path(dataset_root)
    images_root = dataset_root / "AllImages"
    annotations_root = dataset_root / "Annotations"
    image_sets_root = dataset_root / "ImageSets"

    if not images_root.exists() or not annotations_root.exists() or not image_sets_root.exists():
        raise FileNotFoundError(f"HRSC2016-MS structure not found under: {dataset_root}")

    summary: dict[str, int] = {}
    for split in splits:
        split_ids = _read_split_ids(image_sets_root / f"{split}.txt")
        out_images = dataset_root / "images" / split
        out_labels = dataset_root / "labels" / split
        out_images.mkdir(parents=True, exist_ok=True)
        out_labels.mkdir(parents=True, exist_ok=True)

        converted = 0
        for image_id in split_ids:
            src_image = images_root / f"{image_id}.bmp"
            src_xml = annotations_root / f"{image_id}.xml"
            if not src_image.exists():
                raise FileNotFoundError(f"Missing image file: {src_image}")
            if not src_xml.exists():
                raise FileNotFoundError(f"Missing annotation file: {src_xml}")

            _, _, lines = _parse_annotation(src_xml)
            _link_or_copy(src_image, out_images / src_image.name)
            (out_labels / f"{image_id}.txt").write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")
            converted += 1

        summary[split] = converted

    return summary


def build_argparser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Convert HRSC2016-MS into YOLO detect format.")
    parser.add_argument("--dataset-root", default="HRSC2016-MS", help="Path to the HRSC2016-MS dataset root.")
    parser.add_argument("--split", action="append", dest="splits", help="Optional split to convert. Repeat to include multiple.")
    return parser


def main() -> int:
    args = build_argparser().parse_args()
    splits = tuple(args.splits) if args.splits else SPLITS
    summary = convert_hrsc2016_ms(args.dataset_root, splits=splits)
    converted = sum(summary.values())
    if not converted:
        print(f"No HRSC2016-MS samples converted under: {Path(args.dataset_root).resolve()}")
        return 1

    detail = ", ".join(f"{name}={count}" for name, count in summary.items())
    print(f"Converted {converted} HRSC2016-MS samples under: {Path(args.dataset_root).resolve()} ({detail})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
