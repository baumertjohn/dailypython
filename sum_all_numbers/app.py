# Your task for today is to write a Python program that calculates the sum of
# all numbers from 1 to 100.

# You should use a loop to go through the numbers and add them up. Store the
# result in a variable and print it at the end.

def count_to(num):
    total = 0
    for i in range(num + 1):
        total += i
    return total


def main():
    print(count_to(100))
    
    
if __name__ == "__main__":
    main()
