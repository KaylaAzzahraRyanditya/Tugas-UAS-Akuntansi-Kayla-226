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

# Histogram untuk pendapatan
plt.figure(figsize=(10, 6))
sns.histplot(df['Pendapatan'], bins=10, kde=True)
plt.title('Distribusi Pendapatan')
plt.xlabel('Pendapatan')
plt.ylabel('Frekuensi')
plt.show()

# Scatter plot untuk Jumlah Terjual vs Pendapatan
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Jumlah_Terjual', y='Pendapatan', hue='Nama_Produk', style='Nama_Produk')
plt.title('Scatter Plot Jumlah Terjual vs Pendapatan')
plt.xlabel('Jumlah Terjual')
plt.ylabel('Pendapatan')
plt.legend(title='Nama Produk')
plt.show()

# Grafik batang untuk total pendapatan per produk
plt.figure(figsize=(10, 6))
total_pendapatan = df.groupby('Nama_Produk')['Pendapatan'].sum().reset_index()
sns.barplot(data=total_pendapatan, x='Nama_Produk', y='Pendapatan')
plt.title('Total Pendapatan per Produk')
plt.xlabel('Nama Produk')
plt.ylabel('Pendapatan')
plt.show()

# Grafik garis untuk tren penjualan harian per produk
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='Tanggal', y='Jumlah_Terjual', hue='Nama_Produk', marker='o')
plt.title('Tren Penjualan Harian per Produk')
plt.xlabel('Tanggal')
plt.ylabel('Jumlah Terjual')
plt.legend(title='Nama Produk')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
