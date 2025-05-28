# Build a Password Generator GUI with Python
# Function for password creation based on user defined length
# Add optional description input
# Save to file "passwords.txt"

import random


def create_password(length):
    NOUSE_CHARS = "<>'\""
    password = ""
    while len(password) < length:
        pass_char = chr(random.randint(33, 122))
        if pass_char in NOUSE_CHARS:
            continue
        password += pass_char
    return password


def write_to_file(description, password):
    if len(description) == 0:
        description = "No Description"
    with open("passwords.txt", "a") as file:
        file.write(f"{description}: {password}\n")


def main():
    print("Password Generator")
    print("Password Length")
    pass_length = int(input("> "))
    print("Description (optional):")
    description = input("> ")
    _ = input("Press ENTER to Generate Password")
    password = create_password(pass_length)
    print("Generated Password")
    print(password)
    _ = input("Press ENTER to Save Password")
    write_to_file(description, password)
    # Verify file write
    print("\nPassword File:")
    with open("passwords.txt", "r") as file:
        print(file.read())


if __name__ == "__main__":
    main()
