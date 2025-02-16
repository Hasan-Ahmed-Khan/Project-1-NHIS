import tkinter as tk
def button_click(value):
    current = display.get() 
    display.delete(0, tk.END) 
    display.insert(tk.END, current + str(value)) 
def clear_display():
    display.delete(0, tk.END)
def evaluate():
    try:
        result = eval(display.get()) 
        display.delete(0, tk.END)  
        display.insert(tk.END, result)  
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
window = tk.Tk()
window.title("Python Calculator")
display = tk.Entry(window, width=25, borderwidth=5, font=('Arial', 16), justify='right')
display.grid(pady=10, row=0, column=0, columnspan=10)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('c', 4, 0), ('0', 4, 1), ('=', 4, 2), ('/', 4, 3),
]
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(window, text=text, width=9, height=1, font=('Arial', 14), command=evaluate)
    elif text == "c":
        button = tk.Button(window, text=text, width=9, height=1, font=('Arial', 14), command=clear_display)
    else:
        button = tk.Button(window, text=text, width=9, height=1, font=('Arial', 14), command=lambda value=text: button_click(value))
    button.grid(row=row, column=col)
window.mainloop()