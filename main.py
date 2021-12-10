'''Każdą literę tekstu jawnego zamieniamy na literę przesuniętą o 3 miejsca w prawo.

I tak literę a szyfrujemy jako literę d, literę b jako e itd.
W przypadku litery z wybieramy literę c.
W celu odszyfrowania tekstu powtarzamy operację tym razem przesuwając litery o 3 pozycje w lewo.

Wyniki będa zawsze podane małymi literami 

'''
klucz = 3

def szyfruj(txt):
    zaszyfrowany_tekst = ""
    for i in range(len(txt)):
        if ord(txt[i]) > 122 - klucz:
            zaszyfrowany_tekst += chr(ord(txt[i]) + klucz - 26)
        else:
            zaszyfrowany_tekst += chr(ord(txt[i]) + klucz)
    return zaszyfrowany_tekst

tekst = input("Co szyfrujemy, Cezarze?: ")
print("Ciąg zaszyfrowany:\n", szyfruj(str.lower(tekst)))
