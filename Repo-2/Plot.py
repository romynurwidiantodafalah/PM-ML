import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()

# DATA PENJUALAN
# Data
bulan = ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Oct', 'Nov', 'Des']
penjualan = [100, 120, 90, 110, 115, 105, 100, 80, 70, 113, 160, 170]

# Membuat plot
plt.plot(bulan, penjualan, marker='.', color='b', linestyle='-')
plt.bar(bulan, penjualan, color='skyblue')

# Menambahkan judul dan label sumbu
plt.title('Penjualan per Bulan')
plt.xlabel('Bulan')
plt.ylabel('Penjualan')

# Menampilkan plot
plt.grid(True)
plt.show()