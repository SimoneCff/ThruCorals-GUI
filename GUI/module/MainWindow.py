from tkinter import Tk
import threading
import sys

class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        #Title
        self.title("ThruCorals")
        #Window info
        self.geometry("1120x650")
        self.configure(bg="white")
        self.resizable(False, False)
       
    def start_thread(self, target, args=()):
        self.thread = threading.Thread(target=target, args=args, daemon=True)
        self.thread.start()

    def stop_thread(self):
        print("event set")
        self.thread.join()

    def destroy(self):
        super().destroy()
        sys.exit()
