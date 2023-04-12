tuple = ()
sis_name = ('Jane Doe', 'Jolene Doe', 'Melanin Doe')
bro_name = ('Jack Joe', 'Gi Joe', 'Njoo Hapa')
siblings = sis_name + bro_name
no_of_siblings = len(sis_name) + len(bro_name)
print('You have {} siblings.'.format(no_of_siblings))

family_members = list(siblings)

family_members.append('Mother Hen')
family_members.append('Father Hen')

print('Your family members are: ', family_members)

Ja_D, Jo_D, Me_D, Ja_J, Gi_J, Nj_H, *parents = family_members

print(parents)

print(siblings)

fruits = ('Melon', 'Pineapples', 'Oranges', 'Grapes', 'Apples')
vegetables = ('Broccoli', 'Parsley', 'Kales', 'Tomato', 'Cabbage')
animal_products = ('Ghee', 'Eggs', 'Milk', 'Meat', 'Leather')

food_stuff_tp = fruits + vegetables + animal_products

food_stuff_lt = list(food_stuff_tp)
print('First three items: ', food_stuff_lt[0:3])
print('Last three items: ', food_stuff_lt[-4:-1])

print(len(food_stuff_lt))

print('Middle item: ', food_stuff_lt[7])

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

does_exist = 'Estonia' in nordic_countries
print(does_exist)

does_exist2 = 'Iceland' in nordic_countries
print(does_exist2)
