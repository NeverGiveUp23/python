
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




# practice 

class Pet:

    # implement __init__( name , type , tricks ):
    def __init__(self, name , type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 50
        self.noise = noise

    # implement the following methods:
    # sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        return self

    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    # play() - increases the pet's health by 5
    def play(self):
        self.health += 5
        self.energy -= 15
        return self

    # noise() - prints out the pet's sound
    def noise(self):
        print(self.noise)



class Ninja:
    # implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, first_name, last_name , treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    # implement the following methods:
    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()
        return self

    # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):

        if len(self.pet_food) > 0:
            food = self.pet_food.pop()
            print(f"Feeding {self.pet.name} {food}!")
            self.pet.eat()
        else:
            print("Oh no!!! you need more pet food!")
        return self

    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        self.pet.noise()

my_treats = ['Snausage','Bacon',"Trash Bag"]
my_pet_food = ['Pizza','Burger']

nibbles = Pet("Mr. Nibbles","Horse",['nibbles on things','is invisible'],"Hey Hey")

adrien = Ninja("Adrien","Dion",my_treats,my_pet_food, nibbles)

adrien.feed();
adrien.feed();
adrien.feed();