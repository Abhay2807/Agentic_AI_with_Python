# Process Queue

# Queue (it is kind of a shared state)> Can be used to share memory between the processes
# All processes can access the information / values provided inside this queue now

from multiprocessing import Process, Queue


def player_info(queue):
    queue.put(" Putting player information ")

if __name__ == "__main__":
    queue = Queue()
    p = Process(target=player_info, args=(queue,))
    p.start()
    p.join()
    print(f" Value is:{queue.get()} ")


