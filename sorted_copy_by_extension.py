import os
import shutil
import os.path as path
from tkinter import Tk, filedialog


def create_folders_by_extention(path_copy, destination):
    """
    path_copy - file path (str)
    destination - path for copy(str)

    Function copy files to another directory with folders of extension.
    """
    get_extensions = lambda x: os.path.splitext(x)[-1].replace('.', '').lower()
    extensions_set = set()
    for path, dirs, files in os.walk(path_copy): #get different extensions
        extensions_set.update(set(map(get_extensions, files)))
    
    for expansion in extensions_set: #create folders
        if os.path.exists(os.path.join(destination, expansion)):
            pass
        else:
            os.mkdir(expansion)

def copy_files_by_extention(path_copy, destination):
    for pathh, dirs, files in os.walk(path_copy): #copy files
        for file in files:
            extension_file = path.splitext(file)[1][1:] # file extension 
            
            if os.path.exists(os.path.join(destination, extension_file)): #if exists folder with name of extension 
                if file not in os.path.join(destination,extension_file):
                    #shutil.move(file,os.path.join(destination,extension_file)) #for move files
                    shutil.copy(os.path.join(pathh, file), os.path.join(destination,extension_file))
            else:
                create_folders_by_extention(pathh, destination)
                copy_files_by_extention(pathh, destination)


root = Tk() # pointing root to Tk() to use it as Tk() in program.
root.withdraw() # Hides small tkinter window.
root.attributes('-topmost', True) # Opened windows will be active. above all windows despite of selection.

copy_path = filedialog.askdirectory(title='Choose old directory with files') # Returns opened path as str
destination = filedialog.askdirectory(title='Choose new directory for files') # Returns opened path as str

create_folders_by_extention(copy_path, destination)
copy_files_by_extention(copy_path, destination)