######################################

# Functions

def player_info(name, team):
    print(f"Player name {name} plays for IPL team {team}")

player_info("Rohit","MI")
player_info("Kohli","RCB")
player_info("Rahul","DC")

######################################

# Calling multiple functions from a function

def player_age(age):
    print(f"Player's age is {age}")

def player_catg(catg):
    print(f"Player's category is {catg}")

def player_team(team):
    print(f"Player's team is {team}")

def player_info(player_dict):
    for player in player_dict:
        player_age(player["age"])
        player_catg(player["catg"])
        player_team(player["team"])
    print("Printed info related to all given players")


players_list = [
    {"age":34,"catg":"BAT","team":"MI"},
    {"age":32,"catg":"BOW","team":"RCB"},
    {"age":31,"catg":"AR","team":"CSK"},
    {"age":23,"catg":"WK","team":"GT"}
]

player_info(players_list)

######################################

# Returning value from the function

def multiplier(a, b):
    return (a*b)


print(f"Multiplication of 2 and 3 is : {multiplier(2,3)}")

print(f"Multiplication of 20 and 3 is : {multiplier(20,3)}")

print(f"Multiplication of 2 and 30 is : {multiplier(2,30)}")

######################################

## PARAMETERS


def player_info(name, team, age): # These 3 are function's parameters
    print(f"Selected player is {name} of team {team}, with age : {age}")


player_info("Rohit", "MI", 34) # positional arguments > Order matters
player_info(age=43, name="Dhoni", team='CSK') # keyword arguments > Order not matter


######################################

# *args, **kwargs

def sports(*args, **kwargs): # * takes all positional arguments in a tuple, ** takes all keyword / key-value pair arguments in a dictionary
    print(f"Legend Players are : {args}")
    print(f"Sports and legend teams are : {kwargs}")

sports( "Virat Kohli", "Jude bellingham", "Yamal", "Roger Fed", Football = "Real madrid", Cricket = "Mumbai Indians", Hockey = "belgium")

######################################

# Early Return
def print_score(num1, num2):
    if (num1 == num2):
        return (num1 ** num2)
    return (num1 * num2)

print(print_score(3,3))
print(print_score(20,5))

######################################

# Multiple Returns

def numbers_list ():
    return 10, 20

a, b = numbers_list()
print(a)
print(b)

######################################

# Types of Functions

# Recursive 

def print_num (n):
    print(n)
    if n==0 :
        return "Done reached 0"
    return print_num(n-1)

print(print_num(7))


# Lambdas

num_list = [12, 13, 18, 19 ,28, 72, 89, 100]

# Filter out even numbers

even_num = list(filter(lambda x : x%2 == 0 , num_list))
print(even_num)

# Another example 


sum_result = lambda a,b : a+b

print(sum_result(12,16))


######################################

#  Function Documentation

def my_func():
    """This is my function"""
    pass

print(my_func.__doc__)
print(my_func.__name__)



