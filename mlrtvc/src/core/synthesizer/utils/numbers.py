"""
Occurences of numbers, decimal delimiters and other characters are
different in different languages and therefore need different adaptions.
"""

import re
import inflect

# Provide plural inflections, singular noun inflections, “a”/”an” selection for English words, and manipulation of numbers as words
_inflect = inflect.engine()

# English-specific
# Search for a sequence of the form (number, comma, number) or numbers that have at least three digits
_comma_number_re_EN = re.compile(r"([0-9][0-9\,]+[0-9])")
# Search for a sequence of the form (number, decimal point, number)
_decimal_number_re_EN = re.compile(r"([0-9]+\.[0-9]+)")

# Spanish-, German- and French-specific
# Search for a sequence of the form (number, point, number) or numbers that have at least three digits
_comma_number_re = re.compile(r"([0-9][0-9\.]+[0-9])")
# Search for a sequence of the form (number, comma, number)
_decimal_number_re = re.compile(r"([0-9]+\,[0-9]+)")

# Search for a sequence of the form (Pund symbol, (comma), (number))
_pounds_re = re.compile(r"£([0-9\,]*[0-9]+)")
# Search for a sequence of the form (Dollar symbol, (comma or decimal point), (number))
_dollars_re = re.compile(r"\$([0-9\.\,]*[0-9]+)")
# Search for a sequence of the form (Euro symbol, (comma), (number))
_euros_re = re.compile(r"€([0-9\,]*[0-9]+)")

# Search for patterns like 1st, 2nd, 3rd or 4th
_ordinal_re = re.compile(r"[0-9]+(st|nd|rd|th)")
# Search for sequences of numbers, e.g. 256514
_number_re = re.compile(r"[0-9]+")


def _remove_commas(m, language_code):
    """
    Check for ``language_code`` and remove commas.
    """
    if language_code == "en_US":
        return m.group(1).replace(",", "")
    else:
        return m.group(1).replace(".", "")


def _expand_decimal_point(m, language_code):
    """
    Check for ``language_code`` and replace decimal
    points with the word "point".
    """
    if language_code == "en_US":
        return m.group(1).replace(".", " point ")
    else:
        return m.group(1).replace(",", " comma ")


def _expand_ordinal(m):
    """
    Convert numbers to words.
    """
    return _inflect.number_to_words(m.group(0))


def _expand_dollars(m, language_code):
    """
    Check for the ``language_code`` parameter and choose
    the clauses accordingly.
    """
    if language_code == "en_US":
        match = m.group(1)
        parts = match.split(".")

        if len(parts) > 2:
            return match + " dollars"  # Unexpected format

        dollars = int(parts[0]) if parts[0] else 0
        cents = int(parts[1]) if len(parts) > 1 and parts[1] else 0

        if dollars and cents:
            dollar_unit = "dollar" if dollars == 1 else "dollars"
            cent_unit = "cent" if cents == 1 else "cents"
            return "%s %s, %s %s" % (dollars, dollar_unit, cents, cent_unit)
        elif dollars:
            dollar_unit = "dollar" if dollars == 1 else "dollars"
            return "%s %s" % (dollars, dollar_unit)
        elif cents:
            cent_unit = "cent" if cents == 1 else "cents"
            return "%s %s" % (cents, cent_unit)
        else:
            return "zero dollars"
    if language_code == "es_ES":
        match = m.group(1)
        parts = match.split(",")

        if len(parts) > 2:
            return match + " dolares"  # Unexpected format

        dollars = int(parts[0]) if parts[0] else 0
        cents = int(parts[1]) if len(parts) > 1 and parts[1] else 0

        if dollars and cents:
            dollar_unit = "dólar" if dollars == 1 else "dolares"
            cent_unit = "centavo" if cents == 1 else "centavos"
            return "%s %s, %s %s" % (dollars, dollar_unit, cents, cent_unit)
        elif dollars:
            dollar_unit = "dólar" if dollars == 1 else "dolares"
            return "%s %s" % (dollars, dollar_unit)
        elif cents:
            cent_unit = "centavo" if cents == 1 else "centavos"
            return "%s %s" % (cents, cent_unit)
        else:
            return "cero dolares"
    if language_code == "de_DE":
        match = m.group(1)
        parts = match.split(",")

        if len(parts) > 2:
            return match + " Dollar"  # Unexpected format

        dollars = int(parts[0]) if parts[0] else 0
        cents = int(parts[1]) if len(parts) > 1 and parts[1] else 0

        if dollars and cents:
            dollar_unit = "Dollar" if dollars == 1 else "Dollar"
            cent_unit = "Cent" if cents == 1 else "Cent"
            return "%s %s, %s %s" % (dollars, dollar_unit, cents, cent_unit)
        elif dollars:
            dollar_unit = "Dollar" if dollars == 1 else "Dollar"
            return "%s %s" % (dollars, dollar_unit)
        elif cents:
            cent_unit = "Cent" if cents == 1 else "Cent"
            return "%s %s" % (cents, cent_unit)
        else:
            return "null Dollar"
    if language_code == "fr_FR":
        match = m.group(1)
        parts = match.split(",")

        if len(parts) > 2:
            return match + " Dollar"  # Unexpected format

        dollars = int(parts[0]) if parts[0] else 0
        cents = int(parts[1]) if len(parts) > 1 and parts[1] else 0

        if dollars and cents:
            dollar_unit = "dollar" if dollars == 1 else "dollars"
            cent_unit = "cent" if cents == 1 else "centimes"
            return "%s %s, %s %s" % (dollars, dollar_unit, cents, cent_unit)
        elif dollars:
            dollar_unit = "dollar" if dollars == 1 else "dollars"
            return "%s %s" % (dollars, dollar_unit)
        elif cents:
            cent_unit = "cent" if cents == 1 else "centimes"
            return "%s %s" % (cents, cent_unit)
        else:
            return "zero dollars"


def _expand_number(m):
    """Check for the ``language_code`` parameter and select
    the right words.
    """
    if language_code == "en_US":
        num = int(m.group(0))

        if num > 1000 and num < 3000:
            if num == 2000:
                return "two thousand"
            elif num > 2000 and num < 2010:
                return "two thousand " + _inflect.number_to_words(num % 100)
            elif num % 100 == 0:
                return _inflect.number_to_words(num // 100) + " hundred"
            else:
                return _inflect.number_to_words(
                    num, andword="", zero="oh", group=2
                ).replace(", ", " ")
        else:
            return _inflect.number_to_words(num, andword="")
    if language_code == "es_ES":
        num = int(m.group(0))

        if num > 1000 and num < 3000:
            if num == 2000:
                return "dos mil"
            elif num > 2000 and num < 2010:
                return "dos mil " + _inflect.number_to_words(num % 100)
            elif num % 100 == 0:
                return _inflect.number_to_words(num // 100) + " centenar"
            else:
                return _inflect.number_to_words(
                    num, andword="", zero="oh", group=2
                ).replace(", ", " ")
        else:
            return _inflect.number_to_words(num, andword="")
    if language_code == "de_DE":
        num = int(m.group(0))

        if num > 1000 and num < 3000:
            if num == 2000:
                return "zwei tausend"
            elif num > 2000 and num < 2010:
                return "zwei tausend " + _inflect.number_to_words(num % 100)
            elif num % 100 == 0:
                return _inflect.number_to_words(num // 100) + " hundert"
            else:
                return _inflect.number_to_words(
                    num, andword="", zero="oh", group=2
                ).replace(", ", " ")
        else:
            return _inflect.number_to_words(num, andword="")
    if language_code == "fr_FR":
        num = int(m.group(0))

        if num > 1000 and num < 3000:
            if num == 2000:
                return "deux milles"
            elif num > 2000 and num < 2010:
                return "deux milles " + _inflect.number_to_words(num % 100)
            elif num % 100 == 0:
                return _inflect.number_to_words(num // 100) + " cent"
            else:
                return _inflect.number_to_words(
                    num, andword="", zero="oh", group=2
                ).replace(", ", " ")
        else:
            return _inflect.number_to_words(num, andword="")


def normalize_numbers(text, language_code):
    """
    Check for ``language_code``
    """
    if language_code == "en_US":
        text = re.sub(_comma_number_re_EN, _remove_commas, text)
        text = re.sub(_pounds_re, r"\1 pounds", text)
        text = re.sub(_euros_re, r"\1 euros", text)
        text = re.sub(_dollars_re, _expand_dollars, text)
        text = re.sub(_decimal_number_re_EN, _expand_decimal_point, text)
        text = re.sub(_ordinal_re, _expand_ordinal, text)
        text = re.sub(_number_re, _expand_number, text)
        return text
    if language_code == "es_ES":
        text = re.sub(_comma_number_re, _remove_commas, text)
        text = re.sub(_pounds_re, r"\1 libras esterlinas", text)
        text = re.sub(_euros_re, r"\1 euros", text)
        text = re.sub(_dollars_re, _expand_dollars, text)
        text = re.sub(_decimal_number_re, _expand_decimal_point, text)
        text = re.sub(_ordinal_re, _expand_ordinal, text)
        text = re.sub(_number_re, _expand_number, text)
        return text
    if language_code == "de_DE":
        text = re.sub(_comma_number_re, _remove_commas, text)
        text = re.sub(_pounds_re, r"\1 Pfund", text)
        text = re.sub(_euros_re, r"\1 Euro", text)
        text = re.sub(_dollars_re, _expand_dollars, text)
        text = re.sub(_decimal_number_re, _expand_decimal_point, text)
        text = re.sub(_ordinal_re, _expand_ordinal, text)
        text = re.sub(_number_re, _expand_number, text)
        return text
    if language_code == "fr_FR":
        text = re.sub(_comma_number_re, _remove_commas, text)
        text = re.sub(_pounds_re, r"\1 livre sterling", text)
        text = re.sub(_euros_re, r"\1 euros", text)
        text = re.sub(_dollars_re, _expand_dollars, text)
        text = re.sub(_decimal_number_re, _expand_decimal_point, text)
        text = re.sub(_ordinal_re, _expand_ordinal, text)
        text = re.sub(_number_re, _expand_number, text)
        return text
