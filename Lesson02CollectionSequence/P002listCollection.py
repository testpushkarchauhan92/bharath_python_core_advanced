fruitList=[]
print(fruitList)
cricketerList=["Sachin","Virat","Dhoni"]
print(cricketerList)
employeeList=['Pooja','Archana','Jyothi','Shraddha','Aarti']
print(employeeList)
multivalueList=[-3.14,9826012345,'Pushkar',"Bangalore",123,-456]
print(multivalueList)
#indexing
print(multivalueList[2])
#slicing
print(multivalueList[3:5])
#repetition
print(multivalueList*4)
#length of string
print(len(multivalueList))

#adding elements to fruitList
fruitList.append('Apple')
fruitList.append('Watermelon')
fruitList.append('Banana')
fruitList.append('Jackfruit')
fruitList.append('Papaya')
fruitList.remove('Jackfruit')
#fruitList.remove('papaya')
# Del is inbuilt function
del(fruitList[1])
print(fruitList)

# Clear the list
fruitList[:] = []
print(fruitList)

# aggregate operations in list
marks=[90,80,20,60,30]
print(marks)
minMarks = min(marks)
maxMarks = max(marks)
sumMarks = sum(marks)
countMarks = len(marks)
averageMarks = sumMarks / countMarks
print(minMarks)
print(maxMarks)
print(sumMarks)
print(countMarks)
print(averageMarks)
marks.insert(3,99)
print(marks)

# Sort List Asc
marks.sort()
print(marks)

# Sort List Desc
marks.sort(reverse=True)
print(marks)
