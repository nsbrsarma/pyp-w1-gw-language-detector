# -*- coding: utf-8 -*-

"""This is the entry point of the program."""

from languages import LANGUAGES


def detect_language(text, languages=LANGUAGES):
    original_text = text
    
    # Create dictionary with all the languages in LANGUAGES
    lang_stats = {}
    for lang in languages:
        lang_stats[lang['name']] = 0
        
    # Convert text to lower case and remove punctuation marks
    # Note: Some punctuation marks are missing; maybe isalpha()?
    text = text.lower()
    punctuation_marks = [',', '!', '.', '-', ':', ';']
    for mark in punctuation_marks:
        text.replace(mark,"")
    
    # Loop through each word and check if it is in dictionary
    for word in text.split(' '):
        for language in languages:
            if word in language['common_words']:
                lang_stats[language['name']] += 1
                

    # Loop through language count dict and determine language
    high_count = 0
    high_language = None
    for language, count in lang_stats.items():
        if count > high_count:
            high_language = language
            high_count = count
    return high_language