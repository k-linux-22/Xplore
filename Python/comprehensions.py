'''
4 types : 
- List Comprehensions
- Dictionary Comprehensions
- Set Comprehensions
- Generator Comprehensions
'''


""" List Comprehensions """

''' syntax: [output_exp for var in input_list(Predicate expression)] '''

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

names = ["Rajesh", "Juhi", "Pritam", "Farha"]
name_length = {l:len(l) for l in names}
print(name_length)

student_names = ["Sidhu", "Tarun", "Swatantra", "Rupin", "Shubham"]
student_scores = [90, 75, 80, 85, 70]
name_score = {key:value for (key, value) in zip(student_names, student_scores)}
print(name_score)

people = {"Rohan": 21, "Sheetal": 19, "Karan": 18, "Preeti": 22}
seniors = {key:value for (key, value) in people.items() if value>20}
print(seniors)

''' Nested Dictionary Comprehensions '''

'''syntax: 

output_data = {outer_k:{inner_k:my_func(inner_v) for inner_k, inner_v in outer_v.items()} for outer_k, outer_v in outer_dict.items()}

'''