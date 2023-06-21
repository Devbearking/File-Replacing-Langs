# File-Replacing-Langs
Using pyhon to repale .png files in many directories.

# Directory File Copy and Replace Script

This Python script allows you to copy and replace a specific file from one directory to another.

## Prerequisites

- Python 3.x
- The `os` and `shutil` modules, which are part of the Python standard library, are required.

## Usage

1. Clone the repository or download the script file.

2. Modify the script according to your requirements:
    - In the `copy_and_replace_file` function, adjust the error handling and customization based on your needs.
    - Replace the empty `Langs` list with your desired language codes.

3. Run the script by executing the following command:

    ```
    python directory_copy_replace.py
    ```

    - The script will prompt you to provide specific parts of the directory paths and the file name to copy and replace.
    - It will iterate over the `Langs` list, constructing the complete paths based on the provided language codes.

4. The script will attempt to copy and replace the specified file from the source directory to the destination directory for each language.
    - If the file doesn't exist in the source directory, or if it's not a regular file, an error message will be displayed.
    - If the destination directory doesn't exist, an error message will be displayed.
    - If the destination file already exists, it will be removed before the copy operation.
    - After successful copying, a success message will be displayed.
