import zipfile
import os


# Welcome to the zipper program!
# This program will zip up all the files you need to submit for your project.
# You can either use the default files or enter your own.
# The default files are: main_app, orm_skeleton, caller.py, manage.py, requirements.txt

# Enjoy!
def zip_files(directory, files_to_zip, output_zip):
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in files_to_zip:
            file_path = os.path.join(directory, file)
            if os.path.exists(file_path):
                if os.path.isfile(file_path):
                    zipf.write(file_path, os.path.relpath(file_path, directory))
                elif os.path.isdir(file_path):
                    for root, _, files in os.walk(file_path):
                        for f in files:
                            file_to_zip = os.path.join(root, f)
                            zipf.write(file_to_zip, os.path.relpath(file_to_zip, directory))
            else:
                raise FileNotFoundError(f"File or directory '{file}' not found in the specified directory.")


if __name__ == "__main__":
    directory = input("Enter the directory path: ")

    while True:
        use_default_files = input("Use default files to zip? (y/n): ").strip().lower()
        if use_default_files == 'y':
            files_to_zip = ["main_app", "orm_skeleton", "caller.py", "manage.py", "requirements.txt"]
            break
        elif use_default_files == 'n':
            files_to_zip = input("Enter custom file names separated by spaces: ").split()
            break
        else:
            print("Invalid option. Please enter 'y' for default files or 'n' for custom files.")

    output_zip = os.path.join(directory,
                              input("Enter a name for the zip file (without the '.zip' extension): ") + ".zip")

    try:
        zip_files(directory, files_to_zip, output_zip)
        print(f"\nCongratulations! Your files have been successfully zipped and saved to {output_zip}.")
    except FileNotFoundError as e:
        print(f"Error: {e}")