# controllers.py
from models import BlogModel
from views import BlogView

class BlogController:
    def __init__(self):
        self.model = BlogModel()

    # Blog gönderilerini listele
    def bloglari_listele(self):
        BlogView.bloglari_goster(self.model.bloglar)

    # Blog gönderisi ekle
    def blog_ekle(self):
        baslik, icerik = BlogView.blog_ekle()
        self.model.blog_ekle(baslik, icerik)
        print(f"'{baslik}' adlı blog gönderisi eklendi.")

    # Blog gönderisini güncelle
    def blog_guncelle(self):
        secilen_index = BlogView.blog_sec(self.model.bloglar)
        if secilen_index is not None:
            yeni_baslik, yeni_icerik = BlogView.blog_ekle()
            self.model.blog_guncelle(secilen_index, yeni_baslik, yeni_icerik)
            print(f"Blog gönderisi güncellendi.")

    # Blog gönderisini sil
    def blog_sil(self):
        secilen_index = BlogView.blog_sec(self.model.bloglar)
        if secilen_index is not None:
            self.model.blog_sil(secilen_index)
            print("Blog gönderisi silindi.")
