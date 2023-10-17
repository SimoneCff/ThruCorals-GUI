from tkinter import Frame,Label, Text, END,Scrollbar

class Terminal_frame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master
        self.text_widget = Text(master=self.master, bg="#B8B8B8",font=("Inter", 15 * -1))
        self.text_widget.place(x=20, y=75, height=435, width=650)

        self.scroll_y = Scrollbar(self.text_widget, orient="vertical")
        self.text_widget.config(yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side="right", fill="y")

    def See_Transf(self, text):
        self.text_widget.insert(END, text)
        self.text_widget.update()

    def Clear(self):
        self.text_widget.delete("1.0",END)
        self.text_widget.update()
 

    def close(self):
        self.destroy()