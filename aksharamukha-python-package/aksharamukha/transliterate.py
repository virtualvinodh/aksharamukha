import re
from . import Convert,PostOptions,PostProcess,PreProcess
from . import ConvertFix
import json
import requests
import html
import itertools
from collections import Counter
import unicodedata
import io

def removeA(a):
    if a.count('a') == 1:
        return a.replace('a', '')

def unique_everseen(iterable, key=None):
    "List unique elements, preserving order. Remember all elements ever seen."
    # unique_everseen('AAAABBBCCDAABBB') --> A B C D
    # unique_everseen('ABBCcAD', str.lower) --> A B C D
    seen = set()
    seen_add = seen.add
    if key is None:
        for element in itertools.filterfalse(seen.__contains__, iterable):
            seen_add(element)
            yield element
    else:
        for element in iterable:
            k = key(element)
            if k not in seen:
                seen_add(k)
                yield element

def auto_detect(text, plugin = False):
    scripts = []

    for uchar in text:
        try:
            scripts.append(unicodedata.name(uchar).split(' ')[0].lower())
        except ValueError:
            pass
            # print('Script not found')

    counts = Counter(scripts)
    script_percent = []

    for script, count  in counts.items():
        percent = count/len(scripts) * 100
        script_percent.append((percent, script))

    #print(sorted(script_percent))

    if not plugin:
        if len(script_percent) > 0:
            script = sorted(script_percent)[-1][1]
        else:
            script = ''
    else:
        #print('here')
        if len(script_percent) > 0:
            if sorted(script_percent)[-1][1] == 'latin':
                script = sorted(script_percent)[-2][1]
            else:
                script = sorted(script_percent)[-1][1]
        else:
            script = ''

    #print('the script is')
    #print(script)
    inputScript = script[0].upper() + script[1:]

    laoPali = ['ຆ', 'ຉ', 'ຌ', 'ຎ', 'ຏ', 'ຐ', 'ຑ', 'ຒ', 'ຓ', 'ຘ', 'ຠ', 'ຨ', 'ຩ', 'ຬ', '຺']

    if inputScript == 'Bengali':
        if 'ৰ' in text or 'ৱ' in text:
            inputScript = 'Assamese'
    elif inputScript == 'Lao':
        if any(char in text for char in laoPali):
            inputScript = 'LaoPali'
    elif inputScript == 'Batak':
        inputScript = 'BatakKaro'
    elif inputScript == 'Myanmar':
        inputScript = 'Burmese'

        mon = ['ၚ', 'ၛ', '္ည', 'ၞ', 'ၟ', 'ၠ', 'ဳ', 'ဨ']
        if any([char in text for char in mon]):
            inputScript = 'Mon'

        countSub = {'Shan': 0, 'TaiLaing': 0, 'KhamtiShan': 0}

        text = text.replace('ႃ', '')

        for uchar in text:
            try:
                char = unicodedata.name(uchar).lower()
            except:
                pass
            if 'shan' in char:
                countSub['Shan'] += 1
            elif 'tai laing' in char:
                countSub['TaiLaing'] += 1
            elif 'khamti' in char:
                countSub['KhamtiShan'] += 1

        import operator
        sorted_x = sorted(countSub.items(), key=operator.itemgetter(1))

        if countSub['Shan'] > 0 or countSub['TaiLaing'] > 0 or countSub['KhamtiShan'] > 0:
            inputScript = sorted_x[-1][0]


        #shan = ['ႃ', '\u1086', '\u1084', 'ၵ', 'ၶ', 'ၷ', 'ꧠ', 'ၸ', 'ꧡ', 'ꩡ', 'ꧢ', 'ၺ', 'ꩦ', 'ꩧ', 'ꩨ', 'ꩩ', 'ꧣ', 'ၻ', 'ꩪ', 'ၼ','ၽ', 'ꧤ', 'ႁ', 'ꩮ', 'ၹ', 'ၾ']
        #if any([char in text for char in shan]):
            #inputScript = 'Shan'

    elif inputScript == 'Meetei':
        inputScript = 'MeeteiMayek'
    elif inputScript == 'Old':
        inputScript = 'OldPersian'
    elif inputScript == 'Phags-pa':
        inputScript = 'PhagsPa'
    elif inputScript == 'Ol':
        inputScript = 'Santali'
    elif inputScript == 'Sora':
        inputScript = 'SoraSompeng'
    elif inputScript == 'Syloti':
        inputScript = 'SylotiNagri'
    elif inputScript == 'Tai':
        inputScript = 'TaiTham'
    elif inputScript == 'Warang':
        inputScript = 'WarangCiti'
    elif inputScript == 'Siddham':
        preOptions = 'siddhamUnicode'
    elif inputScript == 'Cyrillic':
        inputScript = 'RussianCyrillic'
    elif inputScript == 'Zanabazar':
        inputScript = 'ZanabazarSquare'
    elif inputScript == 'Arabic':
        inputScript = 'Urdu'
    elif inputScript == 'Latin':
        diacritics = ['ā', 'ī', 'ū', 'ṃ', 'ḥ', 'ś', 'ṣ', 'ṇ', 'ṛ', 'ṝ', 'ḷ', 'ḹ', 'ḻ', 'ṉ', 'ṟ', 'ṭ', 'ḍ', 'ṅ', 'ñ']
        Itrans = ['R^i', 'R^I', 'L^i', 'L^I', '.N', '~N', '~n', 'Ch', 'sh', 'Sh']
        if 'ʰ' in text:
            inputScript = 'Titus'
        elif any(char in text for char in diacritics):
            if 'ē' in text or 'ō' in text or 'r̥' in text:
                inputScript = 'ISO'
            else:
                inputScript = 'IAST'
        elif any(char in text for char in Itrans):
            inputScript = 'Itrans'
        else:
            inputScript = 'HK'

    return inputScript

# Cross check with inded convert() funciton within autodetect
# scripts available here must be added there
def detect_preoptions(text, inputScript):
    preoptions = []
    if inputScript == 'Thai':
        textNew = text.replace('ห์', '')
        if '\u035C' in text or '\u0325' in text or 'งํ' in text or '\u0E47' in text:
            preoptions = ['ThaiPhonetic']
        elif '์' in textNew and ('ะ' in text):
            preoptions = ['ThaiSajjhayawithA']
        elif '์' in textNew:
            preoptions = ['ThaiSajjhayaOrthography']
        elif 'ะ' in text or 'ั' in text:
            preoptions =  ['ThaiOrthography']
    elif inputScript == 'Lao' or inputScript == 'LaoPali':
        textNew = text.replace('ຫ໌', '')
        if '໌' in textNew and ('ະ' in text):
            preoptions = ['LaoSajhayaOrthographywithA']
        elif '໌' in textNew:
            preoptions = ['LaoSajhayaOrthography']
        elif 'ະ' in text or 'ັ' in text:
            preoptions = ['LaoTranscription']
    elif inputScript == 'Urdu':
            preoptions = ['UrduShortNotShown']

    return preoptions

def convert(src, tgt, txt, nativize, preoptions, postoptions):
    tgtOld = ""

    if tgt == "" or tgt == "Ignore":
        return txt
    if preoptions == [] and postoptions == [] and nativize == False and src == tgt:
        return txt

    if src == tgt:
        tgtOld = tgt
        tgt = "Devanagari"

    txt = PreProcess.PreProcess(txt,src,tgt)

    if 'siddhammukta' in postoptions and tgt == 'Siddham':
        tgt = 'SiddhamDevanagari'
    if 'siddhamap' in postoptions and tgt == 'Siddham':
        tgt = 'SiddhamDevanagari'
    if 'siddhammukta' in preoptions and src == 'Siddham':
        src = 'SiddhamDevanagari'
    if 'LaoNative' in postoptions and tgt == 'Lao':
        tgt = 'Lao2'
    if 'egrantamil' in preoptions and src == 'Grantha':
        src = 'GranthaGrantamil'
    if 'egrantamil' in postoptions and tgt == 'Grantha':
        tgt = 'GranthaGrantamil'
    if 'nepaldevafont' in postoptions and tgt == 'Newa':
        tgt = 'Devanagari'
    if 'ranjanalantsa' in postoptions and tgt == 'Ranjana':
        tgt = 'Tibetan'
        nativize = False
    if 'ranjanawartu' in postoptions and tgt == 'Ranjana':
        tgt = 'Tibetan'
        nativize = False
    if 'SoyomboFinals' in postoptions and tgt == 'Soyombo':
        txt = '\u02BE' + txt

    for options in preoptions:
      txt = getattr(PreProcess, options)(txt)

    if src == "Oriya" and tgt == "IPA":
        txt = ConvertFix.OriyaIPAFixPre(txt)

    transliteration = Convert.convertScript(txt, src, tgt)

    if src == tgtOld:
        tgt = tgtOld
        transliteration = Convert.convertScript(transliteration, "Devanagari", tgt)

    if nativize:
      transliteration =  PostOptions.ApplyScriptDefaults(transliteration, src, tgt)
      if tgt != 'Tamil':
        transliteration = PostProcess.RemoveDiacritics(transliteration)
      else:
        transliteration = PostProcess.RemoveDiacriticsTamil(transliteration)

    if 'RemoveDiacritics' in postoptions:
      if tgt == 'Tamil':
        postoptions = map(lambda x: 'RemoveDiacriticsTamil' if x == 'RemoveDiacritics' else x, postoptions)

    for options in postoptions:
      transliteration = getattr(PostProcess, options)(transliteration)

    if src == "Tamil" and tgt == "IPA":
        r = requests.get("http://anunaadam.appspot.com/api?text=" + txt + "&method=2")
        r.encoding = r.apparent_encoding
        transliteration = r.text

    if src == "Oriya" and tgt == "IPA":
        transliteration = ConvertFix.OriyaIPAFix(transliteration)

    return transliteration

def process(src, tgt, txt, nativize = True, post_options = [], pre_options = []):
    ## implement src autodetect

    if src == 'autodetect':
        src = auto_detect(txt)
        pre_options = detect_preoptions(txt, src)

    return convert(src, tgt, txt, nativize, pre_options, post_options)




