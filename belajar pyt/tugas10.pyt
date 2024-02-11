import tkinter as tk


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def search_linear():
    target = int(entry.get())
    result = linear_search(arr, target)
    if result != -1:
        result_label.config(text=f"Angka ditemukan di indeks {result}")
    else:
        result_label.config(text="Angka tidak ditemukan.")


def search_binary():
    target = int(entry.get())
    result = binary_search(arr, target)
    if result != -1:
        result_label.config(text=f"Angka ditemukan di indeks {result}")
    else:
        result_label.config(text="Angka tidak ditemukan.")


arr = [5, 8, 12, 15, 20, 22, 30]

root = tk.Tk()
root.title("Aplikasi Pencarian")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

label = tk.Label(frame, text="Masukkan angka yang ingin dicari:")
label.pack()

entry = tk.Entry(frame)
entry.pack()

search_linear_button = tk.Button(
    frame, text="Pencarian Linier", command=search_linear)
search_linear_button.pack()

search_binary_button = tk.Button(
    frame, text="Binary Search", command=search_binary)
search_binary_button.pack()

result_label = tk.Label(frame, text="")
result_label.pack()

root.mainloop()
