# YOLOv12 + DMMA + ECA + P2 Experiment Runbook

This runbook standardizes experiment naming, execution order, and result collection for the paper ablation study on MASATI.

## 1. Experiment Groups

Use these four groups in the paper:

| Group | Paper Name | YAML |
|---|---|---|
| A | YOLOv12 | `ultralytics/cfg/models/v12/yolov12.yaml` |
| B | YOLOv12 + DMMA | `ultralytics/cfg/models/v12/yolov12-dmma-only.yaml` |
| C | YOLOv12 + DMMA + ECA | `ultralytics/cfg/models/v12/yolov12-dmma.yaml` |
| D | YOLOv12 + DMMA + ECA + P2 | `ultralytics/cfg/models/v12/yolov12-dmma-p2-efficient.yaml` |

## 2. Naming Convention

Use one naming rule for every run:

`paper_masati_<group>_<imgsz>_<opt>_e<epochs>_b<batch>_<date>`

Examples:

- `paper_masati_a_yolov12_640_adamw_e300_b16_20260328`
- `paper_masati_b_dmma_only_640_adamw_e300_b16_20260328`
- `paper_masati_c_dmma_eca_640_adamw_e300_b16_20260328`
- `paper_masati_d_dmma_eca_p2_640_adamw_e300_b16_20260328`

## 3. Recommended Unified Training Setting

Keep all ablation groups under the same setting:

| Item | Recommended Value |
|---|---|
| Data | `/usr/sangui/PythonProject/yolov12/data/masati.yaml` |
| Epochs | `150` |
| Image size | `640` |
| Optimizer | `AdamW` |
| Batch size | `6` |
| Device | `0` |
| Project dir | `runs/detect` |

Recommended shared hyperparameters:

- `lr0=0.001`
- `lrf=0.01`
- `weight_decay=0.05`
- `warmup_epochs=5`
- `patience=50`
- `box=10.0`
- `cls=0.3`
- `dfl=1.5`
- `mosaic=1.0`
- `mixup=0.2`
- `copy_paste=0.5`
- `degrees=15.0`
- `flipud=0.5`
- `scale=0.9`
- `close_mosaic=15`
- `amp=True`
- `workers=8`

If GPU memory becomes tight, reduce only `batch`, and record the change. Keep the other settings unchanged across groups.

## 4. Training Commands

Run from the project root on Linux.

Important:

- Do not leave spaces after the line-continuation `\`.
- Reusing the same `name` with `exist_ok=False` will create a new run with a numeric suffix.

### Group A: YOLOv12 baseline

```bash
CUDA_VISIBLE_DEVICES=0 yolo detect train \
  model=ultralytics/cfg/models/v12/yolov12.yaml \
  data=/usr/sangui/PythonProject/yolov12/data/masati.yaml \
  epochs=150 \
  imgsz=640 \
  batch=6 \
  device=0 \
  optimizer=AdamW \
  lr0=0.001 \
  lrf=0.01 \
  weight_decay=0.05 \
  warmup_epochs=5 \
  patience=50 \
  box=10.0 \
  cls=0.3 \
  dfl=1.5 \
  mosaic=1.0 \
  mixup=0.2 \
  copy_paste=0.5 \
  degrees=15.0 \
  flipud=0.5 \
  scale=0.9 \
  close_mosaic=15 \
  amp=True \
  workers=8 \
  project=runs/detect \
  name=paper_masati_a_yolov12_640_adamw_e150_b6_20260328
```

### Group B: YOLOv12 + DMMA only

```bash
CUDA_VISIBLE_DEVICES=0 yolo detect train \
  model=ultralytics/cfg/models/v12/yolov12-dmma-only.yaml \
  data=/usr/sangui/PythonProject/yolov12/data/masati.yaml \
  epochs=150 \
  imgsz=640 \
  batch=6 \
  device=0 \
  optimizer=AdamW \
  lr0=0.001 \
  lrf=0.01 \
  weight_decay=0.05 \
  warmup_epochs=5 \
  patience=50 \
  box=10.0 \
  cls=0.3 \
  dfl=1.5 \
  mosaic=1.0 \
  mixup=0.2 \
  copy_paste=0.5 \
  degrees=15.0 \
  flipud=0.5 \
  scale=0.9 \
  close_mosaic=15 \
  amp=True \
  workers=8 \
  project=runs/detect \
  name=paper_masati_b_dmma_only_640_adamw_e150_b6_20260328
```

### Group C: YOLOv12 + DMMA + ECA

```bash
CUDA_VISIBLE_DEVICES=0 yolo detect train \
  model=ultralytics/cfg/models/v12/yolov12-dmma.yaml \
  data=/usr/sangui/PythonProject/yolov12/data/masati.yaml \
  epochs=150 \
  imgsz=640 \
  batch=6 \
  device=0 \
  optimizer=AdamW \
  lr0=0.001 \
  lrf=0.01 \
  weight_decay=0.05 \
  warmup_epochs=5 \
  patience=50 \
  box=10.0 \
  cls=0.3 \
  dfl=1.5 \
  mosaic=1.0 \
  mixup=0.2 \
  copy_paste=0.5 \
  degrees=15.0 \
  flipud=0.5 \
  scale=0.9 \
  close_mosaic=15 \
  amp=True \
  workers=8 \
  project=runs/detect \
  name=paper_masati_c_dmma_eca_640_adamw_e150_b6_20260328
```

### Group D: YOLOv12 + DMMA + ECA + P2

```bash
CUDA_VISIBLE_DEVICES=0 yolo detect train \
  model=ultralytics/cfg/models/v12/yolov12-dmma-p2-efficient.yaml \
  data=/usr/sangui/PythonProject/yolov12/data/masati.yaml \
  epochs=150 \
  imgsz=640 \
  batch=6 \
  device=0 \
  optimizer=AdamW \
  lr0=0.001 \
  lrf=0.01 \
  weight_decay=0.05 \
  warmup_epochs=5 \
  patience=50 \
  box=10.0 \
  cls=0.3 \
  dfl=1.5 \
  mosaic=1.0 \
  mixup=0.2 \
  copy_paste=0.5 \
  degrees=15.0 \
  flipud=0.5 \
  scale=0.9 \
  close_mosaic=15 \
  amp=True \
  workers=8 \
  project=runs/detect \
  name=paper_masati_d_dmma_eca_p2_640_adamw_e150_b6_20260328
```

## 5. Validation Commands

After each training run, validate with the same image size:

```bash
CUDA_VISIBLE_DEVICES=0 yolo detect val \
  model=runs/detect/<run_name>/weights/best.pt \
  data=/usr/sangui/PythonProject/yolov12/data/masati.yaml \
  imgsz=640 \
  device=0
```

## 6. What to Record

For each run, record:

- `Precision`
- `Recall`
- `mAP50`
- `mAP50-95`
- `Params`
- `GFLOPs`
- `FPS` or `ms/image`
- weights path

Suggested evidence files:

- `results.csv`
- `args.yaml`
- `weights/best.pt`
- PR curve / confusion matrix screenshots

## 7. Paper Table Mapping

Fill your paper tables like this:

| Paper Table | Data Source |
|---|---|
| Table 4.1 Experimental setup | fixed environment + chosen hyperparameters |
| Table 4.2 Comparison experiments | Group A and Group D, plus any external baselines |
| Table 4.3 Ablation study | Groups A, B, C, D |
| Table 4.4 Complexity analysis | Groups A, B, C, D |
| Fig. 4.x Visualization | baseline vs Group D prediction images |

## 8. Result Log Template

Copy this for each experiment:

```text
Run name:
Model yaml:
Weights path:
Epochs:
Batch:
Imgsz:
Precision:
Recall:
mAP50:
mAP50-95:
Params:
GFLOPs:
FPS:
Time per image:
Notes:
```
