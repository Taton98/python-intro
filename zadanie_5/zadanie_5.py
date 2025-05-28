import spacy
from textblob import TextBlob
from deep_translator import GoogleTranslator

# === CZĘŚĆ 1: spaCy ===
print("=== spaCy ===")

# Wczytanie modelu językowego języka angielskiego
nlp = spacy.load("en_core_web_sm")

# Przykładowe zdanie w języku angielskim
text = "Elon Musk bought twiter for 30 billion dolar."

# Przetworzenie tekstu przez model NLP
doc = nlp(text)

# Tokenizacja i rozpoznanie części mowy (POS) oraz zależności składniowych
print("\nTokenizacja i POS tagging:")
for token in doc:
    print(f"{token.text:12} - POS: {token.pos_}, Dependency: {token.dep_}")

# Rozpoznawanie nazwanych jednostek (NER), np. osób, organizacji, kwot
print("\nNamed Entity Recognition (NER):")
for ent in doc.ents:
    print(f"{ent.text:20} - Label: {ent.label_}")

# === CZĘŚĆ 2: TextBlob ===
print("\n=== TextBlob ===")

# Przykładowe zdanie po polsku
blob = TextBlob("Czasami sobie myślę że mam dosyć.")

# Analiza sentymentu – określenie, czy zdanie jest pozytywne, negatywne czy neutralne
print("\nAnaliza sentymentu:")
print(f"Polaryzacja: {blob.sentiment.polarity}, Subiektywność: {blob.sentiment.subjectivity}")

# === CZĘŚĆ 3: deep_translator ===
print("\n=== Tłumaczenie (deep_translator) ===")

# Tłumaczenie zdania na język hiszpański przy użyciu biblioteki deep_translator
try:
    translation = GoogleTranslator(source='auto', target='es').translate(blob.raw)
    print(f"Tłumaczenie na hiszpański:\n{translation}")
except Exception as e:
    print(f"Błąd tłumaczenia: {e}")
