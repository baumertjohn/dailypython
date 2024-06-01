import os
from datetime import datetime

FOLDER = "files"


def make_files():
    """Creates 26 empty text files, one for each letter of the alphabet (a-z)."""
    os.makedirs(FOLDER, exist_ok=True)
    for x in range(26):
        with open(f"{FOLDER}/{chr(x+97)}.txt", "w") as f:
            f.write("")


def make_file_list():
    """Returns a list of all .txt files in the current directory."""
    file_list = []
    for file in os.listdir(FOLDER):
        if file[-4:] == ".txt":
            file_list.append(f"{FOLDER}/{file}")
    return file_list


def change_file_name(file_list):
    """Changes the name of all .txt files in the given list to include the current date."""
    today = datetime.today().strftime("%Y-%m-%d")
    for file in file_list:
        # file format is filename-date.ext
        prefix, ext = file[:-4], file[-4:]
        new_file_name = f"{prefix}-{today}{ext}"
        os.rename(file, new_file_name)


def main():
    """Runs the main script. Creates 26 empty text files, waits for a key press, then renames the files to include the current date."""
    make_files()
    input("File list created - press a key")
    file_list = make_file_list()
    change_file_name(file_list)


if __name__ == "__main__":
    main()
