README
Proje Adı: GUİ Tablo

Bu proje, kullanıcıdan belirli bilgileri alarak bir grafik oluşturmayı amaçlar. Bu bilgiler bir coinin adı, adeti ve alınan fiyatıdır.

Kullanılan Teknolojiler

- Python
- Tkinter
- Requests
- Matplotlib
- Json
- FPDF
  
Dosya Yapısı

- gui.py: Bu dosya, kullanıcı arayüzünü oluşturur ve kullanıcıdan gerekli bilgileri alır.
- grafik.py: Bu dosya, kullanıcıdan alınan bilgileri kullanarak bir grafik oluşturur ve bu bilgileri bir JSON dosyasına kaydeder. Ayrıca, bu bilgileri kullanarak bir kar/zarar grafiği oluşturur ve bu grafiği bir PDF dosyasına ekler.
  
Kullanım

1. gui.py dosyasını çalıştırın.
2. Açılan pencerede, coin ismi, adet ve alınan fiyat bilgilerini girin.
3. "Create" butonuna basın.
4. grafik.py dosyasını çalıştırın. Bu, kullanıcıdan alınan bilgileri kullanarak bir grafik oluşturur ve bu bilgileri bir JSON dosyasına kaydeder. Ayrıca, bu bilgileri kullanarak bir kar/zarar grafiği oluşturur ve bu grafiği bir PDF dosyasına ekler.
   
Fonksiyonlar

- tablo_olustur(pencere): Bu fonksiyon, kullanıcıdan gerekli bilgileri almak için bir arayüz oluşturur. Bu bilgiler coinin adı, adeti ve alınan fiyatıdır.
- create(): Bu fonksiyon, kullanıcıdan alınan bilgileri alır ve grafik.after_create() fonksiyonunu çağırır.
- after_create(): Bu fonksiyon, kullanıcıdan alınan bilgileri kullanarak bir grafik oluşturur ve bu bilgileri bir JSON dosyasına kaydeder. Ayrıca, bu bilgileri kullanarak bir kar/zarar grafiği oluşturur ve bu grafiği bir PDF dosyasına ekler.
  
Notlar

- grafik.after_create(): Bu fonksiyon, create() fonksiyonu tarafından çağrılır. Bu fonksiyon, grafik.py dosyasında tanımlanmıştır ve kullanıcıdan alınan bilgileri kullanarak bir grafik oluşturur.
