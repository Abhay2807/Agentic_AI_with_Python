# making it more efficient using multiprocessing

from multiprocessing import Process
import time

def heavy_calculations():
    print(" Starting heavy CPU work ")
    count = 0
    for x in range(10**7):
        count += x
    print(f" Work done, {count} ")

if __name__ == "__main__": 
    start_time=time.time()
    #Creating two processes
    processes = [Process(target=heavy_calculations) for _ in range(2)]
    [t.start() for t in processes]
    [t.join() for t in processes]
    end_time=time.time()
    print(f"Total process took {end_time-start_time:.2f} seconds")
