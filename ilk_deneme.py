import nltk

# Sertifika sorununu aşmak için ve yeni paketi indirmek için:
try:
    nltk.download('punkt_tab')
except:
    import ssl
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context
    nltk.download('punkt_tab')

text = "Fırat Üniversitesi NLP dersi harika geçecek!"
tokens = nltk.word_tokenize(text)
print("Sonuç:", tokens)