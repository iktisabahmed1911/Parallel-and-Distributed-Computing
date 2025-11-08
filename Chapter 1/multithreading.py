# threading_calculator.py
import threading
import time

results = []   # shared memory

def add(a, b):
    time.sleep(0.5)
    res = a + b
    results.append(f"ADD: {a} + {b} = {res}")
    print(results[-1])

def sub(a, b):
    time.sleep(0.5)
    res = a - b
    results.append(f"SUB: {a} - {b} = {res}")
    print(results[-1])

def mul(a, b):
    time.sleep(0.5)
    res = a * b
    results.append(f"MUL: {a} * {b} = {res}")
    print(results[-1])

def div(a, b):
    time.sleep(0.5)
    res = a / b
    results.append(f"DIV: {a} / {b} = {res}")
    print(results[-1])

# making threads (users doing parallel calculations)
t1 = threading.Thread(target=add, args=(10, 5))
t2 = threading.Thread(target=sub, args=(10, 5))
t3 = threading.Thread(target=mul, args=(10, 5))
t4 = threading.Thread(target=div, args=(10, 5))

# start all
t1.start()
t2.start()
t3.start()
t4.start()

# wait all threads finish
t1.join()
t2.join()
t3.join()
t4.join()

print("\nFinal Shared Result List:")
print(results)


