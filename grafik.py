import requests
import gui
import matplotlib.pyplot as plt
import json
from fpdf import FPDF
import os
karlar = []
zararlar = []
def after_create():
    mevcut_veri = []
    veri = {
    "isim": gui.ad,
    "adet": gui.adet,
    "alisFiyati": gui.alis,
    "anlikDeger" : None
}
    

    def fetch_data():
        url = f"https://rest.coinapi.io/v1/exchangerate/{gui.ad}/USD"
        headers = {
            "X-CoinAPI-Key": "8BE7509A-C40D-433B-A9F1-6FBFC49B5E56"
        }
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Bu, başarısız bir istek durumunda bir hata fırlatacaktır.
            return response.json()
        except requests.RequestException as e:
            print(f"API'den veri alırken bir hata oluştu: {e}")
            return None
    
    data = fetch_data()
    jsonData = data
    veri['anlikDeger'] = data['rate']
    # Dosya mevcut mu diye kontrol et 
    try:
        with open("veri.json", "r") as dosya:
            mevcut_veri = json.load(dosya)
    except (FileNotFoundError, json.JSONDecodeError):  
        mevcut_veri = []

# Yeni veriyi listeye ekle
    mevcut_veri.append(veri)






# Listeyi tekrar dosyaya yaz
    with open("veri.json", "w") as dosya:
        json.dump(mevcut_veri, dosya)
        
    #Dosyayı pie ve tablo için tekrardan okuyacağım
    def okuveYazdir():
        with open("veri.json", "r") as dosya:
            veriler = json.load(dosya)
        global karlar,zararlar
        i = 0
        for veri in veriler:
            
            kar_zarar = veri['anlikDeger'] - veri['alisFiyati']
            if kar_zarar > 0:
                karlar.append(kar_zarar)
            else:
                zararlar.append(kar_zarar) 
        labels = ['Kar', 'Zarar']
        sizes = [abs(sum(karlar)), abs(sum(zararlar))]
        colors = ['green', 'red']

        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
        plt.axis('equal') 

        plt.savefig("kar_zarar.png")
        plt.show()
       

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"Aldiginiz coinlerden Kar/Zarar Grafiginiz", ln=True, align='C')

        pdf.image("kar_zarar.png", x=10, y=30, w=190)
        
        pdf.ln(175)  

        col_widths = [45, 30, 30, 45]
        columns = ["Coin Adi", "Alis Fiyati", "Anlik Deger", "Kar/Zarar"]
        pdf.set_fill_color(200, 220, 255)
        for i, column in enumerate(columns):
            pdf.cell(col_widths[i], 10, column, 1, 0, 'C', 1)
        pdf.ln()

    # Veriyi PDF'e yazdırma
        for entry in veriler:
            coin_name = entry["isim"]
            alis_fiyati = entry["alisFiyati"]
            anlik_deger = entry["anlikDeger"]
            kar_zarar = anlik_deger - alis_fiyati

            pdf.cell(col_widths[0], 10, coin_name, 1)
            pdf.cell(col_widths[1], 10, f"{alis_fiyati:.2f}", 1)
            pdf.cell(col_widths[2], 10, f"{anlik_deger:.2f}", 1)
            pdf.cell(col_widths[3], 10, f"{kar_zarar:.2f}", 1)
            pdf.ln()
        pdf.output("rapor.pdf")
    if data and 'rate' in data:
        kar = data['rate'] - gui.alis
        karYuzdesi = (kar / gui.alis) * 100

        if kar > 0:
            mesaj = f"{gui.ad} coininden {gui.adet} adet aldınız. Sizdeki coinin değeri: ${gui.adet * data['rate']} Şu anki karınız:{karYuzdesi:.2f}%"
        elif kar < 0:
            mesaj = f"{gui.ad} coininden {gui.adet} adet aldınız. Sizdeki coinin değeri: ${gui.adet * data['rate']} Şu anki zararınız:{karYuzdesi:.2f}%"
        else:
            mesaj = "Karınız veya zararınız bulunmuyor."

        print(mesaj)
    else:
        print("API'den beklenen veriyi alamadık.")
    okuveYazdir()    