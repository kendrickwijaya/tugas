import tkinter as tk

def on_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("ken calculator")

entry = tk.Entry(root, width=16, font=('Arial', 20), justify='right')
entry.grid(row=0, column=0, columnspan=4)

button_layout = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]


for (text, row, col) in button_layout:
    button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 16),
                       command=lambda t=text: on_click(t) if t != '=' else calculate() if t != 'C' else clear_entry())
    button.grid(row=row, column=col)


root.mainloop()
