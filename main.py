from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import tkinter
import random
import string

# Assigning variable values
chars = " " + string.ascii_letters + string.digits + string.punctuation
chars = list(chars)
key = chars.copy()
random.shuffle(chars)

# Function to select all using ctrl + a
def msg_select_all(event):
    msg_box.tag_add("sel", "1.0", "end-1c")
    return "break"

def crypt_select_all(event):
    crypted_box.tag_add("sel", "1.0", "end-1c")
    return "break"

# Encryption
def encryption():
    global plain_text, cipher_text, decrypted_once
    decrypted_once = False  # Reset the decryption flag
    plain_text = msg_box.get(1.0, tkinter.END).strip()  # Get the current text from msg_box
    cipher_text = ""
    crypted_box.config(state="normal")
    crypted_box.delete(1.0, tkinter.END)
    for letter in plain_text:
        index = chars.index(letter)
        cipher_text += key[index]
    crypted_box.insert(tkinter.END, cipher_text)
    crypted_box.config(state="disabled")

# Decryption
def decryption():
    global plain_text, cipher_text, decrypted_once
    if not decrypted_once:
        cipher_text = crypted_box.get(1.0, tkinter.END).strip()  # Get the current text from crypted_box
        plain_text = ""
        crypted_box.config(state="normal")
        crypted_box.delete(1.0, tkinter.END)
        for letter in cipher_text:
            index = key.index(letter)
            plain_text += chars[index]
        crypted_box.insert(tkinter.END, plain_text)
        crypted_box.config(state="disabled")
        decrypted_once = True  # Set the decryption flag

# Paste event handler
def paste(event, text_widget):
    try:
        text_widget.delete(tkinter.SEL_FIRST, tkinter.SEL_LAST)
        text_widget.insert(tkinter.SEL_FIRST, root.clipboard_get())
    except tkinter.TclError:
        pass  # clipboard is empty

# Reshuffle
def reshuffle():
    random.shuffle(chars)

# Window Creation
root = Tk()

# Window properties
root.geometry('552x316')
root.resizable(False, False)
root.title("Encryption and Decryption")

# Warning Message
def warning():
    messagebox.askquestion("Warning", "Shuffling will reset the character list. Do you want to continue?")

# Successful message
def success_msg():
    messagebox.showinfo("Reshuffling successful", "Character list reshuffled")

# Label for messages
message_label = Label(root, text="Enter the message:")
message_label.place(x=1, y=5)

# Textbox for messages
msg_box = scrolledtext.ScrolledText(root, wrap=tkinter.WORD, width=60, height=5)
msg_box.place(x=2, y=29, width=550)
msg_box.bind("<Control-a>", msg_select_all)
msg_box.bind("<Control-v>", lambda event: paste(event, msg_box))

# Input for messages
plain_text = msg_box.get(1.0, tkinter.END)
cipher_text = ""
decrypted_once = False  # Flag to track whether decryption has occurred

# Label for encryption/decryption
crypted_label = Label(root, text="Encrypted/Decrypted message:")
crypted_label.place(x=1, y=125)

# Textbox for encryption/decryption
crypted_box = scrolledtext.ScrolledText(root, wrap=tkinter.WORD, width=60, height=5)
crypted_box.place(x=2, y=149, width=550)
crypted_box.config(state="disabled")
crypted_box.bind("<Control-a>", crypt_select_all)
crypted_box.bind("<Control-v>", lambda event: paste(event, crypted_box))

# Buttons
encrypt_button = Button(root, text='Encrypt', command=encryption)
encrypt_button.place(x=2, y=250, width=150, height=60)

decrypt_button = Button(root, text='Decrypt', command=decryption)
decrypt_button.place(x=200, y=250, width=150, height=60)

shuffle_button = Button(root, text='Shuffle', command=lambda: [warning(), reshuffle(), success_msg()])
shuffle_button.place(x=400, y=250, width=150, height=60)

root.mainloop()