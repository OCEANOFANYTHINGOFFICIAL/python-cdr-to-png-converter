import sys
import subprocess
import os
import glob
import argparse
from colorama import Fore, Style

def relative_path(full_path):
    return os.path.relpath(full_path, start=os.getcwd())

def print_colored(message, message_type="info"):
    colors = {
        "info": Fore.CYAN,
        "success": Fore.GREEN,
        "processing": Fore.BLUE,
        "error": Fore.RED,
        "warning": Fore.YELLOW
    }
    color = colors.get(message_type, Fore.WHITE)
    print(f"{color}[{message_type.capitalize()}]{Style.RESET_ALL} {message}")

def convert_cdr_to_png(input_folder, dpi):
    # Ensure output directory exists
    output_folder = os.path.join(input_folder, "output")
    os.makedirs(output_folder, exist_ok=True)

    # Process each CDR file in the input folder
    cdr_files = glob.glob(os.path.join(input_folder, "*.cdr"))
    if not cdr_files:
        print_colored("No CDR files found in the input directory.", "error")
        return

    for cdr_file in cdr_files:
        file_name = os.path.basename(cdr_file)
        output_file = os.path.join(output_folder, file_name.replace('.cdr', '.png'))

        try:
            print_colored(f"Converting {relative_path(cdr_file)} to {relative_path(output_file)}...", "processing")
            subprocess.run([
                'inkscape',
                cdr_file,
                '--export-type=png',
                '--export-filename=' + output_file,
                f'--export-dpi={dpi}'
            ], check=True)
            print_colored(f"Successfully converted {relative_path(cdr_file)} to {relative_path(output_file)}", "success")
        except subprocess.CalledProcessError as e:
            print_colored(f"Failed to convert {cdr_file}: {e}", "error")

def convert_single_cdr_to_png(input_file, output_file, dpi):
    try:
        print_colored(f"Converting {relative_path(input_file)} to {relative_path(output_file)}...", "processing")
        subprocess.run([
            'inkscape',
            input_file,
            '--export-type=png',
            '--export-filename=' + output_file,
            f'--export-dpi={dpi}'
        ], check=True)
        print_colored(f"Successfully converted {relative_path(input_file)} to {relative_path(output_file)}", "success")
    except subprocess.CalledProcessError as e:
        print_colored(f"Failed to convert {input_file}: {e}", "error")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert CDR files to PNG.",
                                     epilog="""
Examples:
  python convert_cdr_to_png.py input_file.cdr output_file.png -dpi 96
  python convert_cdr_to_png.py -f input_folder -dpi 192

DPI Settings:
  1x = 96 DPI (Standard)
  2x = 192 DPI
  4x = 384 DPI
  6x = 576 DPI
  8x = 768 DPI
  ...
  nx = 96 * n DPI
""",
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("input", help="Input file or directory")
    parser.add_argument("output", nargs="?", help="Output file name for single file conversion")
    parser.add_argument("-f", "--folder", action="store_true", help="Indicate that the input is a folder containing CDR files")
    parser.add_argument("-dpi", "--dpi", type=int, default=96, help="Set the DPI for the output PNG (default is 96)")
    args = parser.parse_args()

    if not args.input:
        print_colored("Error: No input provided.", "error")
        sys.exit(1)

    input_path = os.path.abspath(args.input)
    if args.dpi <= 0:
        print_colored("Error: DPI must be a positive integer.", "error")
        sys.exit(1)

    try:
        subprocess.run(['inkscape', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print_colored("Error: Inkscape is not installed or not found in PATH.", "error")
        sys.exit(1)

    if args.folder:
        if not os.path.isdir(input_path):
            print_colored(f"Error: The directory {input_path} does not exist.", "error")
            sys.exit(1)
        try:
            os.makedirs(os.path.join(input_path, "output"), exist_ok=True)
        except PermissionError:
            print_colored("Error: Permission denied to create output directory.", "error")
            sys.exit(1)
        convert_cdr_to_png(input_path, args.dpi)
    else:
        if os.path.isdir(input_path):
            print_colored(f"Error: The input {input_path} is a directory. Use the -f flag for folder conversion.", "error")
            sys.exit(1)
        if not os.path.isfile(input_path):
            print_colored(f"Error: The file {input_path} does not exist.", "error")
            sys.exit(1)
        if not input_path.lower().endswith('.cdr'):
            print_colored("Error: The input file is not a CDR file.", "error")
            sys.exit(1)
        output_file = args.output if args.output else os.path.splitext(input_path)[0] + ".png"
        convert_single_cdr_to_png(input_path, output_file, args.dpi)

    if args.dpi == 96:
        print_colored("Using standard DPI: 96 (1x)", "info")
