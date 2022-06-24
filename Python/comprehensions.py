'''
4 types : 
- List Comprehensions
- Dictionary Comprehensions
- Set Comprehensions
- Generator Comprehensions
'''


""" List Comprehensions """

''' syntax: [output_exp for var in input_list(Predicate expression)]'''

def squaring_list_of_integers(list):
    output_list = [ i**2 for i in input_list if isinstance(i, int)]
    print(output_list)

input_list = [10, 20, 30, 40, 50]
squaring_list_of_integers(input_list)

input_list = [10, 20, 30, "a", 40, 50, "xyz"]
squaring_list_of_integers(input_list)

''' List Comprehensions for Nested loops, using Predicate expression '''

''' syntax: 
[
expressioin for i in list1 [if condition1]
for j in list2 [if condition2] ...

for n in listN [if conditionN]
]
'''

''' here, we create a List by taking elements for a List of lists '''
input_list = [ ['a', 'b'], ['c', 'd', 'e'], ['i', 'j'], ['x', 'y', 'z'] ]

output_list = [term for i in input_list for term in i]

print(output_list)


""" Dictionary Comprehensions """

''' syntax:
output_dict = {key:value for {key, value} in input_dict.items()} 
or
output_dict = {key:value for {key, value} in input_dict.items() if condition }
'''

