thirty = 'Thirty'
days = 'Days'
of = 'Of'
python = 'Python'
space = ' '

course = thirty + space + days + space + of + space + python

print(course)

coding = 'Coding'
fo = 'For'
who = 'All'

company = coding + space + fo + space + who

print(company)

print('the length of the company is: ', len(company))

print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())

print(company.find('Coding'))
first_word = company[0:6]
print(first_word)
print(company.replace('Coding', 'Python'))
print(company.split(', '))
print('the tenth character is: ', company[10])
# company = str(company)

python2 = 'Python For Everyone'
coding2 = 'Coding For All'
acronym1 = python2[0:8:12]
print('Acronym is: ', acronym1)
company2 = company.replace('Coding', 'Python')
# company2 = str(company2)
acronym2 = coding2[0:8:12]
print('Acronym is: ', acronym2)

print('The first character is: ', company[0])

tech_companies = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'

print(tech_companies.split(', '))

# Use index to determine the position of the first occurrence of F in Coding For All.

print(company.index('F'))

#Use rfind to determine the position of the last occurrence of l in Coding For All People.

print(company.rfind('l'))

#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

sentence = 'You cannot end a sentence with because because because is a conjunction'

print('Because first appears here: ', sentence.index('because'))
print('Because first appears here: ', sentence.find('because'))

print(sentence.strip('because because because'))

print('Does the string end with coding?', company.endswith('coding'))
print('Does the string start with Coding?', company.startswith('Coding'or'coding'))

python_libs = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']

joined_python_libs = ' #'.join(python_libs)

print(joined_python_libs)

print('\t I am enjoying this challenge. \n \t I just wonder what is next.')

print('Name\t\t' 'Age\t\t' 'Country\t\t' 'City' '\nAsabeneh\t' '250\t\t' 'Finland\t\t' 'Helsinki')

radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius {} is {} meters square.'.format(radius,area))

a = 8
b = 6

print('{} + {} = {}'.format(a,b, a+b))
print('{} - {} = {}'.format(a,b, a-b))
print('{} * {} = {}'.format(a,b, a*b))
print('{} / {} = {:.2f}'.format(a,b, a/b))
print('{} % {} = {}'.format(a,b, a%b))
print('{} // {} = {}'.format(a,b, a//b))
print('{} ** {} = {}'.format(a,b, a**b))