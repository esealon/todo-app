contents = ["All carrots are to be sliced longitudinally.",
            "The carrots were reportedly sliced.",
            "The slicing process was well presented"]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

# zip, makes to combine both lists to be connected with ean element of the list
for content, filename in zip(contents, filenames):
    # open(f"files....") creates the 3 files, but we need to have a folder with the name files before
    # these files can be created.
    file = open(f"files/{filename}", "w")
    file.write(content)
    file.close()
