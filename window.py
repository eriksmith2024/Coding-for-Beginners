from tkinter import *

window = Tk()
window.title('Label Example')

# Bring window to front
window.deiconify()
window.lift()
window.focus_force()

label = Label(window, text='Hello World')
label.pack(padx=200, pady=200)

window.mainloop()
