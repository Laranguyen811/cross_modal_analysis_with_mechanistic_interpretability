
# Understanding Multimodal Models
AI systems that can process multiple data types —like images, text, and audio combined—are the future. But there is a problem: we do not understand how they work internally as well as we grasp Large Language Models (LLMs).
While researchers have progressed in understanding text-only AI models, multimodal models (those handling multiple data types) remain more mysterious. As Balasubramanian et al. (2025) point out, our ability to interpret these models lags despite their growing importance.

This repository helps our technically minded community better understand multimodal models, including exploring cross-modal representations through the lens of mechanistic interpretability. What is mechanistic interpretability? It is a technique of finding a specific algorithm or computation that a model learns during training. They can use this repository to detect misalignment in AI. What does misalignment mean? Misalignment in AI refers to artificial intelligence systems that fail to align with human values, goals, or intentions. It is designed for iterative experimentation, diagnostic clarity, and reproducible workflows. My cross-modal analysis is exploratory research with loosely formulated hypotheses, less strict testing and fewer details about experimental design. 

## 🔍 Project Overview

- Investigates how mechanistic interpretability techniques can be applied to cross-modal understanding.
- Supports modular experimentation across modalities (e.g., image, text, audio).

## 🧭 Branching Philosophy

This repository uses `dev` as the **default branch** to reflect its active, research-oriented development. Stable releases and polished modules will be merged into `main` when ready.

- `dev`: Active development, experimental features, evolving structure.
- `main`: Reserved for stable, documented releases.

## 🛠️ Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/Laranguyen811/cross_modal_analysis_with_mechanistic_interpretability.git
   cd cross_modal_analysis_with_mechanistic_interpretability
   python -m venv .venv
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1  # On Windows PowerShell
   
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
## 📁 Repository Structure
    
    ├── Cross-modal Analysis with Mechanistic Interpretability.py
    ├── ViT-Prisma/                      # Submodule for ViT-based interpretability
    ├── data/                            # Placeholder for input datasets
    ├── notebooks/                       # Jupyter notebooks for exploratory analysis
    ├── README.md
    └── requirements.txt

## 🧪 Current Experiments
- Layer-wise probing of ViT attention heads across modalities
- Alignment metrics between image and text embeddings
- Mechanistic tracing of feature propagation in multimodal fusion
## 🤝 Contributing
This project is in active development. Contributions are welcome, especially around:
- Mechanistic interpretability techniques
- Cross-modal evaluation datasets
- Visualisation tools for internal model states

Please open an issue or pull request with your ideas.
## 🧠 Design
I am designing this platform based on user feedback and research. Please feel free to email me at laranguyen811@gmail.com. Alternatively, please create an issue for the repository. 

## 📜 License
This repository is licensed under the MIT License. See LICENSE for details.

## 🌱 Ethical Framing
This work is guided by principles of public-good impact, transparency, sustainability and multispecies justice. It aims to advance interpretability in AI systems while remaining accountable to broader ecological and social contexts.

## 🙏 Acknowledgments
Inspired by ongoing work in AI safety, interpretability, and collaborative inquiry. Built with gratitude for open-source communities and systems thinkers everywhere.
This is an ongoing project — iterative, imperfect, and evolving. If you notice issues, have suggestions, or want to share reflections, please feel free to leave feedback via [issues](https://github.com/Laranguyen811/cross_modal_analysis_with_mechanistic_interpretability/issues) or pull requests. Your insights are welcome and appreciated.

This project uses the [Prisma Framework](https://github.com/Prisma-Multimodal/ViT-Prisma),  originally developed by Sonia Joseph and contributors,  licensed under the [MIT License](https://github.com/Prisma-Multimodal/ViT-Prisma/blob/main/LICENSE). We gratefully acknowledge their work on mechanistic interpretability in multimodal models.

## 🤖 AI-Assisted Collaboration

This project has benefited from the use of AI assistants for programming, research, and linguistic enrichment.  
We gratefully acknowledge the following:

- **Microsoft Copilot**  
  Supported legal scaffolding, modular templates, and emotionally intelligent phrasing.  
  [https://copilot.microsoft.com](https://copilot.microsoft.com)

- **Gemini (Google DeepMind)**  
  Assisted with troubleshooting, code refactoring, and conceptual brainstorming.  
  [https://deepmind.google](https://deepmind.google)

- **Claude (Anthropic)**  
  Contributed to ethical reasoning scaffolds, interpretability, and collaborative drafting.  
  [https://www.anthropic.com](https://www.anthropic.com)

These tools were used as collaborative assistants in both programming and research contexts.  
The project author made all final decisions, edits and validations.  
Attribution reflects usage transparency and ethical engagement with generative technologies.


