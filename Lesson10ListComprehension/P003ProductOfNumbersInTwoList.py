# Using normal python programming
list1=[1,3,5]
list2=[2,4,6]

output1=[]
for i in range(len(list1)):
    output1.append(list1[i]*list2[i])
print("Normal Way : Multiply nth Element in List1 with nth Element in List2")
print(output1)

output2=[]
for i in range(len(list1)):
    output2.append(list1[i]*list1[i])
print("Normal Way : Multiply nth Element in List1 with nth Element in List1")
print(output2)

output3=[]
for i in range(len(list2)):
    output3.append(list2[i]*list2[i])
print("Normal Way : Multiply nth Element in List2 with nth Element in List2")
print(output3)

output4=[]
output4=[list1[i]*list2[i] for i in range(len(list1))]
print("List Comprehension : Multiply nth Element in List1 with nth Element in List2")
print(output4)
