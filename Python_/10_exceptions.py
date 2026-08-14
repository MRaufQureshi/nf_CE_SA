# try:
#     x = int(input('Input value: '))
#     print(f"Value is {x}")
# except ValueError:
#     print('Value is not an integer')

# Else exception handling
# try:
#     x = int(input('Input value: '))
#     print(f"Value is {x}")
# except ValueError:
#     print('Value is not an integer')

# else:
#     print(f"Value is {x}")

# While condition exception handling
while True: # We are executing a while loop which is true until it becomes false (meaning run for ever until you get the correct value)
    try:
        x = int(input('Input value: '))
    
    except ValueError:
        print('Value is not an integer')

    else:
        break

print(f"Value is {x}")