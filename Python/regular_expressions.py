'''
Used to check the existance of a Pattern in a given Sequence of Characters.
For example, email IDs, passwords, etc.
'''

import re
''' re.match(pattern, sequence, flags=0) '''
print(re.match("Hello", "Hello"))

''' re.search(pattern, sequence, flags=0) '''
print(re.search("e", "Hello"))
print(re.search("ll", "Hi, my name is Mello"))

''' re.sub(pattern, replace, string, count=0, flags=0) '''
print(re.sub("Hi", "Hello", "Hi, I am a person."))


''' Basic patterns '''
import re

def match_2_strings(str1, str2):
    if re.match(str1, str2):
        print(f"It's a match\n {str1} == {str2}")
    else:
        print(f"It's not a match\n {str1} != {str2}")

a = "Hello"
b = "Hello"
match_2_strings(a, b)
c = "Hello"
d = "Hi"
match_2_strings(c, d)

print(re.match("he.lo.", "hello!"))
print(re.match("hi\w2\w", "hi123"))

print(re.match("hel+o", "hello"))
print(re.match("h*i*", "hii"))


''' Group feature '''
def match_email_format(string):
    match = re.search("([\w]+)@([\w.]+)", string)
    if match:
        print("\n")
        print(match.group())
        print(match.group(1))
        print(match.group(2))
    else:
            print("No match found")

string = "Please contact us at kalilinux@outlook.com"
match_email_format(string)
string = "Please contact us at kali.linux@outlook.com"
match_email_format(string)

