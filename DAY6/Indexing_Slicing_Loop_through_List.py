marks = [90, 78, 76, 67, 79]
#INDEXING -> Indes start from 0
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[-1])
#SLICING -> End index is not included 
print(marks[1:4])
print(marks[:3])
print(marks[3:])
total = 0
for mark in marks: # Loop through a list -> To process every item without writing code again and again
    total = total + mark
print(total)

total_percentage = (total/500)*100
print(f"Your total marks id {total_percentage}")
