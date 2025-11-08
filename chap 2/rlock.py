import threading
import time

lock = threading.RLock()

def nested():
    with lock:
        print(f"{threading.current_thread().name} acquired nested lock")
        time.sleep(1)

def task():
    with lock:
        print(f"{threading.current_thread().name} acquired outer lock")
        nested()
        print(f"{threading.current_thread().name} released outer lock")

t1 = threading.Thread(target=task, name="Thread-1")
t2 = threading.Thread(target=task, name="Thread-2")

t1.start()
t2.start()
t1.join()
t2.join()
    