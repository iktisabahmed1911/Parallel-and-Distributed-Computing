# multiprocessing_calculator.py
from multiprocessing import Process, Queue
import time

def calculate(operation, a, b, q):
    time.sleep(0.5)
    if operation == "add":
        res = a + b
    elif operation == "sub":
        res = a - b
    elif operation == "mul":
        res = a * b
    elif operation == "div":
        res = a / b
    
    q.put(f"{operation.upper()}: {a} & {b} = {res}")

if __name__ == "__main__":
    q = Queue()

    p1 = Process(target=calculate, args=("add", 10, 5, q))
    p2 = Process(target=calculate, args=("sub", 10, 5, q))
    p3 = Process(target=calculate, args=("mul", 10, 5, q))
    p4 = Process(target=calculate, args=("div", 10, 5, q))

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()

    print("\nResults from all processes:")
    while not q.empty():
        print(q.get())
