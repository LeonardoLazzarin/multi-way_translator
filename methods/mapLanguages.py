import os
import json
from libretranslatepy import LibreTranslateAPI


def save_languages_on_file(file):
    """
    Salva la mappatura dei linguaggi su file
    """
    languages = __get_language_googletrans__({})
    languages = __get_language_libre_translation__(languages)
    with open(os.path.abspath(file), 'w') as f:
        f.write(json.dumps(languages, indent=4))
    print(f'File saved in path: {os.path.abspath(file)}')


def __get_language_googletrans__(languages):
    """
    Mappa i codici delle lingue per il linguaggio googletrans. Sono le stesse di textblob
    """
    all_languages = """<tr><td>Afrikaans</td><td><code translate="no" dir="ltr">af</code></td></tr><tr><td>Albanese</td><td><code translate="no" dir="ltr">sq</code></td></tr><tr><td>Amarico</td><td><code translate="no" dir="ltr">am</code></td></tr><tr><td>Arabo</td><td><code translate="no" dir="ltr">ar</code></td></tr><tr><td>Armeno</td><td><code translate="no" dir="ltr">hy</code></td></tr><tr><td>Azero</td><td><code translate="no" dir="ltr">az</code></td></tr><tr><td>Basco</td><td><code translate="no" dir="ltr">eu</code></td></tr><tr><td>Bielorusso</td><td><code translate="no" dir="ltr">be</code></td></tr><tr><td>Bengalese</td><td><code translate="no" dir="ltr">bn</code></td></tr><tr><td>Bosniaco</td><td><code translate="no" dir="ltr">bs</code></td></tr><tr><td>Bulgaro</td><td><code translate="no" dir="ltr">bg</code></td></tr><tr><td>Catalano</td><td><code translate="no" dir="ltr">ca</code></td></tr><tr><td>Cebuano</td><td><code translate="no" dir="ltr">ceb</code> (<a class="external" href="https://en.wikipedia.org/wiki/ISO_639-2">ISO-639-2</a>)</td></tr><tr><td>Cinese (semplificato)</td><td><code translate="no" dir="ltr">zh-CN</code> o <code translate="no" dir="ltr">zh</code> (<a class="external" href="https://tools.ietf.org/html/bcp47">BCP-47</a>)</td></tr><tr><td>Cinese (tradizionale)</td><td><code translate="no" dir="ltr">zh-TW</code> (<a class="external" href="https://tools.ietf.org/html/bcp47">BCP-47</a>)</td></tr><tr><td>Corso</td><td><code translate="no" dir="ltr">co</code></td></tr><tr><td>Croato</td><td><code translate="no" dir="ltr">hr</code></td></tr><tr><td>Ceco</td><td><code translate="no" dir="ltr">cs</code></td></tr><tr><td>Danese</td><td><code translate="no" dir="ltr">da</code></td></tr><tr><td>Olandese</td><td><code translate="no" dir="ltr">nl</code></td></tr><tr><td>Inglese</td><td><code translate="no" dir="ltr">en</code></td></tr><tr><td>Esperanto</td><td><code translate="no" dir="ltr">eo</code></td></tr><tr><td>Estone</td><td><code translate="no" dir="ltr">et</code></td></tr><tr><td>Finlandese</td><td><code translate="no" dir="ltr">fi</code></td></tr><tr><td>Francese</td><td><code translate="no" dir="ltr">fr</code></td></tr><tr><td>Frisone</td><td><code translate="no" dir="ltr">fy</code></td></tr><tr><td>Galiziano</td><td><code translate="no" dir="ltr">gl</code></td></tr><tr><td>Georgiano</td><td><code translate="no" dir="ltr">ka</code></td></tr><tr><td>Tedesco</td><td><code translate="no" dir="ltr">de</code></td></tr><tr><td>Greco</td><td><code translate="no" dir="ltr">el</code></td></tr><tr><td>Gujarati</td><td><code translate="no" dir="ltr">gu</code></td></tr><tr><td>Creolo haitiano</td><td><code translate="no" dir="ltr">ht</code></td></tr><tr><td>Hausa</td><td><code translate="no" dir="ltr">ha</code></td></tr><tr><td>Hawaiano</td><td><code translate="no" dir="ltr">haw</code> (<a class="external" href="https://en.wikipedia.org/wiki/ISO_639-2">ISO-639-2</a>)</td></tr><tr><td>Ebraico</td><td><code translate="no" dir="ltr">he</code> o <code translate="no" dir="ltr">iw</code></td></tr><tr><td>Hindi</td><td><code translate="no" dir="ltr">hi</code></td></tr><tr><td>Hmong</td><td><code translate="no" dir="ltr">hmn</code> (<a class="external" href="https://en.wikipedia.org/wiki/ISO_639-2">ISO-639-2</a>)</td></tr><tr><td>Ungherese</td><td><code translate="no" dir="ltr">hu</code></td></tr><tr><td>Islandese</td><td><code translate="no" dir="ltr">is</code></td></tr><tr><td>Igbo</td><td><code translate="no" dir="ltr">ig</code></td></tr><tr><td>Indonesiano</td><td><code translate="no" dir="ltr">id</code></td></tr><tr><td>Irlandese</td><td><code translate="no" dir="ltr">ga</code></td></tr><tr><td>Italiano</td><td><code translate="no" dir="ltr">it</code></td></tr><tr><td>Giapponese</td><td><code translate="no" dir="ltr">ja</code></td></tr><tr><td>Giavanese</td><td><code translate="no" dir="ltr">jv</code></td></tr><tr><td>Kannada</td><td><code translate="no" dir="ltr">kn</code></td></tr><tr><td>Kazako</td><td><code translate="no" dir="ltr">kk</code></td></tr><tr><td>Khmer</td><td><code translate="no" dir="ltr">km</code></td></tr><tr><td>Kinyarwanda</td><td><code translate="no" dir="ltr">rw</code></td></tr><tr><td>Coreano</td><td><code translate="no" dir="ltr">ko</code></td></tr><tr><td>Curdo</td><td><code translate="no" dir="ltr">ku</code></td></tr><tr><td>Kirghiso</td><td><code translate="no" dir="ltr">ky</code></td></tr><tr><td>Lao</td><td><code translate="no" dir="ltr">lo</code></td></tr><tr><td>Latino</td><td><code translate="no" dir="ltr">la</code></td></tr><tr><td>Lettone</td><td><code translate="no" dir="ltr">lv</code></td></tr><tr><td>Lituano</td><td><code translate="no" dir="ltr">lt</code></td></tr><tr><td>Lussemburghese</td><td><code translate="no" dir="ltr">lb</code></td></tr><tr><td>Macedone</td><td><code translate="no" dir="ltr">mk</code></td></tr><tr><td>Malgascio</td><td><code translate="no" dir="ltr">mg</code></td></tr><tr><td>Malese</td><td><code translate="no" dir="ltr">ms</code></td></tr><tr><td>Malayalam</td><td><code translate="no" dir="ltr">ml</code></td></tr><tr><td>Maltese</td><td><code translate="no" dir="ltr">mt</code></td></tr><tr><td>Maori</td><td><code translate="no" dir="ltr">mi</code></td></tr><tr><td>Marathi</td><td><code translate="no" dir="ltr">mr</code></td></tr><tr><td>Mongolo</td><td><code translate="no" dir="ltr">mn</code></td></tr><tr><td>Myanmar (Birmania)</td><td><code translate="no" dir="ltr">my</code></td></tr><tr><td>Nepalese</td><td><code translate="no" dir="ltr">ne</code></td></tr><tr><td>Norvegese</td><td><code translate="no" dir="ltr">no</code></td></tr><tr><td>Nyanja (Chichewa)</td><td><code translate="no" dir="ltr">ny</code></td></tr><tr><td>Odia (Oriya)</td><td><code translate="no" dir="ltr">or</code></td></tr><tr><td>Pashto</td><td><code translate="no" dir="ltr">ps</code></td></tr><tr><td>Persiano</td><td><code translate="no" dir="ltr">fa</code></td></tr><tr><td>Polacco</td><td><code translate="no" dir="ltr">pl</code></td></tr><tr><td>Portoghese (Portogallo, Brasile)</td><td><code translate="no" dir="ltr">pt</code></td></tr><tr><td>Punjabi</td><td><code translate="no" dir="ltr">pa</code></td></tr><tr><td>Rumeno</td><td><code translate="no" dir="ltr">ro</code></td></tr><tr><td>Russo</td><td><code translate="no" dir="ltr">ru</code></td></tr><tr><td>Samoano</td><td><code translate="no" dir="ltr">sm</code></td></tr><tr><td>Gaelico scozzese</td><td><code translate="no" dir="ltr">gd</code></td></tr><tr><td>Serbo</td><td><code translate="no" dir="ltr">sr</code></td></tr><tr><td>Sesotho</td><td><code translate="no" dir="ltr">st</code></td></tr><tr><td>Shona</td><td><code translate="no" dir="ltr">sn</code></td></tr><tr><td>Sindhi</td><td><code translate="no" dir="ltr">sd</code></td></tr><tr><td>Singalese (singalese)</td><td><code translate="no" dir="ltr">si</code></td></tr><tr><td>Slovak</td><td><code translate="no" dir="ltr">sk</code></td></tr><tr><td>Sloveno</td><td><code translate="no" dir="ltr">sl</code></td></tr><tr><td>Somalo</td><td><code translate="no" dir="ltr">so</code></td></tr><tr><td>Spagnolo</td><td><code translate="no" dir="ltr">es</code></td></tr><tr><td>Sundanese</td><td><code translate="no" dir="ltr">su</code></td></tr><tr><td>Swahili</td><td><code translate="no" dir="ltr">sw</code></td></tr><tr><td>Svedese</td><td><code translate="no" dir="ltr">sv</code></td></tr><tr><td>Tagalog (filippino)</td><td><code translate="no" dir="ltr">tl</code></td></tr><tr><td>Tagico</td><td><code translate="no" dir="ltr">tg</code></td></tr><tr><td>Tamil</td><td><code translate="no" dir="ltr">ta</code></td></tr><tr><td>Tartaro</td><td><code translate="no" dir="ltr">tt</code></td></tr><tr><td>Telugu</td><td><code translate="no" dir="ltr">te</code></td></tr><tr><td>Tailandese</td><td><code translate="no" dir="ltr">th</code></td></tr><tr><td>Turco</td><td><code translate="no" dir="ltr">tr</code></td></tr><tr><td>Turkmeno</td><td><code translate="no" dir="ltr">tk</code></td></tr><tr><td>Ucraino</td><td><code translate="no" dir="ltr">uk</code></td></tr><tr><td>Urdu</td><td><code translate="no" dir="ltr">ur</code></td></tr><tr><td>Uiguro</td><td><code translate="no" dir="ltr">ug</code></td></tr><tr><td>Uzbeco</td><td><code translate="no" dir="ltr">uz</code></td></tr><tr><td>Vietnamita</td><td><code translate="no" dir="ltr">vi</code></td></tr><tr><td>Gallese</td><td><code translate="no" dir="ltr">cy</code></td></tr><tr><td>Xhosa</td><td><code translate="no" dir="ltr">xh</code></td></tr><tr><td>Yiddish</td><td><code translate="no" dir="ltr">yi</code></td></tr><tr><td>Yoruba</td><td><code translate="no" dir="ltr">yo</code></td></tr><tr><td>Zulu</td><td><code translate="no" dir="ltr">zu</code></td></tr>"""
    all_languages = all_languages.split('<tr>')
    for item in all_languages:
        if item != '':
            # Divide il body della tabella per trovare il codice e il linguaggio
            sep = item.split('<td>')[1:]
            language = sep[0].replace('</td>', '')
            code = sep[1].split('</code>')[0].split('>')[1]
            data = f'GoogleTrans: {language}'
            # Aggiorna l'oggetto passato in parametro
            if code not in languages:
                languages[code] = [data]
            else:
                languages[code].append(data)
    return languages


def __get_language_libre_translation__(languages):
    lt = LibreTranslateAPI("https://translate.argosopentech.com/")
    local_languages = lt.languages()
    for item in local_languages:
        data = f'LibreTranslateAPI: {item["name"]}'
        if item['code'] not in languages:
            languages[item['code']] = [data]
        else:
            languages[item['code']].append(data)
    return languages
