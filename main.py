# with open("my_file.txt") as file:
#     content = file.read()
#     print(content)


with open("my_file.txt", mode="a") as file:
    file.write("New Text")

with open("new_file.txt", mode="w") as new_file:
    new_file.write("Hello, my name is Ramy")
