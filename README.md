# Bike Sharing Dashboard

## Deskripsi
Dashboard ini merupakan proyek analisis data untuk menganalisis pola penggunaan layanan bike sharing berdasarkan data yang telah dikumpulkan. Dengan menggunakan Python dan Streamlit, dashboard ini menyediakan visualisasi yang interaktif untuk membantu memahami penggunaan layanan selama berbagai bulan dan jam, serta dampak cuaca terhadap penggunaan.

## Persyaratan
Sebelum menjalankan dashboard, pastikan Anda telah menginstal semua dependensi berikut:
- Python 3.x
- Streamlit
- Pandas
- Matplotlib
- Seaborn
- Plotly (jika digunakan)

## Instalasi Dependensi
Anda dapat menginstal dependensi yang diperlukan dengan menggunakan pip. Jalankan perintah berikut di terminal:

```bash
pip install streamlit pandas matplotlib seaborn plotly
```

## Cara Menjalankan Dashboard
1. **Clone Repository**: Pertama, clone repository ini ke komputer lokal Anda. Jalankan perintah berikut:

    ```bash
    git clone https://github.com/Nanashua/Proyek-Analisis-Data-Dicoding.git
    ```

2. **Navigasi ke Folder Proyek**: Masuk ke folder yang berisi file dashboard Anda. Contoh:

    ```bash
    cd Proyek-Analisis-Data-Dicoding
    ```

3. **Jalankan Dashboard**: Gunakan perintah berikut untuk menjalankan dashboard menggunakan Streamlit:

    ```bash
    streamlit run dashboard.py
    ```

4. **Akses Dashboard**: Setelah menjalankan perintah di atas, dashboard akan terbuka di browser Anda secara otomatis. Jika tidak, Anda dapat mengaksesnya melalui alamat URL yang ditampilkan di terminal, biasanya `http://localhost:8501`.

## Fitur
- **Analisis Penggunaan Bulanan**: Visualisasi jumlah pengguna layanan berdasarkan bulan.
- **Distribusi Pengguna Kasual dan Terdaftar**: Analisis perbandingan antara pengguna kasual dan terdaftar berdasarkan musim.
- **Perilaku Pengguna Berdasarkan Jam**: Analisis pola penggunaan berdasarkan jam layanan.
- **Dampak Cuaca**: Analisis dampak kondisi cuaca terhadap penggunaan layanan.
- **Tren Penggunaan**: Heatmap yang menunjukkan tren penggunaan layanan berdasarkan bulan dan jam.

## Kontribusi
Jika Anda ingin berkontribusi pada proyek ini, silakan buka issue atau buat pull request di repository ini.

## Lisensi
Proyek ini dilisensikan di bawah MIT License. Lihat file [LICENSE](LICENSE) untuk informasi lebih lanjut.
