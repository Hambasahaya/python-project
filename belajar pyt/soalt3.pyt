import tkinter as tk

# Membuat jendela utama
root = tk.Tk()

# Membuat label untuk menampilkan daftar anggota kelompok
daftar_anggota_label = tk.Label(
    root, text="Daftar anggota kelompok 4\n\n1. Zaldy Ramlan")

# buat nampilin daftar anggota
daftar_anggota_label.pack()

root.mainloop()
