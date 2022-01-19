import os
import json

rootdir = 'antiochmod'

count = 0
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file == "json":
            filepath = os.path.join(subdir, file)
            print(count, " ", filepath, end=" -> ")
            f = open(filepath)
            data = json.load(f)
            print(count, end=" ")
            if "author" in data:
                author = data["author"]
                print("Author: {}".format(author))
            else:
                print("Author is missing")
            f.close()
            count += 1