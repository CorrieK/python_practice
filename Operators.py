print (len ('Cory') > len('Dennis'))
print (len('Cory')== len('Kori'))

age = input('enter age: ')
height = float(input('enter your height in centimeters: '))
weight = float(input('enter weight in KGs: '))
converted_height = height/100
float(converted_height)
bmi = weight/converted_height**2
print('Your BMI is: ', bmi)

print('Now lets calculate the area of a triangle')

base = float(input('enter base length: '))
triangle_height = float(input('enter height of the triangle: '))
area_of_triangle = 0.5 * base * triangle_height

print('For a triangle with a base of ', base ,'and a height of ', triangle_height , 'its area is: ', area_of_triangle)

print('Now lets calculate the perimeter')

side_a = input('enter side a: ')
side_b = input('enter side b: ')
side_c = input('enter side c: ')

perimeter = side_a + side_b + side_c

print('the perimeter is: ', perimeter)

print(len('python')!=len('dragon'))

print('ON in Python and Dragon: ', 'on' in 'python' and 'on' in 'dragon')

print('if jargon is in the sentence: ', 'jargon' in 'I hope this course is not full of jargon')

length_of_python = len('python')
float(length_of_python)
str(length_of_python)

print('checking for even numbers')
number = int(input('enter number to check: '))
remainder = number % 2

print('Is the number you entered even? ', remainder is 0)

print('Floor division comparison', 7 // 3 == int(2.7))

print('Check if type of string 10 is equal to type of 10', str(10) == int(10))

print('now we calculate pay')

weekly_hours = int(input('Enter number of hours you work in a week: '))
rate = int(input('How much are you paid in an hour? '))

earning_weekly = rate * weekly_hours

print('tadaa! you earn', earning_weekly, 'per week')