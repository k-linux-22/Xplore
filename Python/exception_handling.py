''' syntax ->
code block
try:
    logic/operations here
except Exception1:
    if there is an exception, execute this block
except Exception2:
    if there is an exception, execute this block
else:
    if there is no exception, execute this block
'''

# import module sys to get the type of exception
import sys

def reciprocal():
    try:
        x = int(input("Enter an integer : "))
        r = 1/x
        print(f"The reciprocal of {x} is {r}")
    except:
        print(f"Oops! {sys.exc_info()[0]} occured.")
        print("Please try again.")

reciprocal()
