import nltk
from nltk.util import ngrams
from collections import Counter

text = "doğal dil işleme ve yapay zeka geleceğin teknolojisidir doğal dil işleme çok eğlencelidir"
tokens = nltk.word_tokenize(text.lower())

# 1. Bigramları (ikili grupları) oluşturalım
ikili_gruplar = list(ngrams(tokens, 2))

# 2. En çok tekrar eden ikiliyi bulalım
bigram_sayilari = Counter(ikili_gruplar)

print("--- N-Gram Analizi (Bigram) ---")
for grup, sayi in bigram_sayilari.most_common(3):
    print(f"{grup[0]} {grup[1]}: {sayi} kez yan yana gelmiş")