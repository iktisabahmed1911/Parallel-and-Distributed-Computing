import threading
import time

barrier = threading.Barrier(3)

def task(n):
    print(f"Thread-{n} waiting at barrier")
    time.sleep(n)  # simulate work
    barrier.wait()  # wait until all threads reach
    print(f"Thread-{n} passed barrier")

threads = []
for i in range(1, 4):
    t = threading.Thread(target=task, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
