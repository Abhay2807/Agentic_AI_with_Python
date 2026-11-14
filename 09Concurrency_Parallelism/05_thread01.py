import threading
import time

def pitch_prep():
    print("Pitch preparation before match")
    time.sleep(2)
    print("Pitch preparation done")

def toss_prep():
    print("Toss preparation before the match")
    time.sleep(3)
    print("Toss preparation done")

# Capturing start time
start_time = time.time()

#Creating the threads
t1 = threading.Thread(target=pitch_prep)
t2=  threading.Thread(target=toss_prep)

# Starting the threads
t1.start()
t2.start()

# Waiting for both threads to complete
t1.join()
t2.join()
# capturing end time

end_time = time.time()

print(f"All prep done in {end_time - start_time}")

