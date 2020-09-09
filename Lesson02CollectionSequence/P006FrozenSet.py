# Set Does not allow duplicates in Python
set={10,20,30,"Pushkar",10,20,30,"Pushkar"}
print(set)
print(type(set))
# Frozen Set similar to Immutable / UnmodifiableSet
# Cannot Update a Frozen Set
f = frozenset(set)
#f.update([20])
