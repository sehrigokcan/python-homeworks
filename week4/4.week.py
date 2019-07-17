##1-)Kullanıcıdan bir input alınız. Input'taki küçük harfleri büyük harfe dönüştüren bir program yazınız.
##Ör input: Hello World! 
##Ör output: HELLO WORLD!

giris=input("Metin: ") # input aldik
print("Buyuk harfle metin: ",giris.upper())  # upper metodu ile inputu buyuk harfe cevirdik 



##2-)Kullanıcıdan bir input alınız. Girmiş olduğu inputta büyük harf sayısı, küçük harf sayısı, rakam sayısı ve bunların haricindeki
##özel karakter sayılarını veren bir program yazınız.

buyukharf=0  # degiskenlere degerleri almak icin onceden tanimlayip 0 atiyoruz 
kucukharf=0
rakam=0
ozelkarakter=0
giris=input("\n Incelemek istediginiz metni giriniz:  ")  #input giris degiskenine aldik
for i in giris:  # degiskenin elemanlari tek tek kontrol edicez
  if i.isupper(): # buyuk harfse 
    buyukharf+=1
  elif i.islower():  # kucuk harfse
    kucukharf+=1
  elif i.isnumeric():  # numerikse 
    rakam+=1
  else:   # hic biri degilse 
    ozelkarakter+=1

print("'{}' degerinde \n{} tane  buyuk harf, \n{} tane kucuk harf, \n{} tane rakam,  \n{} tane ozel karakter vardir.".format(giris,buyukharf,kucukharf,rakam,ozelkarakter))
  

##3-)Kullanıcıdan bir input alınız. Girmiş olduğu inputtaki rakamların toplamını veren bir program yazınız. (Kullanıcı rakam girmek zorunda değil.
##farklı karakter girişi de yapabilir.)
##Örnek input = "art12kl4*"



toplam=0
giris=input("\nRakamlari olan giris yapiniz:")   # kullanicidan input 
for i in giris:  #tek tek degeleri kontrol edelim
  if i.isnumeric():   # numerik ise 
    toplam+=int(i)  # toplam degiskenine sayiya cevirip topla

print("{} degerindeki rakamlarin toplami: {}".format(giris,toplam)) # islem bitince sonucu printle 




##4-)Futbolcular dosyasındaki futbolculardan ismi sesli harf ile başlayanları ayrı bir dosyaya yazdırınız.


with open("futbolcular.txt") as file:  # dosyayi actik
  liste=file.readlines()  # degerlerini liste degiskenine liste seklinde aldik 

sesliharfler="AaEeiIoOuUöüÖÜİ" # sesli harfleri degisken icine attik
for i in liste:  # lstedeki elemanlari kontrol icin for dongusune aldik 
  for a in sesliharfler:  # sesliharfleri tek tek kontrol etmek icin dongu icine aldik
    if i.startswith(a): # eger i ilk harfi sesliharfler icinden biri ise 
      print(i)   #yazdir 
      with open("Seslifutbolcular.txt","a") as dosya:  # dosyayi actik
        dosya.write(i)  # dosyaya da yazdir





##5-)Futbolcular dosyasındaki futbolcu isimlerini yazdığınız program ile Türkçe karakter içermeyecek bir hale getirip yeni bir dosyaya kaydediniz.


with open("futbolcular.txt") as file:  # dosyayi actik
  futbolcular=file.read()  #dosya degerlerini strıng seklınde degıskene attık
  
kaynak="şçöğüiŞÇÖĞÜİ"
hedef="scoguiSCOGUI"
tablo=str.maketrans(kaynak,hedef)  # ceviri tablosu olusturduk str.maketrans metodu ile

with open("futbolcularyeni.txt","w") as file:  # dosyayi actik
  file.write(futbolcular.translate(tablo)) #cevirdigimiz stringi yeni dosyaya kaydettik 







