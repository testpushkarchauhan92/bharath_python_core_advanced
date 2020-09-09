def average(a,b):
    print('a : ', a)
    print('b : ', b)
    return (a+b)/2

# Old Way
# print(average(10,90))

# New Way
print(average(a=10,b=90))

# Sequence does not matter if we use keyword a b. This is called 'Keyword Arguments'
print(average(b=10,a=90))
