"""
Cleaners are transformations that run over the input text at both training and
evaluation time.
Cleaners can be selected by passing a comma-separated list of cleaner names with the "cleaners"
hyperparameter.

There are two ``cleaners`` functions for different situations.

- ``basic_cleaners`` if you wish to not transliterate (in this case, you should also update
the symbols in symbols.py to match your data).
- ``advanced_cleaners`` for texts that can be transliterated to ASCII using the Unidecode library.
"""

import re
from unidecode import unidecode
from .numbers import normalize_numbers

# Regular expression matching whitespace:
_whitespace_re = re.compile(r"\s+")

# List of (regular expression, replacement) pairs for abbreviations in American English:
_abbreviations_en_US = [
    (re.compile("\\b%s\\." % x[0], re.IGNORECASE), x[1])
    for x in [
        ("mrs", "misess"),
        ("ms", "miss"),
        ("mr", "mister"),
        ("dr", "doctor"),
        ("st", "saint"),
        ("co", "company"),
        ("jr", "junior"),
        ("maj", "major"),
        ("gen", "general"),
        ("drs", "doctors"),
        ("rev", "reverend"),
        ("lt", "lieutenant"),
        ("hon", "honorable"),
        ("sgt", "sergeant"),
        ("capt", "captain"),
        ("esq", "esquire"),
        ("ltd", "limited"),
        ("col", "colonel"),
        ("ft", "fort"),
    ]
]

_abbreviations_es_ES = [
    (re.compile("\\b%s\\." % x[0], re.IGNORECASE), x[1])
    for x in [
        ("sra", "señora"),
        ("srta", "señorita"),
        ("sr", "señor"),
        ("d", "don"),
        ("da", "doña"),
        ("dr", "doctor"),
        ("dra", "doctora"),
        ("gob", "gobierno"),
        ("ing", "ingeniero"),
        ("gral", "general"),
        ("tel", "teléfono"),
    ]
]

_abbreviations_de_DE = [
    (re.compile("\\b%s\\." % x[0], re.IGNORECASE), x[1])
    for x in [
        ("fr", "frau"),
        ("hr", "herr"),
        ("fam", "familie"),
        ("str", "straße"),
        ("usw", "und so weiter"),
        ("bzw", "beziehungsweise"),
        ("urspr", "ursprünglich"),
        ("zz", "zurzeit"),
        ("ing", "ingenieur"),
        ("ugs", "umgangssprachlich"),
        ("jmdn", "jemanden"),
        ("jmd", "jemand"),
        ("jmds", "jemandes"),
        ("geb", "geboren"),
        ("eigtl", "eigentlich"),
        ("bes", "besonders"),
        ("allg", "allgemein"),
    ]
]

_abbreviations_fr_FR = [
    (re.compile("\\b%s\\." % x[0], re.IGNORECASE), x[1])
    for x in [
        ("mon", "monsieur"),
        ("mme", "madame"),
        ("fam", "famille"),
        ("ex", "exemple"),
        ("bjr", "bonjour"),
        ("adm", "administration"),
        ("auj", "aujourd'hui"),
        ("bât", "bâtiment"),
        ("bsr", "bonsoir"),
        ("dr", "docteur"),
        ("expr", "expression"),
        ("hist", "histoire"),
    ]
]


def expand_abbreviations(text, language_code):
    """
    Check for the ``language_code`` and replace abbreviations
    with the correct values for that language.
    """
    if language_code == "en_US":
        for regex, replacement in _abbreviations_en_US:
            text = re.sub(regex, replacement, text)
        return text
    if language_code == "es_ES":
        for regex, replacement in _abbreviations_es_ES:
            text = re.sub(regex, replacement, text)
        return text
    if language_code == "de_DE":
        for regex, replacement in _abbreviations_de_DE:
            text = re.sub(regex, replacement, text)
        return text
    if language_code == "fr_FR":
        for regex, replacement in _abbreviations_fr_FR:
            text = re.sub(regex, replacement, text)
        return text


def expand_numbers(text):
    """
    Normalize numbers.
    """
    return normalize_numbers(text)


def lowercase(text):
    """
    Make all letters in text to lowercase letters.
    """
    return text.lower()


def collapse_whitespace(text):
    """
    Collapse whitespaces.
    """
    return re.sub(_whitespace_re, " ", text)


def convert_to_ascii(text):
    """
    Convert text to ASCII format.
    """
    return unidecode(text)


def basic_cleaners(text):
    """
    Basic pipeline that lowercases and collapses whitespaces
    without transliteration.
    """
    text = lowercase(text)
    text = collapse_whitespace(text)
    return text


def advanced_cleaners(text):
    """
    Pipeline for ASCII-compatible text, including a number
    and abbreviation expansion.
    """
    text = convert_to_ascii(text)
    text = lowercase(text)
    text = expand_numbers(text)
    text = expand_abbreviations(text)
    text = collapse_whitespace(text)

    return text
