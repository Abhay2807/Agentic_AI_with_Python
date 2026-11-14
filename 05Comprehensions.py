######################################

# Comprehensions

# List

list_num = [12,17,19,3,72,18,7]

# Find odd numbers

list_odd_num = [ num for num in list_num if num%2 !=0 ]
print(list_odd_num)

# SET


list_num = [3,12,28,72,7,28,7,72,99]

# Find all unique numbers

unique_num = { num for num in list_num}
print(unique_num)

# Another example

dict_players = {

    "mumbai" : ["rohit","bravo","chahal"],
    "chennai" : ["dhoni","raina","bravo"],
    "bengaluru" : ["chahal","kohli","maxwell"],
    "punjab" : ["chahal","maxwell","iyer"]

}

# Filter out all unique(distinct) player names

unique_players = {player for players_list in dict_players.values() for player in players_list}

print(f"Unique players are : {unique_players}")

# Dictionary

prices_usd = {

    "bag" : 20,
    "bat" : 30,
    "rubber" : 1

}

# Convert the prices in USD to INR (*90) and print back the dictionary

prices_inr = {item : price*92  for item , price in prices_usd.items() }

print(prices_inr)


# Generator

list_num = [ 12, 28, 7, 30, 15, 3, 14, 1 , 10 ]

# Give me the sum of numbers but only consider two-digit numbers

sum_result = sum(num for num in list_num if num >= 10)
print(f"The required sum is {sum_result}")



