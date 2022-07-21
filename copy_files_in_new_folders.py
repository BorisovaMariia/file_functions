import os
import shutil
from tkinter import Tk, filedialog

root = Tk()
root.withdraw() # Hides small tkinter window.

root.attributes('-topmost', True) # Opened windows will be active. above all windows despite of selection.

file_with_names = filedialog.askopenfilename(title='Choose file with folders list - txt, encoding ANSI') # Returns opened file
path_for_rename = filedialog.askdirectory(title='Choose directory for create folders') # Returns opened path as str
os.chdir(path_for_rename)

with open (file_with_names, 'rt') as names:
    for name in names:
        try:
            os.mkdir(name.replace("\n", ""))
        except:
            print('Folder already exist')

names_dir_and_file = filedialog.askopenfilename(title='Choose file with folders and files lists - txt, encoding ANSI') # Returns opened file
source = filedialog.askdirectory(title='Choose old directory with files') # Returns opened path as str

with open (names_dir_and_file,'rt') as names:
    for name in names:
        name = name.replace("\t", " ")
        name = name.replace("\n", "")

        folder_and_file = name.split()
        file = folder_and_file.pop(-1)
        if len(folder_and_file) == 2:
            folder_and_file = [folder_and_file[0] + ' ' + folder_and_file[1]]
        
        sor = os.path.join(source, file) #path for copy file
        destin = os.path.join(path_for_rename, str(*folder_and_file))

        os.chdir(path_for_rename)
        shutil.copy(sor, destin, follow_symlinks=True)
        print(folder_and_file, '<-', file)
        files = os.listdir(destin)
