from tkinter import *
from PIL import Image, ImageTk
import os

# Create main window
window = Tk()
window.title("Image Example")

# Bring window to front
window.deiconify()
window.lift()
window.focus_force()

# --- STEP 1: Set the image filename ---
# Make sure the image is in the same folder as this script
image_filename = "python.gif"  # <-- Change to .png if needed

# --- STEP 2: Build full path to the image ---
script_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(script_dir, image_filename)

# --- STEP 3: Load and resize the image ---
# Open the image with Pillow
original_img = Image.open(img_path).convert("RGBA")

# Resize the image to make a smaller version (e.g. for button)
resized_img = original_img.resize((180, 240), Image.Resampling.LANCZOS)

# --- STEP 4: Convert Pillow images to tkinter PhotoImages ---
tk_img = ImageTk.PhotoImage(original_img)
tk_small_img = ImageTk.PhotoImage(resized_img)

# --- STEP 5: Prevent garbage collection by storing references ---
window.tk_img = tk_img
window.tk_small_img = tk_small_img

# --- STEP 6: Create widgets with the image ---

# Full image in a Label
label = Label(window, image=tk_img, bg='white')

# Smaller image in a Button
btn = Button(window, image=tk_small_img)

# Smaller image in a Text widget
txt = Text(window, width=50, height=20)
txt.image_create('1.0', image=tk_small_img)
txt.insert('1.1', ' Python Fun')

# Smaller image in a Canvas, with a magenta line
can = Canvas(window, width=200, height=250, bg='white')
can.create_image((100, 120), image=tk_small_img)
can.create_line(0, 0, 200, 250, width=5, fill='magenta')

# --- STEP 7: Layout the widgets ---
label.pack(side=TOP, pady=10)
btn.pack(side=LEFT, padx=10)
txt.pack(side=LEFT, padx=10)
can.pack(side=LEFT, padx=10)

# --- STEP 8: Run the GUI ---
window.mainloop()
