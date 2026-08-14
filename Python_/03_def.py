# def hello():
#     print("Hello this is a functions")

# name = input("What is your name? ")
# hello()
# print(name)

# Passing variable using parameter
# def hello(to):
#     print("Welcome user: ", to)

# hello(input("What is your name? "))

# Scope
# def main():
#     name = input("What is your name? ")
#     hello(name)

# def hello (name="world"):
#     print("Hello", name)

# main()

# Return
def main():
    x = int(input("Value of x is: "))
    print ("x square is ", square (x))

def square(n):
    return n * n

main()