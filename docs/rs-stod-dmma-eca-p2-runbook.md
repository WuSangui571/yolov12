# RS-STOD Training Runbook for YOLOv12-DMMA-ECA-P2

## Dataset Status

RS-STOD has been prepared with the official COCO train/val split and existing YOLO labels:

| Split | Images |
|---|---:|
| train | 1852 |
| val | 463 |

Label summary:

| Class | Boxes |
|---|---:|
| Small Vehicle | 26939 |
| Large Vehicle | 2240 |
| Ship | 7467 |
| Airplane | 5788 |
| Storage Tank | 5534 |

Generated files:

- `RS-STOD/train.txt`
- `RS-STOD/val.txt`
- `RS-STOD/rs_stod_summary.json`
- `data/rs_stod.yaml`

The split txt files contain paths such as `./yolo/images/1.jpg`, resolved relative to the `RS-STOD` directory. This keeps the dataset portable between Windows and Linux.

## Linux Environment

Use the project root as the working directory after copying the repository to Linux:

```bash
cd /path/to/yolov12
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -e .
pip install -r requirements.txt
```

For an RTX 4090, install a CUDA-enabled PyTorch build that matches your driver/CUDA runtime. For example, with CUDA 12.1:

```bash
pip install --index-url https://download.pytorch.org/whl/cu121 torch==2.2.2 torchvision==0.17.2
```

## Prepare Dataset

Run this once after copying the dataset:

```bash
python prepare_rs_stod.py --root RS-STOD
```

Expected summary:

- 2315 images
- 2315 label files
- 47968 boxes
- 0 bad labels
- 1852 train images
- 463 val images

## Recommended Main Training

This is the main experiment for testing the paper model on RS-STOD:

```bash
CUDA_VISIBLE_DEVICES=0 python train_rs_stod.py train \
  --model ultralytics/cfg/models/v12/yolov12-dmma-p2-advanced.yaml \
  --data data/rs_stod.yaml \
  --name rs_stod_dmma_eca_p2_adv_i800_b8_e300 \
  --epochs 300 \
  --imgsz 800 \
  --batch 8 \
  --workers 8 \
  --device 0
```

The script runs validation after training and writes:

```text
runs/detect/rs_stod_dmma_eca_p2_adv_i800_b8_e300/metrics_summary.json
```

The JSON contains:

- `metrics/precision(B)`
- `metrics/recall(B)`
- `metrics/mAP50(B)`
- `metrics/mAP50-95(B)`
- per-class precision, recall, mAP50, and mAP50-95

## Optional Progressive Training

If the 800 run is stable and you want a higher-resolution result:

```bash
CUDA_VISIBLE_DEVICES=0 python train_rs_stod.py train \
  --model runs/detect/rs_stod_dmma_eca_p2_adv_i800_b8_e300/weights/best.pt \
  --data data/rs_stod.yaml \
  --name rs_stod_dmma_eca_p2_adv_i960_b4_e80 \
  --epochs 80 \
  --imgsz 960 \
  --batch 4 \
  --lr0 0.0003 \
  --mosaic 0.5 \
  --mixup 0.05 \
  --copy-paste 0.2 \
  --scale 0.5 \
  --close-mosaic 10 \
  --workers 6 \
  --device 0
```

## Baseline Comparison

Use the original YOLOv12 as a baseline so the RS-STOD result can be discussed in the paper:

```bash
CUDA_VISIBLE_DEVICES=0 yolo detect train \
  model=ultralytics/cfg/models/v12/yolov12.yaml \
  data=data/rs_stod.yaml \
  epochs=300 \
  imgsz=800 \
  batch=12 \
  optimizer=AdamW \
  lr0=0.001 \
  weight_decay=0.05 \
  close_mosaic=25 \
  patience=60 \
  amp=True \
  device=0 \
  project=runs/detect \
  name=rs_stod_yolov12_baseline_i800_b12_e300
```

Validate the baseline:

```bash
yolo detect val \
  model=runs/detect/rs_stod_yolov12_baseline_i800_b12_e300/weights/best.pt \
  data=data/rs_stod.yaml \
  imgsz=800 \
  batch=12 \
  conf=0.001 \
  iou=0.6 \
  max_det=1000 \
  device=0
```

## Validation

Validate the proposed model and write metrics JSON:

```bash
CUDA_VISIBLE_DEVICES=0 python train_rs_stod.py val \
  --weights runs/detect/rs_stod_dmma_eca_p2_adv_i800_b8_e300/weights/best.pt \
  --data data/rs_stod.yaml \
  --imgsz 800 \
  --batch 8 \
  --conf 0.001 \
  --iou 0.6 \
  --max-det 1000 \
  --device 0
```

## Detection

Run detection on all RS-STOD images:

```bash
CUDA_VISIBLE_DEVICES=0 python train_rs_stod.py predict \
  --weights runs/detect/rs_stod_dmma_eca_p2_adv_i800_b8_e300/weights/best.pt \
  --source RS-STOD/yolo/images \
  --imgsz 800 \
  --conf 0.25 \
  --iou 0.45 \
  --max-det 1000 \
  --device 0
```

Run detection on validation images only by using the generated txt list:

```bash
CUDA_VISIBLE_DEVICES=0 python train_rs_stod.py predict \
  --weights runs/detect/rs_stod_dmma_eca_p2_adv_i800_b8_e300/weights/best.pt \
  --source RS-STOD/val.txt \
  --imgsz 800 \
  --conf 0.25 \
  --iou 0.45 \
  --max-det 1000 \
  --device 0
```

