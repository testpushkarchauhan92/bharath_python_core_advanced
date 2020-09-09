def decoratorFunction(fun):
    def innerFun():
        result = fun()
        return result*2
    return innerFun

# Old Way
# This function will be decorated
# def num():
#     return 5
#
# resultFunction = decoratorFunction(num)
# print(resultFunction())

# New Way
# This function will be decorated once we add annotation
# Function name can be anything not necessarily decoratorFunction
@decoratorFunction
def num():
    return 5

print(num())
