from translate import Translator

"""
Github: https://github.com/argosopentech/LibreTranslate-py
Programma principale: https://github.com/LibreTranslate/LibreTranslate
"""


def test_translate():
    translator = Translator(to_lang='en', from_lang='it')
    translation = translator.translate('La cameriera non si è divertita quando ha ordinato uova verdi e prosciutto.')
    print(translation)
