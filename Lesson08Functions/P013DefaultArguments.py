def average(a=10,b=90):
    print('a : ', a)
    print('b : ', b)
    return (a+b)/2

# When no arguments are passed default values are passed
print(average())
# When some arguments are passed actual values are passed
print(average(a=30))
