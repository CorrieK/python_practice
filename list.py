print('Today we are learning about lists!')

first_list = list()
print(list())
music_taste = ['EDM', 'Deep House', 'Afro House', 'Pop', 'Amapiano', 'Drum and Bass', 'Rock']
music_genres = len(music_taste)
print('You love {} music genres'.format(music_genres))
first_item = music_taste[0]
print(first_item)
middle_item = music_taste[4]
print(middle_item)
last_item = music_taste[-1]
print(last_item)

mixed_data_types = {'name' : 'Dennis',
                    'age' : 27, 
                    'height' : 168,
                    'marital_status' : 'single',
                    'address' : 'Nairobi'
}

print(mixed_data_types)

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print('Leading IT Companies are: ', it_companies)

print('the number of companies are: ', len(it_companies))

print(it_companies[0])
print(it_companies[3])
print(it_companies[6])

it_companies[0]= 'AllureAfrica'

print(it_companies)

it_companies.append('Cisco')

print(it_companies)

it_companies.insert(2, 'Facebook')

# it_companies.swapcase[6]

# print(it_companies)

joined_it_companies = "# ".join(it_companies)

print(joined_it_companies)

does_exist = 'AllureAfrica' in it_companies
print(does_exist)

# print(it_companies.find('AllureAfrica'))

it_companies.sort()

print(it_companies)

it_companies.sort(reverse=True)

print(it_companies)

print(it_companies[0:3])

print(it_companies[-4:-1])

it_companies.pop(1)


print(it_companies)

print(len(it_companies))

it_companies.pop(3)

print(it_companies)

it_companies.pop(-1)

print(it_companies)

it_companies.clear()

del it_companies

#print(it_companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end + back_end

print(full_stack)

full_stack.insert(5, 'Python')
full_stack.insert (6, 'SQL')

print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort(reverse=True)

print('the oldest is: ', ages[0])
print('the youngest is: ', ages[-1])

print(len(ages))
median = ages[4] + ages[5] / 2
print('the median age is: ', median)

# average = int(ages[0:9])/10

import math

avr = ages[0:9]
total = sum(ages)
average = total/10
print(total)

# int(avr)

# average = avr/10

#print(average)

print('the average age is: ', average)

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

ch, Rs, us, *scandic = countries

print(scandic)

print(countries)

print(len(countries) >= len(scandic))






