<p align="center">
  <h1>🔤 Multilingual OCR Pipeline</h1>
  <p><strong>Gujarati + English OCR with AI-Powered Post-Correction</strong></p>
</p>

<p align="center">
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="Python 3.10+"></a>
  <img src="https://img.shields.io/badge/Tesseract-guj+eng-orange.svg" alt="Tesseract">
  <img src="https://img.shields.io/badge/Accuracy-96.8%25-brightgreen.svg" alt="96.8% Accuracy">
</p>

---

## 📋 Overview

A specialized 3-stage OCR pipeline for processing bilingual legal documents (Gujarati-English) with state-of-the-art accuracy. Developed while processing 50,000+ pages of scanned deeds.

## 🎯 The Problem

| Challenge | Impact |
|:---|:---|
| 📄 Mixed-script documents | Standard OCR fails 40%+ |
| 🖨️ Low-quality scans (1970s-2025) | Character confusion |
| ⚖️ Legal terminology | Domain-specific errors |
| ✍️ Handwritten annotations | Recognition failures |

## 🛠️ Technology Stack

| Category | Technology |
|:---|:---|
| **Language** | Python 3.10+ |
| **OCR Engine** | Tesseract 5.0+ (guj+eng) |
| **AI Enhancement** | Google Gemini Vision |
| **Image Processing** | Pillow, pdf2image |
| **Post-Processing** | Domain-specific rules |

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/SGajjar24/multilingual-ocr-pipeline.git
cd multilingual-ocr-pipeline

# Install dependencies
pip install -r requirements.txt

# Install Tesseract (Windows)
# Download from: https://github.com/UB-Mannheim/tesseract/wiki

# Install Tesseract (Linux)
sudo apt install tesseract-ocr tesseract-ocr-guj
```

### Usage Example

```python
from src.ocr_pipeline import MultilingualOCRPipeline

pipeline = MultilingualOCRPipeline(use_gemini=True)
result = pipeline.process("scanned_deed.jpg")

print(f"Text: {result.text}")
print(f"Language: {result.language}")  # "gu" | "en" | "mixed"
print(f"Confidence: {result.confidence}")
```

## 📁 Project Structure

```
multilingual-ocr-pipeline/
├── src/
│   ├── __init__.py
│   └── ocr_pipeline.py      # 3-stage pipeline
├── docs/
│   └── architecture.md      # Technical design
├── requirements.txt
└── README.md
```

## 📊 Benchmarks

| Pipeline Stage | Accuracy | Time/Page |
|:---|:---|:---|
| Stage 1: Tesseract alone | 78.2% | 2s |
| Stage 2: + Gemini Vision | 94.6% | 8s |
| **Stage 3: + Legal Vocabulary** | **96.8%** | 12s |

*Tested on 100 scanned legal deeds (1970-2025)*

## 🔧 3-Stage Pipeline

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Stage 1        │ ──▶ │  Stage 2        │ ──▶ │  Stage 3        │
│  Tesseract OCR  │     │  Gemini Vision  │     │  Legal Vocab    │
│  (guj+eng)      │     │  (AI Correction)│     │  (Domain Rules) │
└─────────────────┘     └─────────────────┘     └─────────────────┘
       78.2%                  94.6%                   96.8%
```

---

## 👤 Author

<table>
  <tr>
    <td><strong>Swetang Gajjar</strong></td>
  </tr>
  <tr>
    <td>Senior AI Engineer | Legal-Tech & Forensic Intelligence Specialist</td>
  </tr>
  <tr>
    <td>
      <a href="https://linkedin.com/in/gajjarswetang">
        <img src="https://img.shields.io/badge/LinkedIn-0077B5?logo=linkedin&logoColor=white" alt="LinkedIn">
      </a>
      <a href="https://github.com/SGajjar24">
        <img src="https://img.shields.io/badge/GitHub-100000?logo=github&logoColor=white" alt="GitHub">
      </a>
      <a href="mailto:gajjarswetang@gmail.com">
        <img src="https://img.shields.io/badge/Email-D14836?logo=gmail&logoColor=white" alt="Email">
      </a>
    </td>
  </tr>
</table>

---

<p align="center">
  <sub>Built with ❤️ while digitizing 50,000+ pages of Gujarati legal documents</sub>
</p>
