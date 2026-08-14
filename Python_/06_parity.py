def main():
    x = int(input('What is the value of x?: '))

    if is_even(x):  # Call the function
        print('Value is Even')
    else:
        print('Value is Odd')

# def  is_even(n):    #Function that check if the value is divisable by 2
#     if n % 2 == 0:
#         return True
#     else:
#         return False

# Simplified Code:
def  is_even(n):    #Function that check if the value is divisable by 2
    return n % 2 == 0 # Check True or False with return.
    
main()