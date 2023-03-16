from googletrans import Translator
from sentence_transformers import SentenceTransformer, util

from methods.IMSLGraphLang import GraphLang

"""
Github: https://github.com/ssut/py-googletrans
"""


def recursive_translate_1(langA, langB, sentA, list_of_sent):
    translator = Translator()
    if sentA not in list_of_sent:
        list_of_sent.append(sentA)
    sent_b = translator.translate(sentA, src=langA, dest=langB).text
    # print("sent_b=",sent_b)
    sent_a1 = translator.translate(sent_b, src=langB, dest=langA).text
    # print("sent_a1=",sent_a1)
    # chiamata ricorsiva
    if sent_a1 not in list_of_sent:
        recursive_translate_1(langA, langB, sent_a1, list_of_sent)


def recursive_translate_2(lang_a, lang_b, lang_c, sent_a, list_of_sent):
    translator = Translator()
    if sent_a not in list_of_sent:
        list_of_sent.append(sent_a)
    sent_b = translator.translate(sent_a, src=lang_a, dest=lang_b).text
    sent_c = translator.translate(sent_b, src=lang_b, dest=lang_c).text
    sent_a1 = translator.translate(sent_c, src=lang_c, dest=lang_a).text
    print("[%s]%s \n[%s]%s \n[%s]%s \n[%s]%s \n\n" % (lang_a, sent_a, lang_b, sent_b, lang_c, sent_c, lang_a, sent_a1))
    # chiamata ricorsiva
    if sent_a1 not in list_of_sent:
        recursive_translate_2(lang_a, lang_b, lang_c, sent_a1, list_of_sent)


def recursive_translate(sent, list_of_lang_pairs, list_of_sent):
    if sent not in list_of_sent:
        list_of_sent.append(sent)

    translator = Translator()
    for langPairs in list_of_lang_pairs:
        # langPairs = [('it', 'en'), ('en', 'fr'), ('fr', 'it')]
        for langPair in langPairs:
            # langPair = ('it', 'en')
            print("[%s]%s => " % (langPair[0], sent), end="")
            sent = translator.translate(sent, src=langPair[0], dest=langPair[1]).text
            print("[%s]%s" % (langPair[1], sent))
        print()
    # chiamata ricorsiva
    if sent not in list_of_sent:
        recursive_translate(sent, list_of_lang_pairs, list_of_sent)


def test_googletrans():
    # translator = Translator()
    # res = translator.translate('La cameriera non si è divertita quando ha ordinato uova verdi e prosciutto.', dest='en', src='it')
    # print(res.text)

    list_of_sent = list()
    lang_a = "it"
    lang_c = "en"
    lang_b = "fr"
    sent_a = "importo a credito sul prestito"

    # recursiveTranslate(lang_a, lang_b, sent_a, list_of_sent)
    recursive_translate_2(lang_a, lang_b, lang_c, sent_a, list_of_sent)
    print(list_of_sent)

    gl = GraphLang()
    # add lang to use in translation
    gl.add_lang("it")
    gl.add_lang("en")
    gl.add_lang("fr")
    gl.add_lang("de")
    # gl.addLang("sp")

    list_of_sent = list()
    gl.find_all_path_translation('it', deep=3)
    sent = "importo a credito sul prestito"
    recursive_translate(sent, gl.get_set_lang_pairs(), list_of_sent)
    print(list_of_sent)


def test_sentence_similarity():
    """Test the test similarity with googletrans"""
    # SEQUENCE IT-RU-IT
    start_sentences = ['La cameriera non si è divertita quando ha ordinato uova verdi e prosciutto.']
    translator = Translator()
    res = translator.translate(
        start_sentences[0],
        dest='ru', src='it'
    )
    res = translator.translate(res.text, dest='it', src='ru')
    result_sentences = [res.text]

    model = SentenceTransformer('all-MiniLM-L6-v2')
    # Compute embedding for both lists
    embeddings1 = model.encode(start_sentences, convert_to_tensor=True)
    embeddings2 = model.encode(result_sentences, convert_to_tensor=True)

    # Compute cosine-similarities
    cosine_scores = util.cos_sim(embeddings1, embeddings2)

    # Output the pairs with their score
    for i in range(len(start_sentences)):
        # print("{} \t\t {} \t\t Score: {:.4f}".format(start_sentences[i], result_sentences[i], cosine_scores[i][i]))
        print(f'Start sentence: {start_sentences[0]}')
        print(f'Result sentence: {result_sentences[0]}')
        print('Score: {:.4f}\n'.format(cosine_scores[i][i]))
