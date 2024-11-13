import tkinter as tk
from tkinter import messagebox

# Fungsi untuk memvalidasi input dan menampilkan hasil prediksi
def hasil_prediksi():
    try:
        for entry in entries:
            nilai = int(entry.get())
            if not (0 <= nilai <= 100):
                raise ValueError("Nilai harus antara 0 dan 100")
        hasil_label.config(text="Prediksi: Teknologi Informasi")
    except ValueError:
        messagebox.showerror("Input Error", "Pastikan semua input adalah angka antara 0 dan 100.")

# Membuat window utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("500x600")
root.configure(bg="#FF69B4")

# Label judul
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 20), bg="#FF69B4")
judul_label.pack(pady=20)

# Frame untuk input nilai mata pelajaran
frame = tk.Frame(root, bg="#FF69B4")
frame.pack(pady=10)

# Menambahkan input untuk nilai mata pelajaran
entries = []
for i in range(10):
    label = tk.Label(frame, text=f"Nilai Mata Pelajaran {i+1}:", font=("Arial", 12), bg="#FF69B4")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
    entry = tk.Entry(frame, width=10, font=("Arial", 14))
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

# Tombol Prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi, font=("Arial", 12, "bold"), bg="#FF1493", fg="white")
prediksi_button.pack(pady=30)

# Label untuk hasil prediksi
hasil_label = tk.Label(root, text="", font=("Arial", 14, "italic", "bold"), fg="white", bg="#FF69B4")
hasil_label.pack(pady=20)

# Menjalankan aplikasi
root.mainloop()