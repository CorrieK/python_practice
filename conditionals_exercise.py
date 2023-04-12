print('Are you old enough to drive, let us find out.')

age = input('Enter your age: ')

legal_driving_age = 18
age = int(age)

deficit = legal_driving_age - age
deficit = int(deficit)

if age >= 18:
    print('You are old enough to drive')
else:
    print('you have', legal_driving_age - age, 'more years to learn how to drive.')
    print('You have {} more years to learn how to drive'.format(deficit))


print('Let us see who is older')

your_age = input('enter your age: ')
your_age = int(your_age)
my_age = input('enter my age: ')
my_age = int(my_age)

if your_age > my_age:
    print('You are older by', your_age - my_age, 'years.')
elif your_age == my_age:
    print('We are agemates')
else:
    print('Be Humble, Sit Down!')

print('Comparing two numbers')

num1 = input('Enter the first number: ')
num1 = int(num1)
num2 = input('Enter the second number: ')
num2 = int(num2)

if num1 > num2:
    print('The first number is greater.')
elif num1 < num2:
    print('The second number is greater.')
else:
    print('The two numbers are equal.')

print('Converting percentage to grade.')

score = input('Enter score of test: ')
score = int(score)

if score < 100:
    if score >= 80 and score <=100:
        print('Your grade is A')
    elif score >= 70 and score <=79:
        print('Your grade is B')
    elif score >= 60 and score <= 69:
        print('Your grade is C') 
    elif score >= 50 and score <= 59:
        print('Your grade is D')
    elif score >= 0 and score <= 49:
        print('Your grade is F')   
else: 
    print('Invalid score')

print('Now we check the seasons')

current_month = input('Enter Current Month: ')
current_month = str(current_month)
current_month = current_month.capitalize() #The check looks for accurate representations we capitalize to account for user input in lower case

if current_month == 'September' or current_month == 'October' or current_month == 'November':
    print('The season is Autumn')
elif current_month == 'December' or current_month == 'January' or current_month == 'February':
    print('The season is Winter')
elif current_month == 'March' or current_month == 'April' or current_month == 'May':
    print('The season is Spring')
elif current_month == 'June' or current_month == 'July' or current_month == 'August':
    print('The season is Summer')
else:
    print('Invalid input')

print('A list with fruits and adding the options we enter')

fruits = ['banana', 'orange', 'mango', 'lemon']

add_fruit = input('Add a fruit to the list: ')
#add_fruit = add_fruit.capitalize()

check_existing = add_fruit in fruits
existing = str(check_existing)

if existing == 'True':
    print('Does {} exist in the list?'.format(add_fruit), existing)
    print('{} exists in the list'.format(add_fruit))
else:
    fruits.append(add_fruit)
    print('{} Was added to the list'.format(add_fruit))
    print('Here is the complete list: ', fruits)

