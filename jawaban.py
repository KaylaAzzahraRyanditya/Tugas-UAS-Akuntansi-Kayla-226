import pandas as pd
data = {
    'Tanggal': ['2024-01-01', '2024-01-01', '2024-01-01', 
                '2024-01-02', '2024-01-02', '2024-01-02', 
                '2024-01-03', '2024-01-03', '2024-01-03', 
                '2024-01-04', '2024-01-04', '2024-01-04'],
    'Nama_Produk': ['Produk A', 'Produk B', 'Produk C', 
                    'Produk A', 'Produk B', 'Produk C', 
                    'Produk A', 'Produk B', 'Produk C', 
                    'Produk A', 'Produk B', 'Produk C'],
    'Jumlah_Terjual': [10, 5, 7, 3, 8, 2, 6, 2, 5, 1, 4, 3],
    'Pendapatan': [500000, 250000, 350000, 150000, 400000, 100000, 300000, 100000, 250000, 50000, 200000, 150000]
}
df = pd.DataFrame(data)
