myList=[9,8,2,6,3]
print(type(myList))

# List to Byte
b = bytes(myList)
print(b)
print(type(b))

# bytes and bytearray is immutable i.e. we cannot add or remove elements
# b[3]=22

b1=bytearray(myList)
print(b1)
print(type(b1))
