# Mengimpor pustaka yang dibutuhkan
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import f1_score, accuracy_score

# Membaca dataset CSV
df = pd.read_csv("ETH-USD.csv")

# Mengubah kolom 'Date' menjadi tipe data datetime dan mengatur sebagai indeks
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Menampilkan plot harga Ethereum
plt.figure(figsize=(10,6))
plt.plot(df.index, df['Close'], color='blue')
plt.title('Harga Ethereum')
plt.xlabel('Tanggal')
plt.ylabel('Harga (USD)')
plt.grid(True)
plt.show()

# Memodelkan ARIMA
model = ARIMA(df['Close'], order=(5,1,0))
model_fit = model.fit()

# Menampilkan ringkasan model
print(model_fit.summary())

# Plot residual errors
residuals = pd.DataFrame(model_fit.resid)
plt.figure(figsize=(10,6))
plt.plot(residuals, color='green')
plt.title('Residual Errors')
plt.xlabel('Tanggal')
plt.ylabel('Residuals')
plt.grid(True)
plt.show()

# Prediksi harga Ethereum
start_date = pd.to_datetime('2023-10-07')
end_date = pd.to_datetime('2024-05-01')
predictions = model_fit.predict(start=start_date, end=end_date, dynamic=False)

# Mengklasifikasikan harga sebenarnya dan prediksi menjadi naik atau turun
df['Actual Change'] = df['Close'].diff().fillna(0)
df['Actual Class'] = df['Actual Change'].apply(lambda x: 1 if x > 0 else 0)
predictions_diff = predictions.diff().fillna(0)
predictions_class = predictions_diff.apply(lambda x: 1 if x > 0 else 0)

# Memotong dataframe sesuai dengan rentang prediksi
actual_class = df.loc[start_date:end_date, 'Actual Class']

# Menghitung skor F1 dan akurasi
f1 = f1_score(actual_class, predictions_class)
accuracy = accuracy_score(actual_class, predictions_class)

print(f"F1 Score: {f1}")
print(f"Accuracy: {accuracy}")

# Plot hasil prediksi
plt.figure(figsize=(10,6))
plt.plot(df.index, df['Close'], color='blue', label='Observasi')
plt.plot(predictions.index, predictions, color='red', label='Prediksi')
plt.title('Prediksi Harga Ethereum')
plt.xlabel('Tanggal')
plt.ylabel('Harga (USD)')
plt.legend()
plt.grid(True)
plt.show()
