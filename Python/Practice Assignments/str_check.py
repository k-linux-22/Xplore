''' accept 2 strings and check if they are identical or 2nd string is a substring of 1st string '''

import re

def match_2_strings(str1, str2):
    
    if re.match(str1, str2):
        print("Both strings are same")
        print(f" \"{str1}\" == \"{str2}\" ")
        
    elif (str1.find(str2)!=-1):
        print(f" \"{str2}\" is a substring of \"{str1}\" ")
    
    else:
        print("No match found.")


str1 = input("Enter string 1 : ")
str2 = input("Enter string 2 : ")
match_2_strings(str1, str2)
