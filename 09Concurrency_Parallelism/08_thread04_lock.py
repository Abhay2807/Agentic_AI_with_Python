# Threading example on thread lock

import threading
import time

# Defining global variable
counter = 0

# Getting the lock
lock = threading.Lock()

def count_incrementer():
    global counter # Accessing global variable
    for x in range(10000):
        with lock: # Applying thread lock
            counter +=1

# Creating multiple threads 

threads = [ threading.Thread(target=count_incrementer)  for x in range(10)]

# Starting all threads

[t.start() for t in threads]

# Waiting for all threads to complete

[t.join() for t in threads]

print(f"Counter value is {counter}")

