# -*- coding: utf-8 -*-
import unittest

from language_detector import detect_language, LANGUAGES


class TestLanguageDetector(unittest.TestCase):

    def setUp(self):
        self.languages = [
            {
                'name': 'Spanish',
                'common_words': [
                    'el', 'la', 'de', 'que', 'y', 'a', 'en', 'un', 'ser', 'se',
                    'no', 'haber', 'por', 'con', 'su', 'para', 'como', 'estar',
                    'tener', 'le', 'lo', 'lo', 'todo', 'pero', 'más', 'hacer',
                    'o', 'poder', 'decir', 'este', 'ir', 'otro', 'ese', 'la',
                    'si', 'me', 'ya', 'ver', 'porque', 'dar', 'cuando', 'él',
                    'muy', 'sin', 'vez', 'mucho', 'saber', 'qué', 'sobre',
                    'mi', 'alguno', 'mismo', 'yo', 'también', 'hasta'
                ]
            },
            {
                'name': 'German',
                'common_words': [
                    'das', 'ist', 'du', 'ich', 'nicht', 'die', 'es', 'und',
                    'der', 'was', 'wir', 'zu', 'ein', 'er', 'in', 'sie', 'mir',
                    'mit', 'ja', 'wie', 'den', 'auf', 'mich', 'dass', 'so',
                    'hier', 'eine', 'wenn', 'hat', 'all', 'sind', 'von',
                    'dich', 'war', 'haben', 'für', 'an', 'habe', 'da', 'nein',
                    'bin', 'noch', 'dir', 'uns', 'sich', 'nur',
                    'einen', 'kann', 'dem'
                ]
            },
            {   'name': 'English',
                'common_words': [
                    'the','be','to','of','and','a','in','that','have','I',
                    'it','for','not','on','with','he','as','you','do','at',
                    'this','but','his','by','from','they','we','say','her',
                    'she','or','an','will','my','one','all','would','there',
                    'their', 'whats','up','out','if','about','who','get','which',
                    'go','me','when','make','can','like','time','no','just',
                    'him','know','take', 'people','into','year','your','good','some',
                    'could','them','see','other','than','then','now','look',
                    'only','come','its','over','think','alsoback','after','use',
                    'two','how','our','work','first','well','way','even','new',
                    'want','because','any','these','give','day','most','us'
                ]
            }
        ]
        self.texts = {
            "spanish": """
                Lionel Andrés Messi Cuccittini (Rosario, 24 de junio de 1987),
                conocido como Leo Messi, es un futbolista argentino11 que juega
                como delantero en el Fútbol Club Barcelona y en la selección
                argentina, de la que es capitán. Considerado con frecuencia el
                mejor jugador del mundo y calificado en el ámbito deportivo como el
                más grande de todos los tiempos, Messi es el único futbolista en la
                historia que ha ganado cinco veces el FIFA Balón de Oro –cuatro de
                ellos en forma consecutiva– y el primero en
                recibir tres Botas de Oro.
                """,
            "german": """
                Messi spielt seit seinem 14. Lebensjahr für den FC Barcelona.
                Mit 24 Jahren wurde er Rekordtorschütze des FC Barcelona, mit 25
                der jüngste Spieler in der La-Liga-Geschichte, der 200 Tore
                erzielte. Inzwischen hat Messi als einziger Spieler mehr als 300
                Erstligatore erzielt und ist damit Rekordtorschütze
                der Primera División.
                """,
            "english": """
                Atticus said to Jem one day, “I’d rather you shot at tin cans in
                the backyard, but I know you’ll go after birds. Shoot all the
                blue jays you want, if you can hit ‘em, but remember it’s a
                sin to kill a mockingbird.” That was the only time I ever
                heard Atticus say it was a sin to do something, and I asked
                Miss Maudie about it. “Your father’s right,” she said.
                """
        }

    def test_detect_language_spanish_with_our_language_specification(self):
        result = detect_language(self.texts["spanish"], self.languages)
        self.assertEqual(result.lower(), 'spanish')

    def test_detect_language_spanish_with_module_language_specification(self):
        result = detect_language(self.texts["spanish"], LANGUAGES)
        self.assertEqual(result.lower(), 'spanish')

    def test_detect_language_german_with_our_language_specification(self):
        result = detect_language(self.texts["german"], self.languages)
        self.assertEqual(result.lower(), 'german')

    def test_detect_language_german_with_module_language_specification(self):
        result = detect_language(self.texts["german"], LANGUAGES)
        self.assertEqual(result.lower(), 'german')
    
    def test_detect_language_english_with_module_language_specification(self):
        result = detect_language(self.texts["english"], LANGUAGES)
        self.assertEqual(result.lower(), 'english')

    def test_detect_language_english_with_our_language_specification(self):
        result = detect_language(self.texts["english"], self.languages)
        self.assertEqual(result.lower(), 'english')