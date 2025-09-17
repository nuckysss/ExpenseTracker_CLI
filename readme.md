Expense Tracker CLI
Expense Tracker is a simple command-line tool to manage your expenses. You can add expenses, update them, delete them, view them, and have a total summary of the expenses. Expenses are saved in a JSON file in the current folder

Features:
$ expense-tracker add --description "Lunch" --amount 20
# Expense added successfully (ID: 1)

$ expense-tracker add --description "Dinner" --amount 10
# Expense added successfully (ID: 2)

$ expense-tracker list
# ID  Date       Description  Amount
# 1   2024-08-06  Lunch        $20
# 2   2024-08-06  Dinner       $10

$ expense-tracker summary
# Total expenses: $30

$ expense-tracker delete --id 2
# Expense deleted successfully

$ expense-tracker summary
# Total expenses: $20

Expense Format
Each expense in expenses.json looks like this, in a list:
{
  "id": 1,
  "date": "2025-09-12T10:00:00"
  "description": "Shoe",
  "amount": 500
}


https://roadmap.sh/projects/expense-tracker
