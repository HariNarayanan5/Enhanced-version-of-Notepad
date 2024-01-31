import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, font, colorchooser
import datetime

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            text_area.delete('1.0', tk.END)
            text_area.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_area.get('1.0', tk.END))

def about():
    messagebox.showinfo("About", "Enhanced Notepad Application\nCreated using Python and Tkinter")

def word_count():
    words = text_area.get('1.0', tk.END).split()
    messagebox.showinfo("Word Count", f"Total words: {len(words)}")

def change_font():
    font_tuple = font.families()
    font_name = font_family.get()
    font_size = font_size_var.get()
    text_area.config(font=(font_name, font_size))

def change_text_color():
    color = colorchooser.askcolor(title="Select Text Color")
    if color[1]:
        text_area.config(fg=color[1])

def find_text():
    find_str = simpledialog.askstring("Find", "Enter text to find:")
    if find_str:
        start_pos = '1.0'
        while True:
            start_pos = text_area.search(find_str, start_pos, stopindex=tk.END)
            if not start_pos:
                break
            end_pos = f"{start_pos}+{len(find_str)}c"
            text_area.tag_add('found', start_pos, end_pos)
            start_pos = end_pos
        text_area.tag_config('found', background='yellow')

def replace_text():
    find_str = simpledialog.askstring("Find", "Enter text to find:")
    replace_str = simpledialog.askstring("Replace", f"Replace '{find_str}' with:")
    if find_str and replace_str:
        start_pos = '1.0'
        while True:
            start_pos = text_area.search(find_str, start_pos, stopindex=tk.END)
            if not start_pos:
                break
            end_pos = f"{start_pos}+{len(find_str)}c"
            text_area.delete(start_pos, end_pos)
            text_area.insert(start_pos, replace_str)
            start_pos = f"{start_pos}+{len(replace_str)}c"

def insert_date_time():
    now = datetime.datetime.now()
    text_area.insert(tk.END, now.strftime("%Y-%m-%d %H:%M:%S"))

root = tk.Tk()
root.title("Full-Featured Notepad")

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

edit_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=lambda: text_area.event_generate("<<Cut>>"))
edit_menu.add_command(label="Copy", command=lambda: text_area.event_generate("<<Copy>>"))
edit_menu.add_command(label="Paste", command=lambda: text_area.event_generate("<<Paste>>"))
edit_menu.add_separator()
edit_menu.add_command(label="Select All", command=lambda: text_area.tag_add("sel", "1.0", "end"))

view_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="View", menu=view_menu)
view_menu.add_command(label="Word Count", command=word_count)
view_menu.add_command(label="Change Font", command=change_font)
view_menu.add_command(label="Change Text Color", command=change_text_color)
view_menu.add_command(label="Find", command=find_text)
view_menu.add_command(label="Replace", command=replace_text)

tools_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="Tools", menu=tools_menu)
tools_menu.add_command(label="Insert Date/Time", command=insert_date_time)

help_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

text_area = scrolledtext.ScrolledText(root, wrap='word', undo=True)
text_area.pack(expand=True, fill='both')

font_family = tk.StringVar()
font_family.set("Arial")
font_size_var = tk.IntVar()
font_size_var.set(12)

root.mainloop()
import tkinter as tk
import webbrowser

def open_url():
    url = entry.get()
    webbrowser.open_new(url)

root = tk.Tk()
root.title("Soldier Browser")

label = tk.Label(root, text="Enter URL:")
label.pack()

entry = tk.Entry(root, width=50)
entry.pack()

button = tk.Button(root, text="Open", command=open_url)
button.pack()

root.mainloop()
