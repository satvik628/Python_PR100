# Python Atm App PR100

# Defining class as ATM
class Atm(object):

    # Defining a function as __init__ form
    def __init__(self,name,balance,withdrawl,atmcardNo,pinNo,bank):
        self.name=name
        self.balance=balance
        self.withdrawl=withdrawl
      #  self.deposit=deposit
        self.atmcardNo=atmcardNo
        self.pinNo=pinNo
        self.bank=bank
    
    # Creating function for getting current account balance
    def getBalance(self):
        return self.balance
   
   # Setting balance function
    def setBalance(self):
        inp=input("Enter Amount to set of "+self.name+": ")
        self.balance=inp

        print('Amout Changed Succesfully')
        print(self.name+"'s balance is : "+self.balance)
    
    # Creating getPyInfo function to get details of user
    def getPyInfo(self):
        print('Informations :--')
        print('        Name : '+self.name)
        print('        Money-Balance : '+self.balance)
        print('        Withdrawl : '+self.withdrawl)
        print('        ATM card  NO. : '+self.atmcardNo)
        print('        Pin No. : '+self.pinNo)
        print('        BANK : '+self.bank)


account1=Atm('Account 1','20,000','0','1234567890','1234','Bank of money') # Creating a account 1 variable to store account 1 details .
account2=Atm('Account 2','10,000','200','12345678900','12345','ABCD Bank') # Creating account 2  variable

# Printing Money Balance
print('BALANCE : '+account1.getBalance())
print('BALANCE : '+account2.getBalance())

# Asking for information by getPyInfo()
account1.getPyInfo()
account2.getPyInfo()

# setBalance
account1.setBalance(account1)



# By Satvik