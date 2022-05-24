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
    
def main():

  account = Account(1122, 20000, 4.5)

  account.withdraw(2500)

  account.deposit(3000)

  print("ID: " + str(account.get_id()))

  print("Balance: " + str(account.get_balance()))

  print("Monthly interest rate: " + str(account.getMonthlyInterestRate()))

  print("Monthly interest: " + str(account.getMonthlyInterest()))

main()