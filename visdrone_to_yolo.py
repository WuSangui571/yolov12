from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable

from PIL import Image

DEFAULT_SPLITS = (
    "VisDrone2019-DET-train",
    "VisDrone2019-DET-val",
    "VisDrone2019-DET-test-dev",
)


def _convert_box(image_size: tuple[int, int], box: tuple[int, int, int, int]) -> tuple[float, float, float, float]:
    """Convert a VisDrone xywh box into normalized YOLO xywh format."""
    width, height = image_size
    x, y, w, h = box
    return ((x + w / 2) / width, (y + h / 2) / height, w / width, h / height)


def convert_visdrone_split(split_dir: str | Path) -> list[Path]:
    """Convert one VisDrone split directory from `annotations/` to YOLO `labels/`."""
    split_dir = Path(split_dir)
    images_dir = split_dir / "images"
    annotations_dir = split_dir / "annotations"
    labels_dir = split_dir / "labels"

    if not annotations_dir.exists():
        raise FileNotFoundError(f"Annotations directory not found: {annotations_dir}")
    if not images_dir.exists():
        raise FileNotFoundError(f"Images directory not found: {images_dir}")

    labels_dir.mkdir(parents=True, exist_ok=True)
    created_files: list[Path] = []

    for annotation_file in sorted(annotations_dir.glob("*.txt")):
        image_file = images_dir / f"{annotation_file.stem}.jpg"
        if not image_file.exists():
            raise FileNotFoundError(f"Matching image not found for {annotation_file.name}: {image_file}")

        image_size = Image.open(image_file).size
        lines: list[str] = []
        rows = annotation_file.read_text(encoding="utf-8").splitlines()

        for row in rows:
            if not row.strip():
                continue
            parts = [part.strip() for part in row.split(",")]
            if len(parts) < 6:
                raise ValueError(f"Invalid annotation row in {annotation_file}: {row}")
            if parts[4] == "0":  # ignored regions
                continue

            cls = int(parts[5]) - 1
            box = _convert_box(image_size, tuple(map(int, parts[:4])))
            lines.append(f"{cls} {' '.join(f'{value:.6f}' for value in box)}")

        label_file = labels_dir / annotation_file.name
        label_file.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")
        created_files.append(label_file)

    return created_files


def convert_visdrone(dataset_root: str | Path, splits: Iterable[str] | None = None) -> list[Path]:
    """Convert all available VisDrone splits under a dataset root."""
    dataset_root = Path(dataset_root)
    if not dataset_root.exists():
        raise FileNotFoundError(f"Dataset root not found: {dataset_root}")

    split_names = tuple(splits) if splits is not None else DEFAULT_SPLITS
    created_files: list[Path] = []

    for split_name in split_names:
        split_dir = dataset_root / split_name
        annotations_dir = split_dir / "annotations"
        images_dir = split_dir / "images"
        if not split_dir.exists():
            continue
        if not annotations_dir.exists() or not images_dir.exists():
            continue
        created_files.extend(convert_visdrone_split(split_dir))

    return created_files


def build_argparser() -> argparse.ArgumentParser:
    """Build the CLI parser for one-click conversion."""
    parser = argparse.ArgumentParser(description="Convert VisDrone2019 annotations to YOLO label format.")
    parser.add_argument(
        "--dataset-root",
        default="VisDrone2019",
        help="Path to the VisDrone2019 dataset root. Defaults to ./VisDrone2019",
    )
    parser.add_argument(
        "--split",
        action="append",
        dest="splits",
        help="Optional split name to convert. Repeat this flag to convert multiple splits.",
    )
    return parser


def main() -> int:
    """CLI entry point."""
    args = build_argparser().parse_args()
    created = convert_visdrone(args.dataset_root, splits=args.splits)
    if not created:
        print(f"No convertible VisDrone splits found under: {Path(args.dataset_root).resolve()}")
        return 1

    print(f"Converted {len(created)} label files under: {Path(args.dataset_root).resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
