it_companies = {'AllureAfrica', 'Microsoft', 'Google', 'Safaricom', 'Amazon'}

print(len(it_companies))

it_companies.add('Twitter')

print(it_companies)

it_companies.update(['Facebook', 'Apple', 'Cisco', 'Oracle'])
print(it_companies)

it_companies.discard('Cisco')
print(it_companies)

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

A.isdisjoint(B)
print(A)

A.intersection(B)
A.issubset(B)
A.symmetric_difference(B)
B.isdisjoint(A)
del A, B, it_companies

age_st = set(age)
print(len(age) == len(age_st))

