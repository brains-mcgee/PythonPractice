# -*- coding: utf-8 -*-
"""
Homework: Testing and Debugging
knf7vg
"""

#The Account/Checking Class and Subclass

#creating superclass Account
class Account:
    def __init__(self, accountNumber, balance): #initializer
        self.accountNumber = accountNumber
        self.balance = balance
    def __str__(self): #to-string method, prints acct number and balance
        acctnobal = "Account Number: " + str(self.accountNumber) + "\nBalance: $"+ str(self.balance)
        return acctnobal

#creating subclass
class Checking(Account):
    def __init__(self, accountNumber, balance, fee): #initializer
        Account.__init__(self, accountNumber, balance) #inheriting from superclass
        self.fee = fee #specific to checking(account)
    def __str__(self): #to-string method, prints acct type, acct number and balance
        newnobal = "Account type: Checking \nAccount Number: " + str(self.accountNumber) + "\nBalance: $" + str(self.balance)
        return newnobal
    def getfee(self): #new method, returns fee
        return str(self.fee)
    def deposit(self, amount): #new method, adds deposit amount to balance
        self.balance = self.balance + amount
    def withdraw(self, amount): #checks withdrawal amount + fee against balance first
        self.total = amount + self.fee #then subtracts withdrawal + fee from balance
        if self.total > self.balance:
            print("Insufficient Funds!")
        else:
            self.balance = self.balance - self.total

''''
Unit Testing
'''
import unittest
import sys
sys.stdout = open('HW3RESULTS.txt', 'w')

#Testing Account 
class AcctTest(unittest.TestCase):
    def test_AcctInit(self):
        
        acct1 = Account("1234", 2000)
        self.assertEqual(acct1.accountNumber, "1234")

if __name__ == '__main__':
    unittest.main()
    
class AcctTest2(unittest.TestCase):
    def test_AcctInit2(self): #initializing test case
        
        acct2 = Account("010101", 789) #creating testcase
        self.assertIsInstance(acct2, Account) #Is acct2 a member of Account class?

if __name__ == '__main__':
    unittest.main()

#Testing Checking Acct Initialize Statement
class CheckingTest(unittest.TestCase):
    def test_Init(self): #initializing testcase
        newacct = Checking('02461', 780, 2) #creating test acct
        self.assertEqual(newacct.balance, 780) 
        #does test acct have a balance of 780?
        
if __name__ == '__main__':
    unittest.main()         
    
class CheckingTest2(unittest.TestCase):
    def test_Init2(self): #initializing testcase
        newacct2 = Checking('18034',40, .5) #creating testcase
        self.assertEqual(newacct2.fee, .5) #does this test acct have fee of .5?

if __name__ == '__main__':
    unittest.main()   
      
#Testing Checking Acct deposit method
class DepositTest(unittest.TestCase):
    def test_Deposit(self): ##initializing testcase
        newacct2 = Checking('18034', 40, .5) #same newacct2 as above
        newacct2.deposit(10) #deposit $10
        self.assertEqual(newacct2.balance, 50) #is the new balance 50?

if __name__ == '__main__':
    unittest.main()
    
class DepositTest2(unittest.TestCase): #testing w/negative balances!
    def test_Deposit2(self): #initializing testcase
        anotheracct = Checking('1234', -10, .5) #new account w/negative balance
        anotheracct.deposit(9) #deposits $9
        self.assertEqual(anotheracct.balance, -1) #is the new balance -1?

if __name__ == '__main__':
    unittest.main()

#Testing Checking Acct withdraw method

class WithdrawTest(unittest.TestCase):
    def test_Withdraw(self): #initializing testcase
        notheracct = Checking ('89271', 50, 1) #another new acct
        notheracct.withdraw(50) #since balance < withdraw + fee, shouldn't work!
        self.assertNotEqual(notheracct.balance, 0) #is balance NOT zero?


if __name__ == '__main__':
    unittest.main()

class WithdrawTest2(unittest.TestCase):
    def test_Withdraw2(self): #initializing testcase
        finalacct = Checking('1234', 9999, .75) #new account
        finalacct.withdraw(1.25) #testing w/non-whole dollar amt
        self.assertEqual(finalacct.balance, 9997) #is the new balance 9997?

if __name__ == '__main__':
    unittest.main()
