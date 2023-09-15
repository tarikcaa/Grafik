import tkinter as tk
from tkinter import ttk
import grafik
adet = None
ad = None
alis = None
def tablo_olustur(pencere):
    # Entry widget'ları oluşturma
    ad_label = tk.Label(pencere, text="Coin ismi")
    ad_label.pack(pady=5)
    ad_entry = tk.Entry(pencere)
    ad_entry.pack(pady=10)
    adet_label = tk.Label(pencere, text="Adet")
    adet_label.pack(pady=5)
    adet_entry = tk.Entry(pencere)
    adet_entry.pack(pady=10)
    alisFiyati_label = tk.Label(pencere, text="Alınan fiyat")
    alisFiyati_label.pack(pady=5)
    alisFiyati_entry = tk.Entry(pencere)
    alisFiyati_entry.pack(pady = 10)

    def create():
        global adet, ad, alis
        adet = int(adet_entry.get())
        ad = ad_entry.get().upper()
        alis = float(alisFiyati_entry.get())
        grafik.after_create() 
        


    create_button = tk.Button(pencere, text="Create", command=create)
    create_button.pack(pady=20)

pencere = tk.Tk()
pencere.title("GUİ Tablo")

tablo_olustur(pencere)

pencere.mainloop()