# from sklearn.cluster import KMeans
# import numpy as np

# # contoh dataset
# X = np.random.rand(100, 2)

# # hitung inersia untuk setiap nilai K antara 1 sampai 11
# inertia = []
# for k in range(1, 11):
#     kmeans = KMeans(n_clusters=k)
#     kmeans.fit(X)
#     inertia.append(kmeans.inertia_)

# # membuat plot inertia
# fig, ax = plt.subplots(figsize=(8, 4))
# sns.lineplot(x=list(range(1, 11)), y=inertia, ax=ax)
# ax.set_title('Cari Elbow')
# ax.set_xlabel('Clusters')
# ax.set_ylabel('Inertia')
# plt.show()

number_of_year = int(input('Masukkan tahun yang di inginkan? '))
year_input = []
for i in range(0, number_of_year):
    year_input.append(int(input('Masukkan tahun = ')))
    hasil1 = year_input[0] / 100
    hasil2 = year_input[0] / 400
    if (hasil1 == 0):
        print('Termasuk Century year')
    elif (hasil2 == 0):
        print('Termasuk tahun kabisat')
for i in year_input:
    hasil3 = year_input[0] / 4
    if (hasil2 != 0):
        print('bukan century year!')
        res = 'Kabisat'
    elif (hasil3 == 0):
        print('Tahun kabisat!')
        res = 'Kabisat'
    else:
        res = 'bukan kabisat'
