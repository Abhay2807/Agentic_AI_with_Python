#####################

# FOR LOOP

for x in range (1,11):
    print(f"Value of x is : {x}")

#####################

# FOR LOOP

teams = ["MI","RCB","CSK","KKR"]

for team in teams:
    print(f"IPL Team : {team}")

#####################

# ENUMERATE

teams = ["MI","RCB","CSK","KKR"]

for index, team in enumerate(teams, start=1):
    print(f"Team number {index} : {team}")

#####################

# zip

players = ["ROHIT","RAJAT","DHONI","GAMBHIR"]
teams = ["MI","RCB","CSK","KKR"]

for player,team in zip(players, teams):
    print(f"{player} is the GOAT captain of IPL team : {team}")


#####################

# WHILE LOOP

money = 10

while (money<100):
    print(f"Current Money is : {money} and it is less than 100")
    money += 20
    print(f"Money after increase is : {money}")

print(f"Final Money amount became : {money}")

#####################


# CONTINUE, BREAK

scores = [12, 28, 72, 3, 7, -28, 90, -10, 0, 11, 13]

# Only print positive scores
# Skip negative scores
# If you find 0, stop checking and printing numbers after that
# Just print 0 found so process terminated


for score in scores:
    if score > 0:
        print(f"Positive Score found : {score}")
    if score < 0:
        print(f"Negative Score, skipping printing!")
    if score == 0 :
        break
print("Zero found so process terminated !")


#####################

# For Else
# List of Tuples

list_tuples1 = [ ("Abhay",18) , ("Rahul",19), ("Varn",19) ]

for person,age in list_tuples1:
    if age>=20:
        print(f"{person} is eligible")
        break
else:
    print("No person is eligible")

list_tuples2 = [ ("Abhay",28) , ("Rahul",19), ("Varn",23) ]

for person,age in list_tuples2:
    if age>=20:
        print(f"{person} is eligible")
        break
else:
    print("No person is eligible")
# Else part will only get execute if for loop does not break
# If we are able to break in for loop else part will not get executed


#####################

# Walrus

list_num =[12, 15, 18, 24, 30]
# Using Walrus operator we are assigning the expression's result to the remainder variable and then checking that variable's value to evaluate the if else condition
for x in list_num:
    if (remainder := x % 5): # True for non-zero values of remainder
        print(f"{x} is not divisible by 5, Remainder is {remainder}")
    else: # For zero values of remainder
        print(f"{x} is divisible by 5, Remainder is {remainder}")


# Another Example

goat_ipl_teams = ["MI","CSK","RCB","KKR"]

if ((user_ipl_team := input("Enter you IPL team code : ").upper().strip()) in goat_ipl_teams):
    print(f"Your team is : {user_ipl_team}")
    print(f"Your IPL team is a goat : {user_ipl_team}")
else:
    print(f"Your team is : {user_ipl_team}")
    print(f"Sorry your IPL team is not a goat : {user_ipl_team}")

#####################

# Using dictionaries in place of if-else / match-case

# List of dictionaries
users = [
    {"id":1, "name":"Abhay", "total": 100, "coupon" : "A1"},
    {"id":2, "name":"Kush", "total": 130, "coupon" : "A4"},
    {"id":3, "name":"Varn", "total": 150, "coupon" : "A3"},
    {"id":4, "name":"Rohit", "total": 200, "coupon" : "A2"}
]

# Dictionaries of coupons : (discount percent, fixed discount)
coupondict = {
    "A1" : (0.3, 10),
    "A2" : (0.2, 20),
    "A3" : (0.5, 30)
}

# Calculate final price for each user after their coupon is applied

for user in users:
    dis_per, fix_dis = coupondict.get(user["coupon"], (0,0)) # default (0,0) if no such coupon found
    total_dis = int(user["total"] * dis_per) + fix_dis
    print(f"Total discount for user_id {user["id"]} and username : {user["name"]} is {total_dis}")
    print(f"Total price to be paid by {user["name"]} is : {user["total"] - total_dis} INR only! ")








