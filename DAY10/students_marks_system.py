marks = {
    "math" : 85,
    "science" : 78,
    "english" : 90,
}
print(marks.get("history", "0"))
for keys in marks.keys():
    print(keys)

total = 0
for value in marks.values():
    total += value
print("Total Marks =", total)

count = len(marks)
print(count)

average_marks = total/count
print(average_marks)
