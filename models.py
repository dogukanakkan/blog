# models.py
import os

class Blog:
    def __init__(self, baslik, icerik):
        self.baslik = baslik
        self.icerik = icerik

class BlogModel:
    def __init__(self, dosya_adi="bloglar.txt"):
        self.dosya_adi = dosya_adi
        self.bloglar = self.bloglari_yukle()

    # Dosyadan blog gönderilerini yükle
    def bloglari_yukle(self):
        bloglar = []
        if os.path.exists(self.dosya_adi):
            with open(self.dosya_adi, 'r') as file:
                for line in file:
                    baslik, icerik = line.strip().split('---')
                    bloglar.append(Blog(baslik, icerik))
        return bloglar

    # Blog gönderilerini dosyaya kaydet
    def bloglari_kaydet(self):
        with open(self.dosya_adi, 'w') as file:
            for blog in self.bloglar:
                file.write(f"{blog.baslik}---{blog.icerik}\n")

    # Blog ekleme
    def blog_ekle(self, baslik, icerik):
        yeni_blog = Blog(baslik, icerik)
        self.bloglar.append(yeni_blog)
        self.bloglari_kaydet()

    # Blog güncelleme
    def blog_guncelle(self, index, yeni_baslik, yeni_icerik):
        self.bloglar[index].baslik = yeni_baslik
        self.bloglar[index].icerik = yeni_icerik
        self.bloglari_kaydet()

    # Blog silme
    def blog_sil(self, index):
        del self.bloglar[index]
        self.bloglari_kaydet()

