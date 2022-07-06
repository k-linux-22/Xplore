""" anonymous functions """


''' Lambda function '''
''' 
- used to create small functions
- a one-time use function 
- can have many arguments, but only one expression
- cannot have a return statement
- returns a function object which can be assigned to a variable
- syntax ->     lambda argument(s) : expression
'''

''' rather than using -
def sqr_of_num(num):
    return num**2
we can use - 
'''
sqr_of_num = lambda x : x**2
print(sqr_of_num(5))
print(type(sqr_of_num))


''' Map '''
'''
- used to perfrom an operation on all the input items
- arguments are provided as function object and any number of iterables like list, dictionary, etc.
- syntax ->    map(function object, iterable 1, iterable 2, ...)
'''

# to print output, always use a data type(list, tuple) because map does not show the output with print

print( list( map( lambda x : x*x, [1, 2, 3, 4, 5] ) ) )

''' for better visualization - 

print( 
    list( 
        map( 
            lambda x : x*x, [1, 2, 3, 4, 5] 
            ) 
        ) 
    )

'''
lst1 = [1,2,3,4]
lst2 = [5,6,7,8]
print(
    list(
        map(
            lambda x, y : x+y, lst1, lst2
        )
    )
)


''' Filter '''
'''
- takes a function object and an iterable
- can only take one iterable as input
- the function object returns a boolean value
- object is called for each element of the iterable
- filter returns only those elements for which the value of the object is True
- syntax ->    filter(function object, iterable)
'''

list1 = [1,2,5,6,8,9,10]
print(
    list(
        filter(
            lambda x : x%2==0, list1
            )
        )
    )

dict1 = [{"name": "Mark", "score": 80},
         {"name": "John", "score": 85}, 
         {"name": "Mary", "score": 70}
        ]
print(
    list(
        filter(
            lambda x : x["score"] >= 80, dict1
            )
        )
    )


''' Reduce '''
'''
- takes a function object and an iterable input
- used to perform operations on a List
- syntax ->     reduce(function object, iterable)
'''
'''
instead of using - 

def list_product(list):
    product = 1
    for i in list:
        product = product*1
    return product

we can use -
'''
import functools
print(
    functools.reduce(
        lambda x, y: x*y, [1,2,3,4]
        )
    )
