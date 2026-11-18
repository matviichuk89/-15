import tkinter as tk
root = tk.Tk()
root.title("Rainbow")
root.geometry("320x260")
root.configure(bg="green")
tk.Button(root, text="Red", bg="red", command=lambda: change_color("red")).pack(pady=10)
tk.Button(root, text="Orange", bg="orange", command=lambda: change_color("orange")).pack(pady=10)
tk.Button(root, text="Yellow", bg="yellow", command=lambda: change_color("yellow")).pack(pady=10)
tk.Button(root, text="Green", bg="green", command=lambda: change_color("green")).pack(pady=10)
tk.Button(root, text="light blue", bg="light blue", command=lambda: change_color("light blue")).pack(pady=10)   
tk.Button(root, text="Blue", bg="blue", command=lambda: change_color("blue")).pack(pady=10)
tk.Button(root, text="Purple", bg="purple", command=lambda: change_color("purple")).pack(pady=10) 
def change_color(color):
    root.configure(bg=color)
    with open(r"C:\Users\Nazar\OneDrive\Desktop\report.txt", "a", encoding="utf-8") as file:
        file.write(color + "\n")
root.mainloop()