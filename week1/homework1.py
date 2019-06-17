##1. HAFTA ÖDEVLER
## 
##1-
##Input ile kullanıcıdan bir kelime yazmasını isteyip, bu kelimeyi altı çizili ve etrafı desenli bir şekilde printleyin.
##



print("Kelime Susleme")
kelime= input("Kelime yaziniz:")
print("*"*((len(kelime)*3)+2),"\n","*",' '*len(kelime),kelime, ' '*len(kelime), '*',"\n","*",' '*len(kelime),"-"*len(kelime), ' '*len(kelime), '*',"\n","*"*((len(kelime)*3)+2),sep="")


##2-
##Kullanıcıdan input ile km cinsinden mesafe bilgisi alıp, bu bilgiyi mile dönüştürün ve sonucu ekrana printleyin.
## 1 km = 0,621371192 mil



print("\nKm - mil donustume")
km= int(input("Degeri km cinsinden giriniz:  "))
mil= km*0.621371192
print("{} km {} mildir. ".format(km,mil))






##3-
##Oğrenci not ortalama programi
##
##Icerik:
##Kullanicidan input ile ad-soyad, vize, final ve ders takip bilgilerini alip bu degerleri yuzdelik oranlarina gore hesaplayin ve yil sonu notunu cikarin.
##
##Yontem:
##-Sinav puanlari ve ders takip puani 0-100 arasidir. 
##-Bir öğrencinin gitmesi gereken toplam ders sayısı 20’dir. Kaçırılan her ders için 5 puan kırılacaktır. (Orn: 3 ders kaciran bir ogrencinin ders takip puani: 100-(3x5)=85 )
##Oranlar :
##- Vize Notu ( 30%)
##- Final Notu (50%)
##- Ders takip (20%)
##
##Sonuc:
##    0.    Output olarak ogrencinin yil sonu puanini ekrana pritleyin. 
##    0.    Ogrenci ad-soyad, vize-final-ders takip bilgilerini ve hesapladiginiz yil sonu puanini “ogrenciNotHesaplama” isimli bir dosyaya kaydedin.

print("\n OGRENCI NOT ORTALAMA PROGRAMI ")
adsoyad = input("Ogrencinin adi-soyadi: ")
vize = int(input("Ogrencinin vize notu: "))
final = int(input("Ogrencinin final notu: "))
takip = int(input("Ogrencinin devamsizlik gun sayisi: "))
derstakipnotu = 100 - (takip*5)
yilsonu = vize * (3/10) + final * (5/10) + vize * (2/10)

print(""" Ogrencinin adi-soyadi: {}
Ogrencinin vize puani: \t{}
Ogrencinin final notu: \t{}
Ogrencinin ders takip notu: \t{}
Ogrencinin yil sonu notu: \t{} """.format(adsoyad,vize,final,derstakipnotu,yilsonu))


dosya= open("ogrenciNotHesaplama.txt","w")
print(adsoyad,vize,final,derstakipnotu,yilsonu, file=dosya)
dosya.close()




##4-
##Faiz hesaplama programi
##
##Icerik:
##Kullanicidan gerekli bilgileri alip faiz tutarini hesaplayin.
##
##Yontem:
##Bu programi calistirabilmeniz icin asagida belirtilen bilgileri input yardimi ile kullanicidan almaniz gerekmektedir. 
##    ⁃    Ana para
##    ⁃    Faiz suresi (yil)
##    ⁃    Faiz orani
##
##Faiz hesaplama formulu:
##Ana para x faiz suresi x faiz orani / 100
##
##Sonuc:
##Gerekli islemleri yaptiktan sonra output olarak toplam faiz tutarini, aylik ve gunluk ortalama faiz tutarini, toplam para miktarini (faiz+ana para);
## 1) print ile ekrana yazin,
## 2) ”faizHesaplama” isimli bir dosyaya        
##     kaydedin.

print("\n FAIZ HESAPLAMA PROGRAMI ")
anapara = float(input("Ana Para : "))
sure = int(input("Faiz Suresi(Yil): "))
oran = float(input("Faiz Orani : "))

faiz = anapara*sure*(oran/100)

print("Faiz: ", faiz)
dosya = open("faizHesaplama.txt","w")
print("Faiz: ",faiz, file=dosya)
dosya.close()

##5-
##Aylik masraf programi
##
##Icerik:
##Aylık giderleri ve bu giderlerin aylik gelire oranini hesaplayan bir program yapmanız istenmektedir.
##
##Yontem:
##Asagida belirtilen harcama kalemlerini ve aylik geliri kullanicidan input ile alip gerekli hesaplamalari yapin
##
##Harcama kalemleri:
##-mutfak, 
##-egitim,
##-giyim, 
##-ulasim.
##
##Sonuc:
##1-Kullanicinin aylik toplam masrafini ve bu masrafin aylik gelirine oranini ekrana printleyin. 
##2- Ayni sonucu “aylikmasraf” isimli bir dosyaya kaydedin.


print("\nAYLIK MASRAF  HESAPLAMA PROGRAMI")
mutfak=float(input("Mutfak masraflariniz: "))
egitim=float(input("Egitim masraflariniz: "))
giyim=float(input("Giyim masraflariniz: "))
ulasim=float(input("Ulasim masraflariniz: "))
gelir=float(input("Aylik geliriniz: "))

toplam = mutfak + egitim + giyim + ulasim

oran= toplam / gelir

print("Aylik toplam masrafiniz: {} Aylik gelirinize orani: {}".format(toplam,oran))

dosya = open("aylikmasraf.txt","w")
print("Aylik toplam masrafiniz: {} Aylik gelirinize orani: {}".format(toplam,oran), file=dosya)
dosya.close()






##6-
##Asagidaki ciktiyi 3 farkli yontem ile printleyin.
##
##Python’un kurucusu Guido Van Rossum, Hollanda’nin Amsterdam’daki  "Universiteit Van Amsterdam" okulundan  1982’de mezun olmuştur.



print("""\n\n Python’un kurucusu Guido Van Rossum, Hollanda’nin Amsterdam’daki  "Universiteit Van Amsterdam" okulundan  1982’de mezun olmuştur.""")

print(" Python’un kurucusu Guido Van Rossum, Hollanda’nin Amsterdam’daki  \"Universiteit Van Amsterdam\" okulundan  1982’de mezun olmuştur.")

print(' Python\'un kurucusu Guido Van Rossum, Hollanda\'nin Amsterdam\'daki  "Universiteit Van Amsterdam" okulundan  1982\'de mezun olmuştur.')




