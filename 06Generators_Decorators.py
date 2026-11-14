######################################


# Generators

# Example 01

def player_names():
    yield "Rohit"
    yield "Dhoni"
    yield "Kohli"

players = player_names()
print(players) # Generator object , just referring to the function
for player in players:
    print(player)



# Example 02

def wom_player_names():
    yield "Smriti"
    yield "Shafali"
    yield "Kaur"

wom_players = wom_player_names()
print(f"First yield : {next(wom_players)}") # First yield
print(f"Next yield : {next(wom_players)}") # Next yield
print(f"Last yield : {next(wom_players)}") # Last yield


# Example 03

# Infinite Generators

def infinite_func():
    count = 1
    while True:
        yield f" Value {count}"
        count+=1

refer = infinite_func()
for _ in range(5):
    print(next(refer))


# Send Value to generators

def gen_send_value():
    print("Sending value to generator")
    value = yield
    while True:
        print(f"Printing the passed value {value}")
        value = yield

pass_value = gen_send_value()
next(pass_value) #start the generator
pass_value.send("Value1")
pass_value.send("Value2")


# Yield from and close the generators

# Example : yield from


def national_players():
    yield "rohit"
    yield "virat"

def international_players():
    yield "smith"
    yield "root"

def players_list():
    yield from national_players()
    yield from international_players()

for player in players_list():
    print(f"Player name : {player}")


# Example : closing the generator

def my_generator():
    try:
        while True:
            print("welcome in generator")
            order = yield "Welcome Inside"
    except:
        print("thanks for the visit")

my_gen = my_generator()
print(next(my_gen))
my_gen.close()


# Combined Example

def data_source():
    try:
        yield 10
        yield 20
        yield 30

        return "Source finished"

    finally:
        print("Data source cleanup")


def pipeline():
    result = yield from data_source()

    print("Source result:", result)

    yield 100


p = pipeline()

print(next(p))
print(next(p))
print(next(p))
print(next(p))
p.close()


#############################################

# Decorators

# Example

def my_decorator(func):
    def wrapper():
        print("before function runs")
        func()
        print("after function has run")
    return wrapper

@my_decorator
def my_name():
    print("My name is Kush")

my_name()
print(my_name.__name__) #Prints wrapper name not original function name

# Example


from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("before function runs")
        func()
        print("after function has run")
    return wrapper

@my_decorator
def my_name():
    print("My name is Kush")

my_name()
print(my_name.__name__) #Prints original function name

#####################################


# Example

from functools import wraps
def logger_decor(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print("before function")
        result = func(*args,**kwargs)
        print("after function")
        return result
    return wrapper

@logger_decor
def sum_func(num1, num2):
    print("Doing calculation")
    return (num1 + num2)

ans = sum_func(12, 16)
print(f"The final answer is {ans}")


# Example
# Multiple Decorators
# Decorators are applied bottom-up, but the resulting wrappers execute outermost-to-innermost (top-down).
from functools import wraps

def my_decor1(func):
    @wraps(func)
    def wrapper():
        print("decor1")
        func()
    return wrapper

def my_decor2(func):
    @wraps(func)
    def wrapper():
        print("decor2")
        func()
    return wrapper

@my_decor2
@my_decor1
def greet():
    print("My name is Abhay Singh!")

greet()

# logging Decorator


from functools import wraps

def logger_decor(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"😎 Running function : {func.__name__}")
        func(*args, **kwargs)
        print(f"❤️ function completed : {func.__name__}")
    return wrapper

@logger_decor
def my_func(name , age=12):
    print(f"Naam : {name} and age is {age}")

my_func("Abhay", 28)
print("*------------------*")
my_func("kush")


##########################


# Example

from functools import wraps

def admin_decor(func):
    @wraps(func)
    def wrapper(role):
        if role.lower() != "admin" :
            print("You do not have the required access")
            return None #best practice 
        else:
            return func(role)
    return wrapper

@admin_decor
def role_check(role):
    print(f"You have the required access {role}")

role_check("AdMin")
role_check("WorKEr")



