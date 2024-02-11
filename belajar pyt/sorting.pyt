data = [2, 5, 6, 7, 84, 3, 4]
Cektukar = False
# bubble sort
for i in range(len(data)-1):
    for j in range(0, len(data) - 1):
        if data[j] > data[j+1]:
            temp = data[j]
            data[j] = data[j+1]
            data[j+1] = temp
            Cektukar = True
