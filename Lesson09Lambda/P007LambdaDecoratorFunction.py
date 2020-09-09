def decoratorFunction(fun):
    def innerFun():
        result = fun()
        return result*2
    return innerFun

# This function will be decorated
def num():
    return 5

resultFunction = decoratorFunction(num)
print(resultFunction())
