myNumList = [9,8,2,6,3]

result1 = map(lambda n:n*2,myNumList)
print(result1)
print(type(result1))

result2 = list(map(lambda n:n*2,myNumList))
print(result2)
print(type(result2))
