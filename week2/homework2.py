
##1.ODEV: BURCUN NE?
##    Kullanicidan dogum gununu ve ayini isteyin, program hangi burc oldugunu soylesin.

print("Dogum Tarihini Gir Burcunu Ogren")

dogumgunu= int(input('Dogum tarihinizi giriniz(Gun) : '))   #Kullanicidan dogum tarihinin gunu integer veri tipiyle aldik
dogumayi= input('Dogum ayinizi giriniz(Ay) : ')     #Kullanicidan dogum tarihinin ayini string veri tipiyle aldik

if (dogumayi=='mart' and (dogumgunu<31 or dogumgunu>=22)) or (dogumayi=='nisan' and (dogumgunu>1 or dogumgunu<=22)):   # Kosul (ay ve tarih araligi) ve (diger ay ve tarih araligi)
  print("Burcunuz: Koc")
                                                             
elif (dogumayi=='nisan' and (dogumgunu<31 and dogumgunu>=21)) or (dogumayi=='mayis' and (dogumgunu>1 and dogumgunu<=21)):
  print("Burcunuz: Boga")
                                                                
elif (dogumayi=='mayis' and (dogumgunu<31 and dogumgunu>=22)) or (dogumayi=='haziran' and (dogumgunu>1 and dogumgunu<=23)):
  print("Burcunuz: Ikizler")
                                                                
elif (dogumayi=='haziran' and (dogumgunu<31 and dogumgunu>=22)) or (dogumayi=='temmuz' and (dogumgunu>1 and dogumgunu<=23)):
  print("Burcunuz: Yengec")
                                                                  
elif (dogumayi=='temmuz' and (dogumgunu<31 and dogumgunu>=24)) or (dogumayi=='agustos' and (dogumgunu>1 and dogumgunu<=22)):
  print("Burcunuz: Aslan")
                                                                  
elif (dogumayi=='agustos' and (dogumgunu<31 and dogumgunu>=23)) or (dogumayi=='eylul' and (dogumgunu>1 and dogumgunu<=22)):
  print("Burcunuz: Basak")

elif (dogumayi=='eylul' and (dogumgunu<31 and dogumgunu>=23)) or (dogumayi=='ekim' and (dogumgunu>1 and dogumgunu<=22)):
  print("Burcunuz: Terazi")
                                                                
elif (dogumayi=='ekim' and (dogumgunu<31 and dogumgunu>=23)) or (dogumayi=='kasim' and (dogumgunu>1 and dogumgunu<=22)):
  print("Burcunuz: Akrep")
                                                               
elif (dogumayi=='kasim' and (dogumgunu<31 and dogumgunu>=23)) or (dogumayi=='aralik' and (dogumgunu>1 and dogumgunu<=22)):
  print("Burcunuz: Yay")
                                                                
elif (dogumayi=='aralik' and (dogumgunu<31 and dogumgunu>=22)) or (dogumayi=='ocak' and (dogumgunu>1 and dogumgunu<=20)):
  print("Burcunuz: Oglak")
                                                                 
elif (dogumayi=='ocak' and (dogumgunu<31 and dogumgunu>=21)) or (dogumayi=='subat' and (dogumgunu>1 and dogumgunu<=19)):
  print("Burcunuz: Kova")
                                                               
elif (dogumayi=='subat' and (dogumgunu<31 and dogumgunu>=20)) or (dogumayi=='mart' and (dogumgunu>1 and dogumgunu<=21)):
  print("Burcunuz: Balik")
else:  # degilse yanlis islem yaptiniz 
  print("Yanlis bir giris yaptiniz.")


##2.ODEV: UZAKLIK BIRIMI DONUSUMU
##    Kullanicadan 2 input alinacak:
##        1-km-mil donusumu mu yapmak istiyor, mil-km donusumu mu yapmak istiyor.
##        2-donusturmek istedigi birimin uzunlugu kactir?
##    Donusum yapilacak birimler mil ve kilometre olacak.

secim = int(input("\n KM MIL HESAPLAMA \nDonusum yapmak istediginiz nedir?\nKm- Mil ise 1,\nMil- Km ise 2 yaziniz: ")) # kullanicidan secim yapmasi istendi

if secim==1:   # eger secim 1 ise yani km-mil ise 
  km=float(input("Km: ")) # Kullanicidan km degeri alindi
  mil=km*0.62137  # formul
  print("Mil: ",mil,"dir")  # Sonuc gosterildi
  
else:   # degilse 
  mil=float(input("Mil: "))  #kullanicidan mil degeri istendi
  km=mil/0.62137   # formul
  print("Km: ",km,"dir")  # sonuc gosterildi 
  

##3.ODEV: PAROLA KARAKTER KONTROLU
##Kullanicidan 3-18 karakter arasinda bir username olusturmasini isteyin.
##Eger usernamede rakam varsa, rakam kullanamayacagina dair gerekli uyariyi yapin.
##Sonrasinda kullanicidan 6 ile 12 karakter araliginda bir parola olusturmasini isteyin.
##Olusturulan parolanin 6dan kisa ya da uzun olmasi durumlarinda gerekli uyarilari yapin. 
##Iki durumun sartlari da saglaniyorsa username ve parolayi hem ekrana printleyin hem de bir dosyaya kaydedin.


print("""\n KAYIT ISLEMI
*Kullanici adi 3-18 karakteri arasinda olmali ve rakam kullanilmamalidir.)
*Parolaniz 6-12 karakter araliginda olmalidir. """)
anahtar=1        # while kontrolu icin dongusu icin sayac tanimlandi 
while anahtar==1:   # kullanici adini dogru girene kadar istenecegi icin dongu kullanildi
  kullaniciadi= input("Kullanici Adiniz: ")  # once kullanici adi alindi
  
  if len(kullaniciadi)<3 or len(kullaniciadi)>18:  # eger 3ten kucuk veya 18den buyuk ise 
    print("Kullanici adinizda 3-18 araliginda karakter kullanmalisiniz. ")  # uyari veriyor 
  else:   # degilse dogru giris yapilmistir donguden cikmak icin anahtar=0 degeri verilerek dongu durduruluyor 
    anahtar=0 
    
anahtar2=1   # sifre icin ayni kontrol yapiliyor 
while anahtar2==1:
  sifre=input("Sifrenizi giriniz: ")
  if len(sifre)<6 or len(sifre)>12:
    print("Parolaniz 6-12 karakter araliginda olmalidir.")
  else:
    anahtar2=0
print("\nDosyaya kaydediliyor....")  
print("\nKullanici adiniz: ", kullaniciadi,"\nParolaniz: ",sifre)
dosya=open("dosya.txt","w")  # dosya.txt adli w kipinde dosya aciliyor 
print(sifre,file=dosya)    # yazdirma islemi yapiliyor 

  
  



##4.ODEV: SAYI TAHMIN OYUNU
##    Bir degiskene 1-10 arasinda bir sayi atayin.Kullanicidan bu sayiyi tahmin etmesini isteyin.
##    Kullanici 5 denemede bilirse 1 yildiz kazansin, 3 denemede bilirse 2 yildiz kazansin, 1 denemede bilirse 3 yildiz kazansin.



print("\n1 den 10a kadar bir sayi tuttum bil bakalim..5 deneme hakkin var")
sayi=5  # sayim 5 
sayac=0 # 5 deneme hakkini kontrol edecek degiskenim
anahtar=1  # donguyu kontrol edecek degiskenim
while anahtar==1: # anahtar=1 ise donguyu islet
  tahmin=int(input("Tahmininiz: "))  # Kullanicidan tahmin isteniyor 
  sayac+=1  # sayac 1 artiriliyor ki tahmin sayisi kontrol edilsin
  if sayi!=tahmin: # eger tuttugum sayi ile ayni degilse 
    print("Bilemediniz...") # mesaj donduruluyor 
    
  elif sayi==tahmin:  # tuttugum sayi ile ayniysa 
    anahtar=0  # donguden cik 
    if sayac==4 or sayac==5: # kac yildiz alacagini hesap etmek icin sayaci kullaniyoruz 4 - 5 ise 
      print("Tebrikler", "\u2b50" ," kazandiniz.") # tek yildiz kazandi \u2b50 yildiz seklinin unicode karsiligi 
      
    elif sayac==2 or sayac==3:   # eger 2 veya 3 denemeden bildi ise 
      print("Tebrikler", "\u2b50" * 2 ," kazandiniz.") # 2 yildiz kazandi yildiz sekli 2 ile carpildi
     
    else: # degilse ilk denemede bilmistir 
      print("Tebrikler", "\u2b50" * 3 ," kazandiniz.") # 3 yildiz kazandi 
  if sayi!=tahmin and sayac==5:  # 5 deneme kontrolu icin while icindeyken kontrol ediliyor sayi dogru tahmin edilemediyse ve sayac 5se yani deneme hakki bittiyse
    print("Deneme hakkiniz bitti :( ") # kullaniciyi bilgilendir 
    anahtar=0  #donguden cik 
   



##5.ODEV: ATM
##Kullanicinin hesabinda 1000 € olsun. Kullaniciya hangi islemi yapmak istedigini sorun. Kullanicinin yapabilecegi islemler:
##        1-bakiye kontrolu
##        2-para yatirma
##        3-para cekme
##    Kullanici hesabinda olan paradan fazla para cekmek isterse uyarin ve islemi yapamayacagini soyleyin.
##    2. ve 3. islemler sonucunda guncel bakiyeyi kullaniciya gosterin. Baska bir islem yapmak isteyip istemedigini sorun.

bakiye=1000.0  # hesabimda varsayilan para 
print("""
Yapabileceginiz islemler:
1-bakiye kontrolu
2-para yatirma
3-para cekme
""")   # kullaniciyi bilgilendirme 
cikis=' '  
while cikis==' ': # cikti degeri " " oldugu surece donguyu dondur 
  secim=int(input("Istediginiz islemi secmek icin numarasini girin: "))  # kullanicidan secim yapmasi isteniyor
  if secim==1:   # 1 ise 
    print("Bakiyenizde ",bakiye," Euro bulunuyor.") # bakiyeyi yazdir 
    
    kontrol=input("\nBaska bir islem yapmak istiyor musunuz(evet / hayir)   : ")  # devam edip isteyip istemedigini sor 
    if kontrol=='evet': # evetse 
      cikis=' ' # dngu sarti devam
    else:
      cikis="a" # hayirsa dongu sartini degistir 
    
  elif secim==2:  # 2 ise 
    miktar=float(input("Yatirmak istediginiz miktari giriniz: ")) # miktari al
    bakiye+=miktar # bakiyeye ekle 
    print("Bakiyenizde ",bakiye," Euro bulunuyor.") # guncel bakiyeyi yazdir 

    kontrol=input("\nBaska bir islem yapmak istiyor musunuz(evet / hayir)    :") # tekrar sor islem yapip yapmak istemedigini
    if kontrol=='evet':
      cikis=' '
    else:
      cikis="a"

  elif secim==3:  # 3 ise 
    miktar=float(input("Cekmek istediginiz miktari giriniz: ")) # miktari al 
    if bakiye<miktar:  # istenilen miktar bakiyede yoksa 
      print("Boyle bir islem yapamazsiniz.") # uyar 
      print("Bakiyenizde ",bakiye," Euro bulunuyor.") # hesabi goster 
      kontrol=input("\nBaska bir islem yapmak istiyor musunuz(evet / hayir)    :")  #cikis kontrol 
      if kontrol=='evet':
        cikis=' '
      else:
        cikis="a"
    else:  # bakiyede istenilen miktar varsa 
      bakiye-=miktar # bakiyeden cikar 
      print("Bakiyenizde ",bakiye," Euro bulunuyor.")  #guncel bakiyeyi goster 
      kontrol=input("\nBaska bir islem yapmak istiyor musunuz(evet / hayir)     :") #cikis kontrol yap
      if kontrol=='evet':
        cikis=' '
      else:
        cikis="a"
  else:  # islemlerden hicbiri degilse 
    print("Yanlis bir islem yaptiniz.")  # uyar 
    kontrol=input("\nBaska bir islem yapmak istiyor musunuz(evet / hayir)    :") # cikis kontrolu yap
    if kontrol=='evet':
      cikis=' '
    else:
      cikis="a"
  
  
  #FEEDBACK 
  #1. Kodlar calisiyor
  #2. 3. soruda sayinin 1 10 araliginda oldugu kontrolu yok bu acik olabilir mi bilemedim.
  #3. mantik hatasi da yok 
  #4. degisken isimleri anlasilir
  #5. gereksiz tekrar var ama istenilen program boyle oldugu icin tekrar ettirdim
  #6. algoritmalar mantikli
  #7. yorum ekledim hersey icin
  #8.isledigim konular kapsaminda olmasi icin gayret ettim :) bazi kodlarin ne kadar buyuk nimet oldugunu anladim 
  #9. Kodlar tamamen ozgun bana ait.. 
  #10.Olabilecek en kisa hali 






