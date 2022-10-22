# greeting = "Hello world!"
# print(greeting)
# favorite_fruits = ["banana", "kiwi", "lychee", "blueberry"]
# num = 77
# parting = "Goodbye!"
# favorite_fruits[0] = 'Felix'
# # append is to add to the end of your line of code #
# favorite_fruits.append('is the best') 
# print(favorite_fruits)
# # you can concat strings with the + sign and turn numbers into a string with the str() method #
# print('Hello ' + str(55))
# # you can use th f"" to concat strings without addin the + sign , this will make it easier#
# print(f' mmy name is {favorite_fruits[0]} and i love basketball')
# #  you can use format() at the end of your statement to concat strings together #
# print('My name is {} and im {} years old.'.format(favorite_fruits[0], num))
# # turn your string to cap the first word in every word #
# x = 'my name is felix'
# print(x.title())

num1 = 42 #assigning num1(variable decleration) to a number
num2 = 2.3 #assigning num2(variable decleration) to a number with decimal
boolean = True #assigning a boolean value True to a variable
string = 'Hello World' # creating a string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #creating a data set with pizza toppings 
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # creating a Dictionary to a person variable
fruit = ('blueberry', 'strawberry', 'banana') #creating a variable fruit with items 
print(type(fruit)) # asking what type of information is fruit
print(pizza_toppings[1]) # calling the [1]index of pizza_toppings data set. (in other words the 2nd data placed in pizza_toppings)
pizza_toppings.append('Mushrooms') #adding mushrooms to the end of pizza_toppings
print(person['name']) #just calling the name in person to print to the console
person['name'] = 'George' #changing the name in person to george
person['eye_color'] = 'blue' #adding eye_color key with blue as its value in person dict. If it isnt in the dict/ it will add it 
print(fruit[2]) #just wants to print banana to the console

"""
below it will print 'its lower' because it is not greater
"""
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3): #will start count at 2 and increment by 3 until it equals 10
    print(x)
x = 0
while(x < 5):
    print(x)
    x += 1

pizza_toppings.pop()
pizza_toppings.pop(1)

print(person)
person.pop('eye_color')
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)