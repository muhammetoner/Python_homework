# Ödev: Listeler ve Tuple'lar
# Konu: Listeler, Tuple'lar, listelerde döngü.
# Görev:
# •	Kullanıcıdan 5 adet sayı alarak bir listeye ekleyin ve bu listenin toplamını, ortalamasını, en büyük ve en küçük elemanını bulun.
# •	Kullanıcıdan aldığı kelimeleri bir listeye ekleyerek ters sıralayan bir program yazın.
# •	Bir liste içindeki tekrar eden elemanları kaldıran bir program yazın.
sayilar = [] 

for i in range(5):
    sayi = int(input(f"{i+1}. sayıyı girin: "))
    sayilar.append(sayi)
print("-"*30)
toplam = sum(sayilar)
ortalama = toplam / len(sayilar)
en_buyuk = max(sayilar)
en_kucuk = min(sayilar)
print(f"Liste: {sayilar}\n toplamı: {toplam}\n ortalması : {ortalama}\n En Büyük deger :{en_buyuk}\n  En küçük {en_kucuk}")
print("-"*30)
kelimeler = [] 
for i in range(5):
    kelime = input(f"{i+1}. kelimeyi girin: ")
    kelimeler.append(kelime)
print("-"*30)
kelimeler.reverse()
print("-"*30)

print("Ters sıralanmış liste:", kelimeler)
print("-"*30)
elemanlar = input("Liste elemanlarını aralarına boşluk koyarak girin: ").split()
benzersiz_liste = []
for eleman in elemanlar:
    if eleman not in benzersiz_liste:
        benzersiz_liste.append(eleman)
print("-"*30)
print("Tekrarsız Liste:", benzersiz_liste)
