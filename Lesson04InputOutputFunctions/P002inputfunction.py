s1=input()
print('You entered for s1 : ',s1)
s2=input('Enter name: ')
print('You entered for s2 : ',s2)
i1=int(input('Enter an integer : '))
print(i1)
f1=float(input('Enter a float : '))
print(f1)

# By default takes string
intList1 = [x for x in input('Enter 3 integer numbers separated by space ').split()]
print(intList1)
floatList1 = [x for x in input('Enter 3 float numbers separated by comma ').split(',')]
print(floatList1)
#type casting to int
intList2 = [int(x) for x in input('Enter 3 integer numbers separated by space ').split()]
print(intList2)
floatList2 = [float(x) for x in input('Enter 3 float numbers separated by comma ').split(',')]
print(floatList2)
