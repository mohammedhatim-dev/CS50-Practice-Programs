# A simple CS50-inspired program to print a pyramid based on user input height
print("--- CS50 Mario Pyramid Practice ---")

while True:
    try:
        height = int(input("Enter pyramid height (1-8): "))
        if 1 <= height <= 8:
            break
        else:
            print("Height must be between 1 and 8.")
    except ValueError:
        print("Please enter a valid integer.")

for i in range(1, height + 1):
    spaces = " " * (height - i)
    hashes = "#" * i
    print(spaces + hashes)