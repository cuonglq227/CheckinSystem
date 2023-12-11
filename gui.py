import tkinter.filedialog as filedialog
import os
from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
from PIL import ImageTk, Image

class GUI():
    def __init__(self):
        self.root = Tk()
        self.frame1 = Frame(self.root)
        self.frame11 = Frame(self.frame1)
        self.frame12 = Frame(self.frame1)
        self.frame2 = Frame(self.root)
        self.frame21 = Frame(self.frame2)
        self.frame22 = Frame(self.frame2)
        self.bottom_frame = Frame(self.root)
                
        self.org_img = None
        self.tmp_img = None
        self.cur_dir = "/"

    def browseOrg(self, frame, text):
        self.org_img = filedialog.askopenfilename(initialdir=self.cur_dir, title="Select file", filetypes=(("image files", "*.jpg *.png "), ("all files", "*.*")))
        for wid in frame.winfo_children():
            if type(wid) == Frame:
                for wi in wid.winfo_children():
                    if type(wi) == ttk.Entry:
                        text.set(self.org_img)
        self.cur_dir = os.path.dirname(self.org_img)
    def browseTmp(self, frame, text):
        self.tmp_img = filedialog.askopenfilename(initialdir=self.cur_dir, title="Select file", filetypes=(("image files", "*.jpg *.png "), ("all files", "*.*")))
        for wid in frame.winfo_children():
            if type(wid) == Frame:
                for wi in wid.winfo_children():
                    if type(wi) == ttk.Entry:
                        text.set(self.tmp_img)
        self.cur_dir = os.path.dirname(self.tmp_img)

    def begin(self):
        if (self.org_img == None) or (self.tmp_img == None):
            messagebox.showerror('Error', 'Vui lòng chọn đủ file')
        else :
            self.root.destroy()
        return

    def show(self):
        self.root.title("Timekeeping machine program")
        
        line = Frame(self.root, height=1, width=400, bg="black", relief='groove')

        org_path = Label(self.frame11, text="Image 1:  ")
        org_text = StringVar()
        org_entry = ttk.Entry(self.frame12, textvariable=org_text, state=DISABLED)
        org_browse = ttk.Button(org_entry, text="Browse", command=lambda: self.browseOrg(self.frame1, org_text))

        tmp_path = Label(self.frame21, text="Image 2:  ")
        tmp_text = StringVar()
        tmp_entry = ttk.Entry(self.frame22, textvariable=tmp_text, state=DISABLED)
        tmp_browse = ttk.Button(tmp_entry, text="Browse", command=lambda: self.browseTmp(self.frame2, tmp_text))

        begin_button = ttk.Button(self.bottom_frame, text='Start Compare', command=self.begin)
        
        self.frame1.pack(side=TOP, fill=X)
        self.frame11.pack(side=TOP, fill=X)
        self.frame12.pack(side=TOP, fill=X)
        org_path.pack(side=LEFT, padx=5)
        org_entry.pack(padx=5, pady=(5,15), fill=X)
        org_browse.pack(side=RIGHT, padx=2, pady=3)

        self.frame2.pack(side=TOP, fill=X)
        self.frame21.pack(side=TOP, fill=X)
        self.frame22.pack(side=TOP, fill=X)
        tmp_path.pack(side=LEFT, padx=5)
        tmp_entry.pack(padx=5, pady=(5,15), fill=X)
        tmp_browse.pack(side=RIGHT, padx=2, pady=3)

        line.pack(padx=10, pady=10, fill=X)
        self.bottom_frame.pack(side=TOP)
        begin_button.pack(pady=(5,15), fill=X)
        self.root.mainloop()

    def getFiles(self):
        return self.org_img, self.tmp_img
