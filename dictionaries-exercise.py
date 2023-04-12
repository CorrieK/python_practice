dog = {}

dog['color'] = ''
dog['breed'] = ''
dog['legs'] = ''
dog['age'] = ''

student = { 'first_name' : ' ', 'last_name' : ' ', 'gender' : ' ', 'age' : ' ', 'marital_status' : ' ', 'skills' : [], 'country' : '', 'city' : ' ', 'address': ' '}

print(len(student))
print(len(dog))

student['skills'].append('HTML')
student['skills'].append('Figma')

student['age'] = 27

keys = student.keys()
print(keys)


values = student.values()
print(values)

student.pop('marital_status')
del dog
