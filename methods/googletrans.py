from googletrans import Translator

"""
Github: https://github.com/ssut/py-googletrans
"""


def test_googletrans():
    translator = Translator()
    res = translator.translate('La cameriera non si è divertita quando ha ordinato uova verdi e prosciutto.', dest='en', src='it')
    print(res.text)
