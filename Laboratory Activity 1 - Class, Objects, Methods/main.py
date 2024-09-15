"""
    main.py
"""

import Accounts
import ATM
import random

Account1 = Accounts.Accounts(account_number = 123456, account_firstname = "Royce", account_lastname = "Chua", current_balance = 1000, address = "Silver Sreet Quezon City", email = "roycechua123@gmail.com")
print("Account 1")
print(Account1.account_firstname)
print(Account1.account_lastname)
print(Account1.current_balance)
print(Account1.address)
print(Account1.email)
print()

Account2 = Accounts.Accounts(account_number = 654321, account_firstname = "John", account_lastname = "Doe", current_balance = 2000, address = "Gold Street Quezon City", email = "johndoe@gmail.com")
print("Account 2")
print(Account2.account_firstname)
print(Account2.account_lastname)
print(Account2.current_balance)
print(Account2.address)
print(Account2.email)
print()



atm1_serialnum = random.randint(123456, 987654)
atm_1 = ATM.ATM(serial_number=atm1_serialnum, personal_account=Account1)

atm2_serialnum = random.randint(123456, 987654)
atm_2 = ATM.ATM(serial_number=atm2_serialnum, personal_account=Account2)


atm_1.deposit(500)
print(f"ATM 1 Serial No. {atm1_serialnum}")
atm_1.check_currentbalance()


atm_2.deposit(300)
print(f"ATM 2 Serial No. {atm2_serialnum}")
atm_2.check_currentbalance()


print("\nATM 1 Transaction History:")
atm_1.view_transactionsummary()
print("\nATM 2 Transaction History:")
atm_2.view_transactionsummary()
