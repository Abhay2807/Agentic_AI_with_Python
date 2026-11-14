# deadlock
# when multiple threads can acquire the lock needed by other threads
# code can go in an infinite/long waiting condition until required locks are released by threads
# To avoid deadlock we can use > logging (thread_safe), enumeration on threads
import threading, time
lock1 = threading.Lock()
lock2 = threading.Lock()

def func1():
    # acquiring lock
    with lock1:
        print("Taken lock1 by func1")
        time.sleep(5)
        with lock2:
            print("taken lock2 by func1")

def func2():
    with lock2:
        print("Taken lock2 by func2")
        with lock1:
            print("taken lock1 by func2")

#creating threads
thread1 = threading.Thread(target=func1)
thread2 = threading.Thread(target=func2)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Main program exit")

