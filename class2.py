class Person:
  def __init__(self, money, name, deposit, paycheck):
    self.money = money
    self.name = name
    self.deposit = deposit
    self.paycheck = paycheck
    
  def money_deposit(self):
    self.deposit = self.money + self.deposit
    print(f"Hello {self.name} here is your daily Balance: {self.deposit}")
    
  def paid(self):
    self.money += self.paycheck
    print(f"your paycheck is {self.paycheck}")
  
felix = Person(1000, "Felix", 9000, 400)
john_doe = Person(30, "John", 400, 500)

print(f"${felix.money} is what I have and my name is {felix.name} and I deposited {felix.deposit}")
felix.money_deposit()
john_doe.money_deposit()
felix.paid()