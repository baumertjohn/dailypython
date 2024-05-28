# Command line based diary program
# Saves to text file named 'year-month-date.txt'
from datetime import datetime


# While loop looking for 'exit' or 'EXIT' (user lower?)
def get_diary_entry():
    diary_entry = ""
    while True:
        diary_line = input("> ")
        if diary_line.lower() == "exit":
            break
        else:
            diary_entry += diary_line + "\n"
    return diary_entry


# Get current date
# Write to text file
def save_diary(diary_entry):
    current_date = datetime.now()
    filename = current_date.strftime("%Y-%m-%d")
    filename = f"{filename}.txt"
    with open(filename, "a", encoding="utf-8") as f:
        f.write(diary_entry)
    print(f"Diary stored to {filename}")


def main():
    # Greet user
    print("Enter your notes for the day, type 'exit' to exit to save and exit.")
    diary_entry = get_diary_entry()
    save_diary(diary_entry)


if __name__ == "__main__":
    main()
