import tkinter as tk

pencere = tk.Tk()

# Düğmeleri oluşturuyoruz
düğme1 = tk.Button(pencere, text="Düğme 1")
düğme2 = tk.Button(pencere, text="Düğme 2")
düğme3 = tk.Button(pencere, text="Düğme 3")

# Düğmeleri ızgaraya yerleştiriyoruz
düğme1.grid(row=0, column=0)
düğme2.grid(row=1, column=1)
düğme3.grid(row=2, column=2)

pencere.mainloop()
