# passing Parameters in a function by reference

def DemoList(myList):
    for i in range(1, 10):
        myList.append(i)
    print(f"The demo list after change : {myList}")

myList = [0]
print(f"The demo list before change : {myList}")
print(f"\n")
DemoList(myList)
