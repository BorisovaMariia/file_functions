import os
import shutil
from tkinter import Tk, filedialog, messagebox
import distutils.dir_util

def copy_files_without_folders(path_copy, destination):
    """
    path - file path (str)

    Function copy files to another directory without folders.
    """
    for path, dirs, files in os.walk(path_copy):
        for file in files:
            source=os.path.join(path, file)
            full_destination = os.path.normpath(os.path.join(destination,os.path.basename(source)))

            try:
                shutil.copyfile(source, full_destination, follow_symlinks=True)
            except:
                pass 


root = Tk() # pointing root to Tk() to use it as Tk() in program.
root.withdraw() # Hides small tkinter window.
root.attributes('-topmost', True) # Opened windows will be active. above all windows despite of selection.

answer = messagebox.askquestion(title='Copy type', message='Do you want to copy files along with folders?')
path_for_copy = filedialog.askdirectory(title='Choose old directory with files') # Returns opened path as str
destination = filedialog.askdirectory(title='Choose new directory for files') # Returns opened path as str

if answer == 'no':
    copy_files_without_folders(path_for_copy, destination)
if answer == 'yes':
    try:
        distutils.dir_util.copy_tree(path_for_copy, destination)
    except:
        pass