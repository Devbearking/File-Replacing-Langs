import os
import shutil

def copy_and_replace_file(file_path, source_directory, destination_directory):
    file_name = os.path.basename(file_path)
    source_file = os.path.join(source_directory, file_name)
    destination_file = os.path.join(destination_directory, file_name)

    try:
        if not os.path.exists(source_file):
            raise FileNotFoundError(f"The file '{file_name}' does not exist in '{source_directory}'.")

        if not os.path.isfile(source_file):
            raise ValueError(f"'{file_name}' is not a file in '{source_directory}'.")

        if not os.path.exists(destination_directory):
            raise FileNotFoundError(f"The destination directory '{destination_directory}' does not exist.")

        if os.path.exists(destination_file):
            os.remove(destination_file)

        shutil.copy2(source_file, destination_directory)
        print(f"Successfully copied '{file_name}' from '{source_directory}' to '{destination_directory}'.")

    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
        
        
# Replace with your desired language codes
Langs = []  

for Lang in Langs:
    # Povide the directory of the file which you what to copy.
    # DON'T FORGET TO ADD '{}' FOR THE LANGS AND .format(Lang)
    directoryOne = "{}".format(Lang)
    # Provide the directory of the file which you what to replace.
    directoryTwo = "{}".format(Lang)

    # The file name with including extension Example ".png", ".jpg"
    fileToCopy = ".png"

    copy_and_replace_file(fileToCopy, directoryOne, directoryTwo)

