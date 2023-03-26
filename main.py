from tkinter import *
from tkinter import filedialog, messagebox, simpledialog

def open_file(event=None):
    try:
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as f:
                text.delete(1.0, END)
                text.insert(1.0, f.read())
    except Exception as e:
        messagebox.showerror("Error", str(e))

def save_file(event=None):
    try:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, "w") as f:
                f.write(text.get(1.0, END))
    except Exception as e:
        messagebox.showerror("Error", str(e))

def undo():
    try:
        text.edit_undo()
    except Exception as e:
        pass

def redo():
    try:
        text.edit_redo()
    except Exception as e:
        pass

def cut():
    try:
        text.event_generate("<<Cut>>")
    except Exception as e:
        pass

def copy():
    try:
        text.event_generate("<<Copy>>")
    except Exception as e:
        pass

def paste():
    try:
        text.event_generate("<<Paste>>")
    except Exception as e:
        pass

def find():
    try:
        search_str = simpledialog.askstring("Find", "Enter text to search:")
        if search_str:
            idx = text.search(search_str, "1.0", END)
            if idx:
                text.tag_remove("search", "1.0", END)
                while idx:
                    end_idx = f"{idx}+{len(search_str)}c"
                    text.tag_add("search", idx, end_idx)
                    idx = text.search(search_str, end_idx, END)
                text.tag_config("search", background="yellow")
                text.focus_set()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def replace():
    try:
        search_str = simpledialog.askstring("Replace", "Enter text to search:")
        if search_str:
            replace_str = simpledialog.askstring("Replace", "Enter replacement text:")
            if replace_str:
                idx = text.search(search_str, "1.0", END)
                if idx:
                    text.tag_remove("search", "1.0", END)
                    while idx:
                        end_idx = f"{idx}+{len(search_str)}c"
                        text.delete(idx, end_idx)
                        text.insert(idx, replace_str)
                        idx = text.search(search_str, END, nocase=1)
                    text.focus_set()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def select_all(event=None):
    text.tag_add(SEL, "1.0", END)
    text.mark_set(INSERT, "1.0")
    text.see(INSERT)
    return 'break'

def word_count():
    words = text.get("1.0", END).split()
    num_words = len(words)
    messagebox.showinfo("Word Count", f"The document contains {num_words} words.")

def set_font(font_name):
    text.configure(font=(font_name, 12))

def create_toolbar(parent):
    toolbar = Frame(parent, bd=1, relief=RIDGE)
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

    font_var = StringVar(value="Courier New")
    font_menu = OptionMenu(toolbar, font_var, "Courier New", "Arial", "Times New Roman", command=set_font)
    font_menu.pack(side=RIGHT, padx=2, pady=2)

    return toolbar

def create_menu_item(menu, label, command, accelerator=None):
    menu.add_command(label=label, command=command, accelerator=accelerator)
    if accelerator:
        root.bind(accelerator, command)

root = Tk()
root.title("Text Editor")
root.geometry("800x600")

# Create a menu bar
menu_bar = Menu(root)
root.config(menu=menu_bar)

# Create a "File" menu with "Open" and "Save" options
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
create_menu_item(file_menu, "Open", open_file, "Ctrl+O")
create_menu_item(file_menu, "Save", save_file, "Ctrl+S")

# Create an "Edit" menu with "Undo", "Redo", "Cut", "Copy", "Paste", "Select All" options
edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
create_menu_item(edit_menu, "Undo", undo, "Ctrl+Z")
create_menu_item(edit_menu, "Redo", redo, "Ctrl+Y")
edit_menu.add_separator()
create_menu_item(edit_menu, "Cut", cut, "Ctrl+X")
create_menu_item(edit_menu, "Copy", copy, "Ctrl+C")
create_menu_item(edit_menu, "Paste", paste, "Ctrl+V")
create_menu_item(edit_menu, "Select All", select_all, "Ctrl+A")

# Create a "Search" menu with "Find" and "Replace" options
search_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Search", menu=search_menu)
create_menu_item(search_menu, "Find", find, "Ctrl+F")
create_menu_item(search_menu, "Replace", replace, "Ctrl+R")

# Create a "Tools" menu with "Word Count" option
tools_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Tools", menu=tools_menu)
create_menu_item(tools_menu, "Word Count", word_count)

# Create a toolbar with buttons and font selection
create_toolbar(root)

# Create a text editor with font selection and word wrapping
text = Text(root, wrap=WORD, font=("Courier New", 12))
text.pack(fill=BOTH, expand=1)

# Keybindings
root.bind("<Control-s>", save_file)
root.bind("<Control-o>", open_file)
root.bind("<Control-z>", undo)
root.bind("<Control-y>", redo)
root.bind("<Control-x>", cut)
root.bind("<Control-c>", copy)
root.bind("<Control-v>", paste)
root.bind("<Control-a>", select_all)
root.bind("<Control-f>", find)
root.bind("<Control-r>", replace)

# Give focus to the text widget
text.focus_set()

# Run the main event loop
root.mainloop()
