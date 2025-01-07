"""Factory for creating extractors."""

from typing import Dict, Type, Optional

from pyvisionai.extractors.base import BaseExtractor
from pyvisionai.extractors.pdf import PDFTextImageExtractor
from pyvisionai.extractors.pdf_page import PDFPageImageExtractor
from pyvisionai.extractors.docx import DocxTextImageExtractor
from pyvisionai.extractors.pptx import PptxTextImageExtractor
from pyvisionai.utils.config import DEFAULT_IMAGE_MODEL


# Map of file types to their extractors
EXTRACTORS: Dict[str, Dict[str, Type[BaseExtractor]]] = {
    "pdf": {
        "text_and_images": PDFTextImageExtractor,
        "page_as_image": PDFPageImageExtractor,  # Recommended for better results
    },
    "docx": {
        "text_and_images": DocxTextImageExtractor,
        "page_as_image": DocxTextImageExtractor,  # Same extractor for both methods
    },
    "pptx": {
        "text_and_images": PptxTextImageExtractor,
        "page_as_image": PptxTextImageExtractor,  # Same extractor for both methods
    },
}


def create_extractor(
    file_type: str,
    extractor_type: str = "page_as_image",
    model: str = DEFAULT_IMAGE_MODEL,
    api_key: Optional[str] = None,
) -> BaseExtractor:
    """
    Create an extractor instance based on file type and extraction method.

    Args:
        file_type: Type of file to process (pdf, docx, pptx)
        extractor_type: Type of extraction:
            - page_as_image (default): Convert each page to image (recommended)
            - text_and_images: Extract text and images separately
        model: Model to use for image descriptions (llama, gpt4)
        api_key: OpenAI API key (required for GPT-4)

    Returns:
        BaseExtractor: An instance of the appropriate extractor
    """
    if file_type not in EXTRACTORS:
        raise ValueError(f"Unsupported file type: {file_type}")

    if extractor_type not in EXTRACTORS[file_type]:
        raise ValueError(f"Unsupported extractor type: {extractor_type}")

    extractor_class = EXTRACTORS[file_type][extractor_type]
    extractor = extractor_class()
    extractor.model = model
    extractor.api_key = api_key
    return extractor
