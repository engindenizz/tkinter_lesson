import tkinter as tk


def calculate_bmi():
    try:
        weight = float(entry_1.get())
        height = float(entry_2.get()) / 100
        bmi = weight / (height ** 2)
        result_label.config(text=f"Your BMI is: {bmi:.1f}")
        print(result_label)
    except ValueError:
        result_label.config(text="Invalid input! Please enter numeric values.")


# screen
screen = tk.Tk()
screen.geometry("300x300")
screen.title("BMI Calculator")
screen.update_idletasks()
screen.minsize(screen.winfo_width(), screen.winfo_height())
screen.maxsize(screen.winfo_width(), screen.winfo_height())
screen.config(bg="orange")
total_columns = 3
for i in range(total_columns):
    screen.grid_columnconfigure(i, weight=1)

# label
label_1 = tk.Label(screen,
                   text="Please enter your weight",
                   bg="orange",

                   )
label_1.grid(row=0, column=0, columnspan=total_columns, padx=5, pady=5)

entry_1 = tk.Entry(screen,
                   width=20,
                   )
entry_1.grid(row=1, column=0, columnspan=total_columns, padx=5, pady=5)

label_2 = tk.Label(screen,
                   text="Please enter your height",
                   bg="orange",
                   )
label_2.grid(row=2, column=0, columnspan=total_columns, padx=5, pady=5)

entry_2 = tk.Entry(screen,
                   width=20,
                   )
entry_2.grid(row=3, column=0, columnspan=total_columns, padx=5, pady=5)
button_1 = tk.Button(screen,
                     text="Calculate",
                     borderwidth=1,
                     padx=5,
                     pady=5,
                     command=calculate_bmi,
                     bg="light green",
                     fg="black",
                     font=("Arial", 12, "bold")
                     )
button_1.grid(row=4, column=0, columnspan=total_columns, padx=5, pady=5)

result_label = tk.Label(screen,
                        text="",
                        bg="orange",
                        )
result_label.grid(row=5, column=0, columnspan=total_columns, padx=5, pady=5)
screen.mainloop()
