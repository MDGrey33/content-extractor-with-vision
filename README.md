# Content Extractor with Vision LLM

This repository contains a Python project that extracts text and images from various file types (PDF, DOCX, PPTX), describes the images using the `llama3.2-vision` model, and saves the results in a specified output directory.

## Features

- Extract text and images from PDF, DOCX, and PPTX files
- Describe images using the `llama3.2-vision` model
- Save extracted text and image descriptions in a specified output directory
- User-friendly command-line interface for specifying input and output folders
- Modular and extensible code structure following SOLID principles
- Compare image descriptions generated by different models

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/file-extractor.git
   cd file-extractor
   ```

2. **Install Poetry**

   If you haven't installed Poetry yet, you can do so by following the instructions on the [Poetry website](https://python-poetry.org/docs/#installation).

3. **Install Dependencies**

   System dependencies:
   - LibreOffice (required for DOCX/PPTX processing)
   - poppler (required for PDF processing)

   Installation commands:
   - macOS (using Homebrew):
     ```bash
     brew install --cask libreoffice
     brew install poppler
     ```

   - Ubuntu/Debian:
     ```bash
     sudo apt-get update
     sudo apt-get install libreoffice poppler-utils
     ```

   - Windows:
     - Download and install [LibreOffice](https://www.libreoffice.org/download/download/)
     - Download and install [poppler](http://blog.alivate.com.au/poppler-windows/)
     - Add the poppler `bin` directory to your system PATH

   Python dependencies:
   ```bash
   poetry install
   ```

## Setup Ollama

1. **Run Ollama Server**
   ```bash
   ollama serve
   ```

2. **Pull Required Model**
   ```bash
   ollama pull llama3.2-vision
   ```

## Configuration

The script's behavior can be customized through the `config.py` file:

```python
# Image description settings
DEFAULT_DESCRIBER = "ollama"  # or "openai"
DEFAULT_MODEL = "llama3.2-vision"  # or "gpt-4", "llava", etc.

# Extraction method settings
DEFAULT_PDF_EXTRACTOR = "page_as_image"  # or "text_and_images"
DEFAULT_DOCX_EXTRACTOR = "page_as_image"  # or "text_and_images"
```

## File Processing Methods

### PDF Files
Two extraction methods are available:
1. **Text and Images** (`text_and_images`):
   - Extracts text and embedded images separately
   - Preserves original text content and formatting
   - Best for PDFs where text extraction is reliable

2. **Page as Image** (`page_as_image`):
   - Converts each page to a high-resolution image (300 DPI)
   - Captures exact visual appearance including layout and formatting
   - Better for PDFs with complex layouts or when text extraction is unreliable

### DOCX Files
Two extraction methods are available:
1. **Text and Images** (`text_and_images`):
   - Extracts text and embedded images separately
   - Preserves original text formatting
   - Best for documents where text content needs to be preserved exactly

2. **Page as Image** (`page_as_image`):
   - Converts each page to an image
   - Captures exact visual appearance including layout
   - Requires LibreOffice for PDF conversion

### PPTX Files
- Converts each slide to an image using LibreOffice
- Captures exact visual appearance of slides
- Generates descriptions for each slide

## Usage

### Command-line Arguments
- `--source` or `-s`: Source folder path (default: `./content/source`)
- `--output` or `-o`: Output folder path (default: `./content/extracted`)
- `--type` or `-t`: File type to process ("pdf", "docx", or "pptx")

### Examples

1. Process DOCX files with default paths:
   ```bash
   poetry run python main.py --type docx
   ```

2. Process PDF files with custom paths:
   ```bash
   poetry run python main.py --source /path/to/source --output /path/to/output --type pdf
   ```

### Output Format
All extraction methods generate:
1. A Markdown file containing:
   - Document title
   - Page/slide numbers
   - Extracted text (for text-based methods)
   - Image descriptions
2. Clean directory structure:
   ```
   content/extracted/
   └── document_name/
       └── document_name.md
   ```

## License

This project is licensed under the [MIT License](LICENSE).
