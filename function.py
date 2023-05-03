# Function to add two numbers 

def add_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum
print('The sum of the two numbers is: ', add_two_numbers(21, 32))

# Function to calculate the area of a circle
def circle_area (radius):
    PI = 3.142
    area = PI * radius ** 2
    return area
print('The area of the circle is: ', circle_area(7))


#Function that takes an arbitrary number of arguments and sums them
def sum_of_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total
print('The sum of the numbers is: ', sum_of_nums(2,5,6))

#Function to convert Degrees in Celsius to Farenheit

def convert_celsius_to_farenheit(degrees_in_celsius):
    degrees_in_farenheit = (degrees_in_celsius * (9/5))+32
    return degrees_in_farenheit
print('Degrees is Farenheit is: ', convert_celsius_to_farenheit(35))

#Function to check season based on month

def check_season(month):
    month = month.capitalize()
    season = ''
    if month == 'December' or month == 'January' or month == 'February':
        season = 'Winter'
    elif month == 'March' or month == 'April' or month == 'May':
        season = 'Spring'
    elif month == 'June' or month == 'July' or month == 'August':
        season = 'Summer'
    elif month == 'September' or month == 'October' or month == 'November':
        season = 'Autumn'
    else:
        return 'Invalid Input.'
    return season
month = input('Enter month you want to check season for: ')
print('The season is: ', check_season(month))

'''
#Function to find the slope of a line Change in Y / Change in X
def slope_of_line():
    slope = 0
    first_x_coordinate 
    second_x_coordinate
    first_y_coordinate
    second_y_coordinate
    slope = int(((second_x_coordinate-first_x_coordinate)/(second_y_coordinate-first_y_coordinate)))
    return slope
first_x_coordinate = int(input('Enter first X Coordinate: ')) #Converting input to int type for all the fields.
second_x_coordinate = int(input('Enter the second X Coordinate: '))
first_y_coordinate = int(input('Enter the first Y Coordinate: '))
second_y_coordinate = int(input('Enter the second Y Coordinate: '))
print('The slope of the line is: ', slope_of_line())


#Function to calculate a quadratic equation ax² + bx + c = 0
def solve_quadratic_eqn(a,b,c):
    solution = 0
    solution = (a*x**2) + b*x + c
    return solution
print('The value of X is: ', solve_quadratic_eqn(1, 5, 6))


#Function that takes a list as a parameter and prints out each element
def print_list(name):
    name = str(name)
    splitted_list = name.split()
    first_location = splitted_list[0]

    return splitted_list
print('The characters in the name are: ', print_list('Asabeneh'))

'''

#Function to capitalize items in a list

def capitalize_list_items():
    items = ['javascript', 'python', 'java', 'solidity']
    if len(items)