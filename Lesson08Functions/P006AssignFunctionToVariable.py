x=6

def display():
    x=5
    print('Printing Local Variable : ')
    print(x)
    print('Printing Global Variable Using globals()[globalVariableName]: ')
    print(globals()['x'])

print('Printing Global Variable : ')
print(x)
display()

print('------------')
#Assigning Function to a Variable
z = display
z()
z()
z()

# If Both Global and Local Variable has same name
# Then Within Function, Local Variable takes precedence over Global Variable
