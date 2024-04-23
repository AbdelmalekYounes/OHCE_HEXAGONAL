import locale
from domain.ohce import OHCE, Language

def run_console_app():
    locale.setlocale(locale.LC_ALL, '')
    loc = locale.getlocale()
    lang = 'French' if 'fr' in loc[0] else 'English'

    language = Language(lang)
    ohce = OHCE(language)
    
    print(ohce.language.greet('morning'))

    try:
        while True:
            input_text = input("Vous: ")
            if input_text.lower() == 'exit':
                print(ohce.language.goodbye())
                break
            response = ohce.analyze_string_without_greeting(input_text)
            print("OHCE:", response)
    except KeyboardInterrupt:
        print("\n" + ohce.language.goodbye())
