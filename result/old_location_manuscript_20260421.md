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
|                      |                      | while preserving     |
|                      |                      | practical inference  |
|                      |                      | efficiency.          |
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
statistics with true ship regions. In parallel, ECA provides channel
reweighting to reinforce informative semantics and suppress redundant
maritime background responses.

The main contributions of this work are summarized as follows. First, we
propose a YOLOv12-based small-ship detection framework that introduces
Difference Mask Mixed Attention to strengthen target-background
separability in complex maritime scenes. Unlike generic attention
enhancement that mainly improves contextual aggregation, DMMA introduces
an auxiliary mask branch to construct normalized pairwise difference
cues and suppress token interactions that are inconsistent with ship
structures. This design is motivated by the observation that waves,
wakes, reefs, and shoreline textures may resemble ships locally, yet
remain inconsistent with true ship regions in structural continuity.
Second, we integrate an ECA-style channel refinement strategy into the
DMMA-enhanced feature extraction process to recalibrate channel-wise
responses and suppress redundant sea-surface texture activations with
limited computational burden. Third, comparison experiments are
conducted on MASATI and HRSC2016-MS against representative CNN-based,
Transformer-based, and ship-specific detectors, including YOLOv8,
RT-DETR, DINO, and LiM-YOLO, and ablation studies are further performed
to analyze the individual and complementary effects of DMMA and ECA. The
proposed model achieves the best mAP@0.5 on both datasets, indicating
its effectiveness in target discovery and target-background
discrimination for optical remote sensing ship detection.

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

To address the representation bottleneck of pure convolution, attention
mechanisms have been increasingly introduced into object detection.
Spatial attention and channel attention first demonstrated that adaptive
feature reweighting can suppress irrelevant responses and improve
detector focus. Subsequently, self-attention based modeling further
expanded receptive interaction by capturing long-range dependencies,
which is valuable when local appearance alone is ambiguous. In
high-resolution remote sensing scenarios, window-based self-attention is
particularly attractive because it provides a practical compromise
between contextual modeling and inference efficiency. This trend
establishes the theoretical basis for integrating mixed attention
structures into YOLO-style detectors for small-ship tasks.

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
offers a lightweight way to capture local cross-channel interaction with
a compact channel-interaction design. Compared with more complex
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
Therefore, merely strengthening generic attention is often insufficient
for small-ship detection in maritime imagery. The key challenge in this
task is not only the lack of long-range contextual interaction, but also
the existence of numerous background patterns that are locally salient
yet structurally inconsistent with real ships. The proposed DMMA is
designed for this specific failure mode: instead of only enhancing
contextual aggregation, it introduces normalized pairwise difference
cues to suppress misleading token interactions before attention
normalization. In this sense, the proposed design differs from generic
attention add-ons that mainly strengthen feature responses but do not
explicitly model target-background inconsistency in complex maritime
scenes. Motivated by this observation, we introduce a difference-aware
attention design that explicitly suppresses inconsistent token
interactions, and further couple it with lightweight channel refinement
to obtain a more targeted solution for small-ship detection in complex
maritime backgrounds.

1.  Method

![](media/image5.png){width="3.301388888888889in"
height="1.7986111111111112in"}This work proposes a YOLOv12-based
small-ship detector for optical remote sensing images. The framework is
centered on two coordinated components: Difference Mask Mixed Attention
(DMMA), which enhances target-background discrimination during
spatial-token interaction, and an ECA-style channel refinement module,
which improves channel-wise feature selection with limited additional
cost. The detector follows the standard backbone-neck-head paradigm of
YOLOv12, while replacing several key feature extraction and fusion units
with DMMA-enhanced modules to improve representation quality for
challenging small-ship scenarios. Figure 2.1 illustrates the overall
architecture of the proposed YOLOv12 + DMMA + ECA framework and
highlights the insertion positions of the DMMA-enhanced modules.

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

$$\Delta_{\text{ij}} = \frac{\left. \parallel M_{i} - M_{j} \right.\parallel_{1}}{\left. \parallel M_{j} \right.\parallel_{1} + \epsilon}$$

where $\epsilon$ is a small constant for numerical stability. The
difference cue is converted into a suppressive gate:

$$G_{\text{ij}} = 1 - \sigma(\Delta_{\text{ij}})$$

$$S = QK^{\top} + B_{\text{rel}} + M_{\text{sw}},$$

where $B_{\text{rel}}$ denotes the learnable relative position bias and
$M_{\text{sw}}$ is the shifted-window mask when window shifting is
enabled. DMMA injects the difference-aware gate into the attention
logits before softmax:

$${\widetilde{S}}_{\text{ij}} = \frac{S_{\text{ij}}}{\tau} \cdot (\eta G_{\text{ij}})$$

where $\tau$ is a learnable head-wise temperature parameter and $\eta$
is a learnable mask scaling factor. The learnable temperature avoids
manually fixing the strength of difference-aware suppression and allows
the model to adapt the gating intensity to different maritime scenes and
feature scales. The final attention map and output feature are obtained
by:

$$A_{\text{ij}} = \text{Softmax}_{j}({\widetilde{S}}_{\text{ij}}),\quad Y = AV$$

This design is not intended to simply amplify arbitrary feature
differences. Instead, the mask branch is jointly optimized with the
final detection objective and is expected to encode structure-related
contrast cues rather than an independent segmentation target. As a
result, large pairwise differences are more likely to appear when two
tokens belong to structurally inconsistent regions, such as
ship-to-wave, ship-to-wake, or ship-to-shoreline interactions, whereas
tokens within coherent ship regions tend to preserve relatively small
differences. The normalized L1 formulation reduces the influence of
absolute activation magnitude and makes the gate less sensitive to scale
variation across windows. Applying the difference-aware gate
multiplicatively to the attention logits directly rescales pairwise
affinity before softmax, so misleading interactions can be suppressed
while compatible interactions remain comparable within the same window.
The learnable temperature parameter and mask scaling factor further
allow the suppression strength to adapt across feature levels and
datasets, although a more systematic sensitivity analysis of these
![](media/image6.png){width="3.3180555555555555in"
height="1.6993055555555556in"}parameters will be investigated in future
work.

**Figure 2.2** []{#_Hlk227687700 .anchor}**Schematic illustration of the
DMMA block with ECA-based channel refinement**

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
structural burden compared with the main DMMA attention path, but it
helps recalibrate informative channels and suppress redundant
sea-surface texture responses. This is particularly useful in maritime
scenes, where wave and wake patterns may activate many background
channels and interfere with small-ship representations.

In implementation, the channel mask is applied to the DMMA attention
output and then combined with the shortcut connection of the original
block. This preserves the residual learning behavior of YOLOv12 while
allowing the ECA branch to emphasize discriminative channels with stable
residual learning behavior.

$$L = \lambda_{\text{box}}L_{\text{box}} + \lambda_{\text{cls}}L_{\text{cls}} + \lambda_{\text{dfl}}L_{\text{dfl}}$$

where $L_{\text{box}}$, $L_{\text{cls}}$, and $L_{\text{dfl}}$ denote
the box regression loss, classification loss, and distribution focal
loss, respectively, and $\lambda_{\text{box}}$, $\lambda_{\text{cls}}$,
and $\lambda_{\text{dfl}}$ are their corresponding balancing
coefficients. Under the single-class setting (nc = 1, ship), the
provided training configuration applies stronger localization emphasis,
such as a larger $\lambda_{\text{box}}$ , to suit tiny-target maritime
detection. In addition, augmentation strategies including mosaic, mixup,
copy-paste, and geometric perturbation are adopted to improve robustness
under appearance variation.

4\. Experiments

***4.1. Experimental Setup***

To evaluate the effectiveness of the proposed method, experiments were
mainly conducted on the MASATI dataset, which is widely used for
maritime ship detection, and supplementary evaluation was further
performed on HRSC2016-MS. Since the current task focuses on ship
detection only, the number of categories was set to one, namely ship.
Each dataset was divided into training, validation, and test subsets
according to the predefined split. For both MASATI and HRSC2016-MS, all
images were randomly split at the image level into training, validation,
and test subsets with a ratio of 8:1:1, corresponding to 80%, 10%, and
10% of the images, respectively. The same split was consistently used
for all compared methods to ensure fair evaluation.

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
Since the released DINO evaluation logs do not provide traditional
Precision values under a fixed confidence threshold, its Precision
entries are left blank in Tables 4.2 and 4.4. The available
recall-related quantity in DINO follows the official COCO evaluation
protocol and is reported as AR@100 rather than the conventional Recall
under a fixed confidence threshold. For completeness, the AR@100 values
are reported in the Recall column with an asterisk, namely 0.469\* on
MASATI and 0.731\* on HRSC2016-MS, corresponding to 46.9% and 73.1%,
respectively. The asterisk indicates that these values are not directly
comparable with the conventional Recall values of YOLOv8, RT-DETR,
LiM-YOLO, and the proposed method.

**Table 4.1** []{#_Hlk227687842 .anchor}**Experimental environment**

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

**Table 4.2** []{#_Hlk227688166 .anchor}**Comparison with representative
detectors on the MASATI dataset**

  **Method**   **Dataset**   **Precision**   **Recall**   **mAP@0.5**   **mAP@0.5:0.95**
  ------------ ------------- --------------- ------------ ------------- ------------------
  YOLOv8       MASATI        0.744           0.612        0.651         0.244
  RT-DETR      MASATI        0.775           0.683        0.683         0.255
  DINO         MASATI        \-              0.469\*      0.668         0.285
  LiM-YOLO     MASATI        0.825           0.724        0.821         **0.546**
  Ours         MASATI        **0.838**       **0.733**    **0.839**     0.531

Note: []{#_Hlk227688290 .anchor}The Recall value marked with \* for DINO
is AR@100 from the COCO evaluation protocol, not the conventional
fixed-confidence Recall. It is reported only as a reference and is not
used for direct Recall ranking.

Table 4.2 reports the comparison results on the MASATI dataset. Compared
with YOLOv8, the proposed YOLOv12 + DMMA + ECA model improves Precision
from 0.744 to 0.838, Recall from 0.612 to 0.733, mAP@0.5 from 0.651 to
0.839, and mAP@0.5:0.95 from 0.244 to 0.531. These improvements indicate
that the proposed difference-aware attention mechanism is effective for
enhancing small-ship representation in complex maritime backgrounds.

Compared with Transformer-based detectors, the proposed model also
achieves clear advantages in terms of mAP-based metrics. It improves
mAP@0.5 by 0.156 over RT-DETR and by 0.171 over DINO, showing that
explicitly modeling target-background differences is more suitable for
the MASATI small-ship detection scenario than directly applying generic
end-to-end Transformer detectors. It should be noted that the DINO
Recall value marked with \* is AR@100 under the COCO protocol and is
therefore not used for direct comparison with the conventional Recall
values of the other detectors.

Compared with LiM-YOLO, a recent ship-specific detector, the proposed
method achieves higher Precision, Recall, and mAP@0.5 on MASATI.
Specifically, mAP@0.5 is improved from 0.821 to 0.839, indicating that
the proposed DMMA + ECA design is effective at improving target
discovery and moderate-IoU detection quality in complex maritime
backgrounds. However, LiM-YOLO still achieves a higher mAP@0.5:0.95 than
the proposed method (0.546 versus 0.531). This result suggests that the
proposed model mainly benefits the separation between ships and
confusing background clutter, whereas strict localization under high IoU
thresholds depends more heavily on precise boundary and shape alignment.
In scenes where ship edges are mixed with wakes or wave structures,
difference-aware suppression may prioritize discriminative separation
over boundary completeness, which helps explain why the gain at mAP@0.5
is more pronounced than the gain at mAP@0.5:0.95. Overall, the proposed
model shows stronger target discovery ability on MASATI, while its
strict localization accuracy still has room for further improvement
compared with LiM-YOLO.

***4.3. Ablation Study on MASATI***

**Table 4.3** []{#_Hlk227688570 .anchor}**Ablation study of YOLOv12
variants on the MASATI dataset**

  **Model**              **DMMA**   **ECA**   **Precision**   **Recall**   **mAP@0.5**   **mAP@0.5:0.95**
  ---------------------- ---------- --------- --------------- ------------ ------------- ------------------
  YOLOv12 baseline       No         No        0.736           0.649        0.628         0.222
  YOLOv12 + ECA          No         Yes       0.745           0.653        0.671         0.319
  YOLOv12 + DMMA         Yes        No        0.834           0.728        0.791         0.522
  YOLOv12 + DMMA + ECA   Yes        Yes       0.838           0.733        0.839         0.531

Table 4.3 reports the ablation results of different YOLOv12 variants on
MASATI. Compared with the original YOLOv12 baseline, the ECA-only model
improves Precision from 0.736 to 0.745, Recall from 0.649 to 0.653,
mAP@0.5 from 0.628 to 0.671, and mAP@0.5:0.95 from 0.222 to 0.319. These
gains indicate that channel-wise redundancy indeed exists in maritime
ship detection, where sea-surface textures and clutter responses occupy
informative channels together with true ship features. Therefore,
lightweight channel recalibration alone can already filter part of the
redundant background information and improve feature selection.

After introducing DMMA, Precision increases to 0.834, Recall to 0.728,
mAP@0.5 to 0.791, and mAP@0.5:0.95 to 0.522. The magnitude of this
improvement is substantially larger than that of ECA alone, showing that
the dominant gain comes from explicitly modeling target-background
interaction rather than simply adding a lightweight attention branch.
This result supports the main design motivation of DMMA, namely that
suppressing structurally inconsistent token interactions is particularly
important for small-ship detection in cluttered maritime scenes.

When ECA is further combined with DMMA, the final YOLOv12 + DMMA + ECA
model achieves the best overall performance, with Precision of 0.838,
Recall of 0.733, mAP@0.5 of 0.839, and mAP@0.5:0.95 of 0.531. Compared
with the DMMA-only model, adding ECA further improves mAP@0.5 by 0.048
and mAP@0.5:0.95 by 0.009. This suggests that ECA should not be viewed
merely as a minor cosmetic refinement. Instead, DMMA first filters
structurally inconsistent spatial-token interactions and produces
cleaner discriminative features, after which ECA further consolidates
the gain by recalibrating informative channels and suppressing residual
sea-surface clutter responses. Overall, the current ablation results
support a clear division of labor: DMMA provides the principal
discrimination gain, while ECA acts as a complementary channel
refinement module with only a limited impact on inference speed.

***4.4. Supplementary Comparison on HRSC2016-MS***

**Table 4.4** [[]{#_Hlk227690068 .anchor}]{#_Hlk227688818
.anchor}**Comparison with representative detectors on the HRSC2016-MS
dataset**

  **Method**   **Dataset**   **Precision**   **Recall**   **mAP@0.5**   **mAP@0.5:0.95**
  ------------ ------------- --------------- ------------ ------------- ------------------
  YOLOv8       HRSC2016-MS   0.720           0.534        0.622         0.363
  RT-DETR      HRSC2016-MS   0.734           0.519        0.595         0.432
  DINO         HRSC2016-MS   \-              0.731\*      0.624         0.466
  LiM-YOLO     HRSC2016-MS   **0.859**       0.678        0.815         **0.607**
  Ours         HRSC2016-MS   0.817           **0.682**    **0.824**     0.538

Note: []{#_Hlk227688857 .anchor}The Recall value marked with \* for DINO
is AR@100 from the COCO evaluation protocol, not the conventional
fixed-confidence Recall. It is reported only as a reference and is not
used for direct Recall ranking.

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
effectiveness over a strong DETR-style detection baseline in terms of
mAP-based evaluation. The DINO Recall value marked with \* is AR@100
under the COCO protocol and is therefore reported only as a reference
rather than used for direct Recall ranking. Compared with LiM-YOLO, the
proposed method achieves slightly higher conventional Recall and
mAP@0.5, while LiM-YOLO obtains higher Precision and mAP@0.5:0.95. This
result is consistent with the observations on MASATI: the proposed DMMA
+ ECA design is more advantageous in target discovery and moderate-IoU
detection quality, whereas LiM-YOLO remains stronger in strict
localization accuracy. For small ship instances, high-IoU evaluation is
highly sensitive to slight deviations in box boundaries. Therefore, the
current results suggest that the proposed method mainly improves the
separability between ships and cluttered backgrounds, but its
localization precision under stricter thresholds still requires further
enhancement.

***4.5. Inference Speed Analysis***

In addition to detection accuracy, inference speed is an important
consideration for practical remote sensing applications. As shown in
Table 4.5, FPS is evaluated on the HRSC2016-MS dataset under the same
hardware and inference settings, and the reported values are
integer-rounded averages over three repeated runs. The baseline YOLOv12
model achieves 76 FPS, while the ECA-only variant achieves 74 FPS. After
introducing DMMA, the FPS reaches 72, and the final YOLOv12 + DMMA + ECA
model achieves 70 FPS. These results indicate that the proposed variants
maintain practical inference throughput on the RTX 4090 platform.
Although the FPS gradually decreases from 76 for the baseline model to
70 for the final YOLOv12 + DMMA + ECA variant, the overall speed
reduction remains limited, suggesting that the proposed attention
modules have only a minor impact on practical inference efficiency.
Therefore, the proposed YOLOv12 + DMMA + ECA model is suitable for
offline or near-real-time maritime surveillance, port monitoring, and
remote sensing interpretation scenarios where detection reliability and
practical throughput are both important.

Although the proposed method achieves the best mAP@0.5 on both MASATI
and HRSC2016-MS, its mAP@0.5:0.95 is still lower than that of LiM-YOLO.
This pattern indicates that DMMA and ECA mainly strengthen target
discovery and moderate-IoU detection quality by suppressing confusing
background interactions and enhancing ship-related responses. However,
high-IoU evaluation is more sensitive to tight boundary alignment. For
small ships, even slight deviations in box size, box extent, or edge
coverage can cause a noticeable IoU drop. When ship boundaries are
heavily mixed with wakes, wave crests, or shoreline textures, the
difference-aware suppression in DMMA may emphasize discriminative
separation more strongly than boundary completeness. This is beneficial
for classification confidence and recall, but is less sufficient for
very precise localization. Therefore, future improvements should focus
more on boundary-aware regression constraints or localization-enhanced
detection heads rather than further increasing global discrimination
alone.

**Table 4.5** []{#_Hlk227689004 .anchor}**Inference speed comparison of
different YOLOv12 variants on HRSC2016-MS**

  **Method**             **FPS**
  ---------------------- ---------
  YOLOv12 baseline       76
  YOLOv12 + ECA          74
  YOLOv12 + DMMA         72
  YOLOv12 + DMMA + ECA   70

***4.6. Visualization Analysis***

![](media/image7.png){width="2.171527777777778in"
height="2.9159722222222224in"}The qualitative results are consistent
with the quantitative findings. In the baseline YOLOv12 model, typical
failure cases include missed detections of tiny low-contrast ships,
false alarms on wake fragments or bright wave crests, and unstable
responses near shorelines or coastal clutter. After introducing DMMA,
many wake-like and wave-texture responses are visibly suppressed, while
weak ship instances become more detectable because the model focuses
more on structurally consistent ship regions instead of surrounding
clutter. After further adding the ECA-style refinement module,
activations on true ship regions become more concentrated and several
residual false responses are reduced, especially in scenes with
repetitive sea-surface textures. Nevertheless, failure cases still
remain when ship boundaries are heavily mixed with wakes or when
extremely small targets occupy only a few pixels, which is consistent
with the weaker mAP@0.5:0.95 performance relative to LiM-YOLO and
indicates that boundary-level localization remains the main limitation
of the current design.

**Figure 4.1** []{#_Hlk227689130 .anchor}**Qualitative comparison
between different variants on the MASATI dataset**

Therefore, both the quantitative and qualitative results indicate that
the combination of DMMA and ECA improves target discovery and response
stability in challenging maritime scenes, while stricter boundary
localization remains a direction for further improvement.

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
LiM-YOLO, the proposed method obtains the best Precision, conventional
Recall, and mAP@0.5 on MASATI. Supplementary experiments on HRSC2016-MS
further show that the proposed method achieves the best conventional
Recall among the methods with fixed-confidence Recall and the best
mAP@0.5 among all compared methods, with a Recall of 0.682 and mAP@0.5
of 0.824. The AR@100 values reported for DINO are marked with \* and are
not directly compared with conventional Recall. These results indicate
that the proposed design is particularly effective for target discovery
and moderate-IoU detection in complex maritime backgrounds.

The ablation study further shows that DMMA is the dominant source of
performance gain, while ECA acts as a complementary channel refinement
module that consolidates the improvement by suppressing residual
background responses. At the same time, the comparison with LiM-YOLO
shows that the proposed model is not uniformly superior under stricter
localization criteria, since its mAP@0.5:0.95 remains lower on both
datasets. Therefore, the present work should be viewed as a detection
framework that emphasizes target-background discrimination and reliable
target discovery rather than a solution that fully resolves high-IoU
localization.

In future work, more fine-grained mechanism validation, including
variants without difference-aware gating, different DMMA insertion
positions, and sensitivity analyses of the learnable temperature and
mask scaling factors, will be investigated. In addition, boundary-aware
regression constraints and localization-enhanced detection heads will be
explored to improve precise box alignment while preserving the current
gains in small-ship discovery.

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
