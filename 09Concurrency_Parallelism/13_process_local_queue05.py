# Also, a lock on every increment introduces synchronization overhead. If the main goal is simply to calculate a total, it can be more efficient for each process to maintain a local counter and return its result, then sum the results in the main process.
# Here is the complete, runnable code using local counters + multiprocessing.Queue, without a lock on every increment.
# Local counters + Process Queue

from multiprocessing import Process, Queue
def incremental_func(queue):
    # Each process has its own local counter
    counter = 0
    for _ in range(1000):
        counter += 1
    # Send the final local result to the main process
    queue.put(counter)

if __name__ == "__main__":
    # Create a queue for collecting results
    queue = Queue()
    # Create 12 processes
    processes = [
        Process(target=incremental_func, args=(queue,))
        for _ in range(12)]
    # Start all processes
    for p in processes:
        p.start()
    # Wait for all processes to finish
    for p in processes:
        p.join()
    # Collect results from all 12 processes
    results = []

    for _ in processes:
        results.append(queue.get())
    # Calculate the final total
    total = sum(results)
    print(f"Individual process results: {results}")
    print(f"Total counter value is {total}")
    # Close the queue
    queue.close()
    queue.join_thread()