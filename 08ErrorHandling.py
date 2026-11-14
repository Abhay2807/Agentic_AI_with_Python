#############################

# Error handling #

# Try Except #

def cricket_players_info(player):
    try:
        print(f"Player : {player}")
        if player.lower() == "na":
            raise ValueError("No info for this player name")
    except ValueError as e:
        print(f"Error : {e}")
    else:
        print(f"{player} is a great player")
    finally:
        print("Info completed, next player please!")

cricket_players_info("Rohit")
cricket_players_info("nA")
cricket_players_info("Kohli")
cricket_players_info("NA")
cricket_players_info("Dhoni")

# Multiple & Custom Exception

class InvalidInfo(Exception):
    pass

def player_info(name, matches):
    name = name.lower()
    player_data = {"rohit": 45, "kohli" : 50}
    try:
        if name not in player_data:
            raise InvalidInfo("No such player found")
        if not isinstance(matches, int):
            raise TypeError("Matches must be integer")
        total_runs = matches * player_data[name]
        print(f"Total runs scored by {name} is {total_runs} at an average of {player_data[name]}")
    except Exception as e:
        print(f"Error is : {e}")
    finally:
        print("Next player please")

player_info("rohit", 100)
player_info("Dhoni", 55)
player_info("KoHli", 90)
player_info("RohIT", 56.2)


