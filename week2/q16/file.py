with open("test.txt", "w") as f:
    f.write("line1\nline2\n")
with open("test.txt", "r") as f:
    print(f.read())
