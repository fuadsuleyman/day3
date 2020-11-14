from ast import literal_eval as make_tuple

names = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
last_names = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

nameAndLastName = list(zip(names, last_names))

print(nameAndLastName)

print('--------------------------------------------------------------')

# Solution without filter and reduce

new_name_lastname_list = []

for i in range(len(names)):
    new_tuple2 = []
    new_tuple2.append(names[i])
    new_tuple2.append(last_names[i])
    new_name_lastname_list.append(tuple(new_tuple2))

print(new_name_lastname_list)
