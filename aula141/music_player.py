import pygame
import os
import tkinter as tk
from tkinter import filedialog


pygame.mixer.init()
pygame.init()


def play_music():
    pygame.mixer.music.play()

def pause_music():
    pygame.mixer.music.pause()

def unpause_music():
    pygame.mixer.music.unpause()

def stop_music():
    pygame.mixer.music.stop()

def load_music():
    file_path = filedialog.askopenfilename(filetypes=[("Music Files", "*.mp3;*.wav")])
    if file_path:
        pygame.mixer.music.load(file_path)
        music_label.config(text=os.path.basename(file_path))


root = tk.Tk()
root.title('Meu Player de Música')

frame = tk.Frame(root)
frame.pack(pady=20)


play_button = tk.Button(frame, text='Play', command=play_music)
play_button.grid(row=0, column=0, padx=10)

pause_button = tk.Button(frame, text='Pause', command=pause_music)
pause_button.grid(row=0, column=1, padx=10)

unpause_button = tk.Button(frame, text='Unpause', command=unpause_music)
unpause_button.grid(row=0, column=2, padx=10)

stop_button = tk.Button(frame, text='Stop', command=stop_music)
stop_button.grid(row=0, column=3, padx=10)

load_button = tk.Button(frame, text='Load', command=load_music)
load_button.grid(row=1, column=0, columnspan=4, pady=10)


music_label = tk.Label(root, text='Nenhuma música carregada')
music_label.pack(pady=10)


root.mainloop()
