print ('Day 2: 30 Days of Python programming')

first_name = 'Cory'
last_name = 'Dennis'
country = 'Kenya'
city = 'Ongata Rongai'
age = 27
year = 1995
is_married = False
is_true = 'introvert'
is_lights_on = True

personal_details = {
'firstname' : 'Dennis',
'lastname' : 'Kori',
'nationality' : 'Kenyan',
'City' : 'Nairobi'
}

print (type(first_name))
print (type(last_name))
print (type(country))
print (type(city))
print (type(age))
print (type(is_married))
print (type(is_true))
print (type(is_lights_on))

#print the length of the firstname
print('the length of your firstname is', len(first_name))

#Declare lengths of the names as variables
first_name_length = len(first_name)
last_name_length = len(last_name)

#Convert the length to integers (in anticipation of -ve numbers)
int(first_name_length)
int(last_name_length)

#Store the result of the comparison in a variable 
math = first_name_length-last_name_length

#print the comparison output
print ('First name is longer by', math, 'characters')

import math
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
division = num_one/num_two
remainder = num_two%num_one
exp = math.pow(num_one,num_two)
print('the power function:', exp)
floor_division = num_one//num_two
pi = 3.14
radius = float(input('Enter radius of the circle:'))
area_of_circle = pi * math.pow(radius,2)
circum_of_circle = 2 * pi * radius

print ('the area is', area_of_circle, 'and the circumference is', circum_of_circle)

first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
country = input('Which country are you a citizen of? ')
city = input('Which is your city of residence? ')
age = input ('Let us know your age ')
year = input ('What year were you born? ')
is_married = input ('What is your marital status? ')
is_true = input ('Tell us one truth about you ')
is_lights_on = input('Did you leave your lights on ')

print('Your details are as follows', 'Name: ', first_name, last_name, 'Country: ', country, 'City of residence: ', city, 'Age', age, 'Year of Birth', year,
'Marital status', is_married, 'A truth about yourself: ', is_true, 'Lights: ', is_lights_on  )
