import pandas as pd

# Membaca dataset dari file CSV yang diunggah
file_path_input = "dataset.csv"
df = pd.read_csv(file_path_input)

# Kriteria tempat_lahir yang diinginkan
desired_tempat_lahir = ["JAKARTA", "TANGERANG", "BOGOR"]

# Memfilter data berdasarkan kriteria tempat_lahir
# Make a copy to avoid SettingWithCopyWarning
filtered_data = df[df['tempat_lahir'].isin(desired_tempat_lahir)].copy()

# Menambahkan kolom 'no' dengan nilai dari 1 sampai 46
filtered_data.loc[:, 'no'] = range(1, len(filtered_data) + 1)

# Memilih kolom yang diinginkan
selected_columns = ["no", "nama", "nik", "alamat"]

# Menyimpan hasil ke file CSV yang sudah disiapkan
file_path_output_base = "my_pertamina"
filtered_data[selected_columns].to_csv(
    f"{file_path_output_base}.csv", index=False)

# Buat sheet baru setiap 11 baris
chunks = [filtered_data[i:i + 46] for i in range(0, len(filtered_data), 46)]
excel_writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')

for idx, chunk in enumerate(chunks):
    # Menyimpan setiap chunk ke file CSV terpisah
    chunk[selected_columns].to_csv(
        f"{file_path_output_base}_sheet{idx + 1}.csv", index=False)

    # Menyimpan setiap chunk ke sheet di file Excel
    chunk[selected_columns].to_excel(
        excel_writer, sheet_name=f'Sheet{idx + 1}', index=False)

excel_writer.save()

print(
    f"File CSV dan Excel telah dibuat: {file_path_output_base}.csv, fix.xlsx")
