import googletrans

translator = googletrans.Translator()
while True:
    ask = input("type the sentence or the word for translation: ")
    language = input("what language do you want to translate it in: ")
    translated = translator.translate(ask, dest=language)
    print(translated.text)
    print('Thank you for useing DJ TRANSLATE ')




