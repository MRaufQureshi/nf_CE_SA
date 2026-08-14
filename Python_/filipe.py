myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

# Here key, value are just variable representing the column and its value above
for key, value in myVehicle.items(): # items() function tells the for loop to traverse the collection
    print("{} : {}".format(key, value)) 