def decoratorFunction(fun):
    def innerFunction(n):
        result = fun(n)
        result += " How are you?"
        return result
    return innerFunction

@decoratorFunction
def greet(name):
    return "Hello " + name

print(greet("Pushkar"))
