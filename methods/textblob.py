from textblob import TextBlob

"""
Github: https://github.com/sloria/TextBlob
"""


def test_textblob():
    textblob = TextBlob('La cameriera non si è divertita quando ha ordinato uova verdi e prosciutto.')
    data = textblob.translate(from_lang='it', to='en')
    print(data)
