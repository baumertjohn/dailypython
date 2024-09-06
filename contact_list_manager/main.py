# Create a program that lets the user submit names and phone numbers through
# the console and stores those numbers in a text file.


def main():
    with open("contacts.txt", "w") as file:
        while True:
            name = input("Enter contact name (or type 'done' to finish): ")
            if name.lower() == "done":
                break
            phone = input(f"Enter phone number for {name}: ")
            file.write(f"{name}: {phone}\n")
    print("Contacts saved to 'contacts.txt'.")


if __name__ == "__main__":
    main()
