class Language:
    def __init__(self, language='English'):
        self.language = language
        self.messages = {
            'English': {'greet': 'Hello', 'goodbye': 'Goodbye', 'well_said': 'Well said!', 'night': 'Good night'},
            'French': {'greet': 'Bonjour', 'goodbye': 'Au revoir', 'well_said': 'Bien dit!', 'night': 'Bonne nuit'},
            'Spanish': {'greet': 'Hola', 'goodbye': 'adiós', 'night': 'Buenas Noches', 'well_said': 'Bien dicho'},
        }

    def greet(self, time_of_day):
        if time_of_day == 'morning':
            return self.messages[self.language]['greet']
        else:
            return self.messages[self.language]['night']

    def goodbye(self):
        return self.messages[self.language]['goodbye']

    def well_said(self):
        return self.messages[self.language]['well_said']

class OHCE:
    def __init__(self, language=Language()):
        self.language = language

    def analyze_string(self, input_text):
        if input_text == input_text[::-1]:
            return self.language.well_said()
        return input_text[::-1]

    def analyze_string_without_greeting(self, input_text):
        if input_text == input_text[::-1]:
            return self.language.well_said()
        return input_text[::-1]



