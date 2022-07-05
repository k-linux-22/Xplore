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
