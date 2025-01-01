# Content Extractor with Vision LLM

This repository contains a Python project that extracts text and images from various file types (PDF, DOCX, PPTX), describes the images using the `llama3.2-vision` model, and saves the results in a specified output directory.

## TODO
- Implement two interfaces for DOCX extraction:
  - Interface 1: Current method (extract text and images separately)
  - Interface 2: Page-as-image method (capture each page as an image)
- Add configuration option in config.py to select DOCX extraction method
- Change PDF extractor to write output in markdown format
- Implement extraction from XLSX in a meaningful way

## Features

- Extract text and images from PDF, DOCX, and PPTX files
- Describe images using the `llama3.2-vision` model
- Save extracted text and image descriptions in a specified output directory
- User-friendly command-line interface for specifying input and output folders
- Modular and extensible code structure following SOLID principles
- Compare image descriptions generated by different models

## Prerequisites

- Python 3.x
- Poetry
- Ollama
- LibreOffice (required for PPTX processing)

## Installation

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Poetry**

   If you haven't installed Poetry yet, you can do so by following the instructions on the [Poetry website](https://python-poetry.org/docs/#installation).

3. **Install LibreOffice**

   LibreOffice is required for processing PPTX files. Install it based on your operating system:

   - macOS (using Homebrew):
     ```bash
     brew install libreoffice
     ```
   
   - Ubuntu/Debian:
     ```bash
     sudo apt-get install libreoffice
     ```
   
   - Windows:
     Download and install from [LibreOffice website](https://www.libreoffice.org/download/download/)

4. **Install Project Dependencies**

   Use Poetry to install the dependencies:

   ```bash
   poetry install
   ```

## Setup Ollama

1. **Run Ollama Server**

   Start the Ollama server by running:

   ```bash
   ollama serve
   ```

2. **Pull the `llama3.2-vision` Model**

   Pull the required model by executing:

   ```bash
   ollama pull llama3.2-vision
   ```

## Configuration

The image description script can be configured using the `config.py` file. The available configuration options are:

- `DEFAULT_IMAGE_PATH`: The default path to the image file to be described.
- `DEFAULT_DESCRIBER`: The default describer to use for generating image descriptions. Available options are "openai" (OpenAI API) and "ollama" (local Ollama model).
- `DEFAULT_MODEL`: The default model to use for image description. The available options depend on the selected describer:
  - OpenAI describer: "gpt-4o" (default), "gpt-3.5-turbo"
  - Ollama describer: "llava", "llava:34b", "llama3.2-vision"

You can modify these configuration options in the `config.py` file to customize the script's behavior according to your requirements.

## Usage

1. **Run the Main Script**

   Execute the main script using Poetry:

   ```bash
   poetry run python main.py
   ```

2. **Provide Input**

   When prompted, enter the following information:
   - Source folder path (default: `./content/source`)
   - Output folder path (default: `./content/extracted`)
   - File type to process (pdf, docx, or pptx)

   The script will process the specified file type from the source folder and save the extracted text and image descriptions in the output folder.

### Command-line Arguments

- `--source` or `-s`: Specifies the path to the source folder containing the files to process. Default: `./content/source`.
- `--output` or `-o`: Specifies the path to the output directory where the extracted content will be saved. Default: `./content/extracted`.
- `--type` or `-t`: Specifies the type of files to process. Accepted values: "pdf", "docx", "pptx".

### Examples

1. Process all DOCX files in the default source folder and save the output to the default output directory:
   ```
   python main.py --type docx
   ```

2. Process all PDF files in a specific source folder and save the output to a specific directory:
   ```
   python main.py --source /path/to/source/folder --output /path/to/output/directory --type pdf
   ```

3. Process all PPTX files in the default source folder and save the output to a specific directory:
   ```
   python main.py --output /path/to/output/directory --type pptx
   ```

### Behavior

- If the `--source` argument is not provided, the script will use the default value of `./content/source` for the source folder.
- If the `--output` argument is not provided, the script will use the default value of `./content/extracted` for the output directory.
- If the `--type` argument is not provided, the script will prompt the user to enter the file type interactively.

## Dependencies

The File Extractor script requires the following dependencies:

- Python 3.x
- PyMuPDF
- python-docx
- python-pptx
- Pillow
- LibreOffice (for PPTX processing)

These dependencies can be installed using the `requirements.txt` file provided in the repository, except for LibreOffice which needs to be installed separately using your system's package manager.

## License

This project is licensed under the [MIT License](LICENSE).
