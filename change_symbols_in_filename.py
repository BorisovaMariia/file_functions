import os
import glob
from tkinter import Tk, filedialog

def replace_space_by_underscore(path):
    """
    path - file path (str)

    Function change symbols in file name. You can change symbols.
    Example: Vik_3 -> Vik-3 
    """
    for infile in glob.glob(path):
        new = infile.replace("_", "-")
        try:
            new = new.replace(" ", "-")
        except:
            pass
        if infile == new:
            continue
        if infile != new:
            print(infile, "==> ", new)
        os.rename(infile, new)


root = Tk() # pointing root to Tk() to use it as Tk() in program.
root.withdraw() # Hides small tkinter window.

root.attributes('-topmost', True) # Opened windows will be active. above all windows despite of selection.

path_for_rename = filedialog.askdirectory() # Returns opened path as str

for path, dirs, files in os.walk(path_for_rename):
    os.chdir(path)
    replace_space_by_underscore(path)