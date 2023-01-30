import random
import secrets

names_file = open("sw_names_list.txt", "r")

names_data = names_file.read()

names_list = names_data.split("\n")


places_file = open("places_list.txt", "r")


places_data = places_file.read()

places_list = places_data.split("\n")


name = secrets.choice(names_list)

place = secrets.choice(places_list)

n = str(random.randint(100, 1000))

n2 = str(random.randint(100, 1000))

password = (name + n + place)

if len(password) > 13:
  print(password)
else:
  print(password + n2)


