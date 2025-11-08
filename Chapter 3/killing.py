from multiprocessing import Process
import time

def task():
    for i in range(5):
        print(f"Working {i}")
        time.sleep(1)

if __name__ == "__main__":
    p = Process(target=task)
    p.start()
    time.sleep(2)  # Let it run for 2 seconds
    p.terminate()  # Kill process
    print("Process terminated")
