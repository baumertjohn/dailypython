# Extract All Digits From a String in Python

# Project Description
# Your task for today is to write a Python program that extracts all the digits
# from a given string and stores them in a list.


# TEXT = "The year is 2025 and the time is 09:45"


def main():
    digit_string = []

    text = input("Enter text to extract digits from: ")

    for char in text:
        try:
            digit_string.append(int(char))
        except ValueError:
            continue

    print(f"The digits found are {digit_string}")


if __name__ == "__main__":
    main()
