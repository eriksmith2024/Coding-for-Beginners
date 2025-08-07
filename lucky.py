import os, sys
from tkinter import *
from random import sample

# Resource path for PyInstaller compatibility
def resource_path(relative_path):
    absolute_path = os.path.abspath(__file__)
    root_path = os.path.dirname(absolute_path)
    base_path = getattr(sys, '_MEIPASS', root_path)
    return os.path.join(base_path, relative_path)

# Window setup
window = Tk()
img = PhotoImage(file=resource_path("lotto.gif"))  # ✅ Assign image to 'img'

# Widgets
imgLbl = Label(window, image=img)
label1 = Label(window, relief='groove', width=2)
label2 = Label(window, relief='groove', width=2)
label3 = Label(window, relief='groove', width=2)
label4 = Label(window, relief='groove', width=2)
label5 = Label(window, relief='groove', width=2)
label6 = Label(window, relief='groove', width=2)
getBtn = Button(window)
resBtn = Button(window)

# Geometry
imgLbl.grid(row=1, column=1, rowspan=2)
label1.grid(row=1, column=2, padx=10)
label2.grid(row=1, column=3, padx=10)
label3.grid(row=1, column=4, padx=10)
label4.grid(row=1, column=5, padx=10)
label5.grid(row=1, column=6, padx=10)
label6.grid(row=1, column=7, padx=(10, 20))
getBtn.grid(row=2, column=2, columnspan=4)
resBtn.grid(row=2, column=6, columnspan=2)

# Static properties
window.title('Lotto Number Picker')
window.resizable(0, 0)
getBtn.configure(text='Get my lucky numbers')
resBtn.configure(text='Reset')

# Initial values
for label in [label1, label2, label3, label4, label5, label6]:
    label.configure(text='...')
resBtn.configure(state=DISABLED)

# Dynamic functions
def pick():
    nums = sample(range(1, 60), 6)
    label1.configure(text=nums[0])
    label2.configure(text=nums[1])
    label3.configure(text=nums[2])
    label4.configure(text=nums[3])
    label5.configure(text=nums[4])
    label6.configure(text=nums[5])
    getBtn.configure(state=DISABLED)
    resBtn.configure(state=NORMAL)

def reset():
    for label in [label1, label2, label3, label4, label5, label6]:
        label.configure(text='...')
    getBtn.configure(state=NORMAL)
    resBtn.configure(state=DISABLED)  # ✅ fix capitalisation bug (was STATE)

getBtn.configure(command=pick)
resBtn.configure(command=reset)

# Launch app
window.mainloop()