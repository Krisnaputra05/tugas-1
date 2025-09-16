from PIL import Image
import matplotlib.pyplot as plt

# Load gambar asli
gambar_asli = Image.open("img/RGB.jpg")

# Konversi gambar asli ke mode "RGB"
gambar_asli = gambar_asli.convert("RGB")

# Mendapatkan ukuran gambar
w, h = gambar_asli.size

# Membuat gambar-gambar hasil rotasi
gambar_rotasi_90 = Image.new("RGB", (h, w))
gambar_rotasi_180 = Image.new("RGB", (w, h))
gambar_rotasi_270 = Image.new("RGB", (h, w))

for x in range(w):
    for y in range(h):
        piksel_asli = gambar_asli.getpixel((x, y))
        
        # Rotasi 90 derajat searah jarum jam
        gambar_rotasi_90.putpixel((h - y - 1, x), piksel_asli)
        
        # Rotasi 180 derajat
        gambar_rotasi_180.putpixel((w - x - 1, h - y - 1), piksel_asli)
        
        # Rotasi 270 derajat searah jarum jam
        gambar_rotasi_270.putpixel((y, w - x - 1), piksel_asli)
        
gambar_rotasi_90.save("report/rotasi90.png")
gambar_rotasi_180.save("report/rotas180.png")
gambar_rotasi_270.save("report/rotasi270.png")

print("Gambar rotasi berhasil disimpan")