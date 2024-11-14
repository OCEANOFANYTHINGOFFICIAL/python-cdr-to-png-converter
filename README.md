# Python CDR to PNG Converter

![GitHub repo size](https://img.shields.io/github/repo-size/OCEANOFANYTHINGOFFICIAL/python-cdr-to-png-converter)
![GitHub contributors](https://img.shields.io/github/contributors/OCEANOFANYTHINGOFFICIAL/python-cdr-to-png-converter)
![GitHub stars](https://img.shields.io/github/stars/OCEANOFANYTHINGOFFICIAL/python-cdr-to-png-converter?style=social)
![GitHub forks](https://img.shields.io/github/forks/OCEANOFANYTHINGOFFICIAL/python-cdr-to-png-converter?style=social)
![GitHub issues](https://img.shields.io/github/issues/OCEANOFANYTHINGOFFICIAL/python-cdr-to-png-converter)

## Overview

This Python utility converts CorelDRAW (CDR) files to PNG format using Inkscape. It supports batch conversion of files within a directory and allows users to specify the output quality via DPI settings.

## Features

- Convert individual CDR files to PNG.
- Batch conversion of all CDR files in a directory.
- Specify DPI for output quality (1x, 2x, 4x, 6x, 8x).
- Color-coded terminal messages for better user experience.

## Requirements

- Python 3.x
- Inkscape

## Inkscape Installation

### Windows

1. Download the Inkscape installer from the [Inkscape website](https://inkscape.org/release/).
2. Run the installer and follow the on-screen instructions to complete the installation.
3. Ensure Inkscape is added to your system PATH during installation.

### Adding Inkscape to PATH on Windows

1. Open the Start Search, type in "env", and select "Edit the system environment variables".
2. In the System Properties window, click on the "Environment Variables" button.
3. In the Environment Variables window, under "System variables", find the `Path` variable and select it. Click "Edit".
4. Click "New" and add the path to the Inkscape installation directory (e.g., `C:\Program Files\Inkscape\bin` or `C:\Program Files (x86)\Inkscape\bin`).
5. Click OK to close all dialog boxes.
6. Open a new command prompt and type `inkscape --version` to verify that Inkscape is now accessible from the command line.

### macOS

1. Download the Inkscape DMG file from the [Inkscape website](https://inkscape.org/release/).
2. Open the DMG file and drag Inkscape to your Applications folder.
3. Open Inkscape from the Applications folder.

### Linux

- **Ubuntu/Debian**:

  ```bash
  sudo apt update
  sudo apt install inkscape
  ```

- **Fedora**:

  ```bash
  sudo dnf install inkscape
  ```

- **Arch Linux**:

  ```bash
  sudo pacman -S inkscape
  ```

Ensure that Inkscape is accessible from the command line by typing `inkscape --version` to verify the installation.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/OCEANOFANYTHINGOFFICIAL/python-cdr-to-png-converter.git
   ```

2. Navigate to the project directory:

   ```bash
   cd python-cdr-to-png-converter
   ```

3. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

## Quick Start

### Windows Virtual Environment Activation

To activate the virtual environment, double-click the `activate_venv.bat` file. This will open a command prompt with the environment activated.

### Linux Virtual Environment Activation

To activate the virtual environment, run the following command in your terminal:

```bash
./activate_venv.sh
```

This will open a new bash session with the environment activated.

## Usage

### Single File Conversion

```bash
python convert_cdr_to_png.py <input_file.cdr> [output_file.png] --dpi <dpi_value>
```

### Batch Conversion

```bash
python convert_cdr_to_png.py -f <input_folder> --dpi <dpi_value>
```

### Examples

- Convert a single file with standard DPI:

  ```bash
  python convert_cdr_to_png.py example.cdr
  ```

- Convert all files in a folder with 4x DPI:

  ```bash
  python convert_cdr_to_png.py -f ./example-folder --dpi 384
  ```

## DPI Settings

- 1x = 96 DPI (Standard)
- 2x = 192 DPI
- 4x = 384 DPI
- 6x = 576 DPI
- 8x = 768 DPI
- nx = 96 * n DPI (Custom DPI settings can be specified for different quality levels)

## License

This project is licensed under the terms of the [GNU General Public License v3.0](LICENSE).

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact

For any inquiries, please contact [OCEANOFANYTHINGOFFICIAL](https://github.com/OCEANOFANYTHINGOFFICIAL).
