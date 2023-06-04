def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname

def sum_numbers(numOne, numTwo):
    sum = numOne + numTwo
    return sum

from random import randint
def user_id_gen_by_user():
    character_limit = int(input("Enter the number of characters for the USER ID: "))
    num_of_IDs = int(input("How many USER IDs do you require? "))
    IDs = []
    
    for _ in range(num_of_IDs):
        user = []
        while len(user) < character_limit:
            character_list = randint(1, 9)
            user.append(str(character_list))
        
        IDs.append(''.join(user))
    
    return IDs

def rgb_color_gen():
    iterations = 3
    code = []
    while len(code) < iterations:
        color_swatch = randint(0, 255)
        code.append(str(color_swatch))
    return ','.join(code)


