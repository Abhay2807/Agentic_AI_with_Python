# daemon threads
# Background threads which automatically shut down when main program exit

import threading
import time

def player_info():
    while True:
        print("fetching player info")
        time.sleep(1) #blocks the thread on which it is running

# Create and start a daemon thread 
threading.Thread(target=player_info, daemon=True).start()

print("main program exit")


