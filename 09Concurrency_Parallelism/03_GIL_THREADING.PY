import threading
import time

def player_info():
    print(f"{threading.current_thread().name} is started")
    count = 0
    for x in range(1000000):
        count+=1
    print(f"{threading.current_thread().name} is finished")

# Creating the threads
thread1 = threading.Thread(target= player_info, name = "Rohit")
thread2 = threading.Thread(target= player_info, name= "Kohli")
# Capturing time before starting threads
start_time = time.time()
# Starting the threads
thread1.start()
thread2.start()
# Waiting till both threads complete
thread1.join()
thread2.join()
# Capturing time after threads are completed
end_time = time.time()

print(f"Information processing completed in time , {end_time-start_time} seconds.")
    
# Here GIL Lock and Mutex is working
