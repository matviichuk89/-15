import tkinter as tk
root = tk.Tk()
root.title("equation")
root.geometry("340x220")
frame = tk.Frame(root)
frame.pack(pady=20)
entry1 = tk.Entry(frame, width=10)
entry1.grid(row=1, column=0, padx=5)
entry2 = tk.Entry(frame, width=10)
entry2.grid(row=1, column=1, padx=5)
entry3 = tk.Entry(frame, width=10)
entry3.grid(row=1, column=2, padx=5)
entry4 = tk.Entry(frame, width=10)
entry4.grid(row=3, column=0, padx=5)
entry5 = tk.Entry(frame, width=10)
entry5.grid(row=3, column=1, padx=5)
entry6 = tk.Entry(frame, width=10)
entry6.grid(row=3, column=2, padx=5)
Label1 = tk.Label(root, text="Результат:")
Label1.pack(pady=10)
Label2 = tk.Label(frame, text="a1")
Label2.grid(row=0, column=0, padx=5, pady=5)
Label3 = tk.Label(frame, text="b1")
Label3.grid(row=0, column=1, padx=5, pady=5)
Label4 = tk.Label(frame, text="c1")
Label4.grid(row=0, column=2, padx=5, pady=5)
Label5 = tk.Label(frame, text="a2")
Label5.grid(row=2, column=0, padx=5, pady=5)
Label6 = tk.Label(frame, text="b2")
Label6.grid(row=2, column=1, padx=5, pady=5)
Label7 = tk.Label(frame, text="c2")
Label7.grid(row=2, column=2, padx=5, pady=5)
tk.Button(frame, text="Обчислити", command=lambda: calculate()).grid(row=4, column=1, pady=10)
def calculate():
    try:
        a1 = float(entry1.get())
        b1 = float(entry2.get())
        c1 = float(entry3.get())
        a2 = float(entry4.get())
        b2 = float(entry5.get())
        c2 = float(entry6.get())
        if a1 == 0 and b1 == 0 and a2 == 0 and b2 == 0:
            if c1 == 0 and c2 == 0:
                Label1.config(text="Результат: Система має безліч розв'язків")
            else:
                Label1.config(text="Результат: Система не має розв'язків")
    
        elif c1 * b2 == c2 * b1 and a1 * b2 == a2 * b1 and a1 * c2 == a2 * c1:
            Label1.config(text="Результат: Система має безліч розв'язків")
        elif a1 * b2 == a2 * b1:
            Label1.config(text="Результат: Система не має розв'язків")
        else:
            x = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)
            y = (a1 * c2 - a2 * c1) / (a1 * b2 - a2 * b1)
            Label1.config(text=f"Результат: x = {x}, y = {y}")
    except ValueError:
        Label1.config(text="Результат: Будь ласка, введіть дійсні числа.")
root.mainloop()