from methods.IMSLGraphLang import GraphLang
from methods.mapLanguages import save_languages_on_file


def main():
    # Create the dictionary with graph elements
    graph_elements = {
        "it": ["en", "fr", "de"],
        "en": ["it", "fr", "de"],
        "fr": ["en", "it", "de"],
        "de": ["en", "fr", "it"]
    }
    gl = GraphLang()
    # è possibile passare già il grafo
    # gl = graphLang(graph_elements)
    # add lang to use in translation
    gl.add_lang("it")
    gl.add_lang("en")
    gl.add_lang("fr")
    gl.add_lang("de")
    # gl.addLang("sp")
    print("LANGS:", gl.get_langs())
    print("TRANS:", gl.edges())

    gl.find_all_path_translation('it', deep=4)

    print(gl.get_all_path_translation())
    """
    [['it', 'en', 'fr', 'it'], 
    ['it', 'en', 'de', 'it'], 
    ['it', 'fr', 'en', 'it'], 
    ['it', 'fr', 'de', 'it'], 
    ['it', 'de', 'en', 'it'], 
    ['it', 'de', 'fr', 'it']]
    """
    print(gl.get_set_lang_pairs())
    """
    [[('it', 'en'), ('en', 'fr'), ('fr', 'it')]
    [('it', 'en'), ('en', 'de'), ('de', 'it')]
    [('it', 'fr'), ('fr', 'en'), ('en', 'it')]
    [('it', 'fr'), ('fr', 'de'), ('de', 'it')]
    [('it', 'de'), ('de', 'en'), ('en', 'it')]
    [('it', 'de'), ('de', 'fr'), ('fr', 'it')]]
    """


if __name__ == '__main__':
    # main()
    save_languages_on_file('./json/languages.json')
