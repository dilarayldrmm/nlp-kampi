import nltk
from nltk.corpus import stopwords
from collections import Counter
import string

# Gerekli paketleri indirelim
nltk.download('stopwords')
nltk.download('punkt_tab')

text = """
Yapay zeka ve doğal dil işleme dünyası çok geniştir. Bu dünyada başarılı olmak için 
çok çalışmak ve bol bol pratik yapmak gerekir. Doğal dil işleme ile harika projeler 
üretebiliriz. Yapay zeka gelecektir.
"""

# 1. Adım: Küçük harfe çevir ve Tokenize et
tokens = nltk.word_tokenize(text.lower())

# 2. Adım: Noktalama işaretlerini ve Stop-words'leri temizle
noktalama = list(string.punctuation)
turkce_durak_kelimeler = stopwords.words('turkish')

temiz_tokens = [kelime for kelime in tokens if kelime not in turkce_durak_kelimeler and kelime not in noktalama]

# 3. Adım: Kelimeleri sayalım
kelime_sayilari = Counter(temiz_tokens)

print("--- ANALİZ SONUÇLARI ---")
print(f"Toplam ham kelime sayısı: {len(tokens)}")
print(f"Temizlenmiş kelime sayısı: {len(temiz_tokens)}")
print("\nEn çok geçen 3 kelime:")
for kelime, sayi in kelime_sayilari.most_common(3):
    print(f"{kelime}: {sayi} kez")