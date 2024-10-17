# views.py

class BlogView:
    @staticmethod
    def bloglari_goster(bloglar):
        if not bloglar:
            print("\nHiç blog gönderisi yok.")
        else:
            print("\nBlog Gönderileri:")
            for i, blog in enumerate(bloglar, 1):
                print(f"{i}. {blog.baslik}\n   {blog.icerik}\n")

    @staticmethod
    def blog_ekle():
        baslik = input("Blog Başlığı: ")
        icerik = input("Blog İçeriği: ")
        return baslik, icerik

    @staticmethod
    def blog_sec(bloglar):
        BlogView.bloglari_goster(bloglar)
        try:
            secim = int(input("İşlem yapmak istediğiniz blog numarasını girin: "))
            if 1 <= secim <= len(bloglar):
                return secim - 1
            else:
                print("Geçersiz seçim.")
                return None
        except ValueError:
            print("Geçersiz seçim.")
            return None
