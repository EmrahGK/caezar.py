import os as pc
import time

pc.system('cmd /c "color b"')

print("""
_______________________________________________
   Şifreleyici ve Şifreyi Çözücü Program
        (çıkmak için q'ya basın)
            İşlemler:
                1.Şifrele
                2.Şifreyi çöz
        NOT: Kaç harli şifreleme
        yapıldığını bilmiyorsanız
        İlk soruyu 'Sezar' olarak
        yanıtlayın.
______________________________________________
""")


def rotate(alfabe,d):
    Lfirst = alfabe[0 : d] 
    Lsecond = alfabe[d :] 
    return Lsecond + Lfirst

def sifrele(yazi, d):
    return yazi.translate(str.maketrans(normal, rotate(normal, d)))

def sifreyi_coz(yazi, d):
  return yazi.translate(str.maketrans(rotate(normal, d), normal))

def kucult(metin):
    try:
        metin = metin.lower()
    except:
        print("HATAAAAAAAA'!'!'!'!")
        time.sleep(1)
        

normal = "abcçdefgğhıijklmnoöprsştuüvyz0123456789!'^+%&/()=?_"
#80 karakter uzunluğunda: print(len(normal))

while(True):
    
    sayi = input("\nKaç harfli şifreleme yapmak istiyorsunuz: ")

    if(sayi == "Sezar" or sayi =="sezar" or sayi == "Caesar" or sayi == "caesar"):
        time.sleep(0.5)
        print("\nSezar fonksiyonu, kaç harfli şifreleme yapıldığını bilmediğiniz durumlar içindir. \n\n")
        sinir = range(0,51)
        asd = 0
        sayi_liste = []
        metin = str(input("Şifresi bilinmeyen metni girin: "))
        
        try:
            metin = metin.lower()
        except:
            print("HATAAAAAAAA'!'!'!'!")
            time.sleep(1)
            break

        for i in sinir:
            if(True):
                sayi_liste.append(i)
                
        while(not sayi_liste == []):
            asd += 1
            time.sleep(0.02)
            print("\n{}. Metin: ".format(asd),sifreyi_coz(metin,asd))
            if(asd >=50):
                print("Ana menüye yönlendiriliyorsunuz..")
                time.sleep(2)
                break

    elif(sayi == "q"):
        print("\nProgramdan çıkılıyor..")
        time.sleep(1)
        break 

    try:
        sayi = int(sayi)
    except ValueError:
        print("Lüfen bir 'sayı' girişi yapın..")
        time.sleep(0.3)
        print("Ana menüye yönlendiriliyorsunuz..")
        time.sleep(0.8)
        continue
    
    time.sleep(1)
    soru = str(input("İşlemi girin(1-2): "))
    
    if(soru == "1"):
        #şifreleme işlemi
        time.sleep(0.5)
        metin = str(input("Şifrelenmesini istediğiniz metni girin: "))
        
        time.sleep(0.5)
        print("{} harfli olarak şifrelenmiş metin: ".format(sayi),sifrele(metin,sayi))
    
    elif(soru == "2"):
        #şifreyi çözme işlemi
        time.sleep(0.5)
        metin = str(input("Şifresinin çözülmesini istediğiniz metni girin."))
        time.sleep(0.5)
        print("{} harfli olarak şifresi çözülmüş metin: ".format(sayi),sifreyi_coz(metin,sayi))

    else:
        print("Ana menüye yönlendiriliyorsunuz..")
        time.sleep(0.8)
        continue