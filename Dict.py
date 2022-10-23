person = {
  "first": "Felix",
  "Last": "Vargas",
  "age": 23,
}

person["email"] = "Felixvjr0@gmail.com"

if "email" not in person:
  person["email"] = "notmyemail.gmail.com"
else:
  print("Would you like to replace your email?")
  
  
print(person["email"])

#this can check if the person has an email assigned to them and if not it will assign it themself


#####
# capitals = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}
# # another way to iterate through the keys
# for key in capitals.keys():
#      print(key)
# # output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
# #to iterate through the values
# for val in capitals.values():
#      print(val)
# # output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
# #to iterate through both keys and values
# for key, val in capitals.items():
#      print(key, " = ", val)
# # output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc

# List of dictionaries
users = [
    {"first": "Ada", "last": "Lovelace"}, # index 0
    {"first": "Alan", "last": "Turing"}, # index 1
    {"first": "Eric", "last": "Idle"} # index 2
]
# Dictionary of lists
resume_data = {
    #        	     0           1           2
    "skills": ["front-end", "back-end", "database"],
    #                0           1
    "languages": ["Python", "JavaScript"],
    #                0              1
    "hobbies":["rock climbing", "knitting"]
}

print(users[1]["first"]) # this is a way to print out the first name of the 1st index of the list type with Dict inside.

print(resume_data["skills"][1]) #this will grab the key and grab the 1st index in it
