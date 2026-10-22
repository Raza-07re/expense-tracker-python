"""A simple JSON-backed command-line expense tracker."""
import json
import os
from pathlib import Path

DATA_FILE = Path(__file__).resolve().with_name("expenses.json")


def load_expenses():
    """Load expenses safely; create an empty list when no data file exists."""
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            expenses = json.load(file)
    except json.JSONDecodeError as error:
        raise ValueError(
            f"{DATA_FILE.name} contains invalid JSON. Back it up and fix the file."
        ) from error
    if not isinstance(expenses, list):
        raise ValueError("Expense data must be a JSON list.")
    for item in expenses:
        if not isinstance(item, dict) or not {"name", "amount", "category"} <= item.keys():
            raise ValueError("An expense entry is missing name, amount, or category.")
        if not isinstance(item["amount"], (int, float)) or item["amount"] <= 0:
            raise ValueError("Expense amounts must be positive numbers.")
    return expenses


def save_expenses(expenses):
    """Write data safely by replacing the file only after a complete write."""
    temporary_file = DATA_FILE.with_suffix(".json.tmp")
    with temporary_file.open("w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4, ensure_ascii=False)
        file.write("\n")
    os.replace(temporary_file, DATA_FILE)


def prompt_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def prompt_amount():
    while True:
        raw_amount = input("Amount: ").strip()
        try:
            amount = float(raw_amount)
            if amount <= 0 or not amount < float("inf"):
                raise ValueError
            return round(amount, 2)
        except ValueError:
            print("Enter a valid amount greater than 0, such as 250 or 99.50.")


def add_expense(expenses):
    expense = {
        "name": prompt_text("Expense name: "),
        "amount": prompt_amount(),
        "category": prompt_text("Category: ").title(),
    }
    expenses.append(expense)
    save_expenses(expenses)
    print(f"Saved: {expense['name']} — {expense['amount']:.2f}")


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\n" + "=" * 58)
    print(f"{'#':<4}{'Name':<24}{'Category':<16}{'Amount':>12}")
    print("-" * 58)
    for number, item in enumerate(expenses, start=1):
        print(f"{number:<4}{item['name'][:22]:<24}{item['category'][:14]:<16}{item['amount']:>12.2f}")
    print("-" * 58)
    print(f"{'Total':<44}{sum(item['amount'] for item in expenses):>14.2f}")


def delete_expense(expenses):
    view_expenses(expenses)
    if not expenses:
        return
    try:
        choice = int(input("Enter the expense number to delete: "))
    except ValueError:
        print("Please enter a whole number.")
        return
    if not 1 <= choice <= len(expenses):
        print("That expense number does not exist.")
        return
    deleted = expenses.pop(choice - 1)
    save_expenses(expenses)
    print(f"Deleted: {deleted['name']}")


def find_expense(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    query = prompt_text("Search by expense name: ").casefold()
    matches = [item for item in expenses if query in item["name"].casefold()]
    if not matches:
        print("No matching expense found.")
        return
    for item in matches:
        print(f"{item['name']} | {item['category']} | {item['amount']:.2f}")


def show_summary(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    total = sum(item["amount"] for item in expenses)
    print(f"\nNumber of expenses: {len(expenses)}")
    print(f"Total spending: {total:.2f}")
    print(f"Average expense: {total / len(expenses):.2f}")
    print("\nSpending by category:")
    totals = {}
    for item in expenses:
        totals[item["category"]] = totals.get(item["category"], 0) + item["amount"]
    for category, amount in sorted(totals.items(), key=lambda pair: pair[1], reverse=True):
        print(f"  {category:<20} {amount:>10.2f}")


def main():
    actions = {
        "1": ("Add expense", add_expense),
        "2": ("View expenses", view_expenses),
        "3": ("Delete expense", delete_expense),
        "4": ("Find expense", find_expense),
        "5": ("Show summary", show_summary),
    }
    try:
        expenses = load_expenses()
    except (OSError, ValueError) as error:
        print(f"Could not load expenses: {error}")
        return

    while True:
        print("\n" + "=" * 32)
        print("         EXPENSE TRACKER")
        print("=" * 32)
        for key, (label, _) in actions.items():
            print(f"{key}. {label}")
        print("0. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "0":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action is None:
            print("Invalid choice. Select 0–5.")
            continue
        try:
            action[1](expenses) if choice == "1" else action[1](expenses)
        except (OSError, ValueError) as error:
            print(f"Could not complete that operation: {error}")


if __name__ == "__main__":
    main()
