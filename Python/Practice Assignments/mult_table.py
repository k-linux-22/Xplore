def multipl_table(num, upto):
    if num>=0 and upto>=0:
        print(f"Table of {num} upto {upto} multiples:")
        for i in range(0, upto+1):
            print(f"{num} x {i} = {num*i}")
    else:
        print("Cannot accept a negative number")

num = int(input("Enter a number : "))
upto = int(input("Enter the table range (number of multiples, like upto 5, 10, or less, or more) : "))
multipl_table(num, upto)
