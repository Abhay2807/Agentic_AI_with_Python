print("Hello World!")

# DATA TYPES

age = 24
print(f"My age is : {age}")

a = 10
b = 6
print(a/b) # Complete decimal value
print(a//b) # Nearest (Left) Integer Value
print(a%b) #Remainder
print(a**b) # a raise to power b

###########################################################

# String

name = "Abhay"
print(name[0]) #first character
print(name[-1]) #last character
print(name[0:5]) #whole name
print(name[0:5:2]) #take characters from start to end, skipping one in between
print(name[::-1]) #reverse the string

###########################################################

# Tuples

my_tuple = (24,"abhay")
print(my_tuple)

###########################################################

# LIST

my_list = ["abhay","kush"]
my_list.append("varnika")
print(my_list)


###########################################################

#Sets

set1 = {1,2,3,4,4}
set2 = {4,5,6}
print(set1)
print(set2)
print(set1.union(set2)) #All unique values from both
print(set1 | set2) #Other way to do union
print(set1.intersection(set2)) #All unique common values from both
print(set1 & set2) #Other way to do intersection

###########################################################

# Dictionary

my_dict = {"name" : "Abhay", "age" : 24, "city" : "Mumbai"}
print(my_dict)
print(my_dict["name"])
print(my_dict.keys())
print(my_dict.values())

my_dict["gf"] ="varnika"
print(my_dict)

###########################################################


