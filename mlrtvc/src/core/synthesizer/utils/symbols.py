"""
Defines the sets of valid/supported symbols used in model text input for different,
supported languages.
The default is a set of ASCII characters that works well for the English language
or text that has been run through Unidecode.
"""

# from . import cmudict

_pad = "_"
_eos = "~"
_characters_en_US = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!'\"(),-.:;? "
_characters_es_ES = (
    "AÁBCDEÉFGHIÍJKLMNÑOÓPQRSTUÚÜVWXYZaábcdeéfghiíjklmnñoópqrstuúüvwxyz!'\"(),-.:;?¿«» "
)
_characters_de_DE = (
    "AÄBCDEFGHIJKLMNOÖPQRSßTUÜVWXYZaäbcdefghijklmnoöpqrstuüvwxyz!'„\"‚‘(),-.:;? "
)
_characters_fr_FR = "AÀÂBCÇDEÈÊËFGHIÎÏJKLMNOÔPQRSTUÙÛVWXYZaàâbcçdeèêëfghiîïjklmnoôpqrstuùûvwxyz!'\"(),-.:;?«» "

# Prepend "@" to ARPAbet symbols to ensure uniqueness (some are the same as uppercase letters):
# _arpabet = ["@' + s for s in cmudict.valid_symbols]


def symbols(language_code):
    if language_code == "en_US":
        return [_pad, _eos] + list(_characters_en_US)  # + _arpabet
    elif language_code == "es_ES":
        return [_pad, _eos] + list(_characters_es_ES)  # + _arpabet
    elif language_code == "de_DE":
        return [_pad, _eos] + list(_characters_de_DE)  # + _arpabet
    elif language_code == "fr_FR":
        return [_pad, _eos] + list(_characters_fr_FR)  # + _arpabet
