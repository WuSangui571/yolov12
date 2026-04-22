Conference Title

Difference Mask Mixed Attention with ECA for Small-Ship Detection in
Optical Remote Sensing Images

Shuai Yuan^a,c,d\*^ , Huize Dou^a,c,d^ , Jinyu Geng^b^, Fangjun
Luan^a,c,d^, Xiaowen Zhang^e,f\ \*^

^a^School of Computer Science and Engineering, Shenyang Jianzhu
University, Shenyang 110168, China

^b^School of Electrical and Control Engineering,Shenyang Jianzhu
University, Shenyang 110168, China

^c^Liaoning Province Big Data Management and Analysis Laboratory of
Urban Construction, Shenyang 110168, China

^d^Shenyang Branch of National Special Computer Engineering Technology
Research Center, Shenyang 110168, China

^e^Changchun Institute of Optics, Fine Mechanics and Physics, Chinese
Academy of Sciences, Changchun 130033, China

^f^University of Chinese Academy of Sciences, Beijing 100049, China

+----------------------+----------------------+----------------------+
| [A R T I C L E I N F |                      | [A B S T R A C       |
| O]{.smallcaps}       |                      | T]{.smallcaps}       |
|                      |                      |                      |
| Keywords:            |                      | Small-ship detection |
|                      |                      | in optical remote    |
| Small ship detection |                      | sensing images       |
|                      |                      | remains challenging  |
| Optical remote       |                      | because targets are  |
| sensing              |                      | usually tiny,        |
|                      |                      | visually weak, and   |
| YOLOv12              |                      | easily confused with |
|                      |                      | complex maritime     |
| Difference Mask      |                      | backgrounds such as  |
| Mixed Attention      |                      | waves, wakes, reefs, |
|                      |                      | and shoreline        |
| Efficient Channel    |                      | clutter. To address  |
| Attention            |                      | this problem, this   |
|                      |                      | paper proposes a     |
|                      |                      | YOLOv12-based        |
|                      |                      | small-ship detector  |
|                      |                      | that integrates      |
|                      |                      | Difference Mask      |
|                      |                      | Mixed Attention      |
|                      |                      | (DMMA) and ECA-style |
|                      |                      | channel attention    |
|                      |                      | for enhanced         |
|                      |                      | target-background    |
|                      |                      | discrimination and   |
|                      |                      | feature refinement.  |
|                      |                      | The DMMA module      |
|                      |                      | improves feature     |
|                      |                      | interaction by       |
|                      |                      | introducing          |
|                      |                      | difference-aware     |
|                      |                      | gating into          |
|                      |                      | window-based         |
|                      |                      | self-attention,      |
|                      |                      | which helps suppress |
|                      |                      | inconsistent         |
|                      |                      | responses between    |
|                      |                      | ship structures and  |
|                      |                      | surrounding clutter. |
|                      |                      | Meanwhile, the       |
|                      |                      | ECA-style channel    |
|                      |                      | refinement module    |
|                      |                      | recalibrates         |
|                      |                      | informative channels |
|                      |                      | with negligible      |
|                      |                      | additional overhead. |
|                      |                      | Experiments on       |
|                      |                      | MASATI and           |
|                      |                      | HRSC2016-MS          |
|                      |                      | demonstrate the      |
|                      |                      | effectiveness of the |
|                      |                      | proposed method. The |
|                      |                      | proposed YOLOv12 +   |
|                      |                      | DMMA + ECA model     |
|                      |                      | achieves 0.839       |
|                      |                      | mAP@0.5 on MASATI    |
|                      |                      | and 0.824 mAP@0.5 on |
|                      |                      | HRSC2016-MS,         |
|                      |                      | outperforming        |
|                      |                      | YOLOv8, RT-DETR,     |
|                      |                      | DINO, and LiM-YOLO   |
|                      |                      | in mAP@0.5 on both   |
|                      |                      | datasets. These      |
|                      |                      | results indicate     |
|                      |                      | that the proposed    |
|                      |                      | difference-aware     |
|                      |                      | attention design     |
|                      |                      | improves             |
|                      |                      | target-background    |
|                      |                      | discrimination and   |
|                      |                      | enhances small-ship  |
|                      |                      | detection            |
|                      |                      | performance in       |
|                      |                      | optical remote       |
|                      |                      | sensing images.      |
+----------------------+----------------------+----------------------+

1.  Introduction

Small-ship detection in optical remote sensing imagery remains a
challenging small-object detection task with direct value for maritime
surveillance, port operation analysis, and coastal security. In
practical scenes, ships often occupy only a few pixels and are embedded
in highly dynamic backgrounds containing waves, reefs, cloud shadows,
and shoreline clutter. These factors cause weak target saliency and high
visual ambiguity, making detectors prone to missed detections and false
alarms. Therefore, improving discriminative representation for tiny
maritime targets under complex backgrounds is a central problem in
remote sensing vision.

Recent one-stage detectors provide an effective speed-accuracy
trade-off, yet performance bottlenecks persist when object scale becomes
extremely small and contextual interference becomes dominant. To address
this, we design a YOLOv12-based detector that couples efficient
global-local attention with lightweight channel refinement. The model is
built around a Difference Mask Mixed Attention (DMMA) mechanism and an
Efficient Channel Attention (ECA) strategy to improve target-background
discrimination and feature representation for small ship detection.

The key motivation of DMMA is not only to aggregate context, but to make
target-background separability explicit during feature interaction. By
explicitly modeling the pixel-level contrast between ships and their
wakes, DMMA encourages the network to emphasize edge-consistent and
structure-consistent responses while suppressing texture noise from sea
clutter. This difference-aware design is especially important in
maritime imagery, where many hard negatives share similar intensity
statistics with true ship regions. In parallel, ECA provides lightweight
channel reweighting to reinforce informative semantics with minimal
computational overhead.

The main contributions of this work are summarized as follows. First, we
propose a YOLOv12-based small-ship detection framework that introduces
Difference Mask Mixed Attention to strengthen target-background
separability in complex maritime scenes. Unlike generic attention
enhancement, DMMA explicitly constructs pairwise difference cues from an
additional mask branch and uses them to suppress inconsistent token
interactions caused by waves, wakes, reefs, and shoreline clutter.
Second, we integrate an ECA-style channel refinement strategy into the
DMMA-enhanced feature extraction process, improving channel-wise
representation with limited additional overhead and reducing redundant
sea-surface texture responses. Third, comparison experiments are
conducted on MASATI and HRSC2016-MS against representative CNN-based,
Transformer-based, and ship-specific detectors, including YOLOv8,
RT-DETR, DINO, and LiM-YOLO. The proposed model achieves the best
mAP@0.5 on both datasets, demonstrating its effectiveness for target
discovery and target-background discrimination in optical remote sensing
ship detection.

1.  Related work

Object detection methods have developed rapidly from traditional
handcrafted-feature frameworks to deep learning based end-to-end
detectors. Early two-stage methods represented by the R-CNN family
achieved strong accuracy through proposal generation and refinement, but
their inference speed was relatively limited for real-time maritime
monitoring. In contrast, one-stage detectors represented by the YOLO
family provided a more practical speed-accuracy balance by directly
regressing bounding boxes and class probabilities in a unified
framework. From early YOLO versions to newer generations, continuous
improvements in backbone design, multi-scale feature fusion, training
strategy, and detection head formulation have significantly strengthened
robustness and engineering usability. For remote sensing tasks,
especially optical ship detection, YOLO-based frameworks have become a
preferred technical route because they support high-throughput
processing while remaining flexible for task-specific module redesign.

Although YOLO detectors are efficient, small-ship detection in optical
remote sensing images remains difficult due to intrinsic scene
characteristics. Compared with natural-image benchmarks, maritime remote
sensing images usually contain larger observation ranges, weaker object
saliency, and more severe background interference. Tiny ship targets are
often mixed with waves, wakes, reefs, shoreline textures, and
illumination fluctuations, causing high inter-class similarity between
true targets and hard negatives. Under these conditions, repeated
downsampling and convolution-only local aggregation may weaken fine
structural cues and lead to missed detections or unstable recall.
Therefore, improving discriminative representation for tiny targets in
complex maritime backgrounds is a key research direction.

![](media/image5.png){width="3.301388888888889in"
height="1.7986111111111112in"}To address the representation bottleneck
of pure convolution, attention mechanisms have been increasingly
introduced into object detection. Spatial attention and channel
attention first demonstrated that adaptive feature reweighting can
suppress irrelevant responses and improve detector focus. Subsequently,
self-attention based modeling further expanded receptive interaction by
capturing long-range dependencies, which is valuable when local
appearance alone is ambiguous. In high-resolution remote sensing
scenarios, window-based self-attention is particularly attractive
because it provides a practical compromise between contextual modeling
and computational cost. This trend establishes the theoretical basis for
integrating mixed attention structures into YOLO-style detectors for
small-ship tasks.

However, generic attention is still insufficient in many maritime scenes
because false responses are frequently caused by subtle visual
similarity between ship regions and surrounding clutter. This motivates
the introduction of a difference-driven mechanism. By explicitly
modeling the pixel-level contrast between ships and their wakes,
difference-aware feature interaction can better emphasize
edge-consistent and structure-consistent target cues while reducing
interference from sea-surface textures. In this sense, the Difference
Mask strategy is not only an operational design but a targeted response
to the core ambiguity of maritime optical detection. It improves
target-background separability at the feature level and provides a
stronger semantic foundation for robust small-ship recognition.

At the same time, channel-level feature selection remains essential for
improving representation efficiency. Efficient Channel Attention (ECA)
offers a lightweight way to capture local cross-channel interaction
without introducing heavy parameter overhead. Compared with more complex
channel-attention blocks, ECA keeps the computational burden low while
still reinforcing informative channels. This property is important for
practical detection systems where accuracy gains must be achieved under
constrained computational budgets. Therefore, combining Difference Mask
based spatial discrimination with ECA based channel refinement forms a
complementary and computationally efficient attention design.

Although existing attention-based detectors improve contextual modeling
and feature reweighting, most of them are still designed as
general-purpose enhancement modules rather than mechanisms tailored to
maritime ambiguity. In optical remote sensing ship detection, many false
responses are caused not only by insufficient context, but also by
subtle visual similarity between true ship regions and surrounding
clutter such as wakes, wave textures, and coastal interference.
Therefore, merely strengthening generic attention is often insufficient.
Motivated by this observation, we introduce a difference-aware attention
design that explicitly suppresses inconsistent token interactions, and
further couple it with lightweight channel refinement to obtain a more
targeted solution for small-ship detection in complex maritime
backgrounds.

1.  Method

This work proposes a YOLOv12-based small-ship detector for optical
remote sensing images. The framework is centered on two coordinated
components: Difference Mask Mixed Attention (DMMA), which enhances
target-background discrimination during spatial-token interaction, and
an ECA-style channel refinement module, which improves channel-wise
feature selection with limited additional cost. The detector follows the
standard backbone-neck-head paradigm of YOLOv12, while replacing several
key feature extraction and fusion units with DMMA-enhanced modules to
improve representation quality for challenging small-ship scenarios.
Figure 2.1 illustrates the overall architecture of the proposed YOLOv12
+ DMMA + ECA framework and highlights the insertion positions of the
DMMA-enhanced modules.

**Figure 2.1 Overall architecture of the proposed YOLOv12 + DMMA + ECA
framework**

The overall network follows a backbone-neck-head paradigm. In the
backbone, shallow and intermediate stages generate hierarchical
features, while the deeper P4 and P5 stages introduce DMMA-enhanced
feature extraction (C2fDMMA) to strengthen long-range dependency
modeling in cluttered maritime scenes. In the neck, a top-down and
bottom-up bidirectional fusion path is used, and C2fDMMA blocks are
inserted into the key P3 and P4 feature-fusion nodes to reduce semantic
dilution during scale transfer. In the head, predictions are produced
from the YOLOv12 detection scales, enabling a balance between detail
preservation and semantic robustness. This design keeps the original
YOLOv12 detection pipeline while replacing selected feature extraction
and fusion units with difference-aware attention blocks.

Inside each DMMA block, the input feature map is first partitioned into
non-overlapping windows, and each window is processed by multi-head
self-attention. For an input feature
$X \in \mathbb{R}^{B \times H \times W \times C}$, the window partition
operation produces
$X_{w} \in \mathbb{R}^{(B \cdot N_{w}) \times N \times C}$, where
$N = w^{2}$ is the number of tokens in each window. A linear projection
is then used to generate four branches, namely query, key, value, and
mask features:

$$\lbrack Q,K,V,M\rbrack = Linear(X_{w}).$$

For the i-th and j-th tokens in the same window, the mask branch is used
to construct a normalized pairwise difference cue:

$$\Delta_{\text{ij}} = \frac{\parallel M_{i} - M_{j} \parallel_{1}}{\parallel M_{j} \parallel_{1} + \epsilon},$$

where $\epsilon$ is a small constant for numerical stability. The
difference cue is converted into a suppressive gate:

$$G_{\text{ij}} = 1 - \sigma(\Delta_{\text{ij}}).$$

$$S = QK^{\top} + B_{\text{rel}} + M_{\text{sw}},$$

where $B_{\text{rel}}$ denotes the learnable relative position bias and
$M_{\text{sw}}$ is the shifted-window mask when window shifting is
enabled. DMMA injects the difference-aware gate into the attention
logits before softmax:

$${\widetilde{S}}_{\text{ij}} = \frac{S_{\text{ij}}}{\tau} \cdot (\eta G_{\text{ij}}),$$

where $\tau$ is a learnable head-wise temperature parameter and $\eta$
is a learnable mask scaling factor. The learnable temperature avoids
manually fixing the strength of difference-aware suppression and allows
the model to adapt the gating intensity to different maritime scenes and
feature scales.The final attention map and output feature are obtained
by:

$$A = Softmax(\widetilde{S}),\quad Y = AV.$$

![](media/image6.png){width="3.3180555555555555in"
height="1.6993055555555556in"}This design is not intended to simply
amplify arbitrary feature differences. Instead, it suppresses unstable
or mismatched token interactions between ship structures and surrounding
clutter, thereby improving target-background separability in complex
maritime scenes. Figure 2.2 provides a schematic illustration of the
internal coupling between difference-aware gating and ECA-based channel
refinement within the DMMA block.

**Figure 2.2 Schematic illustration of the DMMA block with ECA-based
channel refinement**

To complement the difference-aware spatial-token interaction, each DMMA
layer further includes an ECA-style channel refinement module. Given an
input feature map $F \in \mathbb{R}^{B \times C \times H \times W}$,
global average pooling and global max pooling are first applied to
obtain compact channel descriptors. These descriptors are then processed
by lightweight one-dimensional convolution along the channel dimension
to model local cross-channel interaction:

$$z = Conv1D(GAP(F)) + Conv1D(GMP(F)).$$

The channel weights are obtained by sigmoid activation:

$$w = \sigma(z),$$

$$F' = F \odot w.$$

This channel refinement branch introduces only negligible additional
computational overhead compared with the main DMMA attention path, but
it helps recalibrate informative channels and suppress redundant
sea-surface texture responses. This is particularly useful in maritime
scenes, where wave and wake patterns may activate many background
channels and interfere with small-ship representations.

In implementation, the channel mask is applied to the DMMA attention
output and then combined with the shortcut connection of the original
block. This preserves the residual learning behavior of YOLOv12 while
allowing the ECA branch to emphasize discriminative channels with
limited additional overhead.

$$L = \lambda_{\text{box}}L_{\text{box}} + \lambda_{\text{cls}}L_{\text{cls}} + \lambda_{\text{dfl}}L_{\text{dfl}}$$

where $L_{\text{box}}$, $L_{\text{cls}}$, and $L_{\text{dfl}}$ denote
the box regression loss, classification loss, and distribution focal
loss, respectively, and $\lambda_{\text{box}}$, $\lambda_{\text{cls}}$,
and $\lambda_{\text{dfl}}$ are their corresponding balancing
coefficients. With single-class setting ((nc=1), ship). In the provided
training configuration, stronger localization emphasis is applied (e.g.,
larger ($\lambda_{\text{box}}$) to suit tiny-target maritime detection,
while augmentation strategies (mosaic, mixup, copy-paste, geometric
perturbation) further improve robustness under appearance variation.

4\. Experiments

***4.1. Experimental Setup***

To evaluate the effectiveness of the proposed method, experiments were
mainly conducted on the MASATI dataset, which is widely used for
maritime ship detection, and supplementary evaluation was further
performed on HRSC2016-MS. Since the current task focuses on ship
detection only, the number of categories was set to one, namely ship.
Each dataset was divided into training, validation, and test subsets
according to the predefined split. For reproducibility, the number of
images in each subset should be explicitly reported for both MASATI and
HRSC2016-MS when the final dataset split is fixed.

All experiments were carried out in a Linux-based training environment
equipped with an NVIDIA GeForce RTX 4090 GPU with 24 GB memory. The
model development and code modification were completed in a Windows
environment, while the training and evaluation procedures were executed
on Linux. The deep learning framework was based on PyTorch 2.2.2 with
CUDA 11.8, and the detection framework used Ultralytics YOLOv12.

For the ablation study, all YOLOv12 variants were trained under the same
settings. The optimizer was AdamW, the initial learning rate was set to
0.001, the final learning rate factor was 0.01, and the weight decay was
0.05. The total number of epochs was 150, the batch size was 6, and the
input image size was 640 × 640. In addition, mosaic, mixup, and
copy-paste augmentation strategies were adopted to improve robustness
for small target detection. The main evaluation metrics included
Precision, Recall, mAP@0.5, and mAP@0.5:0.95.

For comparison with representative detection frameworks, YOLOv8 is
selected as a mature one-stage CNN-based detector, RT-DETR is selected
as a real-time end-to-end Transformer detector, and DINO is selected as
a strong DETR-style end-to-end detection baseline. In addition, LiM-YOLO
is included as a recent ship-specific detector designed for optical
remote sensing ship detection. These methods provide complementary
baselines from general-purpose real-time detection, Transformer-based
detection, and task-specific ship detection perspectives. All compared
methods are evaluated under the same dataset setting and the same
evaluation metrics whenever the corresponding outputs are available.
Since DINO does not provide complete Precision and Recall results in our
current evaluation record, only its mAP-based metrics are reported..

**Table 4.1 Experimental environment**

+-------------------------+-----------------------------------+
| > **Item**              | > **Configuration**               |
+=========================+===================================+
| > Training environment  | > Linux                           |
+-------------------------+-----------------------------------+
| > GPU                   | > NVIDIA GeForce RTX 4090 (24 GB) |
+-------------------------+-----------------------------------+
| > Framework             | > PyTorch 2.2.2 + CUDA 11.8       |
+-------------------------+-----------------------------------+
| > Detection framework   | > Ultralytics YOLOv12 8.3.63      |
+-------------------------+-----------------------------------+
| > Dataset               | > MASATI, HRSC2016-MS             |
+-------------------------+-----------------------------------+
| > Input size            | > 640 × 640                       |
+-------------------------+-----------------------------------+
| > Batch size            | > 6                               |
+-------------------------+-----------------------------------+
| > Epochs                | > 150                             |
+-------------------------+-----------------------------------+
| > Optimizer             | > AdamW                           |
+-------------------------+-----------------------------------+
| > Initial learning rate | > 0.001                           |
+-------------------------+-----------------------------------+
| > Weight decay          | > 0.05                            |
+-------------------------+-----------------------------------+

***4.2. Comparison with State-of-the-Art Methods on MASATI***

To further evaluate the effectiveness of the proposed method, we compare
it with representative detectors on the MASATI dataset, including
YOLOv8, RT-DETR, DINO, and LiM-YOLO. YOLOv8 is selected as a mature
one-stage CNN-based detector, RT-DETR and DINO represent
Transformer-based end-to-end detection frameworks, and LiM-YOLO is a
recent ship-specific detector designed for optical remote sensing
imagery.

**Table 4.2 Comparison with representative detectors on the MASATI
dataset**

  **Method**   **Dataset**   **Precision**   **Recall**   **mAP@0.5**   **mAP@0.5:0.95**
  ------------ ------------- --------------- ------------ ------------- ------------------
  YOLOv8       MASATI        0.744           0.612        0.651         0.244
  RT-DETR      MASATI        0.775           0.683        0.683         0.255
  DINO         MASATI        \-              \-           0.668         0.285
  LiM-YOLO     MASATI        0.825           0.724        0.821         **0.546**
  Ours         MASATI        **0.838**       **0.733**    **0.839**     0.531

Table 4.2 reports the comparison results on the MASATI dataset. Compared
with YOLOv8, the proposed YOLOv12 + DMMA + ECA model improves Precision
from 0.744 to 0.838, Recall from 0.612 to 0.733, mAP@0.5 from 0.651 to
0.839, and mAP@0.5:0.95 from 0.244 to 0.531. These improvements indicate
that the proposed difference-aware attention mechanism is effective for
enhancing small-ship representation in complex maritime backgrounds.

Compared with Transformer-based detectors, the proposed model also
achieves clear advantages. It improves mAP@0.5 by 0.156 over RT-DETR and
by 0.171 over DINO, showing that explicitly modeling target-background
differences is more suitable for the MASATI small-ship detection
scenario than directly applying generic end-to-end Transformer
detectors.

Compared with LiM-YOLO, a recent ship-specific detector, the proposed
method achieves higher Precision, Recall, and mAP@0.5 on MASATI.
Specifically, mAP@0.5 is improved from 0.821 to 0.839. However, LiM-YOLO
obtains a slightly higher mAP@0.5:0.95 than the proposed method. This
suggests that the proposed DMMA + ECA design is particularly effective
in improving target discovery and target-background discrimination,
while LiM-YOLO still shows advantages under stricter localization
thresholds. Overall, the proposed model provides the best mAP@0.5 on
MASATI and shows strong target discovery ability, while its strict
localization accuracy still has room for further improvement compared
with LiM-YOLO.

***4.3. Ablation Study on MASATI***

**Table 4.3 Ablation study of YOLOv12 variants on the MASATI dataset**

  **Model**              **DMMA**   **ECA**   **Precision**   **Recall**   **mAP@0.5**   **mAP@0.5:0.95**
  ---------------------- ---------- --------- --------------- ------------ ------------- ------------------
  YOLOv12 baseline                            0.736           0.649        0.628         0.222
  YOLOv12 + DMMA         Yes                  0.834           0.728        0.791         0.522
  YOLOv12 + DMMA + ECA   Yes        Yes       0.838           0.733        0.839         0.531

Table 4.3 reports the ablation results of different YOLOv12 variants on
MASATI. Compared with the original YOLOv12 baseline, the DMMA-only model
improves Precision from 0.736 to 0.834, Recall from 0.649 to 0.728,
mAP@0.5 from 0.628 to 0.791, and mAP@0.5:0.95 from 0.222 to 0.522. This
indicates that DMMA is the dominant contributor to the performance
improvement and is effective in enhancing the representation of small
ship targets under complex maritime backgrounds.

After adding ECA, the model further improves Precision from 0.834 to
0.838, Recall from 0.728 to 0.733, mAP@0.5 from 0.791 to 0.839, and
mAP@0.5:0.95 from 0.522 to 0.531. The relatively large improvement in
mAP@0.5 indicates that ECA is not merely a minor post-processing
refinement. In maritime remote sensing images, sea waves, wakes, and
shoreline textures may introduce redundant or misleading channel
responses. ECA helps recalibrate informative channels after DMMA-based
spatial interaction, thereby strengthening ship-related responses and
suppressing background-dominated feature channels. Therefore,
considering the overall performance under the current setting, YOLOv12 +
DMMA + ECA is selected as the final preferred configuration. It should
be noted that the current ablation mainly verifies the contribution of
DMMA and ECA at the module level. More fine-grained variants, such as
ECA-only, ordinary window attention without difference-aware gating, and
different insertion positions, will provide further evidence for the
specific contribution of each internal design.

***4.4. Supplementary Comparison on HRSC2016-MS***

**Table 4.4 Comparison with representative detectors on the HRSC2016-MS
dataset**

  **Method**   **Dataset**   **Precision**   **Recall**   **mAP@0.5**   **mAP@0.5:0.95**
  ------------ ------------- --------------- ------------ ------------- ------------------
  YOLOv8       HRSC2016-MS   0.720           0.534        0.622         0.363
  RT-DETR      HRSC2016-MS   0.734           0.519        0.595         0.432
  DINO         HRSC2016-MS   \-              \-           0.624         0.466
  LiM-YOLO     HRSC2016-MS   **0.859**       0.678        0.815         **0.607**
  Ours         HRSC2016-MS   0.817           **0.682**    **0.824**     0.538

To further evaluate the cross-dataset applicability of the proposed
method, supplementary experiments are conducted on HRSC2016-MS. As shown
in Table 4.4, the proposed YOLOv12 + DMMA + ECA model achieves a
Precision of 0.817, Recall of 0.682, mAP@0.5 of 0.824, and mAP@0.5:0.95
of 0.538. Compared with YOLOv8, the proposed method improves Recall by
0.148 and mAP@0.5 by 0.202. Compared with RT-DETR, it improves Recall by
0.163 and mAP@0.5 by 0.229. These results indicate that the proposed
difference-aware attention design generalizes well to another ship
detection dataset.

Compared with DINO, the proposed method improves mAP@0.5 from 0.624 to
0.824 and mAP@0.5:0.95 from 0.466 to 0.538, further confirming its
effectiveness over a strong DETR-style detection baseline. Compared with
LiM-YOLO, the proposed method achieves slightly higher Recall and
mAP@0.5, while LiM-YOLO obtains higher Precision and mAP@0.5:0.95. This
result indicates that the proposed method is more advantageous in target
discovery and moderate-IoU detection quality, whereas LiM-YOLO remains
stronger in strict localization accuracy. Overall, the HRSC2016-MS
results provide additional evidence that the proposed DMMA + ECA design
is effective across different maritime detection datasets.

***4.5. Complexity Analysis***

![](media/image7.png){width="1.667361111111111in"
height="2.238888888888889in"}In addition to accuracy, computational cost
is an important consideration for practical deployment. As shown in
Table 4.5, the baseline YOLOv12 model has relatively low complexity,
whereas introducing DMMA increases GFLOPs from 5.8 to 8.3, corresponding
to an increase of about 43%. This indicates that the main performance
gain of the proposed framework is achieved through stronger
attention-based feature interaction rather than through a substantial
increase in parameter count. By contrast, the additional ECA-style
channel refinement brings only marginal parameter and complexity
changes. Therefore, the proposed YOLOv12 + DMMA + ECA model should be
understood as an accuracy-oriented configuration for remote sensing
image analysis rather than a highly constrained real-time deployment
model. The reason for retaining the YOLOv12 framework is that it
provides a mature, efficient, and easily reproducible detection
pipeline, while DMMA selectively enhances the feature interaction stages
that are most affected by maritime clutter. This makes the method more
suitable for offline or near-real-time maritime surveillance, port
monitoring, and remote sensing interpretation scenarios where detection
reliability is prioritized over extreme lightweight inference. In future
evaluation, reporting FPS or single-image latency under the same
hardware platform would further clarify the practical speed-accuracy
trade-off of the proposed configuration.

Although the proposed method achieves the best mAP@0.5 on both MASATI
and HRSC2016-MS, its mAP@0.5:0.95 is slightly lower than that of
LiM-YOLO. This indicates that future work should further improve
high-IoU localization accuracy while maintaining the target-background
discrimination advantage brought by DMMA.

**Table 4.5 Complexity comparison of different YOLOv12 variants**

  **Method**             **Params (M)**   **GFLOPs**
  ---------------------- ---------------- ------------
  YOLOv12 baseline       2.112            5.8
  YOLOv12 + DMMA         2.509            8.3
  YOLOv12 + DMMA + ECA   2.509            8.3

***4.6. Visualization Analysis***

The qualitative results are consistent with the quantitative findings.
The baseline YOLOv12 model can detect most clear and medium-scale ships,
but it still misses small or visually weak targets when ships are
surrounded by waves, wakes, shoreline clutter, or low-contrast
sea-surface textures. After introducing DMMA, the detector becomes more
sensitive to these difficult small-ship instances because
difference-aware gating suppresses inconsistent background interactions
and strengthens target-background separability. After further adding the
ECA-style refinement module, the model shows more stable responses on
ship-related regions, suggesting that channel recalibration helps reduce
redundant activations caused by sea-surface texture patterns. However,
some boundary-level localization errors may still remain in scenes where
ship edges are mixed with wakes or wave structures, which is consistent
with the lower mAP@0.5:0.95 compared with LiM-YOLO.

**Figure 4.1 Qualitative comparison between different variants on the
MASATI dataset**

Therefore, both the quantitative and qualitative results indicate that
the combination of DMMA and ECA improves target discovery and response
stability in challenging maritime scenes, while stricter boundary
localization remains a direction for further improvement..

5\. Conclusion

In this paper, we presented a YOLOv12-based small-ship detection
framework for optical remote sensing images by integrating Difference
Mask Mixed Attention and ECA-style channel refinement. The proposed
method aims to improve target-background separability in complex
maritime scenes, where tiny ship targets are easily confused with
surrounding clutter such as waves, wakes, reefs, and shoreline textures.

Experiments on MASATI demonstrate that the proposed YOLOv12 + DMMA + ECA
model achieves a Precision of 0.838, Recall of 0.733, mAP@0.5 of 0.839,
and mAP@0.5:0.95 of 0.531. Compared with YOLOv8, RT-DETR, DINO, and
LiM-YOLO, the proposed method obtains the best Precision, Recall, and
mAP@0.5 on MASATI. Supplementary experiments on HRSC2016-MS further show
that the proposed method achieves the best Recall and mAP@0.5 among the
compared methods, with a Recall of 0.682 and mAP@0.5 of 0.824.

The experimental results indicate that DMMA is effective for enhancing
target-background discrimination and improving small-ship target
discovery, while ECA further strengthens channel-wise feature selection
by suppressing redundant maritime background responses. However, the
comparison with LiM-YOLO also shows that the proposed method still has
room for improvement under stricter localization metrics such as
mAP@0.5:0.95. In future work, we will investigate more efficient
difference-aware attention designs, boundary-aware regression
constraints, and localization-enhanced detection heads to further
improve high-IoU detection quality while maintaining strong target
discovery performance.

Acknowledgements

Acknowledgements and Reference heading should be left justified, bold,
with the first letter capitalized but have no numbers. Text below
continues as normal.

A.  An example appendix

Authors including an appendix section should do so before References
section. Multiple appendices should all have headings in the style used
above. They will automatically be ordered A, B, C etc.

1.  Example of a sub-heading within an appendix

There is also the option to include a subheading within the Appendix if
you wish.

References

Van der Geer, J., Hanraads, J. A. J., & Lupton, R. A. (2000). The art of
writing a scientific article. *Journal of Science Communication, 163*,
51--59.

Strunk, W., Jr., & White, E. B. (1979). *The elements of style* (3rd
ed.). New York: MacMillan.

Mettam, G. R., & Adams, L. B. (1999). How to prepare an electronic
version of your article. In B. S. Jones & R. Z. Smith (Eds.),
*Introduction to the electronic age* (pp. 281--304). New York:
E-Publishing Inc.

Fachinger, J., den Exter, M., Grambow, B., Holgerson, S., Landesmann,
C., Titov, M., et al. (2004). Behavior of spent HTR fuel elements in
aquatic phases of repository host rock formations, 2nd International
Topical Meeting on High Temperature Reactor Technology. Beijing, China,
paper \#B08.

Fachinger, J. (2006). Behavior of HTR fuel elements in aquatic phases of
repository host rock formations. *Nuclear Engineering & Design,* *236*,
54.
