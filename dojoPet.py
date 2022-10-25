
class Pet:
  def __init__(self, name, type, tricks, sound, health=70, energy=50):
    self.name = name
    self.type = type
    self.tricks = tricks
    self.health = health
    self.energy = energy
    self.sound = sound
  
  def sleep(self):
    return (self.energy + 25)
  
  def eat(self):
    self.energy = self.energy + 5
    self.health = self.health + 10
    return self
  
  def play(self):
    self.health = self.health + 5
    return self
  
  def noise(self):
      print(f"{self.sound}")
      

class Ninja(Pet):
    def __init__(self, first_name, last_name, pet, treats, pet_food):
      self.first_name = first_name
      self.last_name = last_name
      self.pet = pet
      self.treats = treats
      self.pet_food = pet_food
      
    def walk(self):
      self.pet.play()
      return self
    
    def feed(self):
      
      if len(self.pet_food) > 0:
        food = self.pet_food.pop()
        print(f"Feeding {self.pet.name} {food}")
        self.pet.eat()
      else:
        print("Oh No!!! you need more pet food")
      return self
    
    def bathe(self,pet):
      print("Shower Time")
      super().sound(pet)
      return self
    
    def ninja_info(self):
      print(f"{self.first_name} {self.last_name} {self.pet} {self.treats} {self.pet_food}")
      
      
pet_noise = Pet(f"Rufus", "German", "Flip", "woof woof", health=70, energy=50)
the_ninja = Ninja("Felix", "Vargas", "Dog", "Bone", "Nibble")
pet_noise.eat()



