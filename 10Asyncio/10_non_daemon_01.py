# Non daemon threads
# practical example using a non-daemon thread + threading.Event() to stop a non-daemon (default) worker thread gracefully.

import time
import threading

def player_data(stop_event):
    while not stop_event.is_set():
        print("fetching player's data")
        time.sleep(1)
    print("player's data is fetched, Worker thread (worker_non_daemon_thread) stopped gracefully!")

# Signal used to request the worker thread to stop
stop_event = threading.Event()
worker_non_daemon_thread = threading.Thread(target=player_data, args=(stop_event, ), daemon=False)
worker_non_daemon_thread.start()
# Main thread continues its work
time.sleep(5)
print("Main thread: requesting worker to stop...")
# Request the worker to stop
stop_event.set()
# Wait until the worker finishes
worker_non_daemon_thread.join()
print("Main program exited.")



