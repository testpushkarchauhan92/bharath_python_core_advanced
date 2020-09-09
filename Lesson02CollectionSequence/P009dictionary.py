myCovidDictionary={"KA":400,"MH":900,"AP":500}
print(myCovidDictionary)
print(myCovidDictionary.items())

print('\nPrinting Keys Start : ')
keys = myCovidDictionary.keys()
for key in keys:
    print(key)
print('\nPrinting Keys End')

print('\nPrinting Values Start : ')
values = myCovidDictionary.values()
for value in values:
    print(value)
print('\nPrinting Values End \n')

# find values one at a time
searchKey = "MH"
print(myCovidDictionary[searchKey])

# delete element, delete is from python 3 not from collection
del myCovidDictionary[searchKey]
print(myCovidDictionary)
