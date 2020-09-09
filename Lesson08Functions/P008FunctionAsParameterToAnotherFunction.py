# Function as parameter to another function single argument
def display(fun):
    return "Hello " + fun

def name():
    return 'Pushkar'

print(display(name()))

# Function as parameter to another function double argument
def display(firstName,lastName):
    return "Hello " + firstName + " "+ lastName

def fname():
    return 'Pushkar'

def lname():
    return 'Chauhan'

print(display(fname(),lname()))
