''' syntax ->   file_object = open(name, mode, buffering)
where, 
name: name of the file
mode: mode in which the file is to be opened
buffering: if value is (0), no buffering occurs, if value is (1), line buffering is performed
'''

''' create a new file or write a file by using 'w' '''
f = open('/home/klinux/Documents/Xplore/Python/new.py', 'w')

''' read the contents of a python file line by line by using 'r' '''
f = open('/home/klinux/Documents/Xplore/Python/new.py', 'r')
for each in f:
    print(each)

# read() can also be used to extract data or read data from a file
print(f.read()) 

f = open('/home/klinux/Documents/Xplore/Python/new.py', 'w')
f.write(" # A new line ")
''' now, all previous data in the file is replaced by # A new file '''
f.close()
''' the close() command terminates all resources in use and frees the system of this particular program '''


''' 'a' is used to add new data to a file '''
f = open('/home/klinux/Documents/Xplore/Python/new.py', 'a')
f.write("\n# This will add a new line")
f.close()

''' 'x' is used to create a new file. If a file already exists, the operation fails '''



''' renaming and deleting a file '''
import os
''' syntax : os.rename("current_file_name", "new_file_name") '''
os.rename("/home/klinux/Documents/Xplore/Python/new.py", "/home/klinux/Documents/Xplore/Python/new_named.py")

''' syntax : os.remove("file_name") '''
os.remove("/home/klinux/Documents/Xplore/Python/new_named.py")
