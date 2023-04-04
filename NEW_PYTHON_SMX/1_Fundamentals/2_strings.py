course="python"  ##---> for single line
message='''
hello, my name is soham '''  ###----> ''' ''' us this for multiple lines

print(len(course)) ## --->6
 ## len() returns the number of items in container


print(course[0]) ##---> p
print(course[-1]) ##---> n
print(course[-2]) ##---> o

## 0   1   2   3   4   5
## p   y   t   h   o   n
##-6  -5  -4  -3  -2  -1

print(course[0:3]) ##---> pyt  // printing characters will be from 0 to 2, index 3 will not be printed
print(course[0:]) ##--->Python
print(course[:3]) ##--> pyt
print(course[:]) ##--->Python
print(course[1:-1]) 