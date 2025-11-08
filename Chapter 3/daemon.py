from multiprocessing import Process
import time

def background_task():
    while True:
        print("Daemon running...")
        time.sleep(1)

if __name__ == "__main__":
    p = Process(target=background_task, daemon=True)
    p.start()
    print("Main process finishing in 3 seconds...")
    time.sleep(3)
