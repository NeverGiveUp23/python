


class Person:
  
  int_rate = 0.5
    
  def __init__(self, money, name, deposit, paycheck):
    self.money = money
    self.name = name
    self.deposit = deposit
    self.paycheck = paycheck
    
  def money_deposit(self):
    self.deposit = self.money + self.deposit
    print(f"Hello {self.name} here is your daily Balance: {self.deposit}")
    return self
    
  def paid(self):
    self.money += self.paycheck
    print(f"your paycheck is {self.paycheck}")
    tax = self.paycheck*Person.tax_rate
    self.paycheck += self.paycheck - tax
    print(f"We will take out {tax} for taxes! You have {self.money} in your account")
    return self
  
  @classmethod
  def change_tax_rate(cls, new_rate):
    cls.tax_rate = new_rate
  
felix = Person(2000, "Felix", 9000, 1000)
john_doe = Person(30, "John", 400, 500)
Person.change_tax_rate(0.1)
print(f"${felix.money} is what I have and my name is {felix.name} and I deposited {felix.deposit}")
felix.money_deposit().paid()
john_doe.money_deposit()


# work on this more and practice classes







  