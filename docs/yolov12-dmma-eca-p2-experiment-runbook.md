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
| Data | `data/masati.yaml` |
| Epochs | `300` |
| Image size | `640` |
| Optimizer | `AdamW` |
| Batch size | `16` |
| Device | `0` |
| Project dir | `runs/detect_paper` |

If GPU memory becomes tight, reduce only `batch`, and record the change.

## 4. Training Commands

Run from the project root on Linux.

### Group A: YOLOv12 baseline

```bash
CUDA_VISIBLE_DEVICES=0 yolo detect train \
  model=ultralytics/cfg/models/v12/yolov12.yaml \
  data=data/masati.yaml \
  epochs=300 \
  imgsz=640 \
  batch=16 \
  optimizer=AdamW \
  project=runs/detect_paper \
  name=paper_masati_a_yolov12_640_adamw_e300_b16_20260328
```

### Group B: YOLOv12 + DMMA only

```bash
CUDA_VISIBLE_DEVICES=0 yolo detect train \
  model=ultralytics/cfg/models/v12/yolov12-dmma-only.yaml \
  data=data/masati.yaml \
  epochs=300 \
  imgsz=640 \
  batch=16 \
  optimizer=AdamW \
  project=runs/detect_paper \
  name=paper_masati_b_dmma_only_640_adamw_e300_b16_20260328
```

### Group C: YOLOv12 + DMMA + ECA

```bash
CUDA_VISIBLE_DEVICES=0 yolo detect train \
  model=ultralytics/cfg/models/v12/yolov12-dmma.yaml \
  data=data/masati.yaml \
  epochs=300 \
  imgsz=640 \
  batch=16 \
  optimizer=AdamW \
  project=runs/detect_paper \
  name=paper_masati_c_dmma_eca_640_adamw_e300_b16_20260328
```

### Group D: YOLOv12 + DMMA + ECA + P2

```bash
CUDA_VISIBLE_DEVICES=0 yolo detect train \
  model=ultralytics/cfg/models/v12/yolov12-dmma-p2-efficient.yaml \
  data=data/masati.yaml \
  epochs=300 \
  imgsz=640 \
  batch=16 \
  optimizer=AdamW \
  project=runs/detect_paper \
  name=paper_masati_d_dmma_eca_p2_640_adamw_e300_b16_20260328
```

## 5. Validation Commands

After each training run, validate with the same image size:

```bash
CUDA_VISIBLE_DEVICES=0 yolo detect val \
  model=runs/detect_paper/<run_name>/weights/best.pt \
  data=data/masati.yaml \
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
