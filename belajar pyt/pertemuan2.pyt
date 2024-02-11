menu = []
for i in range(5):
    x = input("Masukkan menu:")
    menu.append(x)

for idx, item in enumerate(menu, start=1):
    print(f"{idx}. {item}")
user=int(input("pilih menu anda:"))

if user==1:
    print("menu yang anda pilih andalah:",menu[0])
