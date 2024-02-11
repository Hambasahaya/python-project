import tkinter as tk
from tkinter import ttk, Label
from PIL import Image, ImageTk
from gtts import gTTS
import pygame
import os

# Data hewan
pygame.init()
viewval1 = False
viewval2 = False
hewan = {
    1: {
        "nama_hewan": "cat",
        "gambar_hewan": "tb1/FotoHewan/kucing.jpg",
    },
    4: {
        "nama_hewan": "Goat",
        "gambar_hewan": "tb1/FotoHewan/kambing.jpg",
    },
    2: {
        "nama_hewan": "chicken",
        "gambar_hewan": "tb1/FotoHewan/chiken.jpg",
    },
    3: {
        "nama_hewan": "DOG",
        "gambar_hewan": "tb1/FotoHewan/Anjing.jpg",
    },
    5: {
        "nama_hewan": "tb1/Tiger",
        "gambar_hewan": "tb1/FotoHewan/macan.jpg",
    },
    6: {
        "nama_hewan": "OWL",
        "gambar_hewan": "tb1/FotoHewan/owl.jpg",
    },
}
warna = {
    1: {
        "nama_gambar": "Black",
        "gambar_gambar": "tb1/warna/black.jpg",
    },
    2: {
        "nama_gambar": "Blue",
        "gambar_gambar": "tb1/warna/blue.png",
    },
    3: {
        "nama_gambar": "Red",
        "gambar_gambar": "tb1/warna/red.jpg",
    },
    4: {
        "nama_gambar": "Purple",
        "gambar_gambar": "tb1/warna/ungu.png",
    },
    5: {
        "nama_gambar": "Yellow",
        "gambar_gambar": "tb1/warna/yellow.png",
    }
}


def tampilview(event):
    global viewval1
    global viewval2
    if menuselected.get() == "Animals":
        if viewval1 == False:
            tampilAnimals()
            viewval1 = True
        elif viewval1 == True:
            pass
    elif menuselected.get() == "Color":
        if viewval2 == False:
            tampilColor()
            viewval2 = True
        elif viewval2 == True:
            pass


def createVoice(name_file, text):
    audio_path = 'tb1/' + name_file + '.mp3'
    if not os.path.isfile(audio_path):
        say = gTTS(text=text, lang='en')
        say.save(audio_path)


def Playvoice(name_of_file, direc):
    pygame.mixer.init()
    pygame.mixer.music.load(direc + name_of_file + '.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(5)


def eventani(hewan_id):
    if hewan_id == "cat":
        createVoice(hewan_id, hewan_id)
        Playvoice(hewan_id, "tb1/suaraHewan/")
    elif hewan_id == "chicken":
        createVoice(hewan_id, hewan_id)
        Playvoice(hewan_id, "tb1/suaraHewan/")
    elif hewan_id == "DOG":
        createVoice(hewan_id, hewan_id)
        Playvoice(hewan_id, "tb1/suaraHewan/")
    elif hewan_id == "Goat":
        createVoice(hewan_id, hewan_id)
        Playvoice(hewan_id, "tb1/suaraHewan/")
    elif hewan_id == "Tiger":
        createVoice(hewan_id, hewan_id)
        Playvoice(hewan_id, "tb1/suaraHewan/")
    elif hewan_id == "OWL":
        createVoice(hewan_id, hewan_id)
        Playvoice(hewan_id, "tb1/suaraHewan/")


def evengambar(gambar_id):
    # createVoice(gambar_id, gambar_id)
    # Playvoice(gambar_id, "tb1/")
    print(gambar_id)


def tampilAnimals():
    tampilhewan = ttk.Frame(window)
    for i in range(1, len(hewan) + 1):
        image = Image.open(hewan[i]['gambar_hewan'])
        photo = ImageTk.PhotoImage(image)
        resized_image = image.resize((200, 200))
        photo = ImageTk.PhotoImage(resized_image)
        image_label = Label(tampilhewan, image=photo, padx=50, pady=50)
        image_label.photo = photo
        image_label.bind('<Button-1>', lambda event,
                         hewan_id=hewan[i]['nama_hewan']: eventani(hewan_id))
        image_label.pack(side=tk.LEFT)
    tampilhewan.pack()


def tampilColor():
    tampilgambar = ttk.Frame(window)
    for i in range(1, len(warna) + 1):
        image = Image.open(warna[i]['gambar_gambar'])
        photo = ImageTk.PhotoImage(image)
        resized_image = image.resize((200, 200))
        photo = ImageTk.PhotoImage(resized_image)
        image_label = Label(tampilgambar, image=photo, padx=50, pady=50)
        image_label.photo = photo
        image_label.bind('<Button-1>', lambda event,
                         gambar_id=warna[i]['nama_gambar']: evengambar(gambar_id))
        image_label.pack(side=tk.LEFT)
    tampilgambar.pack()
    ke


window = tk.Tk()
window.geometry('800x600')
window.title("Tugas Besar 1")

Kelompok = ttk.Frame(window)
label = Label(Kelompok, text='Kelompok 4: Zaldy Ramlan 41522010284')
label.pack()
Kelompok.pack()

menu = ttk.Frame(window)
label = Label(menu, text='Pilih menu:')
label.pack()
option_menu = ["Animals", "Color"]
menuselected = tk.StringVar(window)
option_menus = ttk.OptionMenu(
    menu,
    menuselected,
    option_menu[0],
    *option_menu,
    command=tampilview)
option_menus.pack()
menu.pack()

window.mainloop()
