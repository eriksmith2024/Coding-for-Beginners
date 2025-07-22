#print('Coding for beginners in easy steps)

# CODE WITH MISSING CLOSING QOUTE MARK FOR ABOVE - ERROR BELOW DETAILS LINE 1 & undetermined string literal
# /usr/local/bin/python3 "/Users/erikjamessmith/Documents/Coding Books/Coding for Beginners/debugging.py"                     
# erikjamessmith@Eriks-MacBook-Air Coding for Beginners % /usr/local/bin/python3 "/Users/erikjamessmith/Documents/Coding Books
# /Coding for Beginners/debugging.py"
#   File "/Users/erikjamessmith/Documents/Coding Books/Coding for Beginners/debugging.py", line 1
#     print('Coding for beginners in easy steps)
#           ^
# SyntaxError: unterminated string literal (detected at line 1)
# erikjamessmith@Eriks-MacBook-Air Coding for Beginners % 


# title = 'Coding for beginners in easy steps'
# print(titel)

# FOR ABOVE LINES ERROR - LINE NUMBER IS IDENTIFIED & ISSUE UNIDENTIFIED titel AND SUGGESTED DID YOU MEAN TITLE
# /usr/local/bin/python3 "/Users/erikjamessmith/Documents/Coding Books/Coding for Beginners/debugging.py"
# erikjamessmith@Eriks-MacBook-Air Coding for Beginners % /usr/local/bin/python3 "/Users/erikjamessmith/Documents/Coding Books/Coding for Begin
# ners/debugging.py"
# Traceback (most recent call last):
#   File "/Users/erikjamessmith/Documents/Coding Books/Coding for Beginners/debugging.py", line 15, in <module>
#     print(titel)
#           ^^^^^
# NameError: name 'titel' is not defined. Did you mean: 'title'?
# erikjamessmith@Eriks-MacBook-Air Coding for Beginners % 

num = 3
print( 'Result' , num * 8 + 4) # does not shgow an error and gives 28 with wrong precedence i.e. to multiply 3 * 8 first then adds 4


num = 3
print( 'Result' , num * (8 + 4))  # to get 36 i.e. to multiply the variable 3 by 12 having alrady added the 8 + 4  you need brackets around the 8 + 4 telling to do this part of calc first
