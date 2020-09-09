print('Print numbers from 1 to 20 and skip multiples of 3')
x=0
while x<20:
    x+=1
    if x%3 == 0:
        continue
    print(x)
