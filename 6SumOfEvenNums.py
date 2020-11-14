from functools import reduce

my_list = [1,2,3,4,5,6,7,8,9,10]

new_list = list(filter(lambda n: n%2==0, my_list))

sum = reduce(lambda a, b: a+b, new_list)

print(sum)

# Solution without filter and reduce

def is_even(n):
    return n%2==0

even_list = []

for num in my_list:
    if is_even(num):
        even_list.append(num)

sum = 0

for num in even_list:
    sum += num

print(sum)