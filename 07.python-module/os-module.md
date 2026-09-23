# OS Module

**The Python os module does not have one fixed number of functions, because the available functions and constants can vary by Python version and operating system (Windows, Linux, macOS).**

**For modern Python 3.x, os provides well over 200 public names when you include functions, constants, classes, and platform-specific features. However, if you're learning Python, it's more useful to organize its functionality into categories rather than memorize a number**

| Category                        | Common functions/features                                        |
| ------------------------------- | ---------------------------------------------------------------- |
| 📁 File & directory operations  | `mkdir()`, `makedirs()`, `rmdir()`, `removedirs()`, `listdir()`  |
| 📄 File operations              | `remove()`, `unlink()`, `rename()`, `replace()`                  |
| 📂 Path operations              | `os.path.join()`, `exists()`, `isfile()`, `isdir()`, `getsize()` |
| 💻 Operating-system information | `name`, `getlogin()`, `getpid()`, `getppid()`                    |
| 🔧 Environment variables        | `environ`, `getenv()`, `putenv()`, `unsetenv()`                  |
| ⚙️ Process management           | `system()`, `popen()`, `exec*()`, `spawn*()`                     |
| 🔐 File permissions             | `chmod()`, `stat()`, `access()`                                  |
| 📊 File/system information      | `stat()`, `lstat()`, `statvfs()`                                 |
| ⏱️ Process timing               | `times()`                                                        |
| 🔤 OS-specific constants        | `sep`, `linesep`, `pathsep`, `curdir`, `pardir`                  |
| 🧭 Working directory            | `getcwd()`, `chdir()`, `fchdir()`                                |
| 🖥️ Terminal/system features    | `isatty()`, `get_terminal_size()`                                |
| 🔗 File descriptors             | `open()`, `close()`, `read()`, `write()`, `dup()`                |

<hr>

> **os also contains the os.path submodule, which provides many path-related functions:**

```py
import os

print(os.getcwd())
print(os.listdir())
print(os.path.exists("data.txt"))
print(os.path.isfile("data.txt"))
print(os.path.isdir("my_folder"))
print(os.path.join("folder", "file.txt"))

```
