+-----------------------------------+-----------------------------------+
| Crossmark                         | ARTICLE TYPE                      |
|                                   |                                   |
| RECEIVED                          | Difference Mask Mixed Attention   |
|                                   | with ECA for Small-Ship Detection |
| dd Month Year                     | in Optical Remote Sensing Images  |
|                                   |                                   |
| REVISED                           | Shuai Yuan^1^, Haoze Shou^2^ and  |
|                                   | Author Name^1,2,\*^               |
| dd Month Year                     |                                   |
|                                   | ^1^ *School of Computer Science   |
| ACCEPTED                          | and Engineering, Shenyang Jianzhu |
|                                   | University, Shenyang 110168,      |
| dd Month Year                     | China*                            |
|                                   |                                   |
| PUBLISHED                         | ^2^ Affiliation                   |
|                                   |                                   |
| dd Month Year                     | \*Author to whom any              |
|                                   | correspondence should be          |
|                                   | addressed.                        |
|                                   |                                   |
|                                   | **E-mail:** reidyuan@163.com      |
|                                   |                                   |
|                                   | **Keywords:** Small ship          |
|                                   | detection, Optical remote         |
|                                   | sensing, YOLOv12, Difference Mask |
|                                   | Mixed Attention, Efficient        |
|                                   | Channel Attention                 |
|                                   |                                   |
|                                   | Abstract {#abstract .IOPP-Abstrac |
|                                   | tHeading}                         |
|                                   | ========                          |
|                                   |                                   |
|                                   | Small-ship detection in optical   |
|                                   | remote sensing images remains     |
|                                   | challenging because targets are   |
|                                   | usually tiny, visually weak, and  |
|                                   | easily confused with complex      |
|                                   | maritime backgrounds such as      |
|                                   | waves, wakes, reefs, and          |
|                                   | shoreline clutter. To address     |
|                                   | this problem, this paper proposes |
|                                   | a YOLOv12-based small-ship        |
|                                   | detector that integrates          |
|                                   | Difference Mask Mixed Attention   |
|                                   | (DMMA) with an ECA refinement     |
|                                   | module to improve                 |
|                                   | target-background discrimination  |
|                                   | and feature refinement. DMMA      |
|                                   | introduces normalized pairwise    |
|                                   | difference cues into window-based |
|                                   | self-attention and uses           |
|                                   | difference-aware gating to        |
|                                   | attenuate structurally            |
|                                   | inconsistent token interactions,  |
|                                   | while the ECA branch further      |
|                                   | recalibrates informative channels |
|                                   | with limited additional overhead. |
|                                   | Experiments on MASATI and         |
|                                   | HRSC2016-MS validate the          |
|                                   | effectiveness of the proposed     |
|                                   | design. The final YOLOv12 + DMMA  |
|                                   | + ECA model achieves 0.829        |
|                                   | mAP@0.5 and 0.545 mAP@0.5:0.95 on |
|                                   | MASATI, and 0.824 mAP@0.5 and     |
|                                   | 0.589 mAP@0.5:0.95 on             |
|                                   | HRSC2016-MS. Under the current    |
|                                   | evaluation setting, the proposed  |
|                                   | method achieves the highest       |
|                                   | mAP@0.5 on both datasets and the  |
|                                   | highest numerical values on the   |
|                                   | four directly comparable metrics  |
|                                   | on HRSC2016-MS among the main     |
|                                   | compared methods. These results   |
|                                   | suggest that the proposed         |
|                                   | difference-aware attention design |
|                                   | is effective for improving        |
|                                   | target-background separability    |
|                                   | and overall small-ship detection  |
|                                   | quality in optical remote sensing |
|                                   | imagery.                          |
|                                   |                                   |
|                                   | 1. Introduction {#introduction .I |
|                                   | OPP-H1}                           |
|                                   | ===============                   |
|                                   |                                   |
|                                   | Small-ship detection in optical   |
|                                   | remote sensing imagery remains a  |
|                                   | challenging small-object          |
|                                   | detection task with direct value  |
|                                   | for maritime surveillance, port   |
|                                   | operation analysis, and coastal   |
|                                   | security. In practical scenes,    |
|                                   | ships often occupy only a few     |
|                                   | pixels and are embedded in highly |
|                                   | dynamic backgrounds containing    |
|                                   | waves, reefs, cloud shadows, and  |
|                                   | shoreline clutter. These factors  |
|                                   | cause weak target saliency and    |
|                                   | high visual ambiguity, making     |
|                                   | detectors prone to missed         |
|                                   | detections and false alarms.      |
|                                   | Therefore, improving              |
|                                   | discriminative representation for |
|                                   | tiny maritime targets under       |
|                                   | complex backgrounds is a central  |
|                                   | problem in remote sensing vision. |
|                                   |                                   |
|                                   | Recent one-stage detectors        |
|                                   | provide an effective              |
|                                   | speed-accuracy trade-off, yet     |
|                                   | performance bottlenecks persist   |
|                                   | when object scale becomes         |
|                                   | extremely small and contextual    |
|                                   | interference becomes dominant. To |
|                                   | address this, we design a         |
|                                   | YOLOv12-based detector that       |
|                                   | couples efficient global-local    |
|                                   | attention with lightweight        |
|                                   | channel refinement. The model is  |
|                                   | built around a Difference Mask    |
|                                   | Mixed Attention (DMMA) mechanism  |
|                                   | and an Efficient Channel          |
|                                   | Attention (ECA) strategy to       |
|                                   | improve target-background         |
|                                   | discrimination and feature        |
|                                   | representation for small ship     |
|                                   | detection.                        |
|                                   |                                   |
|                                   | The key motivation of DMMA is not |
|                                   | only to aggregate context, but to |
|                                   | make target-background            |
|                                   | separability explicit during      |
|                                   | feature interaction. By           |
|                                   | explicitly modeling feature-level |
|                                   | structural contrast between       |
|                                   | ship-related tokens and confusing |
|                                   | maritime background tokens, DMMA  |
|                                   | encourages the network to         |
|                                   | emphasize edge-consistent and     |
|                                   | structure-consistent responses    |
|                                   | while suppressing texture noise   |
|                                   | from sea clutter. This            |
|                                   | difference-aware design is        |
|                                   | especially important in maritime  |
|                                   | imagery, where many hard          |
|                                   | negatives share similar intensity |
|                                   | statistics with true ship         |
|                                   | regions. In parallel, ECA         |
|                                   | provides channel reweighting to   |
|                                   | reinforce informative semantics   |
|                                   | and suppress redundant maritime   |
|                                   | background responses.             |
|                                   |                                   |
|                                   | The main contributions of this    |
|                                   | work are summarized as follows.   |
|                                   | First, we propose a YOLOv12-based |
|                                   | small-ship detection framework    |
|                                   | that introduces Difference Mask   |
|                                   | Mixed Attention to strengthen     |
|                                   | target-background separability in |
|                                   | complex maritime scenes. Unlike   |
|                                   | generic attention enhancement     |
|                                   | modules that mainly improve       |
|                                   | contextual aggregation or feature |
|                                   | reweighting, DMMA explicitly      |
|                                   | models normalized pairwise        |
|                                   | structural inconsistency through  |
|                                   | an auxiliary mask branch and uses |
|                                   | it to attenuate misleading token  |
|                                   | interactions before attention     |
|                                   | normalization. This design is     |
|                                   | motivated by the observation that |
|                                   | waves, wakes, reefs, and          |
|                                   | shoreline textures may resemble   |
|                                   | ships locally, yet remain         |
|                                   | inconsistent with true ship       |
|                                   | regions in structural continuity. |
|                                   | Second, we integrate an ECA       |
|                                   | refinement module into the        |
|                                   | DMMA-enhanced feature extraction  |
|                                   | process to recalibrate            |
|                                   | channel-wise responses and        |
|                                   | suppress redundant sea-surface    |
|                                   | texture activations with limited  |
|                                   | computational burden. Third,      |
|                                   | comparison experiments are        |
|                                   | conducted on MASATI and           |
|                                   | HRSC2016-MS against               |
|                                   | representative CNN-based,         |
|                                   | Transformer-based, and            |
|                                   | ship-specific detectors,          |
|                                   | including YOLOv8, RT-DETR, DINO,  |
|                                   | LiM-YOLO, and FBVF-YOLO, and      |
|                                   | ablation studies are further      |
|                                   | performed to analyze the          |
|                                   | individual and complementary      |
|                                   | effects of DMMA and ECA. The      |
|                                   | proposed model achieves the best  |
|                                   | mAP@0.5 on both datasets,         |
|                                   | indicating its effectiveness in   |
|                                   | target discovery and              |
|                                   | target-background discrimination  |
|                                   | for optical remote sensing ship   |
|                                   | detection.                        |
|                                   |                                   |
|                                   | **2. Related work**               |
|                                   |                                   |
|                                   | Object detection has evolved from |
|                                   | traditional handcrafted-feature   |
|                                   | pipelines to deep learning based  |
|                                   | end-to-end detectors. Among       |
|                                   | modern detectors, the YOLO family |
|                                   | has become a representative       |
|                                   | one-stage route because it offers |
|                                   | an effective balance between      |
|                                   | detection accuracy, inference     |
|                                   | speed, and engineering usability. |
|                                   | With continuous improvements in   |
|                                   | backbone design, multi-scale      |
|                                   | feature fusion, training          |
|                                   | strategy, and detection head      |
|                                   | formulation, YOLO-style           |
|                                   | frameworks have become widely     |
|                                   | used in practical remote sensing  |
|                                   | applications, where               |
|                                   | high-throughput processing and    |
|                                   | flexible architectural            |
|                                   | modification are both important.  |
|                                   |                                   |
|                                   | For optical remote sensing ship   |
|                                   | detection, however, the task      |
|                                   | difficulty is not determined only |
|                                   | by detector efficiency. Compared  |
|                                   | with natural-image benchmarks,    |
|                                   | maritime scenes usually contain   |
|                                   | larger observation ranges, weaker |
|                                   | target saliency, and stronger     |
|                                   | background interference. Small    |
|                                   | ships are often mixed with wakes, |
|                                   | waves, reefs, shoreline textures, |
|                                   | and illumination fluctuation,     |
|                                   | which leads to high visual        |
|                                   | similarity between true targets   |
|                                   | and hard negatives. Under these   |
|                                   | conditions, repeated downsampling |
|                                   | and convolution-dominated local   |
|                                   | aggregation may weaken fine       |
|                                   | structural cues, making detectors |
|                                   | prone to missed detections, false |
|                                   | alarms, and unstable recall.      |
|                                   | Therefore, improving the          |
|                                   | discriminative representation of  |
|                                   | tiny ships under cluttered        |
|                                   | maritime backgrounds remains a    |
|                                   | central problem in this field.    |
|                                   |                                   |
|                                   | To overcome the representation    |
|                                   | bottleneck of pure convolution,   |
|                                   | attention mechanisms have been    |
|                                   | increasingly introduced into      |
|                                   | detection networks. Early spatial |
|                                   | and channel attention modules     |
|                                   | demonstrated that adaptive        |
|                                   | feature reweighting can suppress  |
|                                   | irrelevant responses and improve  |
|                                   | detector focus. Later,            |
|                                   | self-attention based modeling     |
|                                   | further expanded contextual       |
|                                   | interaction by capturing          |
|                                   | long-range dependencies, which is |
|                                   | especially valuable when local    |
|                                   | appearance is ambiguous. In       |
|                                   | high-resolution remote sensing    |
|                                   | imagery, window-based attention   |
|                                   | is particularly attractive        |
|                                   | because it offers a practical     |
|                                   | compromise between contextual     |
|                                   | modeling capability and           |
|                                   | computational cost. These         |
|                                   | developments provide the          |
|                                   | methodological basis for          |
|                                   | integrating mixed attention       |
|                                   | structures into YOLO-style        |
|                                   | detectors for small-object        |
|                                   | detection.                        |
|                                   |                                   |
|                                   | Nevertheless, most existing       |
|                                   | attention-based enhancement       |
|                                   | modules are still designed as     |
|                                   | general-purpose feature boosters  |
|                                   | rather than mechanisms explicitly |
|                                   | tailored to maritime ambiguity.   |
|                                   | In optical remote sensing ship    |
|                                   | detection, many false responses   |
|                                   | arise not only from insufficient  |
|                                   | context, but also from locally    |
|                                   | salient yet structurally          |
|                                   | inconsistent background patterns, |
|                                   | such as wakes, wave textures, and |
|                                   | coastal interference. This means  |
|                                   | that merely strengthening generic |
|                                   | attention is often insufficient.  |
|                                   | The key challenge is to identify  |
|                                   | and suppress misleading token     |
|                                   | interactions between true ship    |
|                                   | regions and confusing background  |
|                                   | structures. Motivated by this     |
|                                   | observation, the proposed DMMA    |
|                                   | introduces normalized pairwise    |
|                                   | difference cues to model          |
|                                   | target-background inconsistency   |
|                                   | and attenuate misleading token    |
|                                   | interactions before attention     |
|                                   | normalization, while an ECA       |
|                                   | refinement module is used to      |
|                                   | recalibrate channel responses     |
|                                   | with limited extra cost. In this  |
|                                   | way, the proposed method is       |
|                                   | positioned not as a generic       |
|                                   | attention add-on, but as a        |
|                                   | task-oriented design for          |
|                                   | improving target-background       |
|                                   | separability in complex maritime  |
|                                   | scenes.                           |
|                                   |                                   |
|                                   | **3. Method**                     |
|                                   |                                   |
|                                   | This work proposes a              |
|                                   | YOLOv12-based small-ship detector |
|                                   | for optical remote sensing        |
|                                   | images. The framework is centered |
|                                   | on two coordinated components:    |
|                                   | Difference Mask Mixed Attention   |
|                                   | (DMMA), which enhances            |
|                                   | target-background discrimination  |
|                                   | during spatial-token interaction, |
|                                   | and an ECA refinement module,     |
|                                   | which improves channel-wise       |
|                                   | feature selection with limited    |
|                                   | additional cost. The detector     |
|                                   | follows the standard              |
|                                   | backbone-neck-head paradigm of    |
|                                   | YOLOv12, while replacing several  |
|                                   | key feature extraction and fusion |
|                                   | units with DMMA-enhanced modules  |
|                                   | to improve representation quality |
|                                   | for challenging small-ship        |
|                                   | scenarios. Figure 1 illustrates   |
|                                   | the overall architecture of the   |
|                                   | proposed YOLOv12 + DMMA + ECA     |
|                                   | framework and highlights the      |
|                                   | insertion positions of the        |
|                                   | DMMA-enhanced modules.            |
|                                   |                                   |
|                                   | ![](media/image1.png){width="6.18 |
|                                   | 8976377952756in"                  |
|                                   | height="1.5361111111111112in"}fig |
|                                   | ure1                              |
|                                   |                                   |
|                                   | The overall network follows a     |
|                                   | backbone-neck-head paradigm. In   |
|                                   | the backbone, shallow and         |
|                                   | intermediate stages generate      |
|                                   | hierarchical features, while the  |
|                                   | deeper P4 and P5 stages introduce |
|                                   | DMMA-enhanced feature extraction  |
|                                   | (C2fDMMA) to strengthen           |
|                                   | long-range dependency modeling in |
|                                   | cluttered maritime scenes. In the |
|                                   | neck, a top-down and bottom-up    |
|                                   | bidirectional fusion path is      |
|                                   | used, and C2fDMMA blocks are      |
|                                   | inserted into the key P3 and P4   |
|                                   | feature-fusion nodes to reduce    |
|                                   | semantic dilution during scale    |
|                                   | transfer. In the head,            |
|                                   | predictions are produced from the |
|                                   | YOLOv12 detection scales,         |
|                                   | enabling a balance between detail |
|                                   | preservation and semantic         |
|                                   | robustness. This design keeps the |
|                                   | original YOLOv12 detection        |
|                                   | pipeline while replacing selected |
|                                   | feature extraction and fusion     |
|                                   | units with difference-aware       |
|                                   | attention blocks.                 |
|                                   |                                   |
|                                   | Inside each DMMA block, the input |
|                                   | feature map is first partitioned  |
|                                   | into non-overlapping windows, and |
|                                   | each window is processed by       |
|                                   | multi-head self-attention. For an |
|                                   | input feature                     |
|                                   | $X \in \mathbb{R}^{B \times H \ti |
|                                   | mes W \times C}$,                 |
|                                   | the window partition operation    |
|                                   | produces                          |
|                                   | $X_{w} \in \mathbb{R}^{(B \cdot N |
|                                   | _{w}) \times N \times C}$,        |
|                                   | where $N = w^{2}$ is the number   |
|                                   | of tokens in each window. A       |
|                                   | linear projection is then used to |
|                                   | generate four branches, namely    |
|                                   | query, key, value, and mask       |
|                                   | features:                         |
|                                   |                                   |
|                                   | $$\lbrack Q,K,V,M\rbrack = Linear |
|                                   | (X_{w}).$$                        |
|                                   |                                   |
|                                   | For the i-th and j-th tokens in   |
|                                   | the same window, the mask branch  |
|                                   | is used to construct a normalized |
|                                   | pairwise difference cue:          |
|                                   |                                   |
|                                   | $$\Delta_{\text{ij}} = \frac{\lef |
|                                   | t. \parallel M_{i} - M_{j} \right |
|                                   | .\parallel_{1}}{\left. \parallel  |
|                                   | M_{j} \right.\parallel_{1} + \eps |
|                                   | ilon}$$                           |
|                                   |                                   |
|                                   | where $\epsilon$ is a small       |
|                                   | constant for numerical stability. |
|                                   | The difference cue is then        |
|                                   | converted into a difference-aware |
|                                   | attenuation gate:                 |
|                                   |                                   |
|                                   | $$G_{\text{ij}} = 1 - \sigma(\Del |
|                                   | ta_{\text{ij}})$$                 |
|                                   |                                   |
|                                   | $$S = QK^{\top} + B_{\text{rel}}  |
|                                   | + M_{\text{sw}},$$                |
|                                   |                                   |
|                                   | where $B_{\text{rel}}$ denotes    |
|                                   | the learnable relative position   |
|                                   | bias and $M_{\text{sw}}$ is the   |
|                                   | shifted-window mask when window   |
|                                   | shifting is enabled. DMMA injects |
|                                   | the difference-aware gate into    |
|                                   | the attention logits before       |
|                                   | softmax:                          |
|                                   |                                   |
|                                   | $${\widetilde{S}}_{\text{ij}} = \ |
|                                   | frac{S_{\text{ij}}}{\tau} \cdot ( |
|                                   | \eta G_{\text{ij}})$$             |
|                                   |                                   |
|                                   | where $\tau$ is a learnable       |
|                                   | head-wise temperature parameter   |
|                                   | and $\eta$ is a learnable mask    |
|                                   | scaling factor. The learnable     |
|                                   | temperature avoids manually       |
|                                   | fixing the strength of            |
|                                   | difference-aware modulation and   |
|                                   | allows the model to adapt the     |
|                                   | gating intensity to different     |
|                                   | maritime scenes and feature       |
|                                   | scales. The final attention map   |
|                                   | and output feature are obtained   |
|                                   | by:                               |
|                                   |                                   |
|                                   | $$A_{\text{ij}} = \text{Softmax}_ |
|                                   | {j}({\widetilde{S}}_{\text{ij}}), |
|                                   | \quad Y = AV$$                    |
|                                   |                                   |
|                                   | This design is not intended to    |
|                                   | simply amplify arbitrary feature  |
|                                   | differences. Instead, the mask    |
|                                   | branch is jointly optimized with  |
|                                   | the final detection objective and |
|                                   | is expected to encode             |
|                                   | structure-related contrast cues   |
|                                   | rather than raw pixel differences |
|                                   | or an independent segmentation    |
|                                   | target. As a result, large        |
|                                   | pairwise differences are more     |
|                                   | likely to appear when two tokens  |
|                                   | belong to structurally            |
|                                   | inconsistent regions, such as     |
|                                   | ship-to-wave, ship-to-wake, or    |
|                                   | ship-to-shoreline interactions,   |
|                                   | whereas tokens within coherent    |
|                                   | ship regions tend to produce      |
|                                   | relatively smaller difference     |
|                                   | cues. The normalized L1           |
|                                   | formulation reduces the influence |
|                                   | of absolute activation magnitude  |
|                                   | and alleviates over-sensitivity   |
|                                   | to local intensity or             |
|                                   | illumination variation, so the    |
|                                   | gate focuses more on relative     |
|                                   | structural inconsistency than on  |
|                                   | raw response scale.               |
|                                   |                                   |
|                                   | Under the present                 |
|                                   | parameterization,                 |
|                                   | $G_{\text{ij}} \in (0,0.5\rbrack$ |
|                                   | because                           |
|                                   | $\Delta_{\text{ij}} \geq 0$.      |
|                                   | Therefore, the gate should be     |
|                                   | interpreted as a relative         |
|                                   | attenuation coefficient rather    |
|                                   | than a binary keep-or-remove      |
|                                   | mask: structurally more           |
|                                   | consistent interactions receive   |
|                                   | the least attenuation under this  |
|                                   | formulation, whereas interactions |
|                                   | associated with larger structural |
|                                   | inconsistency are attenuated more |
|                                   | strongly. The overall modulation  |
|                                   | magnitude is jointly controlled   |
|                                   | by $\eta$ and $\tau$, so the gate |
|                                   | does not act alone as the         |
|                                   | absolute scale of attention.      |
|                                   |                                   |
|                                   | Applying the difference-aware     |
|                                   | gate multiplicatively to the      |
|                                   | attention logits provides a       |
|                                   | content-adaptive rescaling of     |
|                                   | pairwise affinity before softmax. |
|                                   | In this sense, the formulation is |
|                                   | used to attenuate misleading      |
|                                   | interactions on average before    |
|                                   | attention normalization, rather   |
|                                   | than to guarantee strict          |
|                                   | pointwise suppression for every   |
|                                   | gated logit under all sign        |
|                                   | conditions. In practice, the      |
|                                   | design is intended to reduce the  |
|                                   | competition strength of           |
|                                   | structurally inconsistent         |
|                                   | interactions during softmax       |
|                                   | normalization while preserving    |
|                                   | the original attention form and   |
|                                   | implementation simplicity. A more |
|                                   | systematic comparison with other  |
|                                   | gating forms, such as additive    |
|                                   | bias based formulations, will be  |
|                                   | investigated in future work.      |
|                                   |                                   |
|                                   | Figure2                           |
|                                   |                                   |
|                                   | ![](media/image2.png){width="6.31 |
|                                   | 9444444444445in"                  |
|                                   | height="4.770833333333333in"}To   |
|                                   | complement the difference-aware   |
|                                   | spatial-token interaction, each   |
|                                   | DMMA layer further includes an    |
|                                   | ECA refinement module. Given an   |
|                                   | input feature map                 |
|                                   | $F \in \mathbb{R}^{B \times C \ti |
|                                   | mes H \times W}$,                 |
|                                   | global average pooling and global |
|                                   | max pooling are first applied to  |
|                                   | obtain compact channel            |
|                                   | descriptors. These descriptors    |
|                                   | are then processed by lightweight |
|                                   | one-dimensional convolution along |
|                                   | the channel dimension to model    |
|                                   | local cross-channel interaction:  |
|                                   |                                   |
|                                   | $$z = Conv1D(GAP(F)) + Conv1D(GMP |
|                                   | (F)).$$                           |
|                                   |                                   |
|                                   | The channel weights are obtained  |
|                                   | by sigmoid activation:            |
|                                   |                                   |
|                                   | $$w = \sigma(z),$$                |
|                                   |                                   |
|                                   | $$F' = F \odot w.$$               |
|                                   |                                   |
|                                   | This channel refinement branch    |
|                                   | introduces only negligible        |
|                                   | additional structural burden      |
|                                   | compared with the main DMMA       |
|                                   | attention path, but it helps      |
|                                   | recalibrate informative channels  |
|                                   | and suppress redundant            |
|                                   | sea-surface texture responses.    |
|                                   | This is particularly useful in    |
|                                   | maritime scenes, where wave and   |
|                                   | wake patterns may activate many   |
|                                   | background channels and interfere |
|                                   | with small-ship representations.  |
|                                   |                                   |
|                                   | In implementation, the channel    |
|                                   | mask is applied to the DMMA       |
|                                   | attention output and then         |
|                                   | combined with the shortcut        |
|                                   | connection of the original block. |
|                                   | This preserves the residual       |
|                                   | learning behavior of YOLOv12      |
|                                   | while allowing the ECA branch to  |
|                                   | emphasize discriminative channels |
|                                   | with stable residual learning     |
|                                   | behavior.                         |
|                                   |                                   |
|                                   | $$L = \lambda_{\text{box}}L_{\tex |
|                                   | t{box}} + \lambda_{\text{cls}}L_{ |
|                                   | \text{cls}} + \lambda_{\text{dfl} |
|                                   | }L_{\text{dfl}}$$                 |
|                                   |                                   |
|                                   | where $L_{\text{box}}$,           |
|                                   | $L_{\text{cls}}$, and             |
|                                   | $L_{\text{dfl}}$ denote the box   |
|                                   | regression loss, classification   |
|                                   | loss, and distribution focal      |
|                                   | loss, respectively, and           |
|                                   | $\lambda_{\text{box}}$,           |
|                                   | $\lambda_{\text{cls}}$, and       |
|                                   | $\lambda_{\text{dfl}}$ are their  |
|                                   | corresponding balancing           |
|                                   | coefficients. Under the           |
|                                   | single-class setting (nc = 1,     |
|                                   | ship), the provided training      |
|                                   | configuration applies stronger    |
|                                   | localization emphasis, such as a  |
|                                   | larger $\lambda_{\text{box}}$ ,   |
|                                   | to suit tiny-target maritime      |
|                                   | detection. In addition,           |
|                                   | augmentation strategies including |
|                                   | mosaic, mixup, copy-paste, and    |
|                                   | geometric perturbation are        |
|                                   | adopted to improve robustness     |
|                                   | under appearance variation.       |
|                                   |                                   |
|                                   | **4. Experiments**                |
|                                   |                                   |
|                                   | **4.1. *Experimental Setup***     |
|                                   |                                   |
|                                   | To evaluate the effectiveness of  |
|                                   | the proposed method, experiments  |
|                                   | were mainly conducted on the      |
|                                   | MASATI dataset, which is widely   |
|                                   | used for maritime ship detection, |
|                                   | and supplementary evaluation was  |
|                                   | further performed on HRSC2016-MS. |
|                                   | Since the current task focuses on |
|                                   | ship detection only, the number   |
|                                   | of categories was set to one,     |
|                                   | namely ship. When oriented        |
|                                   | annotations were present in the   |
|                                   | source data, they were converted  |
|                                   | to enclosing horizontal boxes for |
|                                   | unified training and evaluation   |
|                                   | with the compared horizontal      |
|                                   | detectors. In the HRSC2016-MS     |
|                                   | experiments, the evaluation was   |
|                                   | conducted under the horizontal    |
|                                   | bounding-box detection setting    |
|                                   | adopted in this study, so all     |
|                                   | compared results were organized   |
|                                   | under the same box                |
|                                   | representation. Each dataset was  |
|                                   | divided into training,            |
|                                   | validation, and test subsets      |
|                                   | according to the split protocol   |
|                                   | adopted in this study. MASATI was |
|                                   | split at the image level into     |
|                                   | training, validation, and test    |
|                                   | subsets with 1422, 473, and 473   |
|                                   | images, respectively,             |
|                                   | corresponding to an approximate   |
|                                   | 6:2:2 partition under the current |
|                                   | study setting. HRSC2016-MS        |
|                                   | followed the predefined ImageSets |
|                                   | split adopted in this study, with |
|                                   | 610 training images, 460          |
|                                   | validation images, and 610 test   |
|                                   | images. These splits were fixed   |
|                                   | and consistently reused for all   |
|                                   | compared methods to ensure fair   |
|                                   | evaluation under the same data    |
|                                   | partition. Dataset statistics and |
|                                   | split details are summarized in   |
|                                   | Table 1, including image numbers, |
|                                   | train/validation/test counts,     |
|                                   | class setting, annotation         |
|                                   | representation, and the split     |
|                                   | protocol used in this study.      |
|                                   |                                   |
|                                   | Table1                            |
|                                   |                                   |
|                                   | All experiments were carried out  |
|                                   | in a Linux-based training         |
|                                   | environment equipped with an      |
|                                   | NVIDIA GeForce RTX 4090 GPU with  |
|                                   | 24 GB memory. The model           |
|                                   | development and code modification |
|                                   | were completed in a Windows       |
|                                   | environment, while the training   |
|                                   | and evaluation procedures were    |
|                                   | executed on Linux. The deep       |
|                                   | learning framework was based on   |
|                                   | PyTorch 2.2.2 with CUDA 11.8, and |
|                                   | the implementation was built on   |
|                                   | PyTorch and the Ultralytics       |
|                                   | detection framework, with         |
|                                   | YOLOv12x serving as the baseline  |
|                                   | architecture.                     |
|                                   |                                   |
|                                   | For the ablation study, all       |
|                                   | YOLOv12 variants were trained     |
|                                   | under the same settings. The      |
|                                   | optimizer was AdamW, the initial  |
|                                   | learning rate was set to 0.001,   |
|                                   | the final learning rate factor    |
|                                   | was 0.01, and the weight decay    |
|                                   | was 0.05. The total number of     |
|                                   | epochs was 150, the batch size    |
|                                   | was 6, and the input image size   |
|                                   | was 640 × 640. In addition,       |
|                                   | mosaic, mixup, and copy-paste     |
|                                   | augmentation strategies were      |
|                                   | adopted to improve robustness for |
|                                   | small target detection. The main  |
|                                   | evaluation metrics included       |
|                                   | Precision, Recall, mAP@0.5, and   |
|                                   | mAP@0.5:0.95. Unless otherwise    |
|                                   | stated, the comparisons within    |
|                                   | the YOLOv12 family used the same  |
|                                   | optimizer, training schedule,     |
|                                   | input resolution, and             |
|                                   | augmentation settings.            |
|                                   |                                   |
|                                   | For comparison with               |
|                                   | representative detection          |
|                                   | frameworks, YOLOv8 is selected as |
|                                   | a mature one-stage CNN-based      |
|                                   | detector, RT-DETR is selected as  |
|                                   | a real-time end-to-end            |
|                                   | Transformer detector, and DINO is |
|                                   | selected as a strong DETR-style   |
|                                   | end-to-end detection baseline. In |
|                                   | addition, LiM-YOLO is included as |
|                                   | a recent ship-specific detector   |
|                                   | designed for optical remote       |
|                                   | sensing ship detection, while     |
|                                   | FBVF-YOLO is further introduced   |
|                                   | as a recent remote-sensing        |
|                                   | super-tiny-object detection       |
|                                   | method published in 2025. These   |
|                                   | methods provide complementary     |
|                                   | baselines from general-purpose    |
|                                   | real-time detection,              |
|                                   | Transformer-based detection,      |
|                                   | task-specific ship detection, and |
|                                   | recent remote-sensing tiny-object |
|                                   | detection perspectives.           |
|                                   |                                   |
|                                   | To ensure a fair comparison, all  |
|                                   | YOLOv12-series ablations and all  |
|                                   | external baselines were           |
|                                   | reproduced by the authors under   |
|                                   | the same data split, optimizer,   |
|                                   | training schedule, input          |
|                                   | resolution, augmentation          |
|                                   | settings, and evaluation protocol |
|                                   | in this study. In other words,    |
|                                   | all compared methods were         |
|                                   | re-trained and re-evaluated under |
|                                   | the present experimental setting  |
|                                   | rather than directly copied from  |
|                                   | previously reported numbers.      |
|                                   | Therefore, the comparison results |
|                                   | in this paper should be           |
|                                   | interpreted as strictly           |
|                                   | controlled reproduced results     |
|                                   | under a unified experimental      |
|                                   | protocol.                         |
|                                   |                                   |
|                                   | For DINO, conventional            |
|                                   | fixed-threshold Precision and     |
|                                   | Recall are not reported in this   |
|                                   | paper because the reproduced      |
|                                   | COCO-style evaluation output does |
|                                   | not provide directly comparable   |
|                                   | values under the same             |
|                                   | confidence-threshold definition   |
|                                   | used for the other detectors.     |
|                                   | Therefore, DINO is compared only  |
|                                   | using mAP-based metrics in Tables |
|                                   | 3 and 5.                          |
|                                   |                                   |
|                                   | Table2                            |
|                                   |                                   |
|                                   | **4.2. *Comparison with           |
|                                   | Representative Detectors on       |
|                                   | MASATI***                         |
|                                   |                                   |
|                                   | To further evaluate the           |
|                                   | effectiveness of the proposed     |
|                                   | method, we compare it with        |
|                                   | representative detectors on the   |
|                                   | MASATI dataset, including YOLOv8, |
|                                   | RT-DETR, DINO, LiM-YOLO, and      |
|                                   | FBVF-YOLO. YOLOv8 is selected as  |
|                                   | a mature one-stage CNN-based      |
|                                   | detector, RT-DETR and DINO        |
|                                   | represent Transformer-based       |
|                                   | end-to-end detection frameworks,  |
|                                   | LiM-YOLO is a recent              |
|                                   | ship-specific detector designed   |
|                                   | for optical remote sensing        |
|                                   | imagery, and FBVF-YOLO is a       |
|                                   | recent remote-sensing             |
|                                   | super-tiny-object detector.       |
|                                   |                                   |
|                                   | Table3                            |
|                                   |                                   |
|                                   | Table 3 reports the comparison    |
|                                   | results on the MASATI dataset.    |
|                                   | Compared with YOLOv8, the         |
|                                   | proposed YOLOv12 + DMMA + ECA     |
|                                   | model improves Precision from     |
|                                   | 0.754 to 0.838, Recall from 0.632 |
|                                   | to 0.733, mAP@0.5 from 0.651 to   |
|                                   | 0.829, and mAP@0.5:0.95 from      |
|                                   | 0.244 to 0.545. Compared with     |
|                                   | RT-DETR, the proposed model       |
|                                   | improves mAP@0.5 by 0.146 and     |
|                                   | mAP@0.5:0.95 by 0.290. Compared   |
|                                   | with DINO, it improves mAP@0.5 by |
|                                   | 0.161 and mAP@0.5:0.95 by 0.260.  |
|                                   | Compared with FBVF-YOLO, a recent |
|                                   | remote-sensing super-tiny-object  |
|                                   | detector, it further improves     |
|                                   | Precision by 0.037, Recall by     |
|                                   | 0.044, mAP@0.5 by 0.074, and      |
|                                   | mAP@0.5:0.95 by 0.075. These      |
|                                   | results indicate that the         |
|                                   | proposed difference-aware         |
|                                   | attention design is effective for |
|                                   | enhancing small-ship              |
|                                   | representation in complex         |
|                                   | maritime backgrounds. In the      |
|                                   | current MASATI comparison, the    |
|                                   | DINO Precision and Recall entries |
|                                   | are left blank because directly   |
|                                   | comparable fixed-threshold values |
|                                   | are not available in the present  |
|                                   | tabulation, and its result is     |
|                                   | therefore discussed only through  |
|                                   | mAP-based metrics.                |
|                                   |                                   |
|                                   | Compared with LiM-YOLO, a recent  |
|                                   | ship-specific detector, the       |
|                                   | proposed method achieves higher   |
|                                   | Precision, Recall, mAP@0.5, and   |
|                                   | mAP@0.5:0.95 on MASATI.           |
|                                   | Specifically, mAP@0.5 is improved |
|                                   | from 0.821 to 0.829 and           |
|                                   | mAP@0.5:0.95 is improved from     |
|                                   | 0.536 to 0.545, indicating that   |
|                                   | the proposed DMMA + ECA design    |
|                                   | improves both target discovery    |
|                                   | and stricter localization quality |
|                                   | on MASATI. This result suggests   |
|                                   | that the proposed method not only |
|                                   | separates ships from confusing    |
|                                   | background clutter effectively,   |
|                                   | but also preserves sufficient     |
|                                   | structural information for        |
|                                   | moderate-to-high IoU evaluation   |
|                                   | in this dataset. Overall, under   |
|                                   | the present evaluation setting,   |
|                                   | the proposed model achieves the   |
|                                   | highest numerical results on      |
|                                   | MASATI among the compared         |
|                                   | methods.                          |
|                                   |                                   |
|                                   | **4.3. *Ablation Study on         |
|                                   | MASATI***                         |
|                                   |                                   |
|                                   | ***Table4***                      |
|                                   |                                   |
|                                   | Table 4 reports the ablation and  |
|                                   | mechanism-validation results of   |
|                                   | different YOLOv12 variants on     |
|                                   | MASATI. Compared with the         |
|                                   | original YOLOv12 baseline, the    |
|                                   | ECA-only model improves Precision |
|                                   | from 0.766 to 0.773, Recall from  |
|                                   | 0.649 to 0.653, mAP@0.5 from      |
|                                   | 0.668 to 0.671, and mAP@0.5:0.95  |
|                                   | from 0.379 to 0.393. These gains  |
|                                   | indicate that channel-wise        |
|                                   | redundancy indeed exists in       |
|                                   | maritime ship detection, where    |
|                                   | sea-surface textures and clutter  |
|                                   | responses occupy informative      |
|                                   | channels together with true ship  |
|                                   | features.                         |
|                                   |                                   |
|                                   | When the difference-aware gate is |
|                                   | removed while retaining the       |
|                                   | auxiliary branch, the YOLOv12 +   |
|                                   | DMMA w/o difference gate model    |
|                                   | reaches 0.806 Precision, 0.693    |
|                                   | Recall, 0.775 mAP@0.5, and 0.467  |
|                                   | mAP@0.5:0.95. Although this       |
|                                   | configuration is better than the  |
|                                   | baseline and the ECA-only model,  |
|                                   | it remains notably inferior to    |
|                                   | the complete DMMA design,         |
|                                   | suggesting that the observed gain |
|                                   | is not explained solely by the    |
|                                   | additional branch or parameter    |
|                                   | increase, but is mainly           |
|                                   | associated with the               |
|                                   | difference-aware gating design    |
|                                   | itself.                           |
|                                   |                                   |
|                                   | The insertion-position ablations  |
|                                   | further show that DMMA is         |
|                                   | effective in both backbone and    |
|                                   | neck, but its contribution is not |
|                                   | uniform across stages. The        |
|                                   | backbone-only variant achieves    |
|                                   | 0.817 Precision, 0.696 Recall,    |
|                                   | 0.799 mAP@0.5, and 0.489          |
|                                   | mAP@0.5:0.95, whereas the         |
|                                   | neck-only variant improves these  |
|                                   | metrics to 0.831, 0.713, 0.819,   |
|                                   | and 0.525, respectively. This     |
|                                   | suggests that for small-ship      |
|                                   | detection, applying DMMA in the   |
|                                   | feature-fusion stages contributes |
|                                   | more directly to                  |
|                                   | target-background discrimination, |
|                                   | because the neck operates on      |
|                                   | semantically richer multi-scale   |
|                                   | features that are closer to the   |
|                                   | final detection decision.         |
|                                   |                                   |
|                                   | Notably, the neck-only variant    |
|                                   | slightly surpasses the standalone |
|                                   | DMMA-only setting on mAP@0.5 and  |
|                                   | mAP@0.5:0.95, indicating that     |
|                                   | simply extending DMMA to more     |
|                                   | stages does not automatically     |
|                                   | yield the best result when        |
|                                   | channel refinement is absent. A   |
|                                   | plausible explanation is that     |
|                                   | early-stage modulation in the     |
|                                   | backbone may introduce stronger   |
|                                   | feature perturbation before       |
|                                   | semantic fusion, whereas          |
|                                   | neck-side deployment more         |
|                                   | directly benefits the fused       |
|                                   | representations used by the       |
|                                   | detector. Therefore, the backbone |
|                                   | + neck design should be           |
|                                   | understood as the most suitable   |
|                                   | configuration for the final DMMA  |
|                                   | + ECA model, rather than as a     |
|                                   | universal guarantee that a        |
|                                   | standalone DMMA-only variant must |
|                                   | outperform neck-only deployment.  |
|                                   | This also indicates that DMMA     |
|                                   | deployment is position-sensitive  |
|                                   | rather than monotonically         |
|                                   | beneficial when used without the  |
|                                   | stabilizing effect of the ECA     |
|                                   | refinement branch.                |
|                                   |                                   |
|                                   | Compared with the DMMA-only       |
|                                   | model, introducing the ECA-based  |
|                                   | channel refinement module         |
|                                   | substantially improves            |
|                                   | performance. The fixed τ / η      |
|                                   | variant achieves 0.835 Precision, |
|                                   | 0.728 Recall, 0.825 mAP@0.5, and  |
|                                   | 0.543 mAP@0.5:0.95, while the     |
|                                   | complete YOLOv12 + DMMA + ECA     |
|                                   | model reaches 0.838 Precision,    |
|                                   | 0.733 Recall, 0.829 mAP@0.5, and  |
|                                   | 0.545 mAP@0.5:0.95. These two     |
|                                   | configurations are close under    |
|                                   | the current setting, but the      |
|                                   | complete YOLOv12 + DMMA + ECA     |
|                                   | model achieves slightly better    |
|                                   | results on all four metrics. This |
|                                   | suggests that learnable τ and η   |
|                                   | provide a modest but consistent   |
|                                   | benefit under the present MASATI  |
|                                   | evaluation setting. More          |
|                                   | importantly, both variants remain |
|                                   | clearly stronger than the         |
|                                   | DMMA-only model, indicating that  |
|                                   | the main observed gain beyond the |
|                                   | baseline still comes from the     |
|                                   | combination of difference-aware   |
|                                   | attention and channel refinement. |
|                                   |                                   |
|                                   | **4.4. *Supplementary Comparison  |
|                                   | on HRSC2016-MS under Horizontal   |
|                                   | Bounding-Box Evaluation***        |
|                                   |                                   |
|                                   | ***Table5***                      |
|                                   |                                   |
|                                   | To further evaluate the           |
|                                   | cross-dataset applicability of    |
|                                   | the proposed method,              |
|                                   | supplementary experiments are     |
|                                   | conducted on HRSC2016-MS by       |
|                                   | comparing the proposed model with |
|                                   | YOLOv8, RT-DETR, DINO, LiM-YOLO,  |
|                                   | and FBVF-YOLO under the           |
|                                   | horizontal bounding-box           |
|                                   | evaluation setting adopted in     |
|                                   | this study. Therefore, the HBB    |
|                                   | results reported in this study    |
|                                   | should not be directly compared   |
|                                   | with oriented-bounding-box        |
|                                   | results in previous HRSC2016      |
|                                   | literature. As shown in Table 5,  |
|                                   | the proposed YOLOv12 + DMMA + ECA |
|                                   | model achieves a Precision of     |
|                                   | 0.837, Recall of 0.728, mAP@0.5   |
|                                   | of 0.824, and mAP@0.5:0.95 of     |
|                                   | 0.589. Compared with YOLOv8, the  |
|                                   | proposed method improves          |
|                                   | Precision by 0.117, Recall by     |
|                                   | 0.194, mAP@0.5 by 0.202, and      |
|                                   | mAP@0.5:0.95 by 0.226. Compared   |
|                                   | with RT-DETR, it improves         |
|                                   | Precision by 0.103, Recall by     |
|                                   | 0.209, mAP@0.5 by 0.229, and      |
|                                   | mAP@0.5:0.95 by 0.157. These      |
|                                   | results indicate that the         |
|                                   | proposed difference-aware         |
|                                   | attention design shows promising  |
|                                   | cross-dataset applicability on    |
|                                   | another ship-detection dataset.   |
|                                   |                                   |
|                                   | Compared with DINO, the proposed  |
|                                   | method improves mAP@0.5 from      |
|                                   | 0.624 to 0.824 and mAP@0.5:0.95   |
|                                   | from 0.466 to 0.589, suggesting   |
|                                   | competitive effectiveness         |
|                                   | relative to a strong DETR-style   |
|                                   | detection baseline in terms of    |
|                                   | mAP-based evaluation. In this     |
|                                   | paper, DINO is compared only      |
|                                   | through mAP-based metrics because |
|                                   | directly comparable               |
|                                   | fixed-threshold Precision and     |
|                                   | Recall values are not available   |
|                                   | under the same evaluation         |
|                                   | definition.                       |
|                                   |                                   |
|                                   | Compared with FBVF-YOLO, the      |
|                                   | proposed method improves          |
|                                   | Precision from 0.828 to 0.837,    |
|                                   | Recall from 0.714 to 0.728,       |
|                                   | mAP@0.5 from 0.819 to 0.824, and  |
|                                   | mAP@0.5:0.95 from 0.555 to 0.589. |
|                                   | Compared with LiM-YOLO, the       |
|                                   | proposed method improves          |
|                                   | Precision from 0.836 to 0.837,    |
|                                   | Recall from 0.678 to 0.728,       |
|                                   | mAP@0.5 from 0.815 to 0.824, and  |
|                                   | mAP@0.5:0.95 from 0.567 to 0.589. |
|                                   | Therefore, under the current      |
|                                   | unified evaluation setting, the   |
|                                   | proposed method achieves the      |
|                                   | highest numerical values on the   |
|                                   | four directly comparable metrics  |
|                                   | on HRSC2016-MS among YOLOv8,      |
|                                   | RT-DETR, LiM-YOLO, FBVF-YOLO, and |
|                                   | the proposed model itself. This   |
|                                   | result suggests that, under the   |
|                                   | current HBB evaluation setting,   |
|                                   | the proposed DMMA + ECA design    |
|                                   | improves both target discovery    |
|                                   | and stricter localization quality |
|                                   | on this dataset, rather than only |
|                                   | improving moderate-IoU detection  |
|                                   | quality. In addition, the         |
|                                   | mechanism-oriented ablations on   |
|                                   | HRSC2016-MS show the same overall |
|                                   | trend as those on MASATI:         |
|                                   | removing the difference-aware     |
|                                   | gate degrades the performance to  |
|                                   | 0.801 Precision, 0.690 Recall,    |
|                                   | 0.778 mAP@0.5, and 0.542          |
|                                   | mAP@0.5:0.95; using fixed τ and η |
|                                   | yields 0.835 Precision, 0.717     |
|                                   | Recall, 0.818 mAP@0.5, and 0.582  |
|                                   | mAP@0.5:0.95; backbone-only       |
|                                   | deployment gives 0.816 Precision, |
|                                   | 0.695 Recall, 0.792 mAP@0.5, and  |
|                                   | 0.554 mAP@0.5:0.95; and neck-only |
|                                   | deployment improves the results   |
|                                   | to 0.834 Precision, 0.717 Recall, |
|                                   | 0.816 mAP@0.5, and 0.575          |
|                                   | mAP@0.5:0.95, while the full      |
|                                   | configuration remains the best.   |
|                                   | This consistency further supports |
|                                   | that the difference-aware gate is |
|                                   | the dominant source of            |
|                                   | improvement, that the neck        |
|                                   | contributes more than the         |
|                                   | backbone when DMMA is used alone, |
|                                   | and that learnable τ and η        |
|                                   | provide additional but smaller    |
|                                   | gains.                            |
|                                   |                                   |
|                                   | **4.5. *Complexity and Inference  |
|                                   | Speed Analysis***                 |
|                                   |                                   |
|                                   | In addition to detection          |
|                                   | accuracy, computational cost and  |
|                                   | inference speed are important     |
|                                   | considerations for practical      |
|                                   | remote sensing applications. As   |
|                                   | shown in Table 6, the baseline    |
|                                   | YOLOv12x model contains 59.1M     |
|                                   | parameters and 199.0G FLOPs,      |
|                                   | while achieving 76 FPS on         |
|                                   | HRSC2016-MS. All FPS values were  |
|                                   | measured on the same RTX 4090     |
|                                   | platform under the same           |
|                                   | HRSC2016-MS evaluation pipeline   |
|                                   | at an input size of 640 × 640,    |
|                                   | and each reported value is the    |
|                                   | integer-rounded average of three  |
|                                   | repeated runs. According to the   |
|                                   | current Ultralytics validation    |
|                                   | pipeline used in this study,      |
|                                   | model warmup is performed before  |
|                                   | timed evaluation, and speed       |
|                                   | statistics are accumulated on a   |
|                                   | per-image basis across            |
|                                   | preprocess, inference, and        |
|                                   | postprocess stages. Unless        |
|                                   | otherwise specified, the default  |
|                                   | validation configuration uses     |
|                                   | standard detect postprocessing    |
|                                   | with IoU threshold 0.7 and half   |
|                                   | precision disabled, i.e. FP32     |
|                                   | evaluation. Because the present   |
|                                   | benchmark record does not         |
|                                   | separately log batch size,        |
|                                   | isolated NMS-only latency, or     |
|                                   | explicit CUDA synchronization     |
|                                   | settings, these items are not     |
|                                   | further claimed here. After       |
|                                   | introducing DMMA and ECA related  |
|                                   | modules, the complexity increases |
|                                   | moderately: the no-gate variant   |
|                                   | and the full model both contain   |
|                                   | 62.7M parameters and 215.4G       |
|                                   | FLOPs, the fixed τ /η variant     |
|                                   | also keeps 62.7M parameters and   |
|                                   | 215.4G FLOPs, the backbone-only   |
|                                   | variant contains 60.7M parameters |
|                                   | and 211.9G FLOPs, and the         |
|                                   | neck-only variant contains 61.2M  |
|                                   | parameters and 213.9G FLOPs. In   |
|                                   | terms of speed, the corresponding |
|                                   | FPS values are 71, 70, 74, 73,    |
|                                   | and 70, respectively.             |
|                                   |                                   |
|                                   | These results show that the       |
|                                   | proposed mechanism-oriented       |
|                                   | variants bring only moderate      |
|                                   | computational overhead relative   |
|                                   | to the baseline, while            |
|                                   | maintaining practical inference   |
|                                   | throughput on the RTX 4090        |
|                                   | platform. Among the position      |
|                                   | ablations, backbone-only and      |
|                                   | neck-only are slightly lighter    |
|                                   | and faster than the full          |
|                                   | configuration, which is           |
|                                   | consistent with their reduced     |
|                                   | DMMA deployment scope. At the     |
|                                   | same time, the full model offers  |
|                                   | a favorable accuracy-cost         |
|                                   | trade-off under the current       |
|                                   | evaluation setting, with only a   |
|                                   | limited FPS reduction from 76 to  |
|                                   | 70.                               |
|                                   |                                   |
|                                   | Under the updated HRSC2016-MS     |
|                                   | evaluation results, the proposed  |
|                                   | full model achieves the best      |
|                                   | values on all four directly       |
|                                   | comparable metrics among the main |
|                                   | compared methods. Combined with   |
|                                   | the complexity results, this      |
|                                   | suggests that the DMMA + ECA      |
|                                   | design offers a reasonable        |
|                                   | accuracy-cost balance for remote  |
|                                   | sensing ship detection under      |
|                                   | cluttered maritime scenes,        |
|                                   | especially when detection         |
|                                   | robustness is prioritized over    |
|                                   | extreme lightweight deployment.   |
|                                   |                                   |
|                                   | Table6                            |
|                                   |                                   |
|                                   | **4.6. *Visualization Analysis*** |
|                                   |                                   |
|                                   | The qualitative results are       |
|                                   | consistent with the quantitative  |
|                                   | findings and help clarify where   |
|                                   | the main gains come from. In the  |
|                                   | baseline YOLOv12 model, typical   |
|                                   | failure cases include false       |
|                                   | negatives on tiny low-contrast    |
|                                   | ships, false positives on wake    |
|                                   | fragments and bright wave crests, |
|                                   | and unstable predictions near     |
|                                   | shorelines or coastal clutter.    |
|                                   | After introducing DMMA, the most  |
|                                   | visible change is the attenuation |
|                                   | of background responses that are  |
|                                   | structurally inconsistent with    |
|                                   | ship regions: many wake-like and  |
|                                   | wave-texture activations are      |
|                                   | weakened, and several previously  |
|                                   | missed weak ship instances become |
|                                   | detectable. After further adding  |
|                                   | the ECA-based channel refinement  |
|                                   | module, true ship responses       |
|                                   | become more concentrated and some |
|                                   | residual false alarms are further |
|                                   | reduced, especially in scenes     |
|                                   | with repetitive sea-surface       |
|                                   | textures. From a qualitative      |
|                                   | perspective, the main gains       |
|                                   | therefore appear to come from two |
|                                   | aspects: fewer false alarms on    |
|                                   | cluttered maritime backgrounds    |
|                                   | and better recovery of weak true  |
|                                   | positives for tiny ships.         |
|                                   |                                   |
|                                   | Nevertheless, failure cases still |
|                                   | remain when ship boundaries are   |
|                                   | heavily mixed with wakes or when  |
|                                   | extremely small targets occupy    |
|                                   | only a few pixels. These residual |
|                                   | errors suggest that the current   |
|                                   | improvements are driven mainly by |
|                                   | better target-background          |
|                                   | discrimination and response       |
|                                   | stabilization, whereas            |
|                                   | fine-grained boundary             |
|                                   | localization under highly         |
|                                   | ambiguous maritime textures       |
|                                   | remains more challenging. This    |
|                                   | interpretation is consistent with |
|                                   | the quantitative results, which   |
|                                   | show clear gains in overall       |
|                                   | detection quality while still     |
|                                   | leaving room for further          |
|                                   | boundary-level refinement.        |
|                                   |                                   |
|                                   | ![](media/image3.png){width="6.18 |
|                                   | 8888888888889in"                  |
|                                   | height="1.5361111111111112in"}Fig |
|                                   | ure3                              |
|                                   |                                   |
|                                   | Therefore, both the quantitative  |
|                                   | and qualitative results indicate  |
|                                   | that the combination of DMMA and  |
|                                   | ECA improves target discovery and |
|                                   | response stability in challenging |
|                                   | maritime scenes, while stricter   |
|                                   | boundary localization remains a   |
|                                   | direction for further             |
|                                   | improvement.                      |
|                                   |                                   |
|                                   | **5. Conclusion**                 |
|                                   |                                   |
|                                   | In this paper, we presented a     |
|                                   | YOLOv12-based small-ship          |
|                                   | detection framework for optical   |
|                                   | remote sensing images by          |
|                                   | integrating Difference Mask Mixed |
|                                   | Attention and an ECA-based        |
|                                   | channel refinement module. The    |
|                                   | proposed method aims to improve   |
|                                   | target-background separability in |
|                                   | complex maritime scenes, where    |
|                                   | tiny ship targets are easily      |
|                                   | confused with surrounding clutter |
|                                   | such as waves, wakes, reefs, and  |
|                                   | shoreline textures.               |
|                                   |                                   |
|                                   | Experiments on MASATI demonstrate |
|                                   | that the proposed YOLOv12 + DMMA  |
|                                   | + ECA model achieves a Precision  |
|                                   | of 0.838, Recall of 0.733,        |
|                                   | mAP@0.5 of 0.829, and             |
|                                   | mAP@0.5:0.95 of 0.545. Compared   |
|                                   | with YOLOv8, RT-DETR, DINO,       |
|                                   | LiM-YOLO, and FBVF-YOLO, the      |
|                                   | proposed method obtains the       |
|                                   | highest conventional Precision,   |
|                                   | Recall, mAP@0.5, and mAP@0.5:0.95 |
|                                   | on MASATI under the current       |
|                                   | reproduced comparison setting.    |
|                                   | Supplementary experiments on      |
|                                   | HRSC2016-MS further show that the |
|                                   | proposed method achieves a        |
|                                   | Precision of 0.837, Recall of     |
|                                   | 0.728, mAP@0.5 of 0.824, and      |
|                                   | mAP@0.5:0.95 of 0.589. On this    |
|                                   | dataset, under the updated        |
|                                   | unified evaluation results, the   |
|                                   | proposed method achieves the      |
|                                   | highest numerical values on the   |
|                                   | four directly comparable metrics  |
|                                   | among YOLOv8, RT-DETR, LiM-YOLO,  |
|                                   | FBVF-YOLO, and the proposed model |
|                                   | itself, namely Precision, Recall, |
|                                   | mAP@0.5, and mAP@0.5:0.95. DINO   |
|                                   | is compared only through          |
|                                   | mAP-based metrics in this paper   |
|                                   | because directly comparable       |
|                                   | fixed-threshold Precision and     |
|                                   | Recall values are not available   |
|                                   | under the same evaluation         |
|                                   | definition. These results suggest |
|                                   | that the proposed design is       |
|                                   | effective for target discovery    |
|                                   | and overall detection performance |
|                                   | in complex maritime backgrounds.  |
|                                   |                                   |
|                                   | The ablation study further shows  |
|                                   | that DMMA is the dominant source  |
|                                   | of performance gain, while ECA    |
|                                   | acts as a complementary channel   |
|                                   | refinement module that helps      |
|                                   | consolidate the improvement by    |
|                                   | suppressing residual background   |
|                                   | responses. The expanded           |
|                                   | mechanism-ablation results        |
|                                   | further indicate that the         |
|                                   | difference-aware gate is the main |
|                                   | source of improvement, that       |
|                                   | neck-side deployment is more      |
|                                   | effective than backbone-only      |
|                                   | deployment when DMMA is used      |
|                                   | alone, and that the learnable     |
|                                   | temperature and mask scaling      |
|                                   | factors provide modest additional |
|                                   | gains under the current setting.  |
|                                   | Overall, the present work should  |
|                                   | be viewed as a task-oriented      |
|                                   | detection framework that improves |
|                                   | target-background discrimination  |
|                                   | and target discovery for          |
|                                   | small-ship detection in complex   |
|                                   | maritime scenes, while still      |
|                                   | leaving room for future           |
|                                   | refinement in fine-grained        |
|                                   | boundary localization.            |
|                                   |                                   |
|                                   | In future work, we will further   |
|                                   | investigate more detailed         |
|                                   | sensitivity analyses of window    |
|                                   | size and head configuration,      |
|                                   | richer response visualization for |
|                                   | the difference-aware suppression  |
|                                   | mechanism, and stronger           |
|                                   | boundary-aware regression         |
|                                   | constraints together with         |
|                                   | localization-enhanced detection   |
|                                   | heads to further improve precise  |
|                                   | box alignment while preserving    |
|                                   | the current gains in small-ship   |
|                                   | discovery.                        |
|                                   |                                   |
|                                   | Acknowledgements {#acknowledgemen |
|                                   | ts .IOPP-H1}                      |
|                                   | ================                  |
|                                   |                                   |
|                                   | Proin pharetra nonummy pede.      |
|                                   | Mauris et orci. Aenean nec lorem. |
|                                   | In porttitor. Donec laoreet       |
|                                   | nonummy augue. Suspendisse dui    |
|                                   | purus, scelerisque at, vulputate  |
|                                   | vitae, pretium mattis, nunc.      |
|                                   | Mauris eget neque at sem          |
|                                   | venenatis eleifend. Ut nonummy.   |
|                                   |                                   |
|                                   | References {#references .IOPP-H1} |
|                                   | ==========                        |
|                                   |                                   |
|                                   | 1.  Surname A, Surname B and      |
|                                   |     Surname C 2015 *Journal Name* |
|                                   |     **37** 074203                 |
|                                   |                                   |
|                                   | 2.  Surname A and Surname B 2009  |
|                                   |     *Journal Name* **23** 544     |
+-----------------------------------+-----------------------------------+
