def get_average():
    with open("files/data.txt", "r") as file:
        data = file.readlines()

    values = data[1:]
    # data[1:] we do this slicing so we don't see the
    # temperature name on it and only the values.
    values = [float(i) for i in values]
    # to make all values to float

    average_local = sum(values) / len(values)
    return average_local


average = get_average()
print(average)