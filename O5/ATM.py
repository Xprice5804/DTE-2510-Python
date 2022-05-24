#from Account import Account

class Account:
    def __init__(self, id = 0, balance = 100, anualIntrestRate = 0):
        self.__id = id
        self.__balance = float(balance)
        self.__anualIntrestRate = float(anualIntrestRate)
        
    #Acsessor methods
    def getId(self):
        return self.__id
    
    def getBalance(self):
        return self.__balance
    
    def getAnualIntrestRate(self):
        return self.__anualIntrestRate
    
    def getMonthlyIntrestRate(self):
        anualIntrest = self.getAnualIntrestRate()
        monthlyIntrest = anualIntrest/12
        return monthlyIntrest
    
    def getMonthlyIntrest(self):
        MonthlyRate = self.getMonthlyIntrestRate()
        MonthlyIntrest = (MonthlyRate * self.getBalance())/100
        return MonthlyIntrest
    
    #mutator methods
    def setId(self, id):
        self.__id = id
        
    def setBalance(self, balance):
        self.__balance = float(balance)
        
    def setAnualIntrestRate(self, intrestrate):
        self.__anualIntrestRate = float(intrestrate)
        
    #Other methods
    def withdraw(self, amount):
        newBalance = self.getBalance() - amount
        self.setBalance(newBalance)
        return
    
    def deposit(self, amount):
        newBalance = self.getBalance() + amount
        self.setBalance(newBalance)
        return
    

class ATM:
    def __init__(self, listOfAccounts):
        self.listofAccounts = listOfAccounts
        self.getAnAccount()

    def getAnAccount(self):
        self.__Id = int(input("Please type inn an account number"))
        
        while True:
            choice = self.getAChoice()
            if choice == 1:
                Balance = self.listofAccounts[self.__Id].getBalance()
                print("Your Balance is " + str(Balance))
                

            elif choice == 2:
                amount = int(input("Pleace enter the amount that you wish to withdraw"))
                if amount > self.listofAccounts[self.__Id].getBalance():
                    print("You cannot withdraw more than what you have")
                    
                elif amount < 0:
                    print("You cannot withraw a negative number, pleace deposit")
                    
                else:
                    self.listofAccounts[self.__Id].withdraw(amount)
                    print("you sucsessfully witdrew " + str(amount))
                    
            elif choice == 3:
                amount = int(input("Please enter the amount to deposit"))
                if amount > 0:
                    self.listofAccounts[self.__Id].deposit(amount)
                    print("you sucsefully deposited "+ str(amount))
                else:
                    print("you cannot deposit a negative number, please use withdraw")
                    
            elif choice == 4:
                self.getAnAccount()
                break

        
    
    def getAChoice(self):
        while True:
            print("\nMain menu")
            print("1: check balance")
            print("2: withdraw")
            print("3: deposit")
            print("4: exit")
            print("Enter a choice: ", end = "")
            choice = int(input())
            if choice < 1 or choice > 4:
                print("Wrong choice, try again: ", end = "")
            else:
                break

        return choice
    
def main():
    listofAccounts = []
    x = 0
    while x < 10:
        listofAccounts.append(Account(x, 100, 1))
        x = x+1
    ATM(listofAccounts)

main()
