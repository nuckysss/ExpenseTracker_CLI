import os 
import datetime
import json
import argparse
import sys

class Expenses:
    def __init__(self, id,description, date, amount):
        self.id = id
        self.description = description
        self.date = date
        self.amount = amount

    def to_dict(self):
        return{
            "id": self.id, "date": self.date, "description": self.description, "amount": self.amount
        }
    
    @staticmethod
    def from_dict(user_expenses):
        return Expenses(
            id = user_expenses["id"], date = user_expenses["date"], description = user_expenses["description"], amount = user_expenses["amount"]
        )

parser = argparse.ArgumentParser(description="Expense Tracker CLI")

parser.add_argument("command", choices = ["add", "update", "delete", "view", "summary"], help= "Action to perform")
parser.add_argument("params", nargs="*", help="Parameters for the command")

args = parser.parse_args()

print(args.command)
print(args.params)
    

def read_expenses():
    if not os.path.exists("expense.json"):
        return []
    try:
        with open("expense.json", "r") as file:
            user_expenses = json.load(file)
            return [Expenses.from_dict(expense) for expense in user_expenses if isinstance(expense, dict)]
    except (json.JSONDecodeError, FileNotFoundError):
        user_expenses =[]

def store_expenses(expenses):
    with open("expense.json", "w") as file:
        json.dump([expense.to_dict() for expense in expenses], file, indent=4)

def add_expense(expenses):
    if not args.params or len(args.params) < 2:
        print("A description and amount are required to add an expense")
        return
    date=args.params[0]
    amount = args.params[1]
    idNum = max([expense.id for expense in expenses], default=0) + 1
    description = datetime.datetime.now().isoformat()
    new_expense = Expenses(idNum, date, description, amount)
    expenses.append(new_expense)
    store_expenses(expenses)
    print(f"Expense(ID: {idNum}) added succesfully")

def update(expenses):
    if not args.params or len(args.params) < 3:
        print("An ID, description and amount are required to add an expense")
        return
    try:
        idNum = int(args.params[0])
    except ValueError:
        sys.exit("ID number must be an interger")
    description =args.params[1]
    amount = args.params[2]
    for expense in expenses:
        if expense.id == idNum:
            expense.description = description
            expense.amount = amount
            expense.date = datetime.datetime.now().isoformat()
            store_expenses(expenses)
            print(f"Expense(ID: {idNum}) updated succesfully")
            return
    print(f"Expense (ID: {idNum}) not found")
      
def delete(expenses):
    if not args.params or len(args.params) < 1:
        sys.exit("An ID number is needed to delete an expense record")
    try:
        idNum = int(args.params[0])
    except ValueError:
        sys.exit("ID number must be an interger")
    for i, expense in enumerate(expenses):
        if expense.id == idNum:
            expenses.pop(i)
            store_expenses(expenses)
            print(f"Expense(ID: {idNum}) deleted succesfully")
            return
    print(f"Expense(ID: {idNum}) not found")

def view_all(expenses):
    if args.params and len(args.params) >= 1:
        everything =[expense for expense in expenses if expense.description == args.params[2]] 
    else:
        everything = expenses
    if not everything:
        print("No expenses found")
    else:
        for something in everything:
            print(f"ID: {something.id} | Date: {something.date} | Description: {something.description} | Amount:  ${something.amount}")

def summary(expenses):
    total: int = 0
    if args.command == "summary":
        for expense in expenses:
            total += int(expense.amount)
        print(f"Total expenses: ${total}")


def main():
    expenses = read_expenses()
    if args.command  == "add":
        add_expense(expenses)
    elif args.command == "update":
        update(expenses)
    elif args.command == "delete":
        delete(expenses)
    elif args.command == "view":
        view_all(expenses)
    elif args.command == "summary":
        summary(expenses)

if __name__ == "__main__":
    main()