import threading
import time

semaphore = threading.Semaphore(3)  # max 3 threads at a time

def access_resource(thread_id):
    with semaphore:
        print(f"Thread-{thread_id} is accessing resource")
        time.sleep(2)
        print(f"Thread-{thread_id} is leaving resource")

threads = []
for i in range(6):
    t = threading.Thread(target=access_resource, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
