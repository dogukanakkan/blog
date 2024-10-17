# app.py
from controllers import BlogController

def menu():
    print("\n--- Basit Blog Uygulaması ---")
    print("1. Blog Gönderilerini Listele")
    print("2. Blog Gönderisi Ekle")
    print("3. Blog Gönderisini Güncelle")
    print("4. Blog Gönderisini Sil")
    print("5. Çıkış")
    return input("Bir seçenek girin: ")

def main():
    controller = BlogController()

    while True:
        secim = menu()
        if secim == "1":
            controller.bloglari_listele()
        elif secim == "2":
            controller.blog_ekle()
        elif secim == "3":
            controller.blog_guncelle()
        elif secim == "4":
            controller.blog_sil()
        elif secim == "5":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
