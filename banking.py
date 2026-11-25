balance = 1000

while True:
    print("\n--- Banking Management System ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Current Balance:", balance)

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            print("Deposit successful!")
            print("Updated Balance:", balance)
        else:
            print("Invalid deposit amount.")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))

        if amount > 0 and amount <= balance:
            balance -= amount
            print("Withdrawal successful!")
            print("Updated Balance:", balance)
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            print("Insufficient balance!")

    elif choice == "4":
        print("Thank you for using the system.")
        break

    else:
        print("Invalid choice. Try again.")
