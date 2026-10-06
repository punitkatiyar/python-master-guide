## Creating a Thread

```
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
