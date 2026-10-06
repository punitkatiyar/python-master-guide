## Creating a Thread

```py
import threading

def welcome():
    print("Hello from thread")


t = threading.Thread(target=welcome)

t.start()
t.join()

print("Main program completed")
```

## methods list

| Method | Purpose |
|---|---|
| `Thread()` | Creates a thread |
| `start()` | Starts thread execution |
| `run()` | Contains thread's execution logic |
| `join()` | Waits for thread to finish |
| `is_alive()` | Checks whether thread is running |



## Example

```py
import threading
import time

def task(name):
    print(f"{name} started")

    time.sleep(2)

    print(f"{name} completed")


t1 = threading.Thread(target=task, args=("Task 1",))
t2 = threading.Thread(target=task, args=("Task 2",))
t3 = threading.Thread(target=task, args=("Task 3",))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("All tasks completed")
```
