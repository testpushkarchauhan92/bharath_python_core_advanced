myTupleEmpty=()
print(myTupleEmpty)
myTupleOne=(40,50,60,"Pushkar",3.14,50,50,50,50)
print(myTupleOne)

#need to add comma to consider it as a tuple otherwise will consider as int
myTupleTwo=(40)
myTupleThree=(40,)
print(type(myTupleTwo))
print(type(myTupleThree))

#indexing
print(myTupleOne[3])
#repetition
print(myTupleOne*2)
#Cannot modify a tuple so no slicing on tuple

print(myTupleOne.count(50))
print(myTupleOne.index("Pushkar"))
