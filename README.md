<!--
 Copyright (c) 2025 Louis Jouret
 
 This software is released under the MIT License.
 https://opensource.org/licenses/MIT
-->

# Text Summarizer

A Python project that uses transformers for text summarization.

## Features
✅ Pre-trained Transformer model  
✅ Fine-tuning with Hugging Face Trainer  
✅ Web UI (Streamlit) and REST API (Flask)  

## Installation

1. Clone the repository:
```bash
git clone https://github.com/LouisJouret/TextSummarizer.git
cd TextSummarizer
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
# or
.\venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Add the parent directory to the Python path before running the training script. You can do this by modifying the `PYTHONPATH` environment variable:
```bash
export PYTHONPATH=$(pwd):$PYTHONPATH
```

## Running the Application

```bash
streamlit run main.py
```
