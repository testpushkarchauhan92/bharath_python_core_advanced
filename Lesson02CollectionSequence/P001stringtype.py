s="Hello World"
str="     Hello python  "
s1="My name is Pushkar"
print(s1)
print("=================")
s2="""My
name
is
Pushkar
"""
print(s2)
print(s2[0])
print("=================")
#repetition
print(s*2)
print("=================")
print(len(s))
print("=================")
#slicing a string
print(s[0:5])
print("slicing a string no end")
#slicing a string no end
print(s[0:])
print("slicing a string no start")
#slicing a string no start
print(s[:10])
print("slicing a string negative numbers")
#slicing a string negative numbers
print(s[-5:-1])
print("slicing a string using step value")
#slicing a string using step value
print(s[0:9:2])
print("=================")
print(s[15::-1])
print("=================")
print(s[::-1])
print("strip function")
# strip function
print(str.strip())
print("lstrip function")
print(str.lstrip())
print("rstrip function")
print(str.rstrip())
print("=================")
print(str.find("He"))
print("=================")
print(str.find("Python",0,len(str)))
print(str.find("Python",0,8))
print("=================")
print(str.count("o"))
print("=================")
print(str.replace("Python", "python3"))
print("string to upper")
print(str.upper())
print("string to lower")
print(str.lower())
print("string to title")
print(str.title())
print("=================")
