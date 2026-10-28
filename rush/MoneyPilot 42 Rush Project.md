# **MoneyPilot — Financial Survival Simulator**

Recommended for Rush00

MoneyPilot is a Python-based personal finance application that helps users track their money, understand spending habits, predict how long their savings will last, and decide whether they can safely afford a purchase.

Instead of building a basic expense tracker, you're creating a small financial decision-support system.

Based on your 42 Bangkok Rush00 instructions, this project can satisfy all 8 mandatory requirements and support several bonus features using only standard Python.

## **1\. What exactly does MoneyPilot do?**

Imagine you're a student with ฿5,000 in your account. You receive some income, pay rent and living expenses, and want to buy something.

MoneyPilot helps answer four questions:

* Where did my money go? Track and categorize income and expenses.  
* How much money do I have? Calculate your current balance.  
* How long will my money last? Estimate cash runway using recurring monthly income and expenses.  
* Can I afford this? Simulate a purchase and check whether you would still have enough money reserved.

### **Example terminal interface**

moneypilot — main.py

CLI Application

MONEYPILOT v1.0

\================================ FINANCIAL DASHBOARD \================================ Current Balance: THB 3,500 Monthly Income: THB 9,000 Monthly Expenses: THB 10,000 Monthly Net Burn: THB 1,000 Cash Runway: 3.5 months \-------------------------------- 1\. Add Transaction 2\. View Transactions 3\. Edit / Delete Transaction 4\. Search & Filter 5\. Financial Summary 6\. Cash Runway Prediction 7\. Can I Afford It? 8\. Exit Enter choice: \_

The numbers above are illustrative. They come from a sample scenario we'll use below.

## **2\. How it satisfies all 8 mandatory requirements**

| Requirement | MoneyPilot implementation | Status |
| ----- | ----- | ----- |
| 1\. Interactive menu | 7 functional options plus Exit |  |
| 2\. Data structures | List of transaction dictionaries, plus settings dictionary |  |
| 3\. Conditional logic | Expense restrictions, reserve rules, valid transaction rules |  |
| 4\. Loops | `while` menu and `for` to process transactions |  |
| 5\. Functions | More than 4 functions, with parameters and return values |  |
| 6\. Algorithms | Balance calculation, runway prediction, spending analysis |  |
| 7\. Error handling | Invalid values, missing IDs, empty records, bad menu choices |  |
| 8\. Functional application | Add → analyze → simulate → update → analyze again |  |

The checkmarks mean the proposed design covers each criterion. Actual compliance depends on implementing and testing the features successfully.

## **3\. Data structures**

Each transaction is stored as a dictionary, and multiple transactions are managed using a list.

```
transactions = [    {        "id": 1,        "type": "income",        "category": "Salary",        "amount": 9000,        "recurring": True,        "description": "Monthly salary"    },    {        "id": 2,        "type": "expense",        "category": "Rent",        "amount": 6000,        "recurring": True,        "description": "Monthly rent"    },    {        "id": 3,        "type": "expense",        "category": "Food",        "amount": 4000,        "recurring": True,        "description": "Monthly food budget"    }]settings = {    "opening_balance": 5000,    "minimum_reserve": 2000,    "next_id": 4}
```

The `recurring` field means an income or expense has already been recorded once and is assumed to repeat each month in future forecasts. One-time expenses don't repeat.

This data structure is easy to understand during the defense and can later be saved to JSON.

## **4\. The three main algorithms**

These are what make MoneyPilot more interesting than a normal transaction tracker.

### **Algorithm 1 — Balance Calculation**

Calculate the current balance from all transactions.

\\\[ \\text{Balance}=\\text{Opening Balance}+\\sum\\text{Income}-\\sum\\text{Expenses} \\\]

Example:

| Transaction | Amount |
| ----- | ----- |
| Starting balance | ฿5,000 |
| Salary | \+฿9,000 |
| Rent | −฿6,000 |
| Food | −฿4,000 |
| Taxi | −฿500 |
| Current balance | ฿3,500 |

Python:

```
def calculate_balance(transactions, opening_balance):    balance = opening_balance    for transaction in transactions:        if transaction["type"] == "income":            balance += transaction["amount"]        else:            balance -= transaction["amount"]    return balance
```

This demonstrates `def`, function parameters, `for`, `if/else`, dictionaries, and `return`.

### **Algorithm 2 — Cash Runway Prediction**

This is the main feature of MoneyPilot.

Cash runway estimates how many months your current savings can support you if your recurring income and expenses continue unchanged.

$MonthlyBurn=RecurringExpenses-RecurringIncome$

If monthly burn is positive:

$Runway(months)=\frac{CurrentBalance}{MonthlyBurn}$

Using the sample data:

Try changing the numbers

Current balance

฿8,000

Monthly recurring income

฿8,000

Monthly recurring expenses

฿9,000

Net monthly cash flow

# **−฿1,000**

Estimated runway

# **8.0 mo**

You have at least 6 months of runway under these assumptions.

\*Simplified forecast assuming constant monthly income and expenses, with no interest or unexpected costs. The no-limit result is not a guarantee.

A useful validation rule is to handle a monthly burn of zero or less separately so your application never divides by zero.

### **Algorithm 3 — Can I Afford It?**

This is your standout interactive feature.

Instead of simply checking whether the user has enough money, MoneyPilot also checks whether the purchase would violate a minimum cash reserve.

$RemainingBalance=Balance-PurchasePrice$

Decision rule: A purchase is considered affordable under the selected reserve policy if the remaining balance is at least the minimum reserve.

Try it:

PURCHASE SIMULATOR · SAMPLE BALANCE ฿3,500

Purchase price

฿2,000

Minimum savings reserve

฿2,000

Not recommended under reserve rule

Balance after purchase

# **฿1,500**

Reserve shortfall

# **฿500**

Your remaining balance would be below your selected reserve.

This demonstration doesn't modify any saved transactions and isn't a full assessment of financial affordability.

In Python, you can implement this with a function accepting `balance`, `price`, and `reserve`, then returning a decision and the remaining balance.

## **5\. Three meaningful business rules**

Your assignment explicitly asks for at least three rules that change the outcome of a user action.

| Rule | Example | Expected outcome |
| ----- | ----- | ----- |
| Valid transaction amount | User enters −500 or 0 | Reject the transaction |
| Insufficient balance | User tries to spend ฿6,000 with only ฿3,500 | Reject the expense |
| Minimum savings reserve | User simulates a ฿2,000 purchase with ฿3,500 balance and ฿2,000 reserve | Warn that purchase violates reserve |

You can also enforce valid transaction categories, prevent duplicate IDs, and reject updates to nonexistent records.

A particularly important defense point: an invalid edit must leave the existing transaction unchanged.

## **6\. Bonus features — how to earn them**

These are the bonus opportunities explicitly supported by Chapter III of your assignment.

Bonus 1: JSON Save and Load

Save transactions and settings in `data.json`. Load them when the application starts, so financial records remain available after restarting Python.

Modules: `json`, `pathlib`.

Bonus 2: Advanced Search and Filtering

Search by category, income/expense type, amount range, or recurring status. Sort results by amount or transaction ID.

Example: Show the five largest food expenses.

Bonus 3: Financial Reports

Show expense totals per category, the largest spending category, and income versus expenses. Optionally export reports as CSV.

Modules: `csv` and standard Python dictionaries.

Bonus 4: Six-Month Financial Projection

Best extra feature

Predict future balances assuming the same recurring cash flow. Show how a simulated purchase changes the projected financial position.

Here's an example of that fourth bonus:

6-month projected balance

Illustrative forecast using starting balance of 3,500 THB, 9,000 THB monthly income, and 10,000 THB monthly expenses.

![Chart][image1]  
Illustrative chart, not required for the CLI. Negative projections indicate a funding shortfall, not permitted account overdrafts.

For the actual terminal application, you could display a simple month-by-month table rather than a graphical chart. You do not need third-party plotting libraries.

## **7\. Recommended code organization**

Keep the code modular but small enough for both students to understand.

```
rush/
├── main.py           # Menu and user interaction
├── transactions.py   # Add, view, edit, delete
├── finance.py        # Calculations and algorithms
├── storage.py        # JSON save/load (bonus)
├── README.md         # Description and run instructions
└── auteur            # Two 42 Intra logins
```

Here are the functions I'd plan:

| Function | Responsibility |
| ----- | ----- |
| `main()` | Run the menu using `while` |
| `add_transaction()` | Create a validated record |
| `view_transactions()` | Display records |
| `edit_transaction()` | Update existing records |
| `delete_transaction()` | Remove records |
| `find_transaction()` | Find a record by ID |
| `calculate_balance()` | Calculate available money |
| `calculate_runway()` | Estimate months of runway |
| `can_afford()` | Simulate a purchase |
| `spending_summary()` | Aggregate spending by category |
| `save_data()` | Save records to JSON |
| `load_data()` | Load saved records |

The first ten functions cover the mandatory design. Saving and loading support a bonus.

Use integers for whole-THB amounts to make arithmetic straightforward, or `Decimal` if you need satang precision.

## **8\. How to divide the project between two teammates**

Developer 1 — Core System

* Main menu  
* Transaction management  
* Input validation  
* Error handling  
* JSON persistence

Developer 2 — Financial Engine

* Balance calculation  
* Runway algorithm  
* Purchase simulator  
* Spending summaries  
* Financial projection

Both developers should jointly test the full application and review the complete code before the defense.

## **9\. Suggested defense demonstration**

You should prepare a complete workflow instead of presenting features individually.

1. Start MoneyPilot  
   Enter an opening balance of ฿5,000 and reserve of ฿2,000.  
2. Add income and expenses  
   Add salary ฿9,000, rent ฿6,000, food ฿4,000 as recurring transactions, plus taxi ฿500 as one-time spending.  
3. Show the financial summary  
   Balance should equal ฿3,500.  
4. Demonstrate the algorithm  
   Show monthly net burn ฿1,000 and estimated runway of 3.5 months.  
5. Simulate a purchase  
   Test ฿2,000 and show the reserve warning. Then test ฿600 and show the allowed result.  
6. Demonstrate error handling  
   Try a negative amount, nonexistent transaction ID, and invalid menu choice. The program must recover without crashing.  
7. Show a bonus  
   Save data to JSON, exit, restart the program, and show that the records were restored.

During testing, also check empty transaction lists, zero recurring expenses, a monthly surplus, and invalid data files. Those are important edge cases for this application.

## **10\. Which features should you actually build?**

For a Rush with two developers, I'd prioritize:

| Feature | Priority |
| ----- | ----- |
| Transaction CRUD | Mandatory |
| Menu and input validation | Mandatory |
| Balance and spending summary | Mandatory |
| Cash runway calculation | Main feature |
| Can I Afford It? | Main feature |
| JSON persistence | First bonus |
| Search/filter/sort | Second bonus |
| 6-month projection | Third bonus |
| Login system | Skip initially |
| Graphical UI | Skip initially |

My recommendation: Build MoneyPilot as a terminal-based financial simulator with three headline capabilities: tracking transactions, predicting cash runway, and evaluating purchases. Complete those and the eight mandatory categories first. Then add JSON persistence, category reports, and projections as bonuses.

The originality you can explain during your defense is that MoneyPilot goes beyond storing expenses: it processes financial records into forecasts and actionable purchase warnings. That makes it a more compelling project than a simple income-and-expense calculator, while remaining manageable using core Python.

[image1]: <data:image/png;base64,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>