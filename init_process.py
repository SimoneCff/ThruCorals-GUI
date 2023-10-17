from __future__ import absolute_import, division, print_function
import os
from tkinter import messagebox, filedialog
from SeaThru.transform import run
from CNN.valuate import Smart_sorting
import tempfile
import zipfile

def create_zip(dir):
    print(dir)

    zip_name = filedialog.asksaveasfilename(
        defaultextension=".zip",
        filetypes=[("File zip", "*.zip")]
    )

    with zipfile.ZipFile(zip_name, "w") as zip_file:
        for root, dirs, files in os.walk(dir):
            for filename in files:
                file_path = os.path.join(root, filename)
                zip_file.write(filename=file_path)

def get_image_list(path):
    image_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".gif"}
    image_list = []

    for foldername, subfolders, filenames in os.walk(path):
        for filename in filenames:
            extension = os.path.splitext(filename)[-1].lower()
            if extension in image_extensions:
                image_path = os.path.join(foldername, filename)
                image_list.append(image_path)

    return image_list


#Start Process
def Start_process(input,dir,terminal):
    terminal.Clear()
    temp_dir = tempfile.mkdtemp()

    dir_v = dir.get_value()
    bright, balance, illum, min, max, fract, add, mul, size, transf, raw = input.submit()
    
    terminal.See_Transf("<TERMINAL> Inizio Processo... \n")
    
    #Check dir exists
    if dir_v == "":
        messagebox.showerror("Process Error"," <Error> : Folder not selected")
        return

    #Check dir exists
    if not os.listdir(dir_v):
        messagebox.showerror("Process Error"," <Error> : Input Folder not found")
        return
    
    image_l = get_image_list(dir_v)

    #Check images inside
    if image_l is None or len(image_l) == 0:
        messagebox.showerror("Process Error","<ERROR> : No Images Found in the folder")
        return

    #Start Loop Transform
    for element in image_l:
        terminal.See_Transf("<SEATHRU> Inizio Trasformazione Immagine : "+os.path.basename(element)+" ")
        try:
            run(element,"SeaThru/models/mono+stereo_1024x320",bright, balance, illum, min, max, fract, add, mul, size, raw,temp_dir)
            terminal.See_Transf("DONE \n")
        except:
            terminal.See_Transf("ERROR \n")

    terminal.See_Transf("<SEATHRU> Processo Terminato Corretamente \n")

    if not transf:
        terminal.See_Transf("<CNN> Inizio Processo Classificazione \n")
        file_list = get_image_list(temp_dir)
        for element in file_list:
            terminal.See_Transf("<CNN> Classificazione Immagine : "+os.path.basename(element)+" ")
            label = Smart_sorting(temp_dir,element)
            terminal.See_Transf("Label : "+label+"\n")
            
    terminal.See_Transf("<CNN> Processo Classificazione Terminato Corretamente \n")
    create_zip(temp_dir)
    messagebox.showinfo("Proccess Done","All Done!, Check Output Folder")