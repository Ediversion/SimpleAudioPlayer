# Import Modules

import pygame
import tkinter as tkr
import os

# Create the main Window
player = tkr.Tk()

# Edit window. Specify the size and title of window
player.title("Simple Audio Player")
player.geometry("205x340")

# Playlist folder where the songs exist
os.chdir("/FolderName")
print(os.getcwd())
song_list = os.listdir()

# Playlist Area
playlist = tkr.Listbox(player, highlightcolor='red', selectmode=tkr.SINGLE)
print(song_list)

for item in song_list:
    pos = 0
    playlist.insert(pos, item)
    pos = pos + 1

# Pygame Inits
pygame.init()
pygame.mixer.init()


# Action Event
def Play():
    # This function loads and plays the song
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    song_var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()


def ExitPlayer():
    pygame.mixer.music.stop()


# Register Buttons(Play and Stop buttons) and fit the buttons in the player window using pack
button1 = tkr.Button(player, width=5, height=3, text="PLAY", command=Play)
button2 = tkr.Button(player, width=5, height=3, text="STOP", command=ExitPlayer)


# Create Song Name
song_var = tkr.StringVar()
song_title = tkr.Label(player, textvariable=song_var)

# Place Widgets
song_title.pack()
button1.pack(fill="x")
button2.pack(fill="x")
playlist.pack(fill="both", expand="yes")
# Activate to run the main window
player.mainloop()
