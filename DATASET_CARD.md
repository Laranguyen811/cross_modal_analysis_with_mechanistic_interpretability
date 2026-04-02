# 📊 Consolidated Data Card & Acknowledgments  
**Repository:** `understand_multimodal_models`

This document provides unified metadata, licensing details, ethical considerations, and usage notes for all external datasets used in this cross‑modal analysis suite. It is designed for transparency, reproducibility, and ease of auditing.

---

## 1. Dataset Summaries

High‑level overview of dataset scale, modality, and original research intent.

| Dataset | Type | Size | Original Motivation | Primary Tasks |
|--------|------|------|---------------------|----------------|
| **MS COCO** | Vision & Language | 330K images; 2.5M labeled instances | Advance vision research with realistic, contextual images | Object Detection, Segmentation, Captioning |
| **CIFAR‑10** | Vision (32×32) | 60,000 images | Benchmark for small‑scale deep learning models | Image Classification (10 classes) |
| **Visual Genome** | Vision & Structured Language | 108K images; 5.4M region descriptions | Connect structured linguistic knowledge to visual imagery | VQA, Scene Graph Generation, Phrase Grounding |

---

## 2. Legal and Ethical Considerations

When publishing work using this suite, **the following citations and license acknowledgments are mandatory**.

| Dataset | License | Required Citation | Source | Known Limitations / Biases |
|--------|----------|------------------|---------|-----------------------------|
| **MS COCO** | CC BY 4.0 | Lin et al. (2014), *Microsoft COCO: Common Objects in Context*, ECCV | cocodataset.org | Western‑centric object distribution; annotator subjectivity |
| **CIFAR‑10** | MIT License | Krizhevsky (2009), *Learning Multiple Layers of Features…* | cs.toronto.edu | Low resolution; limited real‑world diversity |
| **Visual Genome** | CC BY 4.0 | Krishna et al. (2017), *Visual Genome*, IJCV | visualgenome.org | Flickr‑sourced bias; inconsistent annotation quality |

> **Note:** MS COCO and Visual Genome images originate from Flickr and remain subject to their original copyright terms.

---

## 3. Project Risks & Mitigation

Identified risks relevant to multimodal evaluation and the mitigation strategies implemented in this repository.

| Dataset | Identified Risk | Mitigation Strategy in This Suite |
|--------|------------------|-----------------------------------|
| **MS COCO** | Geographic bias → underperformance on non‑Western scenes. Caption subjectivity | Evaluate on dedicated OOD test sets; avoid global generalisation claims. Use all 5 captions per image to reduce annotator‑specific linguistic bias |
| **CIFAR‑10** | Oversimplification → poor transfer to real‑world images | Restrict usage to Proof-of-Concept (PoC), debugging, and encoder sanity‑checks |
| **Visual Genome** | Noisy / vague region descriptions | Pre‑filter descriptions <5 words to ensure meaningful grounding signals |

---

## 4. Project Use

How each dataset is processed and integrated into the codebase.

| Dataset | Usage Description |
|--------|--------------------|
| **MS COCO** | Uses 2017 Train/Val splits. Used for cross‑modal analysis. |
| **CIFAR‑10** | Serves as a lightweight, preliminary cross-modal analysis. |
| **Visual Genome** | Extracts region descriptions and relationships in each image to train fine‑grained grounding and relational reasoning, and understand how and why multimodal models behave in different specific tasks in certain manners. |

---

## Citation

If you use this repository, please cite the original datasets as listed above and consider referencing this project:
@misc{understand_multimodal_models, author = {Lara}, title = {Cross-Modal Understanding and Evaluation Suite}, year = {2026}, note = {GitHub Repository} }

---
