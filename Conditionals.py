print('Today we are learning about conditionals which are important in looping among other use cases')

#IF Condition

name = input('Enter your name: ')

if name == 'Cory':
    print('name successfully changed: ', name)

#IF Else statement where there are only one iteration

if name == 'Cory':
    print('Wazzaaa!!!')
else:
    print('Not Cory!')

#If Elif Else statement for invoking multiple conditions

if name != 'Cory':
    print('Is your name: C?')
elif name == 'Cory':
    print('Wazaaaa!')
else:
    print('Access Denied:', name)

#Short hand IF statement

print('Wazzaaa!!!') if name == 'Cory' else print('Not Cory')

#Nested conditions
#In this example we want to classify user age group based on input
#This example also includes logical operators

print('Want to find out your generation?')

year_of_birth = input('Enter year of birth: ')
year_of_birth = int(year_of_birth)

if year_of_birth > 1945:
    if year_of_birth >= 1946 and year_of_birth <= 1964:
        print('You are a baby boomer')
    elif year_of_birth >= 1965 and year_of_birth <= 1979:
        print('You are a Gen X')
    elif year_of_birth >= 1980 and year_of_birth <= 1994:
        print('You are a Millenial')
    elif year_of_birth >= 1995 and year_of_birth <= 2012:
        print('You are a Gen Z')
    elif year_of_birth >= 2013 and year_of_birth <= 2025:
        print('You are a Gen Alpha')
    elif year_of_birth > 2025:
        print('liar liar pants on fire!')
else:
    print('age group not defined!')