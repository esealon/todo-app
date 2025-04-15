# we can leave it open("file/docs.... without 'r', because by default, 'r' is assigned to it

with open("files/doc.txt", 'r') as file:
    file.read()