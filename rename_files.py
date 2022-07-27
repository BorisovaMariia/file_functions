import os
from tkinter import Tk, filedialog, simpledialog


def change_name_file(split_path, split_text):
    for path, dirs, files in os.walk(split_path): 
        os.chdir(path)
        for file in files:
            (prefix, sep, suffix) = file.rpartition(split_text)
            try:
                new = prefix + suffix
            except:
                pass
            os.rename(file, new)
root = Tk() # pointing root to Tk() to use it as Tk() in program.
root.withdraw() # Hides small tkinter window.
root.attributes('-topmost', True) # Opened windows will be active. above all windows despite of selection.

copy_path = filedialog.askdirectory(title='Choose old directory with files') # Returns opened path as str
split_text = simpledialog.askstring('Input text', 'Input split text') # Returns opened path as str

change_name_file(copy_path, split_text)