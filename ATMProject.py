# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 10:42:13 2021

@author: aguboshimec

Improve on your ATM mockup from last course to include the following:

1. Use functions
2. Include register, and login
3. Generate Account Number
4. Any other improvement you can think of (extra point)

"""


from datetime import datetime
import random
AcccountBal = float (40)
MaximumDailyDep = float(500) #just to catch possiblity of large values
customer_name = input ('What is your name? \n')
posibleUsers = ['emmanuel', 'uju', 'obi', 'musa', 'timothy', 'trump', 'esther', 'olamide']
UserPassword = ['emma', 'uju', 'obi', 'musa', 'timothy', 'trump', 'esther', 'olamide' ]

def AccountNumber():
    return random.randrange(1111111111, 8888888888)
print (AccountNumber())   



if (customer_name in posibleUsers):
    password = input('Please enter your password \n')
    customerID = UserPassword.index(customer_name)
    
    if (password == UserPassword[customerID]):
        
        print ('Welcome, %s' % customer_name)
        print ('Date & Time is: %s' % datetime.now())
        print ('Please, select any of the options: ')
        print ('1. Cash Withdrawal')
        print ('2. Cash Deposit')
        print ('3. Make Complaint')
        
        selectedOption = int(input('Please select an option: '))
        
        if (selectedOption == 1):
            print ('Cash Withdrawal Selected')
            print ('Available Balance = N %d' % AcccountBal )
            WithdrawalAmount = float(input(('Please enter amount to withdrawal \n')))
            
            if WithdrawalAmount > AcccountBal:
                print ('insufficient funds, enter a lower amount')
            
            else:
                AcccountBal -= WithdrawalAmount
                print ('Please take your cash')
                print ('Your current balance is now: %f' % AcccountBal)
        
        elif (selectedOption == 2):
            print ('Cash Deposit Selected')
            print ('Available Balance = N %d' % AcccountBal )
            DepositAmount = float(input(('Please enter amount to deposit \n')))
           
            if DepositAmount > MaximumDailyDep:
                print ('exceeds daily allowable limit, enter a lower amount')
            else:
                AcccountBal += DepositAmount
                print ('Your current balance is now: %f' % AcccountBal)
                               
        elif (selectedOption == 3):
            print ('Make Complaint Selected')
            CustomerComplaint = input('Please enter your complaint \n')
            
            print ('Thank for contacting us. Your complaint has been recieved')
            
        else:
             print ('Invalid Option, please try again')
    else:
        print ('Password Incorrect, please try again')
else:
    print ('Customer Name not found, please try again')