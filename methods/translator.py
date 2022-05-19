from translate import Translator

"""
Github: https://github.com/terryyin/translate-python
"""


def test_translate():
    translator = Translator(to_lang='en', from_lang='it')
    translation = translator.translate('La cameriera non si è divertita quando ha ordinato uova verdi e prosciutto.')
    print(translation)
