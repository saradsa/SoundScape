# import modules
from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog, font
from pygame import mixer
import os


# Initialize tkinter window
root = Tk()
root.title('SoundScape')
root.geometry('1000x600')
root.configure(bg='#2B3638')
root.resizable(False, False)

# initialize mixer
mixer.init()

# Function Declarations

# Function to Open Folder


def open_folder():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END, song)


# Function to play songs
def play_song():
    song_title = playlist.get(ACTIVE)
    if song_title == "":
        error_text = "Don't be so lazy, Open a folder and choose a song."
        music.config(text=error_text)

    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    music.config(text=song_title[0:-4])

# FUnction to stop songs with a fadeout


def stop_song():
    mixer.music.fadeout(700)


# display icon
image_icon = PhotoImage(file='LOGO.png')
root.iconphoto(False, image_icon)

# Display Header and Logo
Header = PhotoImage(file="TOP.png")
Label(root, image=Header, bg="#2B3638").pack()

# BUTTONS

# play button
play_button = PhotoImage(file="PLAY.png")
Button(root, image=play_button, bg="#2B3638",
       bd=0, command=play_song).place(x=190, y=250)

# pause button
pause_button = PhotoImage(file="PAUSE.png")
Button(root, image=pause_button, bg="#2B3638", bd=0,
       command=mixer.music.pause).place(x=50, y=400)

# resume button
resume_button = PhotoImage(file="RESUME.png")
Button(root, image=resume_button, bg="#2B3638", bd=0,
       command=mixer.music.unpause).place(x=194, y=400)

# stop button
stop_button = PhotoImage(file="STOP.png")
Button(root, image=stop_button, bg="#2B3638", bd=0,
       command=stop_song).place(x=338, y=400)

# next button
music = Label(root, text="", font=("Lato", 14), fg="white", bg="#415255")
music.place(x=25, y=18)

# Music Selection Background
menu = PhotoImage(file='Song List Window.png')
Label(root, image=menu, bg="#2B3638").place(x=550, y=220)

# Music Selection Frame
music_frame = Frame(root, bg="#415255")
music_frame.place(x=575, y=305, width=395, height=260)


# Button to open Folder
Button(root, text="Open Folder", width=13, height=2, border=0,
       font=("Lato", 11, "bold"), fg="white", bg="#a1a58a", command=open_folder).place(x=575, y=250)

# scrollbar
scroll = Scrollbar(music_frame)

# create a playlist
playlist = Listbox(music_frame, width=100, font=("Lato", 10), bg="#333333", fg="#90ACB1",
                   selectbackground="lightblue", selectforeground="#2B3638", cursor="hand2", bd=0, yscrollcommand=scroll.set)

# random stuffs copied from stack overflow, it does something don't know what
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT, fill=Y)
playlist.pack(side=LEFT, fill=BOTH)


root.mainloop()
