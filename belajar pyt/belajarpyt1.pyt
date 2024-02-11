# list as (array)
nama_hewan = ["ikan", "ayam", "salmon"]
# cetak
# for i in nama_hewan:
#     print(f""" nama nama hewan anda:{i}\n""")
# panjang = len(nama_hewan)
# for i in range(panjang):
#     print(f"""
#     nama hewan berdasarkan index ke-{i} adalah:{nama_hewan[i]}
#     """)
# for i in range(len(nama_hewan)):
#     print(f"""
#         nama-nama hewan berdasarkan index ke-{i} adalah:{nama_hewan[i]}
#     """)

# menambah data di dalam list
# nama_hewan.insert(2, "kijang")
# # tampilkan nama hewan setlah di tambahkan
# print(nama_hewan[2])

# isi list dengan data di for
# angka_genap = [x for x in range(0, 20, 2)]
# angka_ganjil = [x for x in range(1, 20, 2)]
# print(angka_genap)
# print(angka_ganjil)

# list dengan kondisi
# menghilangka  angka 2
# angka = [x for x in range(1, 10) if x != 2]
# print(angka)

# dictionary as (array assoc)
# data_Hewan = {
#     "nama_hewan": "harimau"
# }
# print(data_Hewan["nama_hewan"])


# mendapatak key-nya
# data_mahasiswa_keys = data_mahasiswa.keys()
# print(data_mahasiswa_keys)
# # mendapkan lansung valuenya
# data_data_mhs = data_mahasiswa.values()
# print(data_data_mhs)
# # mendpakan keduanya(key,value)
# data_mhs2 = data_mahasiswa.items()
# print(data_mhs2)

# menampilkan data dengan loo (for)
# for i in data_mahasiswa:
#     print(i)
# hanya mendapkan key nya saja

# menampikan semua data tanpa mengukan keynya
# for i in data_mahasiswa.values():
#     print(i)
# menampilkan data sesuai key dan value
# for key in data_mahasiswa:
#     print("nama mahsiswa adalah", data_mahasiswa["nama"])

# nested dict
# data_mahasiswa = {
#     "mahasiswa1": {
#         "nama": "agus siswanto"
#     },
#     "mahasiswa2": {
#         "nama": "budi"
#     },
#     "mahasiswa3": {
#         "nama": "yanto"
#     },
#     "mahasiswa4": {
#         "nama": "agus cape bu"
#     },
# }
# mengambil semua key dari nested dict
# key_nested = data_mahasiswa.keys()
# print(key_nested)
# menampilkan salah satu data dari nested dict
# for i in range(len(data_mahasiswa)):
#     print(
#         f"""
#             nama mahasiswanya adalah: {data_mahasiswa["mahasiswa1"]["nama"]}
#     """)
rumah = {
    "dapur": {
        "lemari1": "sendok"
    }
}

print(rumah['dapur']['lemari1'])
