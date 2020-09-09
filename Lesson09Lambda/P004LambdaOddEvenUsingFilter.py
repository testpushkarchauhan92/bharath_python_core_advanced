myNumList = [11,22,33,44,55,22]

result1 = filter(lambda n:n%2==0,myNumList)
print(result1)
print(type(result1))

print("-----------")

# Convert filter into a list
result2 = list(filter(lambda n:n%2==0,myNumList))
print(result2)
print(type(result2))

print("-----------")

for i in result1:
    print(i)

print("-----------")

for i in result2:
    print(i)
