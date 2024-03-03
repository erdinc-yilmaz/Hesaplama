# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 22:24:39 2024

@author: Erdinç (digitalistan)
"""

import matplotlib.pyplot as plt
import numpy as np

while True:
    try:
        AC = int(input("AC kenar uzunluğunu girin: "))
        if AC < 3 or AC > 10:
            print("Lütfen 3 ile 10 arasında bir tamsayı girin.")
            continue  # Giriş değeri uygun değilse döngünün başına geri dön
        break  # Giriş değeri uygunsa döngüden çık
    except ValueError:
        print("Geçersiz giriş. Lütfen bir tamsayı girin.")

while True:
    try:
        AB = int(input("AB kenar uzunluğunu girin: "))
        if AB < 3 or AB > 10:
            print("Lütfen 3 ile 10 arasında bir tamsayı girin.")
            continue  # Giriş değeri uygun değilse döngünün başına geri dön
        break  # Giriş değeri uygunsa döngüden çık
    except ValueError:
        print("Geçersiz giriş. Lütfen bir tamsayı girin.")



# En büyük değeri bul
en_buyuk = max(AC, AB)

# Veri oluştur
# x değerlerini oluştur
x = [i for i in range(en_buyuk + 1)]  # 0'dan A'ya kadar olan sayıları içeren liste

# Veri oluştur
# x değerlerini oluştur
y = [i for i in range(en_buyuk + 1)]  # 0'dan A'ya kadar olan sayıları içeren liste

X_AC_kenari = [0, 0] # AC_nin_X_koordinati_uzerindeki_noktalari
Y_AC_kenari = [0, AC] # AC_nin_Y_koordinati_uzerindeki_noktalari

X_AB_kenari = [0, AB] # AB_nin_X_koordinati_uzerindeki_noktalari
Y_AB_kenari = [0, 0] # AB_nin_Y_koordinati_uzerindeki_noktalari

X_BC_kenari = [AB, 0] # BC_nin_X_koordinati_uzerindeki_noktalari
Y_BC_kenari = [0, AC] # BC_nin_Y_koordinati_uzerindeki_noktalari

BC = np.sqrt(AB**2 + AC**2)

# Çizim yap
plt.plot(X_AC_kenari, Y_AC_kenari, color='blue')  # Grafik çizgisi AC
plt.plot(X_AB_kenari, Y_AB_kenari, color='red')  # Grafik çizgisi AB
plt.plot(X_BC_kenari, Y_BC_kenari, color='green')  # Grafik çizgisi BC


# Eksenlerin uzunluğunun bir birim büyük olması
en_buyuk_arti1 = en_buyuk+1

# Eksenleri ayarla
plt.xlim(-1, en_buyuk_arti1)  # X ekseni sınırlarını ayarla
plt.ylim(-1, en_buyuk_arti1)  # Y ekseni sınırlarını ayarla

# Eksen etiketlerini ekle
plt.xlabel('X Ekseni', color="0.5")
plt.ylabel('Y Ekseni', color="0.5")

# Grid ekleyerek arka planı düzenle
plt.grid(True, linewidth=0.5)  # Koordinat çizgileri kalınlığı

# Eksenlerin üzerindeki sayıların rengini değiştir
plt.gca().tick_params(axis='x', colors='0.5')  # X eksenindeki sayıların rengi
plt.gca().tick_params(axis='y', colors='0.5')  # Y eksenindeki sayıların rengi

# Eksenlerin eşit ölçekli olmasını sağla
plt.gca().set_aspect('equal')


# Açıları hesapla
alpha = np.arccos((AC**2 + BC**2 - AB**2) / (2 * AC * BC))
beta = np.arccos((AB**2 + BC**2 - AC**2) / (2 * AB * BC))
gamma = np.arccos((AB**2 + AC**2 - BC**2) / (2 * AB * AC))


# Dereceye çevirip yazdır
print("C açısı (Alpha) (derece):", np.round(np.degrees(alpha)),"°") # sayılar üste veya alta yuvarlandı.
print("B açısı (Beta) (derece):", np.round(np.degrees(beta)),"°") # sayılar üste veya alta yuvarlandı.
print("A açısı (Gamma) (derece):", np.round(np.degrees(gamma)),"°") # sayılar üste veya alta yuvarlandı.

print(f"Hipotenüs BC kenarı = {BC: .2f}")

# Ölçüleri eksenlere göre yazılması
plt.text(0-0.3, AC/2, f"AC = b = {AC}", rotation=90, ha="center", va="center", fontsize=8, color="blue") # X ekseni etiketi yazılması
plt.text(AB/2, 0-0.4, f"AB = c = {AB}", rotation=0, ha="center", va="center", fontsize=8, color="red") # Y ekseni etiketi yazılması
plt.text((BC/2)*1.1, (AC/2)*1.1, f"BC = a = {BC: .2f}", rotation=360-np.degrees(beta), ha="center", va="center", fontsize=8, color="green") # XY ekseni etiketi yazılması

# Kenar noktalarını eksenlere göre yazılması
plt.text(0-0.3, 0-0.3, "A", ha="center", va="center", fontsize=8, color="blue") # X ekseni A noktası etiketi yazılması
plt.text(AB+0.3, 0-0.3, "B", ha="center", va="center", fontsize=8, color="red") # X ekseni B noktası etiketi yazılması
plt.text(0-0.3, AC+0.3, "C", ha="center", va="center", fontsize=8, color="green") # X ekseni C noktası etiketi yazılması

# Açı değerlerinin üçgen içine eksenlere yuvarlanarak noktasız yazılması
plt.text(0+0.5, 0+0.5, f"{int(np.round(np.degrees(gamma)))} °", ha="center", va="center", fontsize=7.5,) # A açısı etiketi yazılması
plt.text(AB*0.7, 0+0.5, f"{int(np.round(np.degrees(beta)))} °", ha="center", va="center", fontsize=7.5,) # B açısı etiketi yazılması
plt.text(0+0.5, AC*0.8, f"{int(np.round(np.degrees(alpha)))} °", ha="center", va="center", fontsize=7.5,) # C açısı etiketi yazılması

# Alanı hesapla
Alan = (AB + AC) * 2
print(f"Alan = {Alan: .2f}")

# Çevreyi hesapla
Çevre = AB + AC + BC
print(f"Çevre = {Çevre: .2f}")

# Alan ve Çevrenin X, Y eksenine yazılması
plt.text(en_buyuk-0.5, en_buyuk, f"Alan = {Alan: .2f}", ha="center", va="center", fontsize=8) # X ekseni etiketi yazılması
plt.text(en_buyuk-0.5, en_buyuk-1, f"Çevre = {Çevre: .2f}", ha="center", va="center", fontsize=8) # X ekseni etiketi yazılması


# Grafiği göster
plt.show()


