
class BankAccount:
    def __init__(self,bal):
        self.balance = int(bal)

    def withdraw(self, amount):
        print amount
        self.balance =self.balance - int(amount)
        return self.balance

    def deposit(self, amount):
        self.balance += int(amount)
        return self.balance
    def getb(self):
        print 'current balance'
    	return self.balance

if __name__ == '__main__':    
	print 'enter the balance'
	p = raw_input()
	myObj = BankAccount(p)
	
        print myObj.getb()

        import os
 	os.system('clear')
	print 'enter the withdraw amopunt'
	q = raw_input()
	myObj.withdraw(q)
	print myObj.getb()

	import os
        os.system('clear')
        print 'any deposits:'
        z = raw_input()
        myObj.deposit(z)
        print myObj.getb()

