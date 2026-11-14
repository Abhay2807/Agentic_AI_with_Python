# non-daemon Threads
# By deafult threads, which will keep running (until assigned work/func is completed) 
# even if the main program exit

import threading
import time

def player_info():
    #starting a infinite loop
    while True:
        print("fetching player info")
        time.sleep(1) #blocks the thread on which it is running

# Create and start a non-daemon (by default one) thread 
threading.Thread(target=player_info).start()

print("main program exit")


