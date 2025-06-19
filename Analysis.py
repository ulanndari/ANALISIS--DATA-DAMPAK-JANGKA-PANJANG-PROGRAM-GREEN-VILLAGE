# Import library yang diper# Mengonversi kolom 'Date' dari object (teks) ke datetime
print(df.columns)
df['Date'] = pd.to_datetime(df['Date'])

# Menghitung jumlah nilai NaN di setiap kolo
df.isnull().sum()lukan
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Memuat dataset dari file CSV ke dalam DataFrame
df = pd.read_csv('green_village_data.csv')

# Inspeksi cepat untuk memastikan data termuat dengan benar
df.head()



# Mengisi nilai NaN dengan rata-rata kolom masing-masing
df.fillna(df.mean(numeric_only=True), inplace=True)

# Membuat fitur baru 'Total_Waste_kg'
df['Total_Waste_kg'] = df['Organic_Waste_kg'] + df['Recyclable_Waste_kg']

# Menghitung rasio sebagai fitur baru
df['Recycle_Ratio'] = df['Recyclable_Waste_kg'] / df['Total_Waste_kg']

# Menghitung efisiensi, menangani kasus pembagian dengan nol
df['Biogas_Efficiency'] = df['Biogas_Produced_L'] / df['Organic_Waste_kg']
# Mengganti nilai tak terhingga (inf) yang mungkin muncul dengan 0
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df['Biogas_Efficiency'].fillna(0, inplace=True)

# Menampilkan ringkasan statistik untuk semua kolom numerik
df.describe()

# 1. Split: Kelompokkan data berdasarkan 'Date'
# 2. Apply: Terapkan fungsi penjumlahan (.sum()) ke setiap grup
# 3. Combine: Gabungkan hasilnya menjadi DataFrame baru
daily_summary = df.groupby('Date').sum(numeric_only=True)
# Membuat area plot dan mengatur ukurannya
plt.figure(figsize=(12, 6))

# Memplot data sampah organik
plt.plot(daily_summary.index, daily_summary['Organic_Waste_kg'], label='Sampah Organik (kg)', color='green')

# Memplot data biogas dengan penskalaan
plt.plot(daily_summary.index, daily_summary['Biogas_Produced_L'] / 200, label='Biogas Dihasilkan (skala L/200)', color='blue')

# Menambahkan detail pada grafik
plt.title('Tren Harian Sampah Organik vs Produksi Biogas')
plt.xlabel('Tanggal')
plt.ylabel('Jumlah (Kg atau L/200)')
plt.legend()
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Membuat Grafik Sebar untuk melihat korelasi
plt.figure(figsize=(8, 5))
plt.scatter(x=df['Organic_Waste_kg'], y=df['Energy_Credits'], color='purple', alpha=0.5)

# Menambahkan detail pada grafik
plt.title('Hubungan Antara Sampah Organik dan Kredit Energi')
plt.xlabel('Sampah Organik (kg)')
plt.ylabel('Kredit Energi yang Diterima')
plt.grid(True)
plt.tight_layout()
plt.show()

# # Menyimpan DataFrame yang telah diolah ke file CSV baru
df.to_csv('green_village_data.csv', index=False)
print("DataFrame yang telah dianalisis berhasil disimpan sebagai green_village_data.csv")


