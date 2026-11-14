# # race condition
# # When multiple threads can write / update the same memory at same time
# When Threads are accessing/modifying the same shared state without synchronization.
# The race condition itself is caused by the unsynchronized shared resource

#Below code is unpredictable, Most times it may work fine but
# We have no idea which thread is increasing the count variable and there is no locking
#It can give the race condition any time (there is no lock), causing improper results
#Causing huge impact in healthcare/banking/stockMarket applications
import threading
import time

count=0


def count_incrementer():
    # using global variable
    global count
    for _ in range(1000):
        count+=1

# Create 2 threads
threads = [threading.Thread(target= count_incrementer) for _ in range(2)]
for t in threads : t.start()
for t in threads : t.join()
print(f"Count is {count}")


