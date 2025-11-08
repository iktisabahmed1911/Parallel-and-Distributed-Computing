# Threading vs Multiprocessing Calculator

## Introduction
This project demonstrates a simple calculator implemented in Python using **both Multithreading and Multiprocessing**. The goal is to illustrate how Python handles parallel execution using threads and processes, highlighting differences in memory usage, speed, communication, and safety. By performing basic arithmetic operations—addition, subtraction, multiplication, and division—simultaneously, this project provides a practical example of parallel computing concepts for real-world applications.

---

## Summary
In the **Multithreading** version, multiple threads run concurrently within the same process. All threads share the same memory space, allowing them to directly append results to a shared list. This makes communication easy and thread creation lightweight. However, sharing memory can lead to race conditions if multiple threads access or modify the same data simultaneously. Multithreading is generally well-suited for **I/O-bound tasks**, such as reading/writing files, network operations, or GUI updates, where the CPU is often waiting for external input.

In contrast, the **Multiprocessing** version uses separate processes for each operation. Each process has its own independent memory space, which ensures data safety and prevents conflicts. Processes are heavier to create and consume more system resources, but they provide true parallel execution across multiple CPU cores. Communication between processes requires mechanisms like **Queue** or **Pipe**, making it slightly more complex. Multiprocessing is ideal for **CPU-bound tasks**, such as heavy calculations or data processing, where maximizing CPU usage is critical.

---

##  Comparison
While both threads and processes allow tasks to run concurrently, they differ fundamentally in how they share resources and achieve parallelism. **Threads** operate within a single process and share memory, making them lightweight and efficient for tasks that require frequent access to shared data. However, this shared memory comes with the risk of data races, requiring synchronization tools like Locks or Semaphores. **Processes**, on the other hand, operate independently with separate memory, providing safer execution for CPU-intensive workloads. Though process creation is heavier and communication is more complex, the isolation ensures that one process cannot accidentally interfere with another. Choosing between threads and processes depends largely on the type of task: I/O-bound tasks benefit from threads, while CPU-bound tasks benefit from processes.

---

## Conclusion
This calculator project demonstrates the practical differences between multithreading and multiprocessing in Python. Threads provide fast, lightweight parallelism with shared memory, ideal for I/O-bound tasks, while processes provide independent, safe parallel execution for CPU-bound tasks. By comparing both approaches in a simple calculator application, we can understand memory usage, execution speed, communication methods, and safety considerations, helping developers choose the right parallelization strategy for different real-world scenarios.

