# GIL 
# MULTI - PROCESSING

from multiprocessing import Process, current_process
import time

def player_info():
    print(f"Starting the process {current_process().name}")
    count=0
    for x in range(1000000):
        count+=1
    print(f"Ending the process {current_process().name}")

if __name__ == "__main__":
    p1 = Process(target=player_info, name="Process01")
    p2 = Process(target=player_info, name="Process02")
    st = time.time()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    et = time.time()
    print(f"All processes completed in time {et-st}")

