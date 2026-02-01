"""
Multilingual OCR Pipeline - Gujarati + English Legal Document Processing

This module provides a 3-stage OCR pipeline optimized for bilingual legal documents:
1. Tesseract OCR (base extraction)
2. Gemini Vision (error correction)
3. Domain-specific post-processing (legal terminology)
"""

import os
from typing import Dict, List, Optional
from dataclasses import dataclass


@dataclass
class OCRResult:
    """Container for OCR output with confidence scores."""
    text: str
    confidence: float
    language: str  # "gu" | "en" | "mixed"
    corrections_applied: int


class MultilingualOCRPipeline:
    """
    3-stage OCR pipeline for Gujarati-English legal documents.
    
    Stages:
        1. Tesseract (base OCR)
        2. Gemini Vision (AI correction)
        3. Legal vocabulary correction
    
    Example:
        >>> pipeline = MultilingualOCRPipeline()
        >>> result = pipeline.process("scan_001.pdf")
        >>> print(result.text)
    """
    
    # Common OCR errors in Gujarati legal documents
    GUJARATI_CORRECTIONS = {
        "ફાપાલી": "ફારગતી",  # "Faragati" (Relinquishment)
        "નોંધણી નં": "નોંધણી નંબર",  # Registration number
        "સરવે નં": "સર્વે નંબર",  # Survey number
    }
    
    # English legal term corrections
    ENGLISH_CORRECTIONS = {
        "Registation": "Registration",
        "Relinquishrnent": "Relinquishment",
        "Notarised": "Notarized",
    }
    
    def __init__(self, tesseract_lang: str = "guj+eng", use_gemini: bool = True):
        """
        Args:
            tesseract_lang: Tesseract language codes (default: Gujarati + English)
            use_gemini: Whether to use Gemini Vision for error correction
        """
        self.tesseract_lang = tesseract_lang
        self.use_gemini = use_gemini
    
    def _stage1_tesseract(self, image_path: str) -> str:
        """Stage 1: Base Tesseract OCR extraction."""
        # In production, use pytesseract
        # import pytesseract
        # return pytesseract.image_to_string(image_path, lang=self.tesseract_lang)
        return "[Tesseract OCR output would appear here]"
    
    def _stage2_gemini_correction(self, text: str, image_path: str) -> str:
        """Stage 2: Use Gemini Vision to correct OCR errors."""
        if not self.use_gemini:
            return text
        
        # In production:
        # prompt = f"Correct OCR errors in this Gujarati-English text: {text}"
        # return gemini_vision.generate(prompt, image=image_path)
        return text
    
    def _stage3_legal_vocabulary(self, text: str) -> str:
        """Stage 3: Apply domain-specific corrections."""
        corrected = text
        corrections = 0
        
        for wrong, right in {**self.GUJARATI_CORRECTIONS, **self.ENGLISH_CORRECTIONS}.items():
            if wrong in corrected:
                corrected = corrected.replace(wrong, right)
                corrections += 1
        
        return corrected
    
    def process(self, image_path: str) -> OCRResult:
        """
        Run the full 3-stage OCR pipeline.
        
        Args:
            image_path: Path to scanned document image
            
        Returns:
            OCRResult with text, confidence, and metadata
        """
        # Stage 1
        raw_text = self._stage1_tesseract(image_path)
        
        # Stage 2
        corrected_text = self._stage2_gemini_correction(raw_text, image_path)
        
        # Stage 3
        final_text = self._stage3_legal_vocabulary(corrected_text)
        
        # Detect primary language
        gujarati_chars = sum(1 for c in final_text if '\u0A80' <= c <= '\u0AFF')
        total_chars = len(final_text.replace(" ", ""))
        language = "gu" if gujarati_chars / max(total_chars, 1) > 0.5 else "en"
        
        return OCRResult(
            text=final_text,
            confidence=0.85,  # Placeholder
            language=language,
            corrections_applied=0
        )


if __name__ == "__main__":
    pipeline = MultilingualOCRPipeline()
    result = pipeline.process("sample_deed.jpg")
    print(f"Language: {result.language}")
    print(f"Confidence: {result.confidence}")
