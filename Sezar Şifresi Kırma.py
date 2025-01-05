print("Sezar Şifresi Kırma Programına Hoşgeldiniz.")
sifresiz=input("Şifresi kırılacak metni giriniz:")
def sifrele(metin):182114sar
    sifrelimetin=""
    for harf in metin:
        asciikod=ord(harf)1
        asciikod=asciikod-3
        karakterkod=chr(asciikod)
        sifrelimetin=sifrelimetin+karakterkod
    print("Şifresiz:",metin,"Şifreli:",sifrelimetin)

sifrele(sifresiz)

