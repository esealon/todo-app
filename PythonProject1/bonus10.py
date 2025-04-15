try:
    width = float(input("Enter the width of the rectangle: "))
    length = float(input("Enter the length of the rectangle: "))

    if width == length:
        exit("Width and length cannot be equal. That looks like a square")
        
    area = width * length
    print(area)
except ValueError:
    print("Invalid input. Please enter numeric values.")
