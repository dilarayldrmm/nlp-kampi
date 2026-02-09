import re

tweet = "NLP dersi harika başladı! @firatuniversitesi #yapayzeka #nlp2026 #yazilimmühendisliği"

# Görev 1: @ ile başlayan kullanıcı adlarını bul
# Görev 2: # ile başlayan hashtagleri bul

etiketler = re.findall(r'@\w+', tweet)
hashtagler = re.findall(r'#\w+', tweet)

print("Etiketlenen kurum:", etiketler)
print("İlgili konular:", hashtagler)