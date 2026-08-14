# x = int (input("Input the value of x: "))
# y = int (input("Input the value of y: "))

# IF Condition

# if x < y:
#     print ("x is LESS than y")

# if x > y:
#     print ("x is GREATER than y")

# if x == y:
#     print ("x is EQUAL to y")

# if x != y:
#     print ("x is NOT EQUAL than y")

# IF ELSE Condition

# if x < y:
#     print ("x is LESS than y")

# elif x > y:
#     print ("x is GREATER than y")

# elif x == y:
#     print ("x is EQUAL to y")

# elif x != y:
#     print ("x is NOT EQUAL than y")

# OR ELSE Condition

# if x < y or x > y:
#     print ("x is NOT EQUAL to y")
# else:
#     print ("x is EQUAL to y")

#===================
# NEW CHAPTER: WHILE 
#===================

# i = 0
# while i <= 3:
#     print('meow')
#     i = i +1

# for i in [0,1,2]:
#     print('meow')

# while True:
#     n = int(input('What is the value for n?: '))
#     if n > 0:
#         break

# for i in range(n):
#     print('meow')

# Using in main() function

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input('Enter value for n: '))
        if n > 0:
            break
    return n

def meow(n):
    for i in range(n):
        print('meow')
main