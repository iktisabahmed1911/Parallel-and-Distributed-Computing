from multiprocessing import Process
import time

def task(name):
    print(f"{name} started")
    time.sleep(1)
    print(f"{name} finished")

if __name__ == "__main__":
    p1 = Process(target=task, args=("Process-1",))
    p2 = Process(target=task, args=("Process-2",))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
