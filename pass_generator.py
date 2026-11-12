#password generator

from tkinter import *
import numpy as np
import time as t

# list of words and chars
words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
char = ['@', '!', '#', '_']

def password():
    
    nums = np.random.randint(1, 10, 2)
    a = "".join(map(str, nums))


    c1 = np.random.choice(char)
    c2 = np.random.choice(char)
    c3 = np.random.choice(char)

    w1 = np.random.choice(words)
    w2 = np.random.choice(words)
    w4 = np.random.choice(words)

    text = name_entry.get()  
    for e in text[0:3]:
        ascii_val = ord(e)
    pw = c1 + str(ascii_val) + c2 + w1 + c3 + w4 + str(a) + str(a) + w2
    password_label.config(text=pw)  


# GUI setup
root = Tk()
root.title("SECURA")
root.geometry("400x400")

Label(root, text="Enter your name:").pack(pady=5)
name_entry = Entry(root)
name_entry.pack(pady=5)

Button(root, text="Generate Password", command=password).pack(pady=10)

password_label = Label(root, text="", font=("Arial", 14), fg="black")
password_label.pack(pady=10)

root.mainloop()