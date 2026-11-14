# Process Value

# Value (it is kind of a shared state)> Can be used to share memory between the processes
# All processes can access the information / values provided inside this value now

from multiprocessing import Value, Process

def incremental_func(counter):
    for _ in range(1000):
        with counter.get_lock():
            counter.value += 1

if __name__ == "__main__":
    counter = Value('i', 0)
    # creating 12 processes
    processes = [Process(target=incremental_func, args=(counter,)) for _ in range(1,13)]
    [p.start() for p in processes]
    [p.join() for p in processes]
    print(f" Counter value is {counter.value} ")







