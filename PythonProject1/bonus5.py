waiting_list = ["sen", "ben", "john"]
waiting_list.sort()
# .sort, help us to sort the list alphabetically

for index, item in enumerate(waiting_list):
    row = f"{index + 1}.{item.capitalize()}"
    print(row)