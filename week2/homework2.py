
##1.ODEV: BURCUN NE?
##    Kullanicidan dogum gununu ve ayini isteyin, program hangi burc oldugunu soylesin.

print("Dogum Tarihini Gir Burcunu Ogren")

dogumgunu= int(input('Dogum tarihinizi giriniz(Gun) : '))
dogumayi= input('Dogum ayinizi giriniz(Ay) : ')

if (dogumayi=='mart' and (dogumgunu<31 or dogumgunu>=22)) or (dogumayi=='nisan' and (dogumgunu>1 or dogumgunu<=22)):
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
else:
  print("Yanlis bir giris yaptiniz.")


##2.ODEV: UZAKLIK BIRIMI DONUSUMU
##    Kullanicadan 2 input alinacak:
##        1-km-mil donusumu mu yapmak istiyor, mil-km donusumu mu yapmak istiyor.
##        2-donusturmek istedigi birimin uzunlugu kactir?
##    Donusum yapilacak birimler mil ve kilometre olacak.

secim = int(input("Donusum yapmak istediginiz nedir?\nKm- Mil ise 1,\nMil- Km ise 2 yaziniz: "))

if secim==1:
  km=float(input("Km: "))
  mil=km*0.62137
  print("Mil: ",mil,"dir")
  
else:
  mil=float(input("Mil: "))
  km=mil/0.62137
  print("Km: ",km,"dir")
  

##3.ODEV: PAROLA KARAKTER KONTROLU
##Kullanicidan 3-18 karakter arasinda bir username olusturmasini isteyin.
##Eger usernamede rakam varsa, rakam kullanamayacagina dair gerekli uyariyi yapin.
##Sonrasinda kullanicidan 6 ile 12 karakter araliginda bir parola olusturmasini isteyin.
##Olusturulan parolanin 6dan kisa ya da uzun olmasi durumlarinda gerekli uyarilari yapin. 
##Iki durumun sartlari da saglaniyorsa username ve parolayi hem ekrana printleyin hem de bir dosyaya kaydedin.


print(""" KAYIT
*Kullanici adi 3-18 karakteri arasinda olmali ve rakam kullanilmamalidir.)
*Parolaniz 6-12 karakter araliginda olmalidir. """)
sayac=1
while sayac==1:
  kullaniciadi= input("Kullanici Adiniz: ")
  
  if len(kullaniciadi)<3 or len(kullaniciadi)>18:
    print("Kullanici adinizda 3-18 araliginda karakter kullanmalisiniz. ")
  else:
    sayac=0
    
sayac2=1
while sayac2==1:
  sifre=input("Sifrenizi giriniz: ")
  if len(sifre)<6 or len(sifre)>12:
    print("Parolaniz 6-12 karakter araliginda olmalidir.")
  else:
    sayac2=0
print("\nKullanici adiniz: ", kullaniciadi," Parolaniz: ",sifre)
dosya=open("dosya.txt","w")
print(sifre,file=dosya)

  
  



##4.ODEV: SAYI TAHMIN OYUNU
##    Bir degiskene 1-10 arasinda bir sayi atayin.Kullanicidan bu sayiyi tahmin etmesini isteyin.
##    Kullanici 5 denemede bilirse 1 yildiz kazansin, 3 denemede bilirse 2 yildiz kazansin, 1 denemede bilirse 3 yildiz kazansin.



print("1 den 10a kadar bir sayi tuttum bil bakalim..5 deneme hakkin var")
sayi=5
sayac=0
yildiz=0
anahtar=1
while anahtar==1:
  tahmin=int(input("Tahmininiz: "))
  sayac+=1
  if sayi!=tahmin:
    print("Bilemedin...")
    
  elif sayi==tahmin:
    anahtar=0
    if sayac==4 or sayac==5:
      print("Tebrikler 1 yildiz kazandiniz.")
      
    elif sayac==2 or sayac==3:
      print("Tebrikler 2 yildiz kazandiniz.")
     
    else:
      print("Tebrikler 3 yildiz kazandiniz.")
  if sayi!=tahmin and sayac==5:
    print("Deneme hakkin bitti :( ")
    anahtar=0
   



##5.ODEV: ATM
##Kullanicinin hesabinda 1000 € olsun. Kullaniciya hangi islemi yapmak istedigini sorun. Kullanicinin yapabilecegi islemler:
##        1-bakiye kontrolu
##        2-para yatirma
##        3-para cekme
##    Kullanici hesabinda olan paradan fazla para cekmek isterse uyarin ve islemi yapamayacagini soyleyin.
##    2. ve 3. islemler sonucunda guncel bakiyeyi kullaniciya gosterin. Baska bir islem yapmak isteyip istemedigini sorun.

hesap=1000.0
print("""
Yapabileceginiz islemler:
1-bakiye kontrolu
2-para yatirma
3-para cekme
""")
cikis=' '
while cikis==' ':
  secim=int(input("Istediginiz islemi secmek icin numarasini girin: "))
  if secim==1:
    print("Bakiyenizde ",hesap," Euro bulunuyor.")
    
    kontrol=input("\nBaska bir islem yapmak istiyor musunuz(evet / hayir)")
    if kontrol=='evet':
      cikis=' '
    else:
      cikis="a"
    
  elif secim==2:
    miktar=float(input("Yatirmak istediginiz miktari giriniz: "))
    hesap+=miktar
    print("Bakiyenizde ",hesap," Euro bulunuyor.")
    kontrol=input("\nBaska bir islem yapmak istiyor musunuz(evet / hayir)")
    if kontrol=='evet':
      cikis=' '
    else:
      cikis="a"
  elif secim==3:
    miktar=float(input("Cekmek istediginiz miktari giriniz: "))
    if hesap<miktar:
      print("Boyle bir islem yapamazsiniz.")
      print("Bakiyenizde ",hesap," Euro bulunuyor.")
      kontrol=input("\nBaska bir islem yapmak istiyor musunuz(evet / hayir)")
      if kontrol=='evet':
        cikis=' '
      else:
        cikis="a"
    else:
      hesap-=miktar
      print("Bakiyenizde ",hesap," Euro bulunuyor.")
      kontrol=input("\nBaska bir islem yapmak istiyor musunuz(evet / hayir)")
      if kontrol=='evet':
        cikis=' '
      else:
        cikis="a"
  else:
    print("Yanlis bir islem yaptiniz.")
    kontrol=input("\nBaska bir islem yapmak istiyor musunuz(evet / hayir)")
    if kontrol=='evet':
      cikis=' '
    else:
      cikis="a"
  
  
  















