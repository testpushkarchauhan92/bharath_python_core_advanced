# Using regular python programming
print("Using Normal Python Programming : ")
list = []
for value in range(1,11):
    list.append(value**3)
print(list)

# Using list comprehension
print("Using List Comprehension : ")
numList = [x**3 for x in range(1,11)]
print(numList)
