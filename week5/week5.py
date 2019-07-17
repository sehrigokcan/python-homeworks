##*ODEV 1: ADAM ASMACA*
## -Onceden belirlenmis bir kelime degiskene atanacak ve kullanicidan bu kelimeyi harf tahminleriyle bilmesi istenecek.
## -Kullanicinin 6 hamle sansi olacak ve her bir yanlis hamlesinde kalan hamle sayisini gosterin. Ayrica yine her bir yanlis hamle sonucunda adam asmaca oyunu oynarken cizdigimiz yanlis hamle sonucundaki cizimleri sizde ekranda karakterleri kullanarak gosterin.
## -Kullanici harf disinda bir karakter girdiginde gerekli uyariyi yapin ve bunu da yanlis hamle olarak saymayin. Oyun devam etsin.
## -Bir yanlis ve bir dogru hamle yapilmis ornek kod ciktisi:
##
##                          ____
##                         |     |
##                         |     O           5 HAKKINIZ KALDI!!!
##                         |
##                         |
##                        ---
##
##          - a -  -  -  - a -
##
##         harf:
kelime="hollanda"  # kelimemiz  
kelime=list(kelime)    # listeye cevirdik 
k=['-','-','-','-','-','-','-','-']  # kelimenin bos hali 
hak=6  # 6 tane deneme hakki var 
adamasmaca0="""

                          ____
                         |     |
                         |     O      
                         |    /|\\
                         |     |
                         |    /|\\
                        ---\n"""
adamasmaca1="""

                          ____
                         |     |
                         |     O      
                         |    /|\\
                         |     |
                         |     |
                        ---\n"""
adamasmaca2="""

                          ____
                         |     |
                         |     O      
                         |    /|\\
                         |     |
                         |    
                        ---\n"""

adamasmaca3="""

                          ____
                         |     |
                         |     O      
                         |    /|\\
                         |     
                         |    
                        ---\n"""


adamasmaca4="""

                          ____
                         |     |
                         |     O        
                         |     |
                         |     
                         |    
                        ---\n"""

adamasmaca5="""

                          ____
                         |     |
                         |     O        
                         |    
                         |     
                         |    
                        ---\n"""
adamasmaca6="""

                          ____
                         |     |
                         |            
                         |    
                         |     
                         |    
                        ---\n"""

adamasmaca=[adamasmaca0,adamasmaca1,adamasmaca2,adamasmaca3,adamasmaca4,adamasmaca5,adamasmaca6] # durumlari listeye attik

while True:
  bilgi=" {0}\n\t\t{1} HAKKINIZ KALDI\n\n\n".format(adamasmaca[hak],hak)  # durum bilgisi 
  print(bilgi) # yazdiriyoruz 
  for i in k:  # kelimeyi yazdiriyoruz 
    print(*i,end=" ")
  
  harf=input("\nHarf Giriniz: ")   # harf tahminini kullnicidan istedik 
  if not harf.isalpha() or len(harf)!=1:  # eger harf girisi dogru degilse 
    print("Yanlis giris yaptiniz tekrar deneyiniz...")  # uyari veriyoruz 
    continue  # dongunun basina don 
  else:  # degilse 
    if not harf in kelime:  # harf kelime listesinin icinde degilse yani yanlis tahminse 
      hak-=1  # 6 hakkindan 1 ini azalt 
    else: # degilse yani dogruysa 
      for i in range(len(kelime)):  # 
        if kelime[i]==harf:  # kelime listesindeki indexini harfle degistir 
          k[i]=harf  #kelime listesindeki indexini harfle degistir 
    
  if kelime==k:  # eger kelime listesi ile k listesi esitse yani butun harfler bulunmussa  
    print("\nKelimeyi buldunuz.. Tebrikler..")  # tebrik ettik
    print(bilgi)  # son hali yazdirilir 
    for i in k:  # kelimeyi yazdirdik 
      print(*i,end=" ")
    break # bulundguna gore donguden cikabiliriz 
  if hak==0: # eger hakki bitmisse 
    print("Hakkiniz bitti..:(")  # uyariyi verdik 
    print(" {}\n\t\t{} HAKKINIZ KALDI\n\n\n\t".format(adamasmaca[0],0))  # ve adamin asilmis halini yazdirdik 
    for i in kelime:   # dogru kelimeyi yazdirdik 
      print(*i,end=" ")
    break  # hakki bittigine gore donguden cikabiliriz 


##*ODEV 2:SAYI TAHMIN OYUNU:*
## Kendiniz 4 basamakli, rakamlari birbirinden farkli ve icerisinde 0 rakaminin yer almadigi bir sayi belirleyin. 
# Kullanicidan bu sayiyi tahmin etmesini isteyin. Yapilan tahmin sonucu kullanicinin, 
# tahminde bulundugu sayidaki rakamlarin degeri ve yeri dogruysa +1, degeri dogru fakat yeri dogru degilse -1 ciktisi verecegiz. 
# Bu sekilde tahminde bulunmaya devam etmesi saglanacak ve 
# sayiyi tam bir sekilde dogru bildiginde gerekli bilgilendirme yapilip oyun bitirilecek.
##
##  Ornek:           sayi = 1234
##
##         yapilan tahmin = 9831
##
##         (Burada "9" ve "8" rakamlari yanlis oldugu icin ciktiya bir etkisi yok. "3" rakaminin yeri dogru oldugu icin +1, "1" rakami sayi icerisinde yer alan fakat yeri yanlis oldugu icin -1 ciktisi verecegiz.)
##
##         ornek output = +1 -1
##
##         yapilan tahmin = 2134
##
##         ("2" ve "1" rakamlari sayi icerisinde yer aldigi fakat yerlerinin yanlis olmasi nedeniyle ikisi icin -1, "3" ve "4" rakamlarinin yerleri de dogru oldugu icin +1 degerleri donecegiz.)
##
##         ornek output = +2 -2
##
##         yapilan tahmin = 9876
##
##         ornek output = +0 -0
##
##         yapilan tahmin = 2146
##
##         ornek output = +0 -3
print("""\nSAYI TAHMIN OYUNU

Not: Lutfen rakamlari birbirinden ve 0dan farkli 4 basamakli sayi girisi yapiniz.
Cikis icin "q" tusuna tiklayabilirsiniz...
""")


sayi="1234"  # sayim 
sayi=list(sayi)  # listeye cevirdik 
s=0  # sayacim 0 

while True:
  deger1=0  # deger1 0
  deger2=-0  # deger2 0
  s+=1  # sayacimi bir artirdim 
  tahmin=list(input("{}. Tahmininizi Giriniz: ".format(s)))  # tahmin istedik kontrol kolayligi icin listeye cevirdik
  
  for i in tahmin:   # tahmin listemizde donguyle geziyoruz 
    if i in sayi and tahmin.index(i)==sayi.index(i):  # eger sayi listemde i varsa ve indexleri esitse 
      deger1+=1  # deger1 1 arttir 
    elif i in sayi:  # eger sadece icinde varsa indexleri ayni degilse 
      deger2+=1 # deger2 1 arttir 
  if sayi==tahmin:  # esitse sayi ile tahmin 
    print("Tebrikler tahmin dogru...")  # tebrik ettik
    break  # programi kapattik 
  print("+{}  -{}".format(deger1,deger2))   # dongu her bittiginde +deger1 ve -deger2 olarak gosterecek 


##*BONUS ODEV:*
##
## # İki liste tanımlayın.
## # İlk liste 1'den 10'a kadar sayılardan oluşturun.
## # İkinci listeyi sırasıyla a'dan başlayarak 10 harf ile oluşturun.
## # İki liste için de döngü kurup, iki listenin elemanlarının bütün kombinasyonlarından oluşan iki yeni liste oluşturun.
##
## # 3'er elemanli versiyonunda cıktı olarak bu şekilde bir çıktı beklenmektedir:
##
## # 1. [1a, 1b, 1c, 2a, 2b, 2c, 3a, 3b, 3c]
## # 2. [a1, a2, a3, b1, b2, b3, c1, c2, c3]

sayilar=["1","2","3","4","5","6","7","8","9","10"]  #10 sayi 
harfler=['a','b','c',"d","e","f","g","h","i","i"]  # 10 harf
liste1=[]
liste2=[]
for i in sayilar:  # sayilar listesi elemanlari 
    for b in harfler:  # harfler listesi elemanlari 
      liste1.append(i+b) #sirasi ile liste1 yazdir  


for i in harfler:
  for b in sayilar:
    liste2.append(i+b) 

print("1: ",liste1)
print("2: ",liste2)