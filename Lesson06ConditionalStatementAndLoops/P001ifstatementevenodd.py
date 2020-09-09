x=int(input('Enter a number to check even or odd : '))
# handle boundary check for 0
if x==0:
    print(x,' you entered zero')
elif x%2 == 0:
    print(x,' is even')
else:
    print(x,' is odd')
