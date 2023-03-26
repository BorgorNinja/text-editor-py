from tkinter import *
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, "r") as f:
            text.delete(1.0, END)
            text.insert(1.0, f.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "w") as f:
            f.write(text.get(1.0, END))

def cut():
    text.event_generate("<<Cut>>")

def copy():
    text.event_generate("<<Copy>>")

def paste():
    text.event_generate("<<Paste>>")

def set_font(font_name):
    text.configure(font=(font_name, 12))

root = Tk()
root.title("Text Editor")
root.geometry("800x600")

# Create a menu bar
menu_bar = Menu(root)
root.config(menu=menu_bar)

# Create a "File" menu with "Open" and "Save" options
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", accelerator="Ctrl+O", command=open_file)
file_menu.add_command(label="Save", accelerator="Ctrl+S", command=save_file)

# Create a "Edit" menu with "Cut", "Copy", and "Paste" options
edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", accelerator="Ctrl+X", command=cut)
edit_menu.add_command(label="Copy", accelerator="Ctrl+C", command=copy)
edit_menu.add_command(label="Paste", accelerator="Ctrl+V", command=paste)

# Create a toolbar with "Open", "Save", "Cut", "Copy", and "Paste" buttons
toolbar = Frame(root, bd=1, relief=RIDGE)
toolbar.pack(side=TOP, fill=X)

open_button = Button(toolbar, text="Open", command=open_file)
open_button.pack(side=LEFT, padx=2, pady=2)

save_button = Button(toolbar, text="Save", command=save_file)
save_button.pack(side=LEFT, padx=2, pady=2)

cut_button = Button(toolbar, text="Cut", command=cut)
cut_button.pack(side=LEFT, padx=2, pady=2)

copy_button = Button(toolbar, text="Copy", command=copy)
copy_button.pack(side=LEFT, padx=2, pady=2)

paste_button = Button(toolbar, text="Paste", command=paste)
paste_button.pack(side=LEFT, padx=2, pady=2)

# Create a text editor with font selection and word wrapping
text = Text(root, wrap=WORD, font=("Courier New", 12))
text.pack(fill=BOTH, expand=1)

font_var = StringVar(value="Courier New")
font_menu = OptionMenu(toolbar, font_var, "Courier New", "Arial", "Times New Roman", command=set_font)
font_menu.pack(side=RIGHT, padx=2, pady=2)

#keybinds section (which doesn't seem to work)
text.bind("<Control-s>", save_file)
text.bind("<Control-o>", open_file)
#give focus to the text widget
text.focus_set()

# Define functions for menu and toolbar option
root.mainloop()


