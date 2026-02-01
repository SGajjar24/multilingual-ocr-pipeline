# Multilingual OCR Pipeline

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

**Gujarati + English OCR with AI-Powered Post-Correction**

A specialized OCR pipeline for processing bilingual legal documents (Gujarati-English) with state-of-the-art accuracy.

## 🎯 The Problem

Standard OCR fails on:
- 📄 Mixed-script documents (Gujarati + English)
- 🖨️ Low-quality scans (faded, handwritten margins)
- ⚖️ Legal terminology (specialized vocabulary)

## 📊 Benchmarks

| Pipeline | Accuracy | Processing Time/Page |
|:---|:---|:---|
| Tesseract (guj+eng) | 78.2% | 2s |
| Tesseract + Gemini Vision | 94.6% | 8s |
| **This Pipeline (3-stage)** | **96.8%** | 12s |

*Tested on 100 scanned legal deeds (1970-2025)*

## 👤 Author

**Swetang Gajjar** - Senior AI Engineer | Legal-Tech Specialist

Developed while processing 50,000+ pages of Gujarati legal scans (2023-2025)
