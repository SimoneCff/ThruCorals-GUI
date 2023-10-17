from tkinter import Frame, Label, Button, StringVar, filedialog

class Dir_frame(Frame):
    def __init__(self, master, root_bg,root_button_bg):
        super().__init__(master)
        self.root_value = StringVar()

        #Set bg
        bg = Label(master=master,image=root_bg,bg="white")
        bg.place(x=20,y=10)

        #Set Text
        self.root_text = Label(master=master,text=self.root_value.get(),font=("Inter", 15 * -1),bg="#F9F9F9",width=30)
        self.root_text.place(x=78,y=19)

        #Set Button
        root_button = Button(master=master,image=root_button_bg,bg="white",command=self.update_value,bd=0)
        root_button.place(x=560,y=10)

    def update_value(self):
         folder_path_sel = filedialog.askdirectory()
         self.root_value.set(folder_path_sel)
         self.root_text.config(text=folder_path_sel)
         self.root_text.config(justify="left")
    
    def get_value(self):
        return self.root_value.get()