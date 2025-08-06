from tkinter import *

window = Tk()
window.title( 'Image Example')

img = PhotoImage( file = 'python.gif')

label = Label( window, image = img, bg ='magenta')