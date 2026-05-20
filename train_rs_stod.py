#!/usr/bin/env python3
"""Cross-platform training helper for RS-STOD with YOLOv12-DMMA-ECA-P2."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
DEFAULT_MODEL = "ultralytics/cfg/models/v12/yolov12-dmma-p2-advanced.yaml"
DEFAULT_DATA = "data/rs_stod.yaml"
DEFAULT_SOURCE = "RS-STOD/yolo/images"


def norm_path(value: str | Path) -> str:
    return str(Path(value))


def parse_device(value: str | int | None) -> str | int:
    if value is None:
        return 0
    text = str(value).strip()
    if not text:
        return 0
    if text.isdigit():
        return int(text)
    return text


def train_params(args: argparse.Namespace, device: str | int) -> dict[str, Any]:
    return {
        "epochs": args.epochs,
        "batch": args.batch,
        "imgsz": args.imgsz,
        "device": device,
        "optimizer": "AdamW",
        "lr0": args.lr0,
        "lrf": 0.01,
        "momentum": 0.937,
        "weight_decay": 0.05,
        "warmup_epochs": args.warmup_epochs,
        "warmup_momentum": 0.8,
        "box": 10.0,
        "cls": 0.5,
        "dfl": 1.5,
        "mosaic": args.mosaic,
        "mixup": args.mixup,
        "copy_paste": args.copy_paste,
        "scale": args.scale,
        "degrees": args.degrees,
        "translate": 0.15,
        "shear": 5.0,
        "flipud": 0.5,
        "fliplr": 0.5,
        "hsv_h": 0.02,
        "hsv_s": 0.8,
        "hsv_v": 0.5,
        "erasing": 0.4,
        "close_mosaic": args.close_mosaic,
        "patience": args.patience,
        "save_period": args.save_period,
        "amp": True,
        "workers": args.workers,
        "cache": args.cache,
        "cos_lr": True,
        "iou": 0.5,
        "max_det": 1000,
        "project": args.project,
        "name": args.name,
        "exist_ok": args.exist_ok,
        "verbose": True,
    }


def metrics_summary(metrics: Any) -> dict[str, Any]:
    summary = {k: float(v) for k, v in metrics.results_dict.items()}
    per_class = []
    names = getattr(metrics, "names", {})
    for i, cls_id in enumerate(metrics.ap_class_index):
        p, r, map50, map5095 = metrics.class_result(i)
        cls_id = int(cls_id)
        per_class.append(
            {
                "class_id": cls_id,
                "name": names.get(cls_id, str(cls_id)) if isinstance(names, dict) else str(cls_id),
                "precision": float(p),
                "recall": float(r),
                "mAP50": float(map50),
                "mAP50-95": float(map5095),
            }
        )
    summary["per_class"] = per_class
    summary["save_dir"] = str(metrics.save_dir)
    return summary


def save_metrics(metrics: Any, filename: str = "metrics_summary.json") -> Path:
    out = Path(metrics.save_dir) / filename
    out.write_text(json.dumps(metrics_summary(metrics), indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Metrics summary: {out}")
    return out


def train(args: argparse.Namespace, device: str | int) -> None:
    from ultralytics import YOLO

    model = YOLO(norm_path(args.model))
    results = model.train(data=norm_path(args.data), **train_params(args, device))
    best = Path(results.save_dir) / "weights" / "best.pt"
    print(f"Training complete. Best weights: {best}")
    if args.val_after and best.exists():
        val(args, device, str(best))


def val(args: argparse.Namespace, device: str | int, weights: str | None = None) -> None:
    from ultralytics import YOLO

    weights = weights or args.weights
    if not weights:
        weights = Path(args.project) / args.name / "weights" / "best.pt"
    model = YOLO(norm_path(weights))
    metrics = model.val(
        data=norm_path(args.data),
        imgsz=args.imgsz,
        batch=args.batch,
        device=device,
        conf=args.conf,
        iou=args.iou,
        max_det=args.max_det,
        plots=True,
        save_json=args.save_json,
        verbose=True,
    )
    save_metrics(metrics)


def predict(args: argparse.Namespace, device: str | int) -> None:
    from ultralytics import YOLO

    weights = args.weights or Path(args.project) / args.name / "weights" / "best.pt"
    model = YOLO(norm_path(weights))
    model.predict(
        source=norm_path(args.source),
        imgsz=args.imgsz,
        conf=args.conf,
        iou=args.iou,
        max_det=args.max_det,
        device=device,
        save=True,
        save_txt=True,
        save_conf=True,
        verbose=True,
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="RS-STOD trainer for YOLOv12-DMMA-ECA-P2")
    parser.add_argument("mode", choices=["train", "val", "predict"], nargs="?", default="train")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--data", default=DEFAULT_DATA)
    parser.add_argument("--weights", default=None)
    parser.add_argument("--source", default=DEFAULT_SOURCE)
    parser.add_argument("--device", default=os.getenv("YOLO_DEVICE", "0"))
    parser.add_argument("--project", default="runs/detect")
    parser.add_argument("--name", default="rs_stod_dmma_eca_p2")
    parser.add_argument("--epochs", type=int, default=300)
    parser.add_argument("--batch", type=int, default=8)
    parser.add_argument("--imgsz", type=int, default=800)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--lr0", type=float, default=0.001)
    parser.add_argument("--warmup-epochs", type=float, default=5.0)
    parser.add_argument("--mosaic", type=float, default=1.0)
    parser.add_argument("--mixup", type=float, default=0.15)
    parser.add_argument("--copy-paste", type=float, default=0.35)
    parser.add_argument("--scale", type=float, default=0.8)
    parser.add_argument("--degrees", type=float, default=15.0)
    parser.add_argument("--close-mosaic", type=int, default=25)
    parser.add_argument("--patience", type=int, default=60)
    parser.add_argument("--save-period", type=int, default=25)
    parser.add_argument("--cache", default=False)
    parser.add_argument("--conf", type=float, default=0.001)
    parser.add_argument("--iou", type=float, default=0.6)
    parser.add_argument("--max-det", type=int, default=1000)
    parser.add_argument("--save-json", action="store_true")
    parser.add_argument("--no-val-after", dest="val_after", action="store_false")
    parser.add_argument("--exist-ok", action="store_true")
    parser.set_defaults(val_after=True)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    device = parse_device(args.device)
    if args.mode == "train":
        train(args, device)
    elif args.mode == "val":
        val(args, device)
    else:
        predict(args, device)


if __name__ == "__main__":
    main()
