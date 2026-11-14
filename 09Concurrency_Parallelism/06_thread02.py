import threading
import time

def making_biryani(type, wait_time):
    print(f"Starting to cook {type} biryani")
    time.sleep(wait_time)
    print(f"{type} biryani is ready to serve")

t1 = threading.Thread(target=making_biryani, args=("Hyderabadi", 2))
t2 = threading.Thread(target=making_biryani, args=("Kolkata", 3))

t1.start()
t2.start()
t1.join()
t2.join()



