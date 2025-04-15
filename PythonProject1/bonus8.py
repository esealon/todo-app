date = input("Enter today's date: ")
mood = input("How do you rate your mood today from 1 to 10? ")
thoughts = input("let your thoughts flow:\n")

with open(f"experiments/journal/{date}.txt", 'w') as file:
    # 2 * "\n" it means that there are two spaces
    file.write(mood + 2 * "\n")
    file.write(thoughts)