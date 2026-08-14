# Concept of dictionary is 2 dimensional
# How to create a dictionary:
# We use {} with variable and this defines its a  dictionary
# my_list = {
#     "asd" : "house1",
#     "fgh" : "house2",
#     "jkl" : "house1"
# }

# print(my_list["asd"])
# print(my_list["fgh"])
# print(my_list["jkl"])

# We first print the keys
# for list in my_list:
#     print(list)

# Now we print the keys and its index value
# for list in my_list:
#     print(list, my_list[list])

# List of dictionary
# Here name, email, city are KEYS
# Here values or definition are Rauf, xyz, Berlin for example 
new_list = [
    {'name' : 'Rauf', 'email': 'xyz', 'city': 'Berlin'},
    {'name' : 'ZUY', 'email': 'UYUY', 'city': 'laknsldna'},
    {'name' : 'Roansdonao', 'email': 'xakjbsdkyz', 'city': 'kaakjsdb'},
]

for i_index in new_list: # Here it iterates - new_list has 3 records
    print(i_index['name'], i_index['email']) # Here it goes to inside those records and return what ever value is of "name"