'''
for number in range(11):
    print('Output from For Loop', number)

num = 1
while num >= 1 and num <=10:
    print('Output from while loop', num)
    num = num + 1
else:
    print('Done Iteration')

character = '#'
# print(character)

iteration_number = 1

character_list = list(character)

while iteration_number >=1 and iteration_number <=7:
    # print(character_list)    
    joined_character_list = ' '.join(character_list)
    print(joined_character_list)
    character_list.append(character)    
    iteration_number += 1
else:
    print('')

initial = 0

while initial >= 0 and initial <= 10:
    print('{} * {} = {}'.format(initial,initial,initial ** 2))
    initial += 1
else:
    print('End of multiplicaion table')


names = ['Python', 'Numpy','Pandas','Django', 'Flask']

for name in names:
    print(name)



print('Even numbers between 0 and 100 are: ')

first = 0

while first >= 0 and first <= 100:
    if first % 2 != 0:
        first += 1
        continue
    else:
        print(first)
        first += 1

'''
import math

for number in range(101):
    total = sum(number)
    print('The sume of all numbers is ', total)

            
        

