# Build a Password Generator GUI with Python
# Function for password creation based on user defined length
# Add optional description input
# Save to file "passwords.txt"

import random


def create_password(length):
    password = ""
    for _ in range(length):
        pass_char = chr(random.randint(33, 122))
        password += pass_char
    return password


def write_to_file(passwords):
    pass


def main():
    pass_length = int(input("Enter integer for password length: "))
    print(create_password(pass_length))


if __name__ == "__main__":
    main()
