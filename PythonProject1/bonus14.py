from PythonProject1.convertors14 import convert
from PythonProject1.parsers14 import parse

feet_inches = input("Enter feet in inches: ")

f, i = parse(feet_inches)
result = convert(f, i)

if result < 1:
    print("Kid is too small")
else:
    print("Kid can use the slide.")