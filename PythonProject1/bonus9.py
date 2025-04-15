from string import digits

password = input("Enter your password: ")
result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True

result["digit"] = digit

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result["uppercase"] = uppercase

print(result)

if all(result.values()):
    # all(result) what it does is if at least one of the results is false, then the statement is false.
    # we use .value(), it means the all is checking the values of the dictionary
    print("Password is strong")
else:
    print("Password is weak")
