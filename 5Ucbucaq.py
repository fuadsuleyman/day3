old_list = [(3,4,5),(6,8,10),(3,10,7)]

sorted_old_list = []

for i in old_list:
    sorted_old_list.append(sorted(i))

def check_trangle(nums):
    return nums[0]+nums[1] > nums[2]

trangle_list = list(filter(check_trangle, sorted_old_list))

print(trangle_list)

# Solution without filter

new_list_nonFilter = []

for item in sorted_old_list:
    if check_trangle(item):
        new_list_nonFilter.append(item)

print(new_list_nonFilter)
