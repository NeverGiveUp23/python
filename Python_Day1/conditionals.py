x = 12
if x > 50:
    print("bigger than 50")
else:
    print("smaller than 50")
    # because x is not greater than 50, the second print statement is the only one that will execute
    
x = 55
if x > 10:
  print("bigger than 10")
elif x > 50:
  print("bigger than 50")
else:
  print("smaller than 10")
    # even though x is greater than 10 and 50, the first true statement is the only one that will execute, so we will only see 'bigger than 10'
    
if x < 10:
  print("smaller than 10")
    # nothing happens, because the statement is false   


for i in range(2, 21, 2):
  print(i)
  
the_list = ['felix', 'vargas', 'jr']
# for x in the_list:
#   print(x)
  
for i in range(0, len(the_list)):
    print(i, the_list[i])
    
count = 0
while count <= 5:
    print("looping - ", count) #this will grab your string and add count each time the string is called to loop through
    count += 1

y = 3
while y > 0:
    print(y)
    y = y - 1
    # break
else:
    print("Final else statement")

y = 3
while y > 0:
    print(y)
    y = y - 1
    if y == 0:
        break
else:		# only executes on a clean exit from the while loop (i.e. not a break)
  print("Final else statement")
# output: 3, 2, 1

