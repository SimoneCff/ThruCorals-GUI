from .module.MainWindow import MainWindow
from .module.Inputs import Input_frame
from .module.dir import Dir_frame
from .module.terminal import Terminal_frame
from tkinter import PhotoImage, Label, Button
from init_process import Start_process

from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def init_app():
    app = MainWindow()
    
    #Add Images
    Waves_bg = PhotoImage(file=relative_to_assets('image_1.png'))

    entry_bg_l = PhotoImage(file=relative_to_assets('entry_1.png'))
    entry_bg_s = PhotoImage(file=relative_to_assets('entry_2.png'))
    Input_bg = PhotoImage(file=relative_to_assets('input_bg.png'))
    check_bg = PhotoImage(file=relative_to_assets('check.png'))

    root_bg = PhotoImage(file=relative_to_assets('root_frame.png'))
    root_button_bg = PhotoImage(file=relative_to_assets('button_2.png'))
    start_bg = PhotoImage(file=relative_to_assets('button_1.png'))

    #Set Frames
    input_f = Input_frame(app,entry_bg_l,entry_bg_s,Input_bg,check_bg)
    dir_f = Dir_frame(app,root_bg,root_button_bg)
    term_f = Terminal_frame(app)

    #Set Image
    Waves_Label = Label(app,image=Waves_bg,bg="white")
    Waves_Label.place(x=-2.0,y=510.0)

    #Set Start Buton
    Start = Button(master=app,image=start_bg,bg="white",bd=0,command=lambda: app.start_thread(Start_process,(input_f,dir_f,term_f)))
    Start.place(x=800,y=530)

    #Start Setting Up
    input_f.pack()
    dir_f.pack()
    term_f.pack()
    
    #Start Loop
    app.mainloop()