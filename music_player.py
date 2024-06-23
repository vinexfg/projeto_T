import pygame
import os
import tkinter as tk
from tkinter import filedialog

pygame.mixer.init()
pygame.init()

music_file ='https://www.youtube.com/watch?v=fuWYBmXbgkU&list=PL4T2jwgFRmoEY1HP5FFsTB891d8bcm6jq&ab_channel=GuerradosTronos'

pygame.mixer.music.load(music_file)


def play_music():
    pygame.mixer.music.play()

def pause_music():
    pygame.mixer.music.pause()

def unpause_music():
    pygame.mixer.music.unpause()

def stop_music():
    pygame.mixer.music.stop()

def load_music():
    file_path = filedialog.askopenfilename()
    if file_path:
        pygame.mixer.music.load(file_path)
        music_label.config(text=os.path.basename(file_path))

root = tk.Tk()
root.title('Mine player de musica')

frame = tk.Frame(root)
frame.pack(pady=20)

play_button = tk.Button(frame, text='Play', command=play_music)
play_button.grid(row=0, column=0, padx=10)

pause_button = tk.Button(frame, text="Pause", command=pause_music)
pause_button.grid(row=0, column=0, padx=10)

unpause_button = tk.Button(frame, text="Unpause", command=unpause_music)
unpause_button.grid(row=0, column=2, padx=10)

stop_button = tk.Button(frame, text='Stop', command=pause_music)
stop_button.grid(row=0, column=3, padx=10)

load_button = tk.Button(frame, text='Load', command=load_music)
load_button.grid(row=1, column=0, columnspan=4, pady=10)

music_label = tk.Label(root, text='Nenhuma musica carregada')
music_label.pack(pady=10)



running = True

while running:
    print('Escolha uma opção: play; pause; unpause; stop; quit')
    choice = input('->').lower()

    if choice == 'play':
        play_music()
    elif choice =='pause':
        pause_music()
    elif choice == 'unpause':
        unpause_music()
    elif choice == 'stop':
        stop_music()
    else:
        print('opção invalida')
    
pygame.quit()