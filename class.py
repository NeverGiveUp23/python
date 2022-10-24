# class User:
  def __init__(self):
    self.first_name = "Felix"
    self.last_name = 'Vargas'
    self.age = 29

print("Hello")
user_felix = User()
print(user_felix.first_name)

user_2 = User()
print(user_2.first_name)

# adjusting user classes

class Shoe:
  def __init__(self, brand, shoe_type, price):
    self.brand = brand
    self.type = shoe_type
    self.price = price
    self.in_stock = True
skater_shoe = Shoe("Nike", "Air-Force", 79.99)
print(skater_shoe.brand)

#above will make a class with the description of the items in the init method, and than assigning it to each other and after creating a shoe.

class User:
  def __init__(self, name, email):
    self.name = name
    self.email = email
  def greeting(self):
    print(f"Hello, my name is {self.name}")
    
felix = User("Felix", "felixvjr0@gmail.com")
felix.greeting()

# this will get us to print out the user's name, assign the parameters the its on self.name and create a function that will put it all together for the user.
#create a new variable to assign it the User class with the parameters describing the user.

class User2:
  def __init__(self, first_name, last_name, email, age):
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.age = age
    self.is_rewards_member = False
    self.gold_card_points = 0
  def display(self):
    print(f"{self.first_name} \n{self.last_name} \n{self.email} \n{self.age} \n{self.is_rewards_member} \n{self.gold_card_points}")
    return self
  def enroll(self):
    user_info.is_rewards_member = True
    user_info.gold_card_points = 200
    return self
user_info = User2("Felix", "Vargas Jr", "felixvjr0@gmail.com", 29)
user_info.enroll().display()

# above is a way to adjust classes and th user by being a member and listing out their info

