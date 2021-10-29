from pytube import YouTube
from tkinter import *
from tkinter import filedialog

root = Tk()

highed = 380
withed = 545

Programm_title = "Ez Youtube Video Downloader"
root.geometry(f"{withed}x{highed}")
root.title(Programm_title)
root.iconbitmap('F:\Tirth\Code\Python\projects\my_gui\Youtube_Downloader\icoDownload.ico')

# Variables

global My_Video


# Functions
def Video_Get():
    global video_title
    global My_Video
    My_Video = YouTube(Ask_For_Link_Entry.get())
    video_title = My_Video.title
    titlo.config(text=f"Title:- {video_title}")


def Open_Folder():
    global Opened_Destination_Path
    Opened_Destination_Path = filedialog.askdirectory()
    Seen_Location.config(text="Download Location :-" + Opened_Destination_Path)


def Downloader_File():
    a = Opened_Destination_Path
    streamer = My_Video.streams.first()
    My_Video.streams.get_highest_resolution().download(a)


# Main Display


Ask_For_Link_Label = Label(root, text="Enter Video Link", font=('Helvetica 12 bold')).grid(column=1, row=1)
Ask_For_Link_Entry = Entry(root, width=90, bg='#73767a')
Ask_For_Link_Entry.grid(column=1, row=2, ipady=4)

Genrate = Button(root, text="Get Video", font='Helvetica 8 bold', command=Video_Get).grid(pady=12, column=1, row=3)

titlo = Label(root)
titlo.config(text='Title:- *Video Title Will Appear Here*', bg='#d4d6a7')
titlo.grid(column=1, row=4)

Last_Frame = Frame(root)
Last_Frame.grid(column=1, row=5)

Download_Destination_button = Button(Last_Frame, text="Set Download Location", command=Open_Folder).grid(column=1,
                                                                                                         row=6, pady=15)
Seen_Location = Label(Last_Frame, text="Download Location :- /Downloads")
Seen_Location.grid(column=1, row=7)

Download_Butt = Button(Last_Frame, text="Download", command=Downloader_File, bg='#f54949',
                       font='Helvetica 12 bold').grid(row=8, column=1, pady=13)

Exit_it = Button(root, command=quit, text="Exit").grid(column=1, row=9, pady=18)

root.mainloop()
