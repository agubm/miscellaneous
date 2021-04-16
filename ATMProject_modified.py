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
from validate_email import validate_email # to validate our email formats, email should be of the format abc@xyz.com
import random

MaximumDailyDep = float(500) #just to catch possiblity of large values
AcccountBal = float (40) #assume balance is on a promo, with all customers having min. account of N40

def AccountNumber():
    return random.randrange(1111111111, 8888888888) #generate a 10digit account number

CustomerDataBase = {} #database
emptyDataBase = not CustomerDataBase
    
def Customerlogin(): #login with account number and password
    print ('*****Customer Login *****')
    print ('Please Login')
    
    LoginSuccessful = False
    
    while  LoginSuccessful == False:
        
        isTenDigitPassword = False    
        while not isTenDigitPassword:
            InputCustomerAccountNumber = input('Please enter your Account Number: \n')

            if len(InputCustomerAccountNumber) == 10 and InputCustomerAccountNumber.isdigit() and InputCustomerAccountNumber != ' ' :
                isTenDigitPassword = True
            else:
                print('Your Account Number must filled and only digits')
        
        print('Your Account Number entered is: ' + InputCustomerAccountNumber)
       
        password  = input('Please enter your password: \n ')
        
        for CustomerAccountNumber, CustomerDetails in CustomerDataBase.items():
            if (CustomerAccountNumber == InputCustomerAccountNumber):
                if (CustomerDetails[3] == password):
                    LoginSuccessful = True
                           
            print ('Invalid Account Number or Password')  
        BankingServices()

def CustomerRegister():
    global CustomerFirstName, CustomerLastName, CustomerEmail, UserPassword, AcccountBal, CustomerAccountNumber
    CustomerAccountNumber = AccountNumber() 
    print ('*****Customer Registration *****')
    IsValid = False
    CustomerEmail = input('enter your email address \n')
    while IsValid == False:
        ValidEmail = validate_email(CustomerEmail)
        if ValidEmail == True:
            IsValid = True
            print ('email is valid')
        else:
            print ('email not valid, enter valid email with format: abc@xyz.com')
            CustomerRegister()
        
    CustomerFirstName = input ('enter your first name \n')
    CustomerLastName = input ('enter your last name \n')
    
    CustomerPassword = (input ('choose login password \n').lower()) # eliminates possibility of error
    CustomerPassword_confirm = (input ('re-enter login password \n').lower())
    
    
    IsPWDValid = False #initiate password as not valid
    while IsPWDValid == False:
        if CustomerPassword == CustomerPassword_confirm:
            print ('password same')
            UserPassword = CustomerPassword_confirm
            IsPWDValid = True
        else:
            print ('password not same')
            CustomerRegister() #registration form clears, and registration begin over again
    
        CustomerAccountNumber = AccountNumber()  
        print('Your Account Number is: %s' % CustomerAccountNumber)
    
    CustomerDataBase[CustomerAccountNumber] = [CustomerFirstName, CustomerLastName, CustomerEmail, UserPassword, AcccountBal]
    #return CustomerDataBase
    
    print ('Registration Successful! Account Has Been Created')
    
    Customerlogin()  

def withdrawalOperation():
    global AcccountBal
    print ('Cash Withdrawal Selected')
    print ('Available Balance = N %d' % AcccountBal )
     #we try to catch the error of empty input and numeric input only
    isInput= False
    while not isInput:
        WithdrawalAmount = (input(('Please enter amount to withdrawal \n')))

        if  len(WithdrawalAmount) >=1 and WithdrawalAmount.isdigit():
            WithdrawalAmount = int(WithdrawalAmount)
            isInput = True
        else:
            print('Ammount must be enter and whole number')
    
    print('Chosen Amount to Withdrawal is: %d' % WithdrawalAmount)
        
    if AcccountBal < WithdrawalAmount:
        print ('insufficient funds, enter a lower amount')
        withdrawalOperation()
    else:
        AcccountBal = AcccountBal - WithdrawalAmount
        print ('Please take your cash')
        print ('Your current balance is now: '"{:.2f}".format(AcccountBal))
        BankingServices()
        
def depositOperation(): 
    global AcccountBal
    print ('Cash Deposit Selected')
    print ('Available Balance = N %d' % AcccountBal )
    #we try to catch the error of empty input and numeric input only
    isInput= False
    while not isInput:
        DepositAmount = (input(('Please enter amount to deposit \n')))

        if  len(DepositAmount) >=1 and DepositAmount.isdigit():
            DepositAmount = int(DepositAmount)
            isInput = True
        else:
            print('Ammount must be enter and whole number')
    
    print('Chosen Amount to deposit is: %d' % DepositAmount)
  
    if DepositAmount > MaximumDailyDep:
        print ('exceeds daily allowable limit, enter a lower amount')
        depositOperation()
    else:
        AcccountBal = AcccountBal + DepositAmount
        print ('Your current balance is now: ' "{:.2f}".format(AcccountBal)) # converts to 2 decimal palces
        BankingServices()
                           
def makeComplaint():   
    print ('Make Complaint Selected')
    CustomerComplaint = input('Please enter your complaint \n')
    
    print ('Thank for contacting us. Your complaint has been recieved')
    BankingServices()
    

def BankingServices():
    OptionSelectedBankingOps = False
    while OptionSelectedBankingOps == False:
        
        print ('Welcome %s %s ' % (CustomerFirstName, CustomerLastName ))
        print ('Date & Time is: %s' % datetime.now())
        print ('Please, select any of the options: ')
        print ('1. Cash Deposit')
        print ('2. Cash Withdrawal')
        print ('3. Make Complaint')
        print ('4. Logout')
        
        selectedOption = int(input('Please select an option: \n'))
     
        if (selectedOption == 1):
            OptionSelectedBankingOps = True
            depositOperation()           
        elif (selectedOption == 2):
            OptionSelectedBankingOps = True
            withdrawalOperation()        
        elif (selectedOption == 3):
            OptionSelectedBankingOps = True
            makeComplaint()        
        elif (selectedOption == 4):
            OptionSelectedBankingOps = True           
            init()
        else:
            print('Invalid Option Selected')
            BankingServices()
                    
def init():
    selectedOption = False
    print('Welcome to EAGUB Microfinance Bank')
    while selectedOption == False: #with this loop, the system becomes iterative until a valid option is selected
        
        QueryAccountinfo = int(input('Do you have an account with ZuriT: \n Press: 1- Yes or 2- No:  '))
        if QueryAccountinfo == 1 and emptyDataBase == False:
            selectedOption = True
            Customerlogin()
        elif QueryAccountinfo == 1 and emptyDataBase == True:
            print ('You don''t have an account yet, please register')
            selectedOption = True
            init()
        elif QueryAccountinfo == 2:
            selectedOption = True                       
            CustomerRegister()
        else:
            print ('Try Again! Wrong option selected or Please register if new user')
init()



