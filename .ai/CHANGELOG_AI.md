# AI Change Log（AI修改日志）

> 目的：记录每次由 AI 参与的改动，避免后续任务重复造轮子或破坏既有行为。
> 要求：每次合并前必须追加一条记录（倒序）。

---

## [2026-04-22] 补充 DMMA 机制消融实验开关与实验配置
- 背景/需求：
  - 根据论文审稿意见，需要补充 difference gate 去除、固定/可学习 tau 与 eta、以及不同插入位置的机制消融实验代码支持。
- 修改类型：feat / docs
- 影响范围：检测模型模块 / v12 模型配置 / 测试
- 变更摘要：
  1) 为 DMMA 注意力补充 difference gate 开关，以及固定/可学习 temperature 与 mask scale 的配置能力。
  2) 为 C2fDMMA 与多尺度 MSDMMALayer 透传上述开关，保持旧配置兼容。
  3) 新增 no-gate、fixed-scale、backbone-only、neck-only 四份 v12 消融配置。
  4) 在 tests 中新增最小构图与参数形态校验用例。
- 涉及文件：
  - `/ultralytics/nn/modules/transformer.py`
  - `/ultralytics/nn/modules/block.py`
  - `/ultralytics/cfg/models/v12/yolov12-dmma-no-gate.yaml`
  - `/ultralytics/cfg/models/v12/yolov12-dmma-fixed-scale.yaml`
  - `/ultralytics/cfg/models/v12/yolov12-dmma-backbone-only.yaml`
  - `/ultralytics/cfg/models/v12/yolov12-dmma-neck-only.yaml`
  - `/tests/test_python.py`
- 检索与复用策略：
  - 检索关键词：DMMA、C2fDMMA、DifferenceMaskAttention、yolov12-dmma、ablation
  - 找到的旧实现：
    - `DifferenceMaskAttention`
    - `DMMALayer`
    - `C2fDMMA`
    - `yolov12-dmma.yaml`
    - `yolov12-dmma-only.yaml`
  - 最终选择：复用现有 DMMA 主链路并参数化扩展，不新增训练入口。
- 风险点：
  - 当前 Windows 工作环境缺少 torch，无法在本地完成真实模型构图验证。
  - 新 YAML 需要在 Linux 训练环境中做一次实际加载确认。
- 验证方式：
  - 已完成修改文件的 Python 语法级静态校验（py_compile）。
  - 待在具备 torch 的环境中执行目标测试与模型加载验证。
- 后续建议：
  - 在 Linux 环境优先跑 `YOLO(cfg).info()` 或一次 dry-run，确认四份配置都能正常构图。
  - 训练完成后补充论文中的机制消融表与公平性说明表。

---

## [YYYY-MM-DD] <变更标题>
- 背景/需求：
- 修改类型：feat / fix / refactor / docs
- 影响范围：A业务 / B业务 / 公共模块 / 数据模型
- 变更摘要：
  1) ...
  2) ...
- 涉及文件：
  - `/path/file1`
  - `/path/file2`
- 检索与复用策略：
  - 检索关键词：
  - 找到的旧实现：
  - 最终选择：复用/修改/新建（说明原因）
- 风险点：
  - ...
- 验证方式：
  - ...
- 后续建议：
  - ...

---
