def calculate(a,b):
    sum = a+b
    sub = a-b
    mul = a*b
    div = a/b
    return sum,sub,mul,div

result = calculate(10,5)
print('Printing Tuple : ')
print(result)

print('Printing Values using Loop : ')
for value in result:
    print(value)
