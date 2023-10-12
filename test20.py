import os
import string
def my_function(dirname, find, replace):
    filenames = os.listdir(dirname)
    for filename in filenames:
        path = dirname + "\\" + filename
        print(path)
        if os.path.isdir(path):
            print("is a folder")
            my_function(path, find, replace)
        elif path.endswith(".txt"):
            old_contents = read(path)
            n = old_contents.count(find)
            if n == 0
            print("could not find" + find)
            continue
        new_contents = old_contents.replace(find, replace)
        responese = input(" replace" + str(n) + " occurrences" + "")