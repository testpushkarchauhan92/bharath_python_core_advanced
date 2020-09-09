from functools import reduce

myNumList = [2,3,3,2]
result1 = reduce(lambda x,y:x+y,myNumList)
print('Sum of All List Elements')
print(result1)

result2 = reduce(lambda x,y:x*y,myNumList)
print('Product of All List Elements')
print(result2)
