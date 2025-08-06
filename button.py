from tkinter import *
window = Tk()
window.title( 'Button example ')

# Bring window to front
window.deiconify()
window.lift()
window.focus_force()

btn_end = Button( window, text = 'Close', command =exit)

def tog():
    if window.cget('bg') == 'magenta':
        window.configure( bg ='lightgray')
    else:
        window.configure( bg = 'magenta')


btn_tog = Button( window, text = 'Switch', command=tog)

btn_tog.pack( padx = 120, pady = 20 )
btn_end.pack(padx = 120, pady = 20 )

window.mainloop()