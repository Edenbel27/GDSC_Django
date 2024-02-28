import unittest

class Car:
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def information(self):
        return f'make= {self.make} "\n" model = {self.model} "\n" year = {self.year}'


class Electric_Car (Car):
    
    def __init__(self,battery_capacity):
        self.battery_capacity=battery_capacity
   
    def information1(self):
        return f'battery_capacity = {self.battery_capacity}'


class BankAccount:
    
    def __init__(self, name, account_number):
        self.name=name
        self.account_number= account_number
        self.balance=0
    
    def withdraw(self, amount):
        
        if amount<=self.balance and (type(amount)==int or type(amount)==float):
            self.balance-= amount
            return (f'Currently your balance is : {self.balance}')
        else:
            return (f'Insufficient balance.')


    def deposit(self,amount):
        if type(amount)==int or type(amount)==float:
            self.balance+= amount
            return (f'Currently your balance is : {self.balance}')
        else:
            return (f'Invalid input!!!')


class shape:
    def __init__(self):
        pass
    def calc_area(self):
        pass


class circle(shape):
    def __init__(self, radius):
        self.radius=radius
    
    def calc_area(self):
        if type(self.radius)==int or  type(self.radius)==float:
            area= 3.14*(self.radius**2)
            return(f"The area of the circle is  : {area}")

        else:
            return (f"The radius entered is invalid.")


class rectangle(shape):
    def __init__(self,length, width):
        self.length=length
        self.width=width
    def calc_area(self):
        parameters=[self.length,self.width]
        for parameter in parameters:
            if type(parameter)==int or type(parameter)==float:
                condition==True
            else:
                condition==False
                break
        if condition==True:
            area=self.length*self.width
            return(f'area of the rectangle: {area}')
        else:
            return(f"Invalid input!!!")


class Triangle(shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def calc_area(self):
        parameters=[self.base,self.height]
        for parameter in parameters:
            if type(parameter)==int or type(parameter)==float:
                condition==True
            else:
                condition==False
                break
        if condition==True:
            area=(1/2)*self.base*self.height
            return(f'area of the rectangle: {area}')
        else:
            return(f"Invalid input!!!")


class TestBankAccount(unittest.TestCase):

        def setUp(self):
             self.bank_account = BankAccount("Eden_Belayneh", "2728")
        
        def test_deposit(self):
            self.bank_account.deposit(100)
            self.assertEqual(self.bank_account.balance, 100)

            """ checks if the deposit method correctly increases the balance of the BankAccount object by 
        the specified amount"""

        def test_withdrawal_sufficient_funds(self):
            self.bank_account.deposit(100)
            self.bank_account.withdraw(50)
            self.assertEqual(self.bank_account.balance, 50)

            """checks if the withdraw method correctly decreases the balance of the BankAccount object by
            the specified amount when there are sufficient funds."""
            
        def test_withdrawal_insufficient_funds(self):
            self.bank_account.deposit(100)
            withdrawal_result = self.bank_account.withdraw(150)
            self.assertEqual(withdrawal_result, "Insufficient balance.")
            self.assertEqual(self.bank_account.balance, 100)

            """checks if the withdraw method returns 'Insufficient funds' and does not change the balance
            when there are insufficient funds for the withdrawal."""

        def test_initial_balance(self):
            self.assertEqual(self.bank_account.balance, 0)

            """checks if the initial balance of a new BankAccount object is correctly set to 0."""

if __name__ == "__main__":
    unittest.main()