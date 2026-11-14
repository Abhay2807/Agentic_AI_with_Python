###########################################################

#Conditionals

#Example-01

blood_type = input("Enter your blood_type : ").lower()
print(f"You entered blood_type : {blood_type}")
if blood_type == 'a':
    print("Rare blood type")
elif blood_type == 'b':
    print("Common blood type")
elif blood_type == 'o':
    print("Very very rare blood type")
else:
    print("Sorry we do not have any info for this blood type!")

#Example-02

age = int(input("Enter your age (only as an integer) :  "))
print(f"Entered age is : {age}")
if age>=18:
    print("You are an adult and can vote!")
else:
    print("You are not an adult, so cannot vote!")


# Ternary Operator

exam_score = int(input("Enter your integer score out of 100 : "))
print(f"Your exam_score out of 100 is : {exam_score}")
exam_result = "passed" if exam_score>=33 else "failed"
print(f"Your exam result is : {exam_result}")

# Match Case Usage

print("Info is Available for IPL team codes : RCB/MI/CSK/KKR")
team_code = input("Please enter your fav IPL team code : ").lower()
print(f"Entered IPL team code is {team_code}")

match team_code:
    case "rcb":
        print("RCB has won 2 IPL trophies!")
    case "csk":
        print("CSK has won 5 IPL trophies!")
    case "kkr":
        print("KKR has won 3 IPL trophies!")
    case "mi":
        print("MI has won 5 IPL trophies!")
    case _:
        print(f"No information available for this IPL team code : {team_code}")




























