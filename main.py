import json as js
def add_expense():
    try:
                with open("expenses.json", "r") as file:
                    expenses = js.load(file)
    except FileNotFoundError:
    
                expenses = []
    name = input("Enter expense name: ")
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")

    expense = {
                "name": name,
                "amount": amount,
                "category": category
            }
    
    expenses.append(expense)            
    with open("expenses.json", "w") as file:
                js.dump(expenses, file, indent=4)
    print("Expense saved successfully!")

def view_expense():

    try:
        with open("expenses.json", "r") as file:
            expenses = js.load(file)

        if not expenses:
            print("No expenses found.")

        else:
            print("\n========== EXPENSES ==========")

            for expense in expenses:
                print(f"Name: {expense['name']}")
                print(f"Amount: {expense['amount']}")
                print(f"Category: {expense['category']}")
                print("------------------------------")

    except FileNotFoundError:
        print("No expense file found.")

def delete_expense():
        try:
        
            with open("expenses.json", "r") as file:
                expenses = js.load(file)

            if not expenses:
                print("No expenses found.")

            else:
                
                print("\n========== EXPENSES ==========")

                for index, expense in enumerate(expenses, start=1):
                    print(f"{index}. {expense['name']} - {expense['amount']} - {expense['category']}")

                
                choice = int(input("\nEnter expense number to delete: "))

                
                if 1 <= choice <= len(expenses):
                    deleted_expense = expenses.pop(choice - 1)

                
                    with open("expenses.json", "w") as file:
                        js.dump(expenses, file, indent=4)

                    print(f"{deleted_expense['name']} deleted successfully!")

                else:
                    print("Invalid expense number.")

        except FileNotFoundError:
            print("No expense file found.")        
    
def find_expense():
   
    with open("expenses.json", "r") as file:
        expenses = js.load(file)

    search_name = input("Enter expense name: ")

    found = False

    for expense in expenses:
        if expense["name"].lower() == search_name.lower():
            print("\nExpense Found!")
            print("Name:", expense["name"])
            print("Amount:", expense["amount"])
            print("Category:", expense["category"])

            found = True
            break

    if not found:
        print("Expense not found.")

def show_total():
   with open("expenses.json", "r") as file:
        expenses = js.load(file)

        total = 0

        for expense in expenses:
            total += expense["amount"]

        print(f"Total Expense: {total}") 

while (True):
    print("========================= EXPENSE TRACKER =========================\n")
    print("1. add expense")
    print("2. view expense")
    print("3. Delete Expense")
    print("4. find expense")
    print('5.show total')
    print("6. exit")
    choice=input('enter your choice : ')

    if choice == "1":
    
           add_expense()
        
    elif choice=="2":
            
            view_expense()
    
    elif choice=="3":
    
          delete_expense()

    elif choice=="4":
         find_expense()
    elif choice=="5":
         show_total()
    elif choice=="6":
         break 
    else:
         print("invalid choice!")