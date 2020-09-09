# Lambda is an anonymous function which does not have a name
# Lambda will always return a function back
def cube(n):
    return n**3

print(cube(2))

print("----------")

functionReturnedByLambda = lambda n:n**3
print(functionReturnedByLambda(3))

print("----------")
