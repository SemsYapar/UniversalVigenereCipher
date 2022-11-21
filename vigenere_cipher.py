#Sems tarafından kodlandı
"""
Bazı sayıların meraklılar için açıklaması:
Unicode ile çalışıyor bu güzel makina yani piyasadaki diğer vigenere toollar gibi sadece küçük veya sadece büyük alfabetik karakterler değil bütüün unicode evreni üzerinden şifreleme yapılıcak bir yapıda yazıldı
Bu sebepten bazı aralıkları filtrelemek durumunda kaldım bunlar 2 kümeden oluşuyor bir küme unicode tablosuna göre 0 ila 32 indexleri arasında tanımlanmış esc, tab gibi okunamayan karakterler diğer kümede 127. indexteki delete ile başlıyor ve ismini daha önce hiç duymadığım ana gene okunamayan karakterlerden oluşuyor kodda asıl efor sarf ettiğim kısım bu karakterlere şifrelenen veya çözülen metini denk gelmemesini sağlamaya çalışmak oldu
Bunun için şifreleme fonksiyonunda şifrelenen karakterin bu aralıklarda olup olmadığını kontrol ediyorum ve öyleyse o aralıktan kurtarmak için aralıkları atlıyorum 
Bunuda şu şekil bir mantıkla yapmaya karar verdim: öncelikle her karaktere ne olursa olsun 33 ekliyorum. null karakter tablodaki ilk karakter bu ve bundan sonra gelen bütün karakterlere 32 ekliyorum ki bu aralıktan çıkıldığından emin olayım
İkinci aralıktan kurtulmak içinde karakterin 127 ve ondan daha büüyk olup olmadığını kontrol ediyorum öyleyse 2. aralıktan kurtulduğundan emin olmak için ondan 34 çıkarıyorum çünkü bu aralıkta 127-160 yani 34 tane karakter bulunuyor
"""

banner = """
Vigenere şifreleme makinasına hoş geldin, bu eski bir simetrik şifreleme yöntemidir. \"Çoklu Sezar şifreleme\" olarak düşünebilirsin, metin tek bir shift leme (kaydırma) değeri ile değilde belirlenen anahtarın içindeki harflerin tekabül ettiği sayıların sırayla kaydırma değeri olarak kullanılması ile şifreleriz, bu sayede şifrenin çözümünde frekans analizi (harflerin ne kadar kaydırıldığını bulmak) zorlaşır çünkü artık şifre kırıcının anahtarın uzunluğu kadar sezar şifresi kırması gerekir. Algoritmayı araştırmaya başlamadan önce bir kaç deneme yapmaya ne dersin.
"""

not_be_encrypted = [' ', '\n', '!', '"', ',', '-', '.']
def vige_encrypt(text, key):
    if len(text) < len(key):
        print("La oğlum hiç metin anahtardan daha küçük olur mu aklını mı oynattın")
        exit()
    encrypted_text = ""
    k = 0
    for c in text:
        if c in not_be_encrypted:#space, enter ve sık kullanılan noktalama karakterlerini anahtarımız kolayca ifşa olmasın diye şifrelemiyeceğiz
            encrypted_text += c
        else:
            #print(f"{ord(c)} {ord(key[k])}")
            char_num = ord(c) + 33 + ord(key[k])
            if char_num >= 127:
                encrypted_text += chr(char_num + 34)
            else:
                encrypted_text += chr(char_num)
            k += 1
            if k == len(key):
                k = 0
    return encrypted_text

def vige_decrypt(text, key):
    if len(text) < len(key):
        print("La oğlum hiç metin anahtardan daha küçük olur mu aklını mı oynattın")
        exit()
    decrypted_text = ""
    k = 0
    for c in text:
        if c in not_be_encrypted:#space, enter ve sık kullanılan noktalama karakterlerini anahtarımız kolayca ifşa olmasın diye şifrelemiyeceğiz
            decrypted_text += c
        else:
            #print(f"{ord(c)} {ord(key[k])}")
            char_num = ord(c)
            if char_num < 0:
                char_num += 33#Bu durum normalde olmaz çünkü encrpyt fonksiyonu char_num un yüzde yüz 32 den büyük olucağını garantiler ama olurda manuel olarak decrpyt fonksiyonu çağrılırsa ve char_num 32 den küçük olursa o zaman sadece anahtarı çıkarmamız yeticektir.
            if char_num-34 >= 127:
                decrypted_text += chr((char_num - 33 - 34 - ord(key[k]))%1114112)
            else:
                decrypted_text += chr((char_num - 33 - ord(key[k]))%1114112)#yanlış şifre denemelerinde programın çökmemesi için mod alıyoruz
            k += 1
            if k == len(key):
                k = 0
    return decrypted_text

if __name__ == "__main__":
    mode = input(f"{banner}\nŞifreleyek mi? Çözek mi hacı? (ş/ç)-> ")
    if mode == "ş":
        text = input("Ne özelin var? (metin)-> ")
        if text:
            key = input("Şifreni talep ediyorum (anahtar)-> ")
            encrypted_text = vige_encrypt(text, key)
            print("Metnini şifreledik -> ", encrypted_text)
        else:
            print("Oğlum düzgünce metni gir dellendirme")
    elif mode == "ç":
        encrypted_text = input("Neyi sakladın? (şifreli metin)-> ")
        if encrypted_text:
            key = input("Şifreni talep ediyorum (anahtar)-> ")
            decrypted_text = vige_decrypt(encrypted_text, key)
            print("İşte metnin -> ", decrypted_text)
        else:
            print("Oğlum düzgünce şifreli metni gir dellendirme")
