
# f = open("myfile.txt", "a+")

# for i in range (3):
#     f.write("\nThis is text {0}\n".format(i))
# f.seek(0)
# red = f.read()
# print(red)
# if (f.close()):
#     print("file is closed")

try:
    with open("myfile.txt", "r") as file:
        content = file.read()
        file.write("This is a new line")
        print(content)
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
