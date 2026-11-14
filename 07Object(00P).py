#########################################

# Object Oriented Programming (OOP)

# Basics
# Example

class automobiles(): # creating a class
    pass

class firms():
    pass


cars = automobiles() # creating an object from a class
corporate = firms()

print(type(automobiles))
print(type(corporate))
print(type(corporate) is firms)
print(type(cars) is automobiles)
print(type(cars) is firms)

# Example

# Namespace

class school:
    students = 300

school1 = school()

print(f"Class {school.students}")
print(f"Object {school.students}")

school.location = "Mumbai"
print(f"Class {school.location}")
print(f"Object {school1.location}")

school1.location = "Delhi"
print(f"Class {school.location}")
print(f"Object {school1.location}")


# object namespace
print(f"Object {school1.__dict__}")
# class  namespace
print(f"Class {school.__dict__}")

# Attribute shadowing
# Example

class sports:
    name = "sport"
    type = "type"

sport1 = sports()
sport1.name = "cricket"
sport1.type = "outdoor"

print(f"class name {sports.name}")
print(f"object or instance name {sport1.name}")

del sport1.name # deleted name set for sport1

print(f"object name now {sport1.name}")

# Self Argument
# Example


class company:
    name = "hdfc"

    def comp_name(self):
        return (f"Company name is {self.name}")

comp1 = company()
print(comp1.comp_name()) # calling method using object , no need to pass context

comp2 = company()
comp2.name = "ibm"
print(comp2.comp_name())

comp3 = company()
comp3.name = "crisil"
print(company.comp_name(comp3)) # calling method using class , need to pass context

# Constructors and Init
# Example

class players_info:

    def __init__(self, team="xyz", player="abc", matches=0):
        self.team = team
        self.player = player
        self.matches = matches

    def player_summary(self):
        print(f"Player {self.player} has played {self.matches} matches for team : {self.team}")

player1 = players_info()
player1.player_summary()

player2 = players_info("Mumbai", "Rohit", 228)
player2.player_summary()

player3 = players_info(player= "Kohli", matches = 172)
player3.player_summary()

# Inheritance & Composition
# Example

class cricket:
    def __init__(self, league):
        self.league = league

    def league_info(self):
        print(f"The league name is {self.league}")

class IPL(cricket): # creating child class (inheritance)
    def league_age(self):
        print("t20 cricket league")

class SPL:
    SPL_cls = cricket # composition

    def __init__(self):
        self.country = self.SPL_cls("SPL")

    def league_loc(self):
        print(f"League {self.country.league} played in SL")
        self.country.league_info()

class BBL(IPL):
    BBL_cls = SPL

mi = IPL("ipl")
mi.league_age()
mi.league_info()
print(mi.league)
jt = SPL()
jt.country.league_info()
jt.league_loc()
ps = BBL("bbl")
ps.league_info()

######################


# Accessing base class using super() method

class Sports:
    def __init__(self, name, place):
        self.name = name
        self.place = place

class Cricket(Sports):
    def __init__(self, name, place, player):
        super().__init__(name, place)
        self.player = player

player1 = Cricket("Rohit","Mumbai","International")
print(f"{player1.name} {player1.place} {player1.player}")


# Another example


class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def show_employee(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")


class Manager(Employee):
    def __init__(self, name, employee_id, team_size):
        super().__init__(name, employee_id)
        self.team_size = team_size

    def show_manager(self):
        self.show_employee()
        print(f"Team size: {self.team_size}")


manager1 = Manager("Kush", 101, 8)

manager1.show_manager()


##############

# Method Resolution Order (MRO)

class A:
    label = "class a"

class B(A):
    label = "class b"

class C(A):
    label = "class c"

class D(C, B):
    pass

class E(B, C):
    pass

obj1 = D()
print(obj1.label)
obj2 = E()
print(obj2.label)

###########################

# Static Methods

class sports:

    @staticmethod # Decorator and with use of this decorator, this method of the class can be used directly, without object creation
    def game_info(data):
        return[item.strip() for item in data.split(",")]
    
raw_data = "  Cricket,Football , Hockey,   Tennis , "
cleaned_data = sports.game_info(raw_data)
print(cleaned_data)

###############################

# Class Methods

class sports:
    def __init__(self, game, place, player):
        self.game = game
        self.place = place
        self.player = player

    @classmethod
    def sports_info_dict(cls, sports_dict):
        return cls(sports_dict["game"],
                   sports_dict["place"],
                   sports_dict["player"])
    
    @classmethod
    def sports_info_string(cls, sports_str):
        game, place, player = sports_str.split("-")
        return cls(game, place , player)


sports_raw_dict={
    "game" : "Cricket", "place" : "England", "player" : "Sachin"
}    
obj1 = sports("Hockey", "India", "Gyanchand")
obj2 = sports.sports_info_dict(sports_raw_dict)
obj3 = sports.sports_info_string("Football-England-Messi")

print(obj1.__dict__)
print(obj2.__dict__)
print(obj3.__dict__)

######################

# Property Decorators (getter and setter)

class sports:
    def __init__(self, name):
        self._name = name

    #getter
    @property
    def name(self):
        return f"name is {self._name}"
    
    #setter
    @name.setter
    def name(self, name):
        if name == "cricket":
            self._name = "Cricket"
        else:
            self._name = "Non-Cricket"

obj1 = sports("Football")
print(obj1.name)
obj1.name = "cricket"
print(obj1.name)
obj1.name = "Hockey"
print(obj1.name)
        






