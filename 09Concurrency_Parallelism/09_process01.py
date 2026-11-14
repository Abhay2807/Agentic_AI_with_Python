# Example where threading does not work efficiently
# CPU BOUND > HEAVY COMPUTATIONAL OPERATIONS / WORK

import threading
import time

def heavy_calculations():
    print(" Starting heavy CPU work ")
    count = 0
    for x in range(10**7):
        count += x
    print(f" Work done, {count} ")

start_time=time.time()
#Creating two threads
threads = [threading.Thread(target=heavy_calculations) for _ in range(2)]
[t.start() for t in threads]
[t.join() for t in threads]
end_time=time.time()
print(f"Total process took {end_time-start_time:.2f} seconds")

