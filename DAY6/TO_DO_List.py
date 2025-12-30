tasks = []
while True:
         print("\n TO DO LIST")
         print("1. Add Task")
         print("2. View Task")
         print("3. Exit")

         choose = input("Choose an option: ")
         if choose == "1":
              task = input("Enter a task: ")
              tasks.append(task)
              print("Task Added")
         elif choose == "2":
              print("\n Your Taks:")
              for task in tasks:
                print("-", task)
         elif choose == "3":
              print("Goodbye")
         else:
              print("Invalid number")
