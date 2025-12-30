#ATM menu system
balance = 1000
while True:
    print("\n ATM Menu")
    print("1. Check the Balance")
    print("2. Deposite")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Choose an option")
    if choice == "1":
        print(balance)
    elif choice == "2":
        amount = int(input("Enter a balance:"))
        new_balance = balance + amount
        print(new_balance)
    elif choice == "3":
        withdraw = int(input("Withdraw amount:"))
        if balance < withdraw:
                print("Insaficient Amount")
        else:
            withdraw_amount = withdraw - balance 
            print(withdraw_amount)
    elif choice == "4":
        print("Thank You for using ATM")

    else:
         print("Invalid Choice")
