import re
from . import Convert,PostOptions,PostProcess,PreProcess
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

def auto_detect(text):
    scripts = []

    for uchar in text:
        try:
            scripts.append(unicodedata.name(uchar).split(' ')[0].lower())
        except ValueError:
            pass
            # print('Script not found')

    counts = Counter(scripts)
    script_percent = []

    # print(counts)

    for script, count  in counts.items():
        percent = count/len(scripts) * 100
        script_percent.append((percent, script))

    if len(script_percent) > 0:
        script = sorted(script_percent)[-1][1]
    else:
        script = ''

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
        if 'ะ' in text or 'ั' in text:
            preoptions =  ['ThaiOrthography']
    elif inputScript == 'Lao' or inputScript == 'LaoPali':
        if 'ະ' in text or 'ັ' in text:
            preoptions = ['LaoTranscription']
    elif inputScript == 'Urdu':
            preOptions = ['UrduShortNotShown']

    return preoptions

def convert(src, tgt, txt, nativize, preoptions, postoptions):
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

    for options in preoptions:
      txt = getattr(PreProcess, options)(txt)

    transliteration = Convert.convertScript(txt, src, tgt)

    if nativize:
      transliteration =  PostOptions.ApplyScriptDefaults(transliteration, src, tgt)
      if tgt != 'Tamil':
        transliteration = PostProcess.RemoveDiacritics(transliteration)
      else:
        transliteration = PostProcess.RemoveDiacriticsTamil(transliteration)

    for options in postoptions:
      transliteration = getattr(PostProcess, options)(transliteration)

    if src == "Tamil" and tgt == "IPA":
        r = requests.get("http://anunaadam.appspot.com/api?text=" + txt + "&method=2")
        r.encoding = r.apparent_encoding
        transliteration = r.text

    return transliteration

def process(src, tgt, txt, nativize = True, post_options = [], pre_options = []):
    ## implement src autodetect

    if src == 'autodetect':
        src = auto_detect(txt)
        pre_options = detect_preoptions(txt, src)

    return convert(src, tgt, txt, nativize, pre_options, post_options)




