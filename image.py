from tkinter import *

window = Tk()
window.title( 'Image Example')

img = PhotoImage( file = 'python.gif')

label = Label( window, image = img, bg ='magenta')

small_img = PhotoImage.subsample( img , x = 2, y = 2)

btn = Button( window, image = small_img )

txt = Text( window, width = 25, height = 7 )
txt.image_create('1.0', image = small_img )
txt.insert('1.1','Python Fun')