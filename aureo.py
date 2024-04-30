import tkinter as tk
from flask import *
from tkinter import messagebox
from pytube import YouTube

class App:
    def download(video_link):
        try:
            url = video_link
            youtube = YouTube(url)
            messagebox.showinfo(message="Demarage du telechargement !")
            video = youtube.streams.first()
            video.download("Video")
            messagebox.showinfo(message="Telechargée avec succes !", title="Reusite")
            quit(messagebox.showinfo(message="Merci d'avoir utilisée nos service"))
        except Exception:
            messagebox.showerror(message="Invalide", title=404)
            quit()
            
    def main_menu():
        def download_video():
            link = link_entry.get()
            App.download(link)
            
        window = tk.Tk()
        window.geometry("650x80")
        window.title("Téléchargement de vidéo")
        
        # Entrée pour le lien de la vidéo
        link_label = tk.Label(window, text="Entrez le lien de la vidéo:")
        link_label.pack()
        
        link_entry = tk.Entry(window)
        link_entry.pack()
        
        # Bouton pour télécharger la vidéo
        download_button = tk.Button(window, text="Télécharger", command=download_video)
        download_button.pack()
        
        window.mainloop()

if __name__ == "__main__":
    App.main_menu()