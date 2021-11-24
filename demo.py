#python variable - does not require declaration
# first_name = 'Dj'
# print(first_name)

# #single & double quotes both work for strings
# last_name = "Tiwari"
# print(last_name)

# #python variables can change type
# age = "thirty one"
# age = 10
# print(age)

# # type function shows the type of a give value
# # print(type(first_name))
# # print(type(age))

# #if statement & if-else statement
# # if age >= 18:
# #   print('i can do whatever')
# # else:
# #   print('i need permission')
  
# # if-elif-else statement
# if age >= 18:
#   print('i am an adult, give me my beverage')
# elif age < 13:
#   print('i am a kid i can only dream')
# else:
#   print('still a little ways to go')

# # for-in-loop 
# for x in ['robert','caitlin','bry','quy','kelsey','stephen']:
#   print(x)

# #more examples of for-in-loop
# characters = ['Louise','takumi','Jiraiya','totoro','marge','Courage the cowardly dog']
# for cool_cats in characters:
#   print(cool_cats.capitalize())

#working with data-csv

open_file = open("FinalGrades.csv")
for row in open_file:
  print(row)

#takes pointer back to the starting position in the csv file
open_file.seek(0)

# for row in open_file:
#   print(row[0])

open_file.close()

# a more complicated look at what we can do with the data
open_grades = open("FinalGrades.csv")

total_a = 0
total_b = 0
total_c = 0

for line in open_grades:
  line = line.rstrip('\n').split(',')
  # print(line)
  for value in line:
    if value == "A":
      total_a += 1
    elif value == "B":
      total_b += 1
    elif value == "C":
      total_c += 1

print("A's:", total_a)
print("B's:", total_b)
print("C's:", total_c)

open_grades.close()





