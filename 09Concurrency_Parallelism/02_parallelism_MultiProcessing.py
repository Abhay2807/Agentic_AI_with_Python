##### Parallelism ###

### Multi-Processing

from multiprocessing import Process
import time

def player_info(name):
    print(f"Player info displaying , {name} is Indian player")
    time.sleep(2)
    print(f"{name} info displaying completed")

if __name__ == "__main__":
    players=[
        Process(target = player_info, args=(f"Player {x}", ))
        for x in range(1,4)
    ]

    # starting the processes

    for p in players:
        p.start()

    # wait for all processes to complete

    for p in players:
        p.join()

    print("All players covered!")