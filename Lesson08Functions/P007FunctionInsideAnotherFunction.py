# Defining Function inside another function
def display(name):
    def message():
        return "Hello "
    result = message()+name
    return result

myResult = display('Pushkar')
print(myResult)

# You cannot invoke inner function without calling outer function
