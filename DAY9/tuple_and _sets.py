# Tupel
#Collection of item
#-are ordered
#- are immutable
#- allow duplicate values 
# -use parentheses
# Why use Tuple
# Answer: Data should never change, you want to protect a data  

fruits = ("Apple", "Banana", "Orange")
print(fruits)

print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[2:])

#Tuple with duplicates 
numbers = (1, 2, 3, 4, 2)
print(numbers) #Duplicates are allowed in tuple
 
print(len(numbers)) #tuple Length 
print(len(fruits))

#Looping through tuple
for num in numbers:
    print(num)

for fruit in fruits:
    print(fruit)


# Set is a collection that stores unique value only, is unoredered, use curly braces, no indexing
cities = {"New York", "London", "Tokyo"}
print(cities) #Order may change every time you run the code 

marks = {11, 11, 23, 45}
print(marks) #Duplicate 11 is remove automatically 

marks.add(95)
print(marks)

marks.remove(11)
print(marks)

marks.discard(23)
print(marks)

##SET OPERATIONS 
# UNION(Combine all the uique items) 
# - symbol: |  
# - method: .union

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A.union(B))
print(A | B)
print(A.intersection(B))
print(A & B)
print(A.symmetric_difference(B))
print(A ^ B)
print(A.difference(B))
print(A - B)


