import threading
import time

event = threading.Event()

def waiter():
    print(f"{threading.current_thread().name} waiting for event")
    event.wait()  # blocks until event is set
    print(f"{threading.current_thread().name} detected event!")

def setter():
    time.sleep(2)
    print("Event is set!")
    event.set()  # signal all waiting threads

t1 = threading.Thread(target=waiter, name="Waiter-1")
t2 = threading.Thread(target=waiter, name="Waiter-2")
t1.start()
t2.start()

threading.Thread(target=setter).start()

t1.join()
t2.join()
