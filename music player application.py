import os
import tkinter as tk
from tkinter import filedialog, messagebox
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")

        self.music_folder = ""
        self.music_files = []
        self.current_index = 0
        self.paused = False

        self.create_widgets()

    def create_widgets(self):
        self.select_folder_button = tk.Button(self.root, text="Select Folder", command=self.select_folder)
        self.select_folder_button.pack(pady=10)

        self.play_button = tk.Button(self.root, text="Play", command=self.play)
        self.play_button.pack(pady=5)

        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause, state=tk.DISABLED)
        self.pause_button.pack(pady=5)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop, state=tk.DISABLED)
        self.stop_button.pack(pady=5)

    def select_folder(self):
        self.music_folder = filedialog.askdirectory()
        if self.music_folder:
            self.music_files = [file for file in os.listdir(self.music_folder) if file.endswith(".mp3")]
            if not self.music_files:
                messagebox.showerror("Error", "No music files found in selected folder.")
                return
            self.current_index = 0
            self.load_music()
            self.play_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.NORMAL)

    def load_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join(self.music_folder, self.music_files[self.current_index]))

    def play(self):
        if not pygame.mixer.get_init():
            messagebox.showerror("Error", "Please select a music folder first.")
            return
        pygame.mixer.music.play()
        self.play_button.config(state=tk.DISABLED)
        self.pause_button.config(state=tk.NORMAL)

    def pause(self):
        if self.paused:
            pygame.mixer.music.unpause()
            self.pause_button.config(text="Pause")
            self.paused = False
        else:
            pygame.mixer.music.pause()
            self.pause_button.config(text="Resume")
            self.paused = True

    def stop(self):
        pygame.mixer.music.stop()
        self.play_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
