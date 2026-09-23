# Python GUI = Graphical User Interface

**Python has several GUI (Graphical User Interface) libraries that you can use to build desktop applications such as calculators, login systems, billing software, text editors, dashboards, and management systems.**



```
┌─────────────────────────────┐
│       Student Login         │
├─────────────────────────────┤
│ Username: [_____________]   │
│ Password: [_____________]   │
│                             │
│       [ Login ]             │
└─────────────────────────────┘
```

## A GUI application provides visual elements such as:

- Windows
- Buttons
- Text boxes
- Labels
-  Menus
- Checkboxes
- Radio buttons
- Tables
- Dialog boxes
- Images

##
- variables
- data types
- if/else
- loops
- functions
- lists
- tuples
- dictionaries
- sets
- classes & objects
- exceptions
- modules
- file handling




| Library             | Difficulty            | Best For                                    |
| ------------------- | --------------------- | ------------------------------------------- |
| **Tkinter**         | Beginner              | Simple desktop apps                         |
| **CustomTkinter**   | Beginner–Intermediate | Modern-looking Tkinter apps                 |
| **PyQt**            | Intermediate–Advanced | Professional desktop applications           |
| **PySide**          | Intermediate–Advanced | Professional/commercial applications        |
| **Kivy**            | Intermediate          | Touchscreen & cross-platform apps           |
| **wxPython**        | Intermediate          | Native-looking desktop apps                 |
| **PyGObject (GTK)** | Advanced              | Linux/GTK applications                      |
| **Dear PyGui**      | Intermediate          | Fast tools, dashboards, developer utilities |


```py
import tkinter as tk

window = tk.Tk()

label = tk.Label(
    window,
    text="Hello Python"
)

label.pack()

window.mainloop()
```
