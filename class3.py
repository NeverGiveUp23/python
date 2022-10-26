class Store:
  def __init__(self, name):
    self.name = name
    self.list_of_products = []
    
    
  def add_product(self, new_product):
    self.list_of_products.append(new_product)
    return self
  
  def sell_product(self, id):
    self.list_of_products.pop(id)
    # print(f"{self.list_of_products}")
    return self
    
class Product:
  def __init__(self, name, price, category):
    self.name = name
    self.price = price
    self.category = category
    
  def update_price(self, percent_change, is_increased):
    self.percent_change = percent_change
    self.is_increased = False
    
    if is_increased == True:
      self.price = self.price + (self.price * percent_change)
      print(f"Your price is now {self.price}")
      return self
    else: 
      is_increased = False
      print(f"Your price is {self.price}")
    return self
      
  def print_info(self):
    print(f"{self.name}, {self.price}, {self.category}")
    return self
  
 
adidas = Store('Adidas')
adidas_products = Product("Classics", 49.99, "Low-Top")
adidas.add_product("Yeezy").add_product("Boosts").add_product("Stan-smiths").add_product("Classics").add_product("Harden Vol.2")
print(adidas.list_of_products)
adidas.sell_product(3)
adidas_products.print_info()