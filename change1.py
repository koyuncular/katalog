import os
import time

# Klasör yolunu belirt
folder_path = r"C:\Users\user\Desktop\KOYUNCULAR_KATALOG\SLAYTLAR"


# Klasör içerisindeki dosyaların isimlerini al
file_names = os.listdir(folder_path)

# Şu anki zamanı al
current_time = time.time()

# Dosyalar için döngü oluştur
for file_name in file_names:
  # Dosya yolunu oluştur
  file_path = os.path.join(folder_path, file_name)
  
  # Dosya bilgilerini al
  file_stats = os.stat(file_path)
  
  # Dosya değişiklik tarihini al
  modification_time = file_stats.st_mtime
  
  # Dosya son 24 saat içinde değiştiyse
  if modification_time > current_time - 24 * 3600:
    # Dosya ismini yazdır
    print(file_name)
