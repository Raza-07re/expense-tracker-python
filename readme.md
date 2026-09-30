
# 📁 Project Structure

Start with a simple structure:

```text
expense-tracker/
│
├── main.py
├── expenses.json
└── README.md
```

Later, when the project becomes larger, you can divide it into multiple modules.

---

# 🚀 Phase 1 — Create the Basic Program

Create:

```text
main.py
```

The program should display a menu:

```text
=========================
      EXPENSE TRACKER
=========================

1. Add Expense
2. View Expenses
3. Delete Expense
4. Show Total
5. Exit

Enter your choice:
```

Use a `while` loop so the menu continues appearing until the user chooses Exit.

---

# 📝 Phase 2 — Add an Expense

Create an option that asks the user:

```text
Enter expense name:
Enter amount:
Enter category:
```

Example:

```text
Enter expense name: Lunch
Enter amount: 500
Enter category: Food
```

Store the expense in a dictionary:

```python
expense = {
    "name": "Lunch",
    "amount": 500,
    "category": "Food"
}
```

---

# 📋 Phase 3 — Store Multiple Expenses

Create a list to store multiple dictionaries.

Example:

```python
expenses = [
    {
        "name": "Lunch",
        "amount": 500,
        "category": "Food"
    },
    {
        "name": "Bus",
        "amount": 100,
        "category": "Transport"
    }
]
```

Your program should allow the user to add as many expenses as they want.

---

# 👀 Phase 4 — View Expenses

Create a function:

```python
def view_expenses():
    ...
```

Display expenses in a readable format.

Example:

```text
=========================
       EXPENSES
=========================

1. Lunch       | 500 | Food
2. Bus         | 100 | Transport
3. Coffee      | 250 | Food
```

---

# 💰 Phase 5 — Calculate Total Expenses

Create:

```python
def calculate_total():
    ...
```

Example:

```text
Total Expenses: Rs. 850
```

Use a loop to calculate the total.

Later, try solving the same problem using a list comprehension or `sum()`.

---

# 🗑️ Phase 6 — Delete an Expense

Allow the user to select an expense:

```text
Select expense number to delete: 2
```

Then remove it from the list.

Example:

```text
Expense deleted successfully!
```

Practice:

* List indexing
* `pop()`
* User input
* Error handling

---

# 🔍 Phase 7 — Search Expenses

Add:

```text
6. Search Expenses
```

Ask:

```text
Enter search term:
```

For example:

```text
Enter search term: food
```

Show matching expenses.

Practice:

* String methods
* Loops
* Conditions

---

# 🏷️ Phase 8 — Filter by Category

Add:

```text
7. Filter by Category
```

Example:

```text
Enter category: Food
```

Output:

```text
Food Expenses
----------------
Lunch      Rs.500
Coffee     Rs.250
Dinner     Rs.700
```

---

# 📊 Phase 9 — Category Summary

Create a function:

```python
def category_summary():
    ...
```

The output should look like:

```text
=========================
    CATEGORY SUMMARY
=========================

Food:        Rs. 1450
Transport:   Rs. 500
Shopping:    Rs. 2000
Bills:       Rs. 3500
```

This is an important part of the project because you will practice working with dictionaries.

---

# 📅 Phase 10 — Add Dates

Add a date to every expense.

Example:

```python
expense = {
    "name": "Lunch",
    "amount": 500,
    "category": "Food",
    "date": "2026-09-30"
}
```

Use Python's:

```python
datetime
```

module.

Ideally, the application should automatically use today's date instead of asking the user.

---

# 💾 Phase 11 — Save Data to a File

At this point, your expenses disappear whenever the program closes.

Fix this by saving them to:

```text
expenses.json
```

Use Python's:

```python
json
```

module.

Create:

```python
def save_expenses():
    ...
```

The program should save the expense list whenever appropriate.

---

# 📂 Phase 12 — Load Data

When the program starts, it should read:

```text
expenses.json
```

Create:

```python
def load_expenses():
    ...
```

The program flow should become:

```text
Program starts
      ↓
Load expenses
      ↓
Display menu
      ↓
User performs actions
      ↓
Save expenses
      ↓
Program exits
```

---

# ⚠️ Phase 13 — Error Handling

Your program should not crash if the user enters invalid information.

For example:

```text
Enter amount: abc
```

Instead of crashing:

```text
ValueError
```

Show:

```text
Invalid amount. Please enter a number.
```

Practice:

```python
try:
    ...
except:
    ...
```

Also handle:

* Invalid menu choices
* Negative amounts
* Empty names
* Invalid expense numbers
* Missing JSON file
* Corrupted JSON data

---

# 🧹 Phase 14 — Refactor Your Code

Once everything works, improve your code.

Instead of putting everything inside one giant loop:

```python
while True:
    ...
    ...
    ...
    ...
```

Create functions:

```python
def add_expense():
    pass

def view_expenses():
    pass

def delete_expense():
    pass

def calculate_total():
    pass

def search_expenses():
    pass

def category_summary():
    pass

def save_expenses():
    pass

def load_expenses():
    pass

def main():
    pass
```

Then:

```python
if __name__ == "__main__":
    main()
```

This is where you start practicing **real program structure**.

---

# 🏗️ Phase 15 — Introduce OOP

Do NOT start with classes.

Only after your functional version works, create an `Expense` class.

Example:

```python
class Expense:
    def __init__(self, name, amount, category, date):
        self.name = name
        self.amount = amount
        self.category = category
        self.date = date
```

Then consider creating:

```python
class ExpenseTracker:
    ...
```

This gives you practice with:

* Classes
* Objects
* `__init__`
* Instance attributes
* Methods
* Encapsulation

---

# 🧪 Phase 16 — Test Your Program

Before adding more features, manually test:

### Add

```text
✓ Add valid expense
✓ Add multiple expenses
✓ Add zero amount
✓ Add negative amount
✓ Add invalid amount
```

### Delete

```text
✓ Delete existing expense
✓ Delete invalid expense
```

### Search

```text
✓ Search existing expense
✓ Search nonexistent expense
```

### File

```text
✓ Save data
✓ Load data
✓ Start program with no file
```

---

# 🌟 Phase 17 — Add Advanced Features

Only after the basic application is working should you add these.

## Monthly Report

Example:

```text
=========================
      MONTHLY REPORT
=========================

Total Income:    Rs. 80,000
Total Expenses:  Rs. 35,500
Balance:         Rs. 44,500
```

---

## Expense Statistics

Display:

```text
Highest Expense: Rs. 5000
Lowest Expense:  Rs. 100
Average Expense: Rs. 850
```

---

## Expense Sorting

Allow:

```text
Sort by amount
Sort by date
Sort by category
Sort by name
```

---

## Budget

Allow the user to set:

```text
Monthly Budget: Rs. 50,000
```

Then display:

```text
Budget:       Rs. 50,000
Spent:        Rs. 35,500
Remaining:    Rs. 14,500
```

---

## Income Tracking

Add income:

```text
Salary       Rs. 80,000
Freelancing  Rs. 20,000
```

Then calculate:

```text
Total Income
Total Expenses
Remaining Balance
```

---

# 🎯 Final Version

Your final command-line application could have:

```text
===============================
       EXPENSE TRACKER
===============================

1. Add Expense
2. View Expenses
3. Delete Expense
4. Search Expenses
5. Filter by Category
6. Calculate Total
7. Category Summary
8. Monthly Report
9. Set Budget
10. Add Income
11. View Balance
12. Save Data
13. Exit
```

---

# 📚 Skills You Should Be Able to Demonstrate

After completing this project, you should understand how to use:

```text
Variables
   ↓
Data Types
   ↓
Conditions
   ↓
Loops
   ↓
Lists & Dictionaries
   ↓
Functions
   ↓
Exception Handling
   ↓
File Handling
   ↓
JSON
   ↓
Modules
   ↓
OOP
```

---

# 🏆 Project Rule

Do not copy the entire project from ChatGPT.

Build each feature yourself.

When you get stuck:

1. Understand the problem.
2. Try solving it yourself.
3. Search your Python knowledge.
4. Debug your code.
5. Ask for help only when you cannot move forward.

The goal is not simply to finish the Expense Tracker.

The goal is to become comfortable writing Python without depending on tutorials for every line.

---

# 🚀 Recommended Milestones

### Milestone 1 — Basic Python

```text
Menu
Add expense
View expenses
Calculate total
Delete expense
```

### Milestone 2 — Better Python

```text
Search
Categories
Filtering
Dates
Error handling
```

### Milestone 3 — File Handling

```text
Save JSON
Load JSON
Persistent data
```

### Milestone 4 — Clean Code

```text
Functions
Modules
Refactoring
```

### Milestone 5 — OOP

```text
Expense class
ExpenseTracker class
```

### Milestone 6 — Advanced Features

```text
Budget
Income
Reports
Statistics
Sorting
```

---

# ✅ Definition of Done

The project is complete when:

* [ ] User can add expenses
* [ ] User can view expenses
* [ ] User can delete expenses
* [ ] User can search expenses
* [ ] User can filter by category
* [ ] User can calculate total expenses
* [ ] User can see category totals
* [ ] Expenses have dates
* [ ] Data is saved to JSON
* [ ] Data is loaded when the program starts
* [ ] Invalid input is handled
* [ ] Code is organized into functions
* [ ] OOP version has been implemented
* [ ] Program has been tested manually
* [ ] README is complete

---

# 🎓 Final Objective

This is a **learning project**, not a production financial application.

The main objective is:

```text
Learn Python
     ↓
Practice Python
     ↓
Build something yourself
     ↓
Debug it
     ↓
Improve the code
     ↓
Understand why it works
```

Once you finish this project independently, you can move to a second project that introduces APIs, databases, or a framework.
