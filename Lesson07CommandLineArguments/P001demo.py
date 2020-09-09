# sys is module to get cmd line args
import sys
list=sys.argv
for i in list:print(i)

print("Length of list : ")
print(len(list))

# retrieve argument from list
print("Retrieve element at 0 index : ")
print(list[0])

#python3 P001demo.py 123 456 789
