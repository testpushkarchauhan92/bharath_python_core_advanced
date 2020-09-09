# Regular Way
a=[2,4,6,8]
b=[3,6,9]
result1=[]
result2=[]

for i in a:
    if i in b:
        result1.append(i)

print("Using Normal Way : ")
print(result1)

print("Using List Comprehension : ")
result2 = [i for i in a if i in b]
print(result2)
