# DevIllustrate AI
### Technical Documentation Graphic Generator

DevIllustrate AI is a beginner-friendly text-to-image application. It uses Stable Diffusion through Hugging Face Diffusers and provides a Streamlit interface.

## Features
- Text-to-image generation
- Prompt enhancement
- Four visual styles: Professional 3D, Flat Vector, Blueprint and Isometric
- Adjustable inference steps, guidance scale, image size and seed
- Negative prompt field
- PNG preview, saving and download

## Project structure

```text
DevIllustrate-AI/
├── app.py
├── generator.py
├── prompt_engine.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
├── assets/
└── outputs/
```

## Requirements
- Python 3.10 or 3.11 recommended
- Internet connection for downloading the model
- NVIDIA GPU recommended; CPU mode is supported but can be very slow
- Several GB of disk space for model files

## Setup on Windows (VS Code)

1. Install Python and open this folder in VS Code.
2. Open the terminal in the project folder.
3. Create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\activate
```

4. Install PyTorch using the correct command for your computer from:
   https://pytorch.org/get-started/locally/

5. Install the project dependencies:

```powershell
pip install -r requirements.txt
```

6. Run the app:

```powershell
streamlit run app.py
```

7. Open the local address shown in the terminal (usually http://localhost:8501).

## Setup in Google Colab

1. Open Google Colab and create a notebook.
2. Choose Runtime > Change runtime type > T4 GPU (if available).
3. Upload/extract this project ZIP, or clone/copy the source files into the Colab session.
4. Install dependencies:

```python
!pip install -q -r requirements.txt
```

5. Run Streamlit using a suitable tunnel or run the app locally in a supported environment. The simplest beginner workflow is to use VS Code for the Streamlit interface and Colab for GPU experiments.

## Hugging Face model access

The configured model is `stable-diffusion-v1-5/stable-diffusion-v1-5`. If Hugging Face asks you to accept model terms or sign in, visit the model page, review and accept its conditions, then authenticate in your environment using `hf auth login` (or the supported Hugging Face CLI for your installed version).

## Important notes

- The first run downloads the model and may take time.
- Start with 512x512 resolution.
- GPU memory requirements vary by hardware and library versions.
- Generated images may contain incorrect or unreadable text. Do not treat generated technical labels or connections as verified engineering diagrams.
- This starter project disables the optional Stable Diffusion safety checker in the pipeline configuration. For a public deployment, review the model's license and safety requirements and enable appropriate content safeguards before publishing.

## Example prompt

`A cloud computing architecture showing users, a frontend application, backend services, a database and cloud servers, with clear visual grouping.`

## Troubleshooting

**CUDA out of memory:** use 512x512, reduce inference steps, close other GPU applications, or use a GPU with more memory.

**Model download/access error:** check internet connectivity and model access requirements on Hugging Face.

**Missing package:** activate your virtual environment and run `pip install -r requirements.txt` again.
