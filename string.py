progress = 'Day 4 of 30 days learning python'
print(progress.title())
first_name = input('Enter your first name: ')
second_name = input('Enter your second name: ')

full_name = 'You can call me {} {}'.format(first_name, second_name)

print(full_name)

print('hello', first_name, ' ', second_name, '\n we are now going to calculate the area of a trapezium')

side_a = input('Enter length of side a: ')
side_b = input('Enter length of side b: ')
height = input('Enter height: ')

#Converting the dimensions to integers to support the math function

side_a = int(side_a)
side_b = int(side_b)
height = int(height)

area_of_trapezium = (((side_a + side_b)/2)*height)

output = 'For a trapezium whose sides measure {} and {}, and has a height of {}, the area is {:.3f}'.format(side_a,side_b,height,area_of_trapezium)

print(output)

print(full_name.find('ory')) #Finding incidence of "Ory" in the full name
print(first_name.count('n')) #Counting the number of times "n" appears
print(first_name.capitalize(), second_name.capitalize())
print(full_name.split(','))
