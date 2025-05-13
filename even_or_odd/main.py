# Check if Number is Even or Odd
# Daily Python


def get_user_input():
    """Prompts the user to enter an integer and returns it."""
    while True:
        user_input = input("Enter an integer: ")
        try:
            return int(user_input)
        except ValueError:
            print("Please enter valid integer!\n")


def even_check(num):
    """Checks if a number is even and returns True if it is, False otherwise."""
    if num % 2 == 0:
        return True


def main():
    """Main function to greet the user, get an integer input, and check if it's odd or even."""
    print("Hello, enter a number to see if it is odd or even")
    num = get_user_input()
    if even_check(num):
        print("Your number is even.")
    else:
        print("Your number is odd.")


if __name__ == "__main__":
    main()
