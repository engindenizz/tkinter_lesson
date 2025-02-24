import tkinter
#screen
window = tkinter.Tk()
window.title("Tkinter Project")
window.minsize(600, 600)
FONT = ("Arial", 10, "bold")
def click_button():
    input_entry = my_entry.get()
    print(input_entry)
    my_entry.delete(0, "end"),
#label
my_label = tkinter.Label(
   text="This is my label",
   font=FONT,)
#button
my_button = tkinter.Button(
    text="Click me",
    font=FONT,
    command=click_button,

)
#entry
my_entry = tkinter.Entry(
    width=20,

)

my_label.pack()
my_button.pack()
my_entry.pack()

window.mainloop()