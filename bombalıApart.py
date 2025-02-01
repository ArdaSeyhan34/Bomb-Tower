import random
import time
from time import sleep
def kapı_sec(kat):
    try:
        if kat<=2:bomba_sayısı=1
        elif kat<=6:bomba_sayısı=2
        elif kat<=9:bomba_sayısı=3
        else:bomba_sayısı=4
        bombalı_kapılar=[]
        kapılar=["kirmizi","mavi","yesil","sari","mor"]
        while True:
            secilen_renk=input("Seçmek istediğiniz kapının rengini giriniz: ")
            kucultulmus=secilen_renk.lower().replace('ı','i').replace('ö','o').replace('ü','u').replace('ş','s').replace('ğ','g').replace('ç','c').strip()
            if kucultulmus not in kapılar:print("Sadece kapıların renklerinden birini giriniz!!!")
            else:break
        if bomba_sayısı==1:bombalı_kapılar=[random.choice(kapılar)]
        elif bomba_sayısı>1:bombalı_kapılar=random.sample(kapılar,bomba_sayısı)
        sonuc=True
        for i in bombalı_kapılar:
            if kucultulmus==i:
                sonuc=False
                break
        return sonuc
    finally:
        print("Kapı seçimi yapıldı")
        print("OoOoOoOooOoOoOoOoO")
        sleep(2)
def oyunu_baslat():
    print("Merhaba Oyun Başlıyor!!!")
    print("Kirmizi, mavi, yesil, sari, mor\nBir tane renk seçin:")
    kat=1
    while kat<11:
        sonuc=kapı_sec(kat)
        if sonuc==False:
            print("BOOOMMM")
            exit()
        else:
            print(f"Tebrikler {kat}. katı başarıyla geçtiniz.")
            if kat==10:print("Oyunu tamamlayan Dünyadaki tek insan oldunuz, tebrikler!!!!!!")
            kat+=1

oyunu_baslat()
