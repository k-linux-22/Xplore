def bytes_of_Strings():
    x = bytes("Hello World! ", "utf-8")
    y = bytes("Hello World! ", "utf-16")
    z = bytes("Hello World! ", "utf-32")
    print("\n", x)
    print("\n", y)
    print("\n", z)

bytes_of_Strings()

def bytes_of_Numbers():
    """
    only use numbers from 0 to 255
    """
    a = bytes(5)
    b = bytes(65)
    c = bytes(173)
    d = bytes(254)
    print("\n", a)
    print("\n", b)
    print("\n", c)
    print("\n", d)

bytes_of_Numbers()