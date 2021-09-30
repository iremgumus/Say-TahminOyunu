print("""****************

Sayı tahmin oyunu
1 ile 40 arasında bir sayı söyleyiniz.
7 hakkınız vardır.

***************""")

import random
import time

rastgele_sayı = random.randint(1,40)
hak = 7

while True:
    sayı = int(input("Sayı giriniz:"))
    if (sayı < rastgele_sayı):
        print("Sorgulanıyor...")
        time.sleep(1)
        print("Daha büyük bir sayı giriniz")
        hak -= 1
        print("Hakkınız:",hak)
    elif (sayı > rastgele_sayı):
        print("Sorgulanıyor...")
        time.sleep(1)
        print("Daha küçük bir sayı giriniz")
        hak -= 1
        print("Hakkınız:",hak)
    else:
        print("Sorgulanıyor...")
        time.sleep(1)
        print("Tebrikler başarılı tahminde bulundunuz.Sayınız:",rastgele_sayı)
        break
    if (hak == 0):
        print("Hakkınız kalmadı...")
        print("Sayınız:",rastgele_sayı)
        break
