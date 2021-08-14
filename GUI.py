# -*- coding: utf-8 -*-

'''
Copyright © 2021  Bartłomiej Duda
License: GPL-3.0 License 
'''

import os
import sys
import struct
import tkinter as tk
from tkinter import messagebox, StringVar, OptionMenu, filedialog, ttk, Text, LabelFrame, Radiobutton, Scrollbar
from PIL import ImageTk, Image
import webbrowser
import traceback
import pyperclip  # pip install pyperclip
from datetime import datetime
import tkinter.ttk as ttk
import center_tk_window    # pip install center_tk_window
import ea_image_logic



# Program tested on Python 3.7.0


#default app settings
WINDOW_HEIGHT = 460
WINDOW_WIDTH = 450
MIN_WINDOW_HEIGHT = WINDOW_HEIGHT
MIN_WINDOW_WIDTH = WINDOW_WIDTH  
MAX_WINDOW_HEIGHT = WINDOW_HEIGHT
MAX_WINDOW_WIDTH = WINDOW_WIDTH


class EA_MAN_GUI:
    def __init__(self, master, in_VERSION_NUM):
        self.master = master
        self.VERSION_NUM = in_VERSION_NUM
        master.title("EA GRAPHICS MANAGER " + in_VERSION_NUM)
        master.minsize(MIN_WINDOW_WIDTH, MIN_WINDOW_HEIGHT) 
        master.maxsize(MAX_WINDOW_WIDTH, MAX_WINDOW_HEIGHT) 
        
            
        self.allowed_filetypes = [ ('EA Graphics files', ['*.fsh', '*.psh', '*.ssh', '*.msh', '*.xsh']), 
                                   ('All files', ['*.*'])
                                 ]     
        
        self.allowed_signatures = ( "SHPI", #PC games
                                    "SHPP", #PS1 games 
                                    "SHPS", #PS2 games
                                    "ShpX", "SHPX", #XBOX games
                                    "SHPM" #PSP games 
                                  )

        #main frame
        self.main_frame = tk.Frame(master, bg='#f0f0f0')
        self.main_frame.place(x=0, y=0, relwidth=1, relheight=1)


        #treeview widget
        self.treeview_widget = ttk.Treeview(show="tree")
        self.treeview_widget.place(x= 10, y= 10, width=120, height=405)   
   
        self.treeview_widget.insert('', tk.END, text='file1.SSH', iid=0, open=False)
        self.treeview_widget.insert('', tk.END, text='file2.FSH', iid=1, open=False)
        
        # adding children of first node
        self.treeview_widget.insert('', tk.END, text='bubbles img', iid=5, open=False)
        self.treeview_widget.insert('', tk.END, text='title img', iid=6, open=False)
        self.treeview_widget.move(5, 0, 1)
        self.treeview_widget.move(6, 0, 1)

                   


        self.butt1 = tk.Button(self.main_frame, text="OPEN", command=lambda: self.open_file() )
        self.butt1.place(x= 150, y= 70, width=60, height=20)       
        
        
        # menu
        self.menubar = tk.Menu(master)
        
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Open File", command=lambda: self.open_file())
        self.filemenu.add_command(label="Scan Directory", command=lambda: self.scan_dir())
        self.filemenu.add_command(label="Save as...", command=lambda: self.save_as())
        self.filemenu.add_command(label="Close File", command=lambda: self.close_font())
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=master.destroy)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        
        self.helpmenu = tk.Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="About...", command=lambda: self.show_about_window())
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)
        
        
        self.filemenu.entryconfig(2, state="disabled") 
        self.filemenu.entryconfig(3, state="disabled") 
        
        master.config(menu=self.menubar)        
    
    
    
    
    def open_file(self):
        try:
            in_file = filedialog.askopenfile(filetypes=self.allowed_filetypes, mode='rb')   
            in_file_path = in_file.name 
        except:
            messagebox.showwarning("Warning", "Failed to open file!")
            return
        
        try:
            sign = in_file.read(4).decode("utf8")
            if sign not in self.allowed_signatures:
                raise
        except:
            messagebox.showwarning("Warning", "File not supported!")
            return
        
        ea_image_logic.bd_logger("Loading file...")
            
     
    def add_to_tree(self):
        pass
     
        
   
    def web_callback(self, url):
        webbrowser.open_new(url)   
        
    def show_about_window(self):
            t = tk.Toplevel()
            t.wm_title("About")
            
            a_text = ( "EA Graphics Manager\n"
                       "Version: " + self.VERSION_NUM + "\n"
                       "\n"
                       "Program has been created\n"
                       "by Bartłomiej Duda.\n"
                       "\n"
                       "If you want to support me,\n"
                       "you can do it here:" )        
            a_text2 = ( "https://www.paypal.me/kolatek55" )
            a_text3 = ( "\n"
                        "If you want to see my other tools,\n"
                        "go to my github page:" )
            a_text4 = ( "https://github.com/bartlomiejduda" )
            
            l = tk.Label(t, text=a_text)
            l.pack(side="top", fill="both", padx=10)
            l2 = tk.Label(t, text=a_text2, fg="blue", cursor="hand2")
            l2.bind("<Button-1>", lambda e: self.web_callback(a_text2))
            l2.pack(side="top", anchor='n')
            l3 = tk.Label(t, text=a_text3)
            l3.pack(side="top", fill="both", padx=10)        
            l4 = tk.Label(t, text=a_text4, fg="blue", cursor="hand2")
            l4.bind("<Button-1>", lambda e: self.web_callback(a_text4))
            l4.pack(side="top", anchor='n')    
        
            center_tk_window.center_on_screen(t)