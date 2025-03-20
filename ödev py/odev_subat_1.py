# Ödev: Fonksiyonlar
# Konu: Fonksiyonlar, parametreler, return.
# Görev:
# •	Girilen iki sayının toplamını, farkını, çarpımını ve bölümünü bulan bir hesap makinesi fonksiyonu yazın.
# •	Kullanıcının girdiği bir kelimenin palindrom olup olmadığını kontrol eden bir fonksiyon yazın.
# Örnek: "kek" -> palindrom, "masa" -> değil
# •	Kullanıcının yaşını girerek kaç yıl sonra 100 yaşına ulaşacağını hesaplayan bir fonksiyon yazın.
def topla():
      sayi1=int(input("lütfen ilk sayıyı giriniz: "))
      sayi2=int(input("lütfen ikinci  sayıyı giriniz: "))
      top= sayi1+sayi2
      carp= sayi1*sayi2
      fark = sayi1-sayi2
      bol= sayi1//sayi2
      print(f"{sayi1} + {sayi2} = {top}")
      print(f"{sayi1} X {sayi2} = {carp}")
      print(f"{sayi1} - {sayi2} = {fark}")
      print(f"{sayi1} / {sayi2} = {bol}")
      
topla()

def yas():
      gir=int(input("Lütfen yaşınız giriniz bizde kaç yıl sonra 100 yaşında olcagınzı size söylüyelim ! :  ")) 
      if gir< 100:
            hesap=100-gir
            print(f"{hesap}  yıl sonra 100  yaşına gireceksiniz")
      else:
           print("zaten 100  yaşındasın ne diye giriyon yaşını get de matematik ögren ")
  
yas()

def palindrom_mu(kelime):
    return kelime == kelime[::-1] 


kelime = input("Bir kelime girin: ").lower() 


if palindrom_mu(kelime):
    print(f"'{kelime}' bir palindromdur.")
else:
    print(f"'{kelime}' bir palindrom değildir.")

      
 