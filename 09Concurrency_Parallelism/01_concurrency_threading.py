########## CONCURRENCY ###########

### 01 : THREADING : THREADS

#### MULTI THREADING

# USING ONLY ONE CORE, MULTIPLE THREADS BEING USED
# GETTING SWITCHED FREQUENTLY AND PERFORMING TASKS 

import threading
import time

def player_desc():
    for x in range(1,5):
        print(f"Player #{x} is a Indian origin Player")
        time.sleep(1)

def player_exp():
    for x in range(1,3):
        print(f"Player #{x} has very large experience of playing")
        time.sleep(5)

# Creating Threads for these 2 functions / tasks

player_desc_thread = threading.Thread(target=player_desc)
player_exp_thread = threading.Thread(target=player_exp)

# Starting / Invoking the threads

player_desc_thread.start()
player_exp_thread.start()

# Wait for both threads to finish

player_desc_thread.join()
player_exp_thread.join()

print(f"All information displayed , Thanks !")