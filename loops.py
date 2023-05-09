print('In this session we will learn about the For and While loop')

#While loop
#In this example we have a code that asks a user for an input as long as the number of entries is not exhausted
''' 
number_of_employees = 10
employee_list = []

while number_of_employees <= 10 and number_of_employees > 0:
    employee_name = input('Enter employee name: ')
    employee_list.append(employee_name)
    print('The new entry is for {} and the existing entries are {}.'.format(employee_name, employee_list))
    number_of_employees = number_of_employees - 1
    print('The remaining entries are: ', number_of_employees)
else:
    print('Maximum number of names has been reached')

'''

#Break and continue
#Printing odd numbers between 1 and 10

number = 1
number = int(number)
'''
while number <= 20:
    if number == 13:
        break

    if number % 2 == 0:
        number = number + 1   
        continue
    else:
        print(number)
        number += 1
'''    
        
#For Loop
coding_language = 'Python'
numbers = [1,2,3,4,5,6]
for number in numbers:
    print(number)

for letter in coding_language:
    print(letter)

for i in range(len(coding_language)):
    print(coding_language[i])

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)


names = ['Jane', 'John', 'Doe']
for name in names:
    print(name)

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)