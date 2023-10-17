from tkinter import Frame, Entry, DoubleVar, IntVar, Label, BooleanVar, Checkbutton

class Input_frame(Frame):
    def __init__(self, master, entry_bg_l, entry_bg_s, input_bg, check_bg):
        super().__init__(master)
        
        #values
        self.brigh_val = DoubleVar(value=2.0)
        self.balance_val = DoubleVar(value=0.5)
        self.illuminant_val = DoubleVar(value=0.01)
        self.min_val = DoubleVar(value=0.0) 
        self.max_val = DoubleVar(value=1.0)
        self.fraction_val = DoubleVar(value=0.05)
        self.add_val = DoubleVar(value=2.0)
        self.mul_val = DoubleVar(value=10.0)
        self.size_val = IntVar(value=320)
        self.transform_val = BooleanVar(value=False)
        self.raw_val = BooleanVar(value=False)


        #Bg
        Bg = Label(master=master,image=input_bg,bg="white")
        Bg.place(x=718,y=75)

        #Entries:

        #Bright
        Entry_1_bg = Label(master=master, image=entry_bg_l,bg="white")
        Entry_1_bg.place(x=877.5,y=89.5)
        Entry_1_l = Label(master=master,text="Brightness : ",font=("Inter", 20 * -1),bg="white")
        Entry_1_l.place(x=734.0,y=88.0)
        Entry_1 = Entry(master=master,textvariable=self.brigh_val,bd=0, bg="#D9D9D9",fg="#000716",highlightthickness=0)
        Entry_1.place(x=895.0,y=93.0,width=65.0,height=21.0)

        #Attenuation
        Entry_2_bg = Label(master=master, image=entry_bg_l,bg="white")
        Entry_2_bg.place(x=877.5,y=129.5)
        Entry_2_l = Label(master=master,text="Balance of Att :",font=("Inter", 20 * -1),bg="white")
        Entry_2_l.place(x=734.0,y=127.0)
        Entry_2 = Entry(master=master,textvariable=self.balance_val,bd=0, bg="#D9D9D9",fg="#000716",highlightthickness=0)
        Entry_2.place(x=895.0,y=133.0,width=65.0,height=21.0)

        #Illuminant
        Entry_3_bg = Label(master=master, image=entry_bg_l,bg="white")
        Entry_3_bg.place(x=877.5,y=169.5)
        Entry_3_l = Label(master=master,text="Illuminat Map :",font=("Inter", 20 * -1),bg="white")
        Entry_3_l.place(x=734.0,y=167.0)
        Entry_3 = Entry(master=master,textvariable=self.illuminant_val,bd=0, bg="#D9D9D9",fg="#000716",highlightthickness=0)
        Entry_3.place(x=895.0,y=173.0,width=65.0,height=21.0)

        #Min-Max Depth
        Entry_4mi_bg = Label(master=master, image=entry_bg_s,bg="white")
        Entry_4mi_bg.place(x=847.5,y=214.5)
        Entry_4mi_l = Label(master=master,text="Min Depth :",font=("Inter", 20 * -1),bg="white")
        Entry_4mi_l.place(x=734.0,y=212.0)
        Entry_4mi = Entry(master=master,textvariable=self.min_val,bd=0, bg="#D9D9D9",fg="#000716",highlightthickness=0)
        Entry_4mi.place(x=857.0,y=218.0,width=17.0,height=21.0)

        Entry_4ma_bg = Label(master=master, image=entry_bg_s,bg="white")
        Entry_4ma_bg.place(x=1017.5,y=214.5)
        Entry_4ma_l = Label(master=master,text="Max Depth :",font=("Inter", 20 * -1),bg="white")
        Entry_4ma_l.place(x=904.0,y=212.0)
        Entry_4ma = Entry(master=master,textvariable=self.max_val,bd=0, bg="#D9D9D9",fg="#000716",highlightthickness=0)
        Entry_4ma.place(x=1027.0,y=218.0,width=17.0,height=21.0)

        #fraction
        Entry_5_bg = Label(master=master, image=entry_bg_l,bg="white")
        Entry_5_bg.place(x=877.5,y=267.5)
        Entry_5_l = Label(master=master,text="Data Fraction :",font=("Inter", 20 * -1),bg="white")
        Entry_5_l.place(x=734.0,y=267.0)
        Entry_5 = Entry(master=master,textvariable=self.fraction_val,bd=0, bg="#D9D9D9",fg="#000716",highlightthickness=0)
        Entry_5.place(x=895.0,y=271.0,width=65.0,height=21.0)

        #add
        Entry_6_bg = Label(master=master, image=entry_bg_l,bg="white")
        Entry_6_bg.place(x=877.5,y=307.5)
        Entry_6_l = Label(master=master,text="Add. Depth:",font=("Inter", 20 * -1),bg="white")
        Entry_6_l.place(x=734.0,y=307.0)
        Entry_6 = Entry(master=master,textvariable=self.add_val,bd=0, bg="#D9D9D9",fg="#000716",highlightthickness=0)
        Entry_6.place(x=895.0,y=311.0,width=65.0,height=21.0)

        #mul
        Entry_7_bg = Label(master=master, image=entry_bg_l,bg="white")
        Entry_7_bg.place(x=877.5,y=347.5)
        Entry_7_l = Label(master=master,text="Mul. Depth:",font=("Inter", 20 * -1),bg="white")
        Entry_7_l.place(x=734.0,y=347.0)
        Entry_7 = Entry(master=master,textvariable=self.mul_val,bd=0, bg="#D9D9D9",fg="#000716",highlightthickness=0)
        Entry_7.place(x=895.0,y=351.0,width=65.0,height=21.0)
        
        #size
        Entry_8_bg = Label(master=master, image=entry_bg_l,bg="white")
        Entry_8_bg.place(x=877.5,y=387.5)
        Entry_8_l = Label(master=master,text="Size :",font=("Inter", 20 * -1),bg="white")
        Entry_8_l.place(x=734.0,y=387.0)
        Entry_8 = Entry(master=master,textvariable=self.size_val,bd=0, bg="#D9D9D9",fg="#000716",highlightthickness=0)
        Entry_8.place(x=895.0,y=391.0,width=65.0,height=21.0)

        #Check
        Transform_bg = Label(master=master,image=check_bg,bg="white")
        Transform_bg.place(x=894.0,y=440.0)
        Transfor_l = Label(master=master,text="Transform Only :",font=("Inter", 20 * -1),bg="white")
        Transfor_l.place(x=734.0,y=437.0)
        Transfor_c = Checkbutton(master=master,variable=self.transform_val,bg="#D9D9D9",onvalue=True,offvalue=False)
        Transfor_c.place(x=901.0,y=447.0,width=15.0,height=13.0)

        raw_bg = Label(master=master,image=check_bg,bg="white")
        raw_bg.place(x=1014.0,y=440.0)
        raw_l = Label(master=master,text="RAW:",font=("Inter", 20 * -1),bg="white")
        raw_l.place(x=944.0,y=437.0)
        raw_c = Checkbutton(master=master,variable=self.raw_val,bg="#D9D9D9",onvalue=True,offvalue=False)
        raw_c.place(x=1021.0,y=447.0,width=15.0,height=13.0)
    
    def submit(self):
        return self.brigh_val.get(),self.balance_val.get() ,self.illuminant_val.get(), self.min_val.get(), self.max_val.get(), self.fraction_val.get(), self.add_val.get(), self.mul_val.get(), self.size_val.get(), self.transform_val.get(), self.raw_val.get()