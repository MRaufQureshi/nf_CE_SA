#First stand
print ("Hello, world!")
print ("Lets understand the print command itself!")

#What does print takes? 
# print (*object, sep='', end='\n', file=sys.stdout, flush=False)
# sep is separate, end is what do you want to do at the end, file is file name, 
# file is where you want to store your output
# flush is it forces the computer to write the text onto your hard drive instantly rather than waiting

# Example :

# 1. Open a file to use with the 'file' parameter
with open("myFile.txt", "w") as my_file:
    
    # 2. Call print() demonstrating all parameters
    print("2026-08-13", "10:20:00", "ERROR", "Lost of time..", 
          sep=" | ", 
          end=" [RETRYING...]\n", 
          file=my_file, 
          flush=True)


#Functions:
# input ("What's your name: ") Takes input but does not writes out
# .strip() Helps in removing space and characters

# var1 = input ("What's your name: ").strip().title()
# print (f"My name is: {var1}")

#Variables:
# var1 = input("What's your name? ")
# print ("User name is: " + var1) 

# # .strip()
# var2 = input("What's your name? ")
# var2 = var2.strip()
# print (f"Hello, {var2}")

# # .title()
# var3 = input("What's your name? ")
# var3 = var3.title()
# print (f"Hello, {var3}")

# # .title()
# var4 = input("What's your name? ")
# var4 = var4.strip().title()
# print (f"Hello, {var4}")

#Combine functions
# var1 = input ("What's your name: ").strip().title()
# print (f"My name is: {var1}")

