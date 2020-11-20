# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox
import tkinter
import time
import sys
from pytube import YouTube 
from pytubemp3 import YouTube

window=Tk()
window.title('//ABDUL_MUID')
window.geometry('340x200')
window.resizable(width=False, height=False)
window.configure(bg='black')
ttk.Label(window, text = "YouTube File Downloader",background = 'black', foreground ="green",font = ("Times New Roman", 15)).grid(row = 0, column = 1,padx=10,pady=25) 
l1=Label(window, text="URL")
l1.grid(row=5,column=0)
l1.configure(bg='black', foreground='green')
l1=Label(window, text="Format")
l1.grid(row=10,column=0)
l1.configure(bg='black', foreground='green')
url_text=StringVar()
url_entry = Entry(window, textvariable=url_text)
e1=Entry(window,textvariable=url_text)
e1.grid(row=5,column=1)
n = tk.StringVar() 
format = ttk.Combobox(window, width = 5, textvariable = n) 
format['values'] = ('MP3','MP4') 
format.grid(column = 1, row = 10) 
format.current() 
#ttk.Separator(window).place(x=0, y=200, relwidth=5)

def code():
    youtube_link=url_entry.get()
    ext_format=format.get()
    print("Searching File...")
    animation = ["[■□□□□□□□□□□□□□□]","[■■□□□□□□□□□□□□□]", "[■■■□□□□□□□□□□□□]", "[■■■■□□□□□□□□□□□]", "[■■■■■□□□□□□□□□□]", "[■■■■■■□□□□□□□□□]", "[■■■■■■■□□□□□□□□]", "[■■■■■■■■□□□□□□□]", "[■■■■■■■■■□□□□□□]", "[■■■■■■■■■■□□□□□]", "[■■■■■■■■■■■□□□□]","[■■■■■■■■■■■■□□□]", "[■■■■■■■■■■■■■□□]", "[■■■■■■■■■■■■■■□]", "[■■■■■■■■■■■■■■■]" ]
    for i in range(len(animation)):
        time.sleep(0.2)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    print("\n File Found!!! \n Stand-By For Download...")
    try:
        if ext_format=="MP4":
            yt_obj = YouTube(youtube_link) 
            filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
            filters.get_highest_resolution().download()
        else:
            yt_obj = YouTube(youtube_link) 
            YouTube(youtube_link).streams.filter(only_audio=True).first().download()
        print("Downloading....")
        animationTwo = "|/-\\"

        for i in range(100):
            time.sleep(0.1)
            sys.stdout.write("\r" + animationTwo[i % len(animationTwo)])
            sys.stdout.flush()
        print("___________/")
        print('File Downloaded Successfully')
    except Exception as e:
        print(e)

btn=Button(window, text='Download', bd='5', command=code)
btn.grid(row = 15, column=1, padx=25,pady=25)
window.mainloop()

