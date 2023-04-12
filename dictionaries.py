print('Day N of 30 Days of Python: Today we learn dictionaries')

personal_details = {
    'first_name' : 'Dennis',
    'second_name' : 'Kori',
    'is_married' : False,
    'has_kids' : False,
    'age' : 27,
    'skills' : ['Photoshop', 'Figma', 'Javascript', 'Python', 'Azure', 'AWS']  
}

print(len(personal_details))

print(personal_details['first_name']) #Using variable name
print(personal_details.get('second_name')) #Using .get method

personal_details['City'] = 'Nairobi' #Adding a new field to the dictionary
personal_details['skills'].append ('HTML') #Adding new field within the dictionary
personal_details['skills'].insert(4, 'CSS') #Adding to a specific index position
print(personal_details)

#Modifying a variable

personal_details['second_name'] = 'Cory'

print(personal_details)

#Checking for keys (variables)

print('City' in personal_details)
print('id_no' in personal_details)

#Removing elements

personal_details.pop('is_married') #Removal based on keyname 
personal_details.popitem() #Removes last item
del personal_details['has_kids'] #Removes the entire field

print(personal_details)

#Getting the keys
keys = personal_details.keys()
print(keys)

#Getting the values
values =personal_details.values()
print(values)