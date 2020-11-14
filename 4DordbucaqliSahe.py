old_list = [(3,4),(10,3),(5,6),(1,9)]

def get_sahe(myList):
    result = 1
    for x in myList:
         result = result * x 
    return result 

new_list = list(map(get_sahe, old_list))

print(new_list)

# Solution without map

new_list_nonMap = []

for item in old_list:
    new_list_nonMap.append(get_sahe(item))

print(new_list_nonMap)