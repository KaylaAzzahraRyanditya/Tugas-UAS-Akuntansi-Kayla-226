import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data penjualan
data = {
    'Tanggal': ['2024-01-01', '2024-01-01', '2024-01-01', 
                '2024-01-02', '2024-01-02', '2024-01-02', 
                '2024-01-03', '2024-01-03', '2024-01-03', 
                '2024-01-04', '2024-01-04', '2024-01-04'],
    'Nama_Produk': ['Produk A', 'Produk B', 'Produk C', 
                    'Produk A', 'Produk B', 'Produk C', 
                    'Produk A', 'Produk B', 'Produk C', 
                    'Produk A', 'Produk B', 'Produk C'],
    'Jumlah_Terjual': [10, 5, 7, 
                       3, 8, 2, 
                       6, 2, 5, 
                       1, 4, 3],
    'Pendapatan': [500000, 250000, 350000, 
                   150000, 400000, 100000, 
                   300000, 100000, 250000, 
                   50000, 200000, 150000]
}

# Buat DataFrame dari data
df = pd.DataFrame(data)

# Total pendapatan untuk setiap produk
total_pendapatan = df.groupby('Nama_Produk')['Pendapatan'].sum()
print("Total Pendapatan per Produk:\n", total_pendapatan)

# Produk dengan jumlah penjualan tertinggi
total_jumlah_terjual = df.groupby('Nama_Produk')['Jumlah_Terjual'].sum()
produk_terlaris = total_jumlah_terjual.idxmax()
print("Produk dengan jumlah penjualan tertinggi:", produk_terlaris)

# Pendapatan rata-rata per hari
rata_rata_pendapatan_harian = df.groupby('Tanggal')['Pendapatan'].mean()
print("Pendapatan Rata-rata per Hari:\n", rata_rata_pendapatan_harian)

# Grafik tren penjualan harian untuk setiap produk
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='Tanggal', y='Jumlah_Terjual', hue='Nama_Produk', marker='o')
plt.title('Tren Penjualan Harian per Produk')
plt.xlabel('Tanggal')
plt.ylabel('Jumlah Terjual')
plt.legend(title='Nama Produk')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
