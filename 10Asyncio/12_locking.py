# Locking > To avoid race condition scenario
# Use a threading.Lock to ensure only one thread updates the shared counter at a time.
# with lock: makes the increment a protected critical section. Other threads must wait until the lock is released.

import threading
import time

count=0
my_lock = threading.Lock()


def count_incrementer():
    # using global variable
    global count
    for _ in range(1000):
        with my_lock:
            count+=1
        

# Create 2 threads
threads = [threading.Thread(target= count_incrementer) for _ in range(2)]
for t in threads : t.start()
for t in threads : t.join()
print(f"Count is {count}")


