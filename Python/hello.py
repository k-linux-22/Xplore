# def greetings(name, greeting="Hello"):
#     print(f"{greeting}, {name}.")
# greetings("John")


def greetings(*names, greeting="Hello"):
    for name in names:
        print(f"{greeting}, {name}.")
# greetings("John", "Ham", "Tiger")


# convert output to txt file
# python hello.py > hello.txt