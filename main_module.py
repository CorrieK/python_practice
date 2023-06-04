from module import generate_full_name, sum_numbers, user_id_gen_by_user, rgb_color_gen
print(generate_full_name("Dennis", "Kori"))
print(sum_numbers(48, 56))

from module import generate_full_name as names, sum_numbers as total
print("Your names are: ", names("Dennis", "Kori"))
print("The total is: ", total(48,56))

from statistics import *
ages = [20,56,48,59,65,54,894,562,5,21]
print('The mean of the ages is: ',mean(ages))
print('The median of the ages is', median(ages))
print('The standard deviation of the ages is: ', stdev(ages))

import math

print(math.pi)

#print("Your user IDs are as follows: ", random_user_id())

#print(user_id_gen_by_user())

print(rgb_color_gen())
