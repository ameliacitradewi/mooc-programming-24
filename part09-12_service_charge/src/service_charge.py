# WRITE YOUR SOLUTION HERE:
class BankAccount:
    def __init__(self, owner: str, account_number: int, balance: float):
        self.__owner = owner
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount: float):
        self.__balance += amount
        self.__service_charge()
    
    def withdraw(self, amount: float):
        self.__balance -= amount
        self.__service_charge()
    
    def __service_charge(self):
        admin = 0.01 * self.__balance
        self.__balance -= admin

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance: float):
        return self.__balance

# Example Usage
account = BankAccount("Randy Riches", "12345-6789", 1000)
account.withdraw(100)
print(account.balance)
account.deposit(100)
print(account.balance)  
