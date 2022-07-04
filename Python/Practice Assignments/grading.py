''' 
subN_m == Marks obtained in a subject 
subN_t == Total marks of a subject
avg == Average of marks obtained
prcnt == Percentage obtained
'''

def grade(roll_num, name, sub1_m, sub2_m, sub3_m, sub4_m, sub1_t, sub2_t, sub3_t, sub4_t):
    # avg = (sub1_m + sub2_m + sub3_m + sub4_m)/4
    prcnt = ((sub1_m + sub2_m + sub3_m + sub4_m)*100)/(sub1_t + sub2_t + sub3_t + sub4_t)
    if prcnt >= 80:
        print(f"Total percentage : {prcnt}")
        print("Grade : A")
        print(f"R.No.: {roll_num}, {name}, Promoted Successfully")
    
    elif prcnt < 80 and prcnt >= 60:
        print(f"Total percentage : {prcnt}")
        print("Grade : B")
        print(f"R.No.: {roll_num}, {name}, Promoted Successfully")
    
    elif prcnt < 60 and prcnt >= 40:
        print(f"Total percentage : {prcnt}")
        print("Grade : C")
        print(f"R.No.: {roll_num}, {name}, Promoted Successfully")

    elif prcnt < 40:
        print(f"Total percentage : {prcnt}")
        print("Grade : F")
        print(f"R.No.: {roll_num}, {name}, Not Promoted")

roll_num = int(input("Student Roll number : "))
name = str(input("Student Name : "))

sub1_m = int(input("Marks obtained in sub1 : "))
# sub1_t = int(input("Toal marks of sub1 : "))
sub1_t = 50

sub2_m = int(input("Marks obtained in sub2 : "))
# sub2_t = int(input("Toal marks of sub2 : "))
sub2_t = 50

sub3_m = int(input("Marks obtained in sub3 : "))
# sub3_t = int(input("Toal marks of sub3 : "))
sub3_t = 50

sub4_m = int(input("Marks obtained in sub4 : "))
# sub4_t = int(input("Toal marks of sub4 : "))
sub4_t = 50

print("\n")
grade(roll_num, name, sub1_m, sub2_m, sub3_m, sub4_m, sub1_t, sub2_t, sub3_t, sub4_t)