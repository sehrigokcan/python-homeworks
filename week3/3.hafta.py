##1.ODEV: HESAP OLUSTURMA
##Kullanicidan, kullanici adi ve parola olusturarak hesap olusturmasini isteyin. Bu aldiginiz bilgileri bir dosyaya yazdirin.
#Her gırıste dosyadakı bılgıler sıfırlanmasın kayıt bılgılerı dosyaya eklenmeye devam etsın.
#Kullanici daha once girilmis olan bir kullanici adiyla hesap olusturmak isterse, bu kullanici adinin daha once secildigini ve baska bir kullanici adiyla hesap olusturmasini isteyin.

print("\t HESAP OLUSTUR \n")
while True:        # kullanicinin varolan kullaniciadi secmesi ihtimalinden kodlari dongu icine aldik
  kullaniciadi=str(input("Kullanici Adiniz: "))  
  parola=str(input("Parolaniz: "))

  file=open("HesapBilgileri.txt","r")  # dosyamizi readable olarak actik
  veri=file.read() # dosya icindeki verileri string deger olarak veri degiskenine atadik 
  if kullaniciadi in veri:  # eger veri degiskeninde yani dosya icinde kullaniciadi varsa 
    print("Bu kullanici adi daha once alinmis. Lutfen baska bir kullanici adi seciniz.") #uyar
  else: #degilse 
    file=open("HesapBilgileri.txt","a")  # dosyayi sonradan eklenebilir actik
    veri=kullaniciadi+"\t"+parola+"\n"  # girecegimiz degeri veri degiskenine atadik 
    file.write(veri)  # dosyaya yazdirdik 
    file.close()  #kapattik
    print("Hesabiniz basariyla olusturuldu..")  # kullaniciya bilgi mesaji verdik
    break  # islem tamamlandigina gore donguden ciktik 





##2.ODEV: SAYI TAHMIN OYUNU
##   Bir degiskene 0-100 arasinda bir deger atayin. 
# Kullanicidan bu sayiyi tahmin etmesini isteyin. 
# Kullaniciyi yaptigi tahminlere gore yonlendirin. Kacinci denemede bildigini soyleyin.


print("""
\tSAYI TAHMIN OYUNU
""")
#WHILE DONGUSU ILE
sayi=78  # tuttugum sayi 
thmn=0
while True:     #bulana kadar donguyu dondur 
  tahmin=int(input("Tahmininiz: ")) #  kullanicidan tahmini al 
  thmn+=1 # deneme sayisini bulmak icin degiskeni 1 arttir
  if (tahmin==sayi):     # eger dogruysa
    print("Tebrikler...",thmn,". denemende bildin...")  # tebrik edip 
    break  # donguden cik 
  elif tahmin>sayi :  # tahmin buyukse 
    if tahmin-sayi<=5:  # ve tahmin ile sayi arasinda fark 5 ise yani cok yaklastiysa 
      print("Ooo cok yaklastin.. Hadi bakalim ... Biraz daha asagi..")
    else:  #degilse 
      print("Fazla yukari ciktin daha kucuk sayi...")
  elif(tahmin<sayi):  # # eger tahmin edilen sayi kucukse 
    if sayi-tahmin<=5:  # ve yaklasik bir sayi girildiyse 
      print("Ooo cok yaklastin.. Hadi bakalim ... Biraz daha yukari..")
    else:
      print("Fazla yukari ciktin daha buyuk sayi...")

# For dongusu ile 

sayi=78  # tuttugum sayi 
for  i in range(1,50):     #bulana kadar azami 50 deneme hakki verdik 
  tahmin=int(input("Tahmininiz: ")) # kullanicidan tahmini al 
  if (tahmin==sayi):    # eger dogruysa 
    print("Tebrikler...",i,". denemende bildin...") # tebrik edip 
    break # donguden cikiyoruz 
  elif tahmin>sayi :  # tahmin buyukse 
    if tahmin-sayi<=5:  
      print("Ooo cok yaklastin.. Hadi bakalim ... Biraz daha asagi..")  # bu uyariyi ver 
    else:  # degilse 
      print("Fazla yukari ciktin daha kucuk sayi...")  #bu uyariyi ver 
  elif(tahmin<sayi):  # eger tahmin edilen sayi kucukse 
    if sayi-tahmin<=5:  # ve yaklasik bir sayi girildiyse 
      print("Ooo cok yaklastin.. Hadi bakalim ... Biraz daha yukari..")  # bu uyariyi ver 
    else:  # degilse 
      print("Fazla yukari ciktin daha buyuk sayi...")  # bu uyariyi ver 



##3.ODEV: LISTE AYIKLAMA
##   Ekte gonderilmis olan text dosyasinda 3 takimin futbolcularinin isimleri ve takimlari yer almaktadir. Sizden 3 tane dosya olusturmanizi
##   ve bu 3 dosyaya futbolculari takimlarina gore ayirmanizi istiyoruz. Ayrica kaynak dosyanin bulunamamasi durumunda da gerekli uyariyi yapmalisiniz.

print("\n DOSYA AYIKLAMA \n")

file=open("futbolcular.txt")  # ayiklayacagimiz dosyayi actik
veri=file.readlines()  # dosya icindekileri satir satir liste seklinde veri degiskenine atadik
for i in veri:  #veri listesindeki elemanlari tek tek gostermek icin for dongusu actik 
  if "Fenerbahçe" in i:  #eger listenin elemaninda yani bir satirlarinda Fenerbahce varsa
    file1=open("fb.txt","a") # fb.txt dosyasini ac 
    file1.write(i) # listedeki veriyi bu dosyaya yaz 
  elif "Galatasaray" in i: # galatasaray yaziyorsa 
    file2=open("gs.txt","a")
    file2.write(i)
  elif "Besiktas" in i:  # besiktas yaziyorsa 
    file3=open("bjk.txt","a")
    file3.write(i)
  else:
    print("Kaynak dosyalar bulunamiyor...")
    
file.close()    #dosyalari kapattik  
file1.close()  
file2.close()
file3.close()
print("Dosyaniz ayiklandi...")

    






      
##
##4.ODEV: ALAN-HACIM HESAPLAMA
##   Karenin, ucgenin ve diktortgenin alanlarini hesaplayan, kup,kure ve koni seklinde olan cisimlerin hacmini hesaplayan bir program yazmanizi istiyoruz.
# Kullanicidan hangi seklin alanini veya hangi sekildeki cismin hacmini hesaplamak istedigini sormalisiniz ve o islem icin gereken verileri isteyip hesaplamayi yapmalisiniz.
#Tum bu islemleri yaparken hata alinabilecek durumlari ongorerek gerekli onlemleri almalisiniz.
menu="""
\t\tALAN HESAPLAMALARI
\t1.Kare
\t2.Ucgen
\t3.Dikdortgen

\t\tHACIM HESAPLAMALARI
\t4. Kup
\t5. Kure
\t6. Koni
Istenen hesaplamanin numarasini giriniz.
Cikmak isterseniz "q" basiniz...
"""
print(menu)

while True:
  islem=input("\nIstediginiz islemin numarasini giriniz: ")
  if islem=="1":
    kenar=float(input("Karenin bir kenar uzunlugunu giriniz: "))
    print("Karenin Alani: " , pow(kenar,2), " m²")
  elif islem=="2":
    tabanuzunlugu=float(input("Taban uzunlugunu giriniz: "))
    yukseklik=float(input("Yukseklik degerini giriniz: "))
    print("Ucgenin Alani: ", (tabanuzunlugu*yukseklik)/2, " m²")
  elif islem=="3":
    kenar1=float(input("Kenar uzunlugunu giriniz: "))
    kenar2=float(input("Kenar uzunlugu giriniz: "))
    print("Dikdortgenin Alani: ", kenar1*kenar2, " m²")
  elif islem=="4":
    kenar=float(input("Kupun bir kenar uzunlugunu giriniz: "))
    print("Kupun Hacmi: " , pow(kenar,3), " m³")
  elif islem=="5":
    yaricap=float(input("Yaricapi giriniz: "))
    print("Kurenin Hacmi(♎ 3 alirsak): ",4/(3*3*pow(yaricap,3))," m³")
  elif islem=="6":
    yaricap=float(input("Yaricapi giriniz: ")) 
    yukseklik=float(input("Yukseklik degerini giriniz: "))
    print("Koninin Hacmi: (♎ 3 alirsak)", (1/3)*3*pow(yaricap,2)*yukseklik, " m³")
  elif islem=="q":
    print("Gule gule... ")
    break
  else:
    print("Yanlis bir islem yaptiniz..Lutfen menudeki degerlerden birini giriniz..\n",menu)
    pass





##5.ODEV: FIZZ BUZZ
##   1'den 100'e kadar sayilari yazdirin. Fakat 3'e tam bolunen sayilarin yerine FIZZ, 5'e tam bolunen sayilarin yerine BUZZ, hem 3'e hem de 5'e tam bolunebilen sayilarin yerine FIZZBUZZ yazsin.


print("\n FIZZ BUZZ \n")

for i in range(1,101):  # range ile 1 den baslanip 100e kadar sayilar kontrolu icin for acildi
  if i%3==0 and i%5==0: # eger 3 ve 5 bolumunden kalan 0 ise  
    print("FIZZBUZZ")
  elif i%5==0:  # eger 5 ile bolumunden kalan 0 ise 
    print("BUZZ")
  elif i%3==0:   # eger mod 3 0 ise 
    print("FIZZ")
  else:   # hic biri degilse sayiyi yazdir 
    print(i)









##6.ODEV: ASAL SAYI MI?
##   Kullanicidan aldiginiz sayinin asal sayi olup olmadigini sorgulayan bir program yazmanizi istiyoruz.

print("\tASAL SAYI KONTROLU ")

sayi=int(input("Sayi giriniz: "))
for i in range(2,sayi):  # eger sayi 1 haric 2 den kendi degerine kadar hicbir sayi ile bolunmuyorsa asaldir 
  if sayi%i==0:  # sayinin kendisinden kucuk her degerle bolunup bolunmedigi kontrolu yapiliyor 
    print("Sayi Asal Degil...")  # bolunmusse asal degildir 
    break   # donguden cik 
  else:
    print("Sayi Asal sayidir...Kendisinden baska hicbir boluneni yok.")   # degilse asaldir 
    break   #donguden cik 



#2. secenek
sayi=int(input("Sayi giriniz: "))
sayac=0
for i in range(2,sayi):
  if sayi%i==0:
    sayac+=1   # eger bolunuyorsa sayaci 1 arttir 
    break
if sayac!=0:  #sayac 0dan farkliysa yani bolundugu bir deger varsa 
  print("Asal sayi degildir")   # asal degil 
else:
  print("Asal sayidir")


