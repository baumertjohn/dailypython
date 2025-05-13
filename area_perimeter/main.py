# A simple script to calculate area and perimeter from user inputted numbers
# Utilize functions and error checking


def calculate_area(length, width):
    return length * width


def calculate_perimeter(length, width):
    return 2 * (length + width)


def get_user_inputs():
    while True:
        try:
            length = float(input("Enter length: "))
            break
        except ValueError:
            print("Enter Integer or Float!")
            continue
    while True:
        try:
            width = float(input("Enter width: "))
            break
        except ValueError:
            print("Enter Integer or Float!")
            continue
    return length, width


def main():
    while True:
        print("What would you like to calculate")
        user_choice = input("Choose (A)rea, (P)erimeter, or e(X)it.> ").lower()
        if user_choice == "x":
            print("Good Bye...\n")
            break
        elif user_choice == "a":
            area = calculate_area(*get_user_inputs())
            print(f"The area would be {area}\n")
        elif user_choice == "p":
            perimeter = calculate_perimeter(*get_user_inputs())
            print(f"The perimeter would be {perimeter}\n")
        else:
            print("Please pick A, P, or X\n")


if __name__ == "__main__":
    main()
