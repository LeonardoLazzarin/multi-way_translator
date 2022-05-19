import goslate

"""

Non funziona più perché dicono che google ha aggiornato le sue policy per non permettere a programmi semplici come questi di accedere
Dicono che teoricamente sistemi più sofisticati sono possibili
https://pypi.org/project/goslate/ 

"""


def test_goslate():
    gs = goslate.Goslate()
    print(gs.get_languages())
    print(gs.translate('Ciao. Cosa vuoi tradurre oggi?', target_language='af', source_language='it'))
