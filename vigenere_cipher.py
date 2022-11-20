
from itertools import cycle, chain
from string import printable

#Sems tarafından kodlandı
#EKSİKLİKLER: Eğer şifrelenmiş karakter, boşluğa eş değerse decrpyt edilirken eski haline dönüştürülemez çünkü boşlukları encrpyt yada decrpyt etmiyorum buna bir çözüm bulamadım henüz
banner = """
Vigenere şifreleme makinasına hoş geldin, bu eski bir simetrik şifreleme yöntemidir. \"Çoklu Sezar şifreleme\" olarak düşünebilirsin, metin tek bir shift leme (kaydırma) değeri ile değilde belirlenen anahtarın içindeki harflerin tekabül ettiği sayıların sırayla kaydırma değeri olarak kullanılması ile şifreleriz, bu sayede şifrenin çözümünde frekans analizi (harflerin ne kadar kaydırıldığını bulmak) zorlaşır çünkü artık şifre kırıcının anahtarın uzunluğu kadar sezar şifresi kırması gerekir. Algoritmayı araştırmaya başlamadan önce bir kaç deneme yapmaya ne dersin.
"""
def vige_encrypt(text, key):
    if len(text) < len(key):
        print("La oğlum hiç metin anahtardan daha küçük olur mu aklını mı oynattın")
        exit()
    encrpyted_text = ""
    k = 0
    for c in text:
        if c == " ":#space karakterini anahtarımız kolayca ifşa olmasın diye şifrelemiyeceğiz
            encrpyted_text += " "
        else:
            char_num = ord(c) + 33 + ord(key[k])
            #print(f"{ord(c)} {ord(key[k])}")
            if char_num >= 127:
                encrpyted_text += chr(char_num + 34)
            else:
                encrpyted_text += chr(char_num)
            k += 1
            if k == len(key):
                k = 0
    return encrpyted_text

def vige_decrpyt(text, key):
    if len(text) < len(key):
        print("La oğlum hiç metin anahtardan daha küçük olur mu aklını mı oynattın")
        exit()
    decrpyted_text = ""
    k = 0
    for c in text:
        if c == " ":#space karakterini anahtarımız kolayca ifşa olmasın diye şifrelemiyeceğiz
            decrpyted_text += " "
        else:
            #print(f"{ord(c)} {ord(key[k])}")
            char_num = ord(c)
            if char_num < 0:
                char_num += 33#Bu durum normalde olmaz çünkü encrpyt fonksiyonu char_num un yüzde yüz 32 den büyük olucağını garantiler ama olurda manuel olarak decrpyt fonksiyonu çağrılırsa ve char_num 32 den küçük olursa o zaman sadece anahtarı çıkarmamız yeticektir.
            if char_num-34 >= 127:
                decrpyted_text += chr(char_num - 33 - 34 - ord(key[k]))
            else:
                decrpyted_text += chr(char_num - 33 - ord(key[k]))
            k += 1
            if k == len(key):
                k = 0
    return decrpyted_text


if __name__ == "__main__":
    mode = input(f"{banner}\nŞifreleyek mi? Çözek mi hacı? (ş/ç)-> ")
    if mode == "ş":
        text = input("Ne özelin var? (metin)-> ")
        if text:
            key = input("Şifreni talep ediyorum (anahtar)-> ")
            encrpyted_text = vige_encrypt(text, key)
            print("Metnini şifreledik -> ", encrpyted_text)
        else:
            print("Oğlum düzgünce metni gir dellendirme")
    elif mode == "ç":
        encrypted_text = input("Neyi sakladın? (şifreli metin)-> ")
        if encrypted_text:
            key = input("Şifreni talep ediyorum (anahtar)-> ")
            decrpyted_text = vige_decrpyt(encrypted_text, key)
            print("İşte metnin -> ", decrpyted_text)
        else:
            print("Oğlum düzgünce şifreli metni gir dellendirme")