name = input('Enter your name: ')

# if name == "RAUF":
#     print('Name is: ', name)
# else:
#     print('Go Home!')

# Match case
# match name:
#     case "Rauf": # if condition
#         print('Name is: ', name)
#     case 'X':   # if condition
#         print('Name is: ', name)  
#     case _:     # else condition
#         print('Who now?')

# Match case with OR condition

match name:
    case "Rauf" | "Maddie" | "Steven": # OR condition
        print('Name is: ', name)
    case 'X':   # if condition
        print('Name is: ', name)  
    case _:     # else condition
        print('Who now?')
