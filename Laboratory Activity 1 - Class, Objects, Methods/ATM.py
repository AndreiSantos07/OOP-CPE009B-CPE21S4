"""
    ATM.py
"""


class ATM:
    
    def __init__(self, serial_number = 0, personal_account = None):
        self.serial_number = serial_number
        self.personal_account = personal_account
        self.transactions = []
    
    def deposit(self, amount):
        self.personal_account.current_balance += amount
        self.transactions.append(f"The amount that was deposited is {amount}")
        print("\nDeposit Complete")
        
    def withdraw(self, amount):
        if amount > self.personal_account.current_balance:
            print("Invalid transaction, not enouugh balance.")
        else:
            self.account.current_balance -= amount
            self.transactions.append(f"You withdraw {amount}")
            print("Withdrawal Complete.")
            
    def check_currentbalance(self):
        print(f"Your Current Balance: {self.personal_account.current_balance}")
    
    def view_transactionsummary(self):
        print("Transaction Summary:")
        for transaction in self.transactions:
            print(transaction)


