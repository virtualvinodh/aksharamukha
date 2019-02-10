from flask import Flask, jsonify, request, redirect
from flask_cors import CORS
import re
import Convert,PostOptions,PostProcess,PreProcess
import json
import requests
import html
import itertools
from collections import Counter
import unicodedata

app = Flask(__name__)
CORS(app)

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

@app.route('/demo', methods=['POST', 'GET'])
def main_site():
    return redirect("http://aksharamukha-api.appspot.com/spa-mat")
    # return "This is a backend for <a href=\"http://aksharamukha.appspot.com\">Aksharamukha</a>."

def removeA(a):
    if a.count('a') == 1:
        return a.replace('a', '')

@app.route('/api/autodetect', methods=['POST', 'GET'])
def auto_detect():
    scripts = []
    text = request.json['text']

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

    return script

@app.route('/api/commonletters', methods=['POST', 'GET'])
def common_letters():
    script1 = request.json['script1']
    script2 = request.json['script2']
    letters = request.json['letters']

    results = {}

    if script1 == 'Tamil':
        pp = 'RemoveDiacriticsTamil'
    else:
        pp = 'RemoveDiacritics'

    letters_script1 = [convert('HK', script1, x, False,[],[pp]) for x in letters]
    letters_script2 = [convert('HK', script2, x, False,[],[pp]) for x in letters]

    letters_script1_hk = [convert(script1, 'HK', x, False,[],[pp]) for x in letters_script1]
    letters_script2_hk = [convert(script2, 'HK', x, False,[],[pp]) for x in letters_script2]

    leters_common = set(letters_script1_hk) & set(letters_script2_hk)

    letters_script1_common = [convert('HK', script1, x, False,[],[pp]) for x in leters_common]
    letters_script2_common = [convert('HK', script2, x, False,[],[pp]) for x in leters_common]

    results['script1'] = letters_script1_common
    results['script2'] = letters_script2_common


    return jsonify(results)


@app.route('/api/syllabary', methods=['POST', 'GET'])
def syllabary_list():
    results = {}
    vowelsAll = ['a', 'A', 'i', 'I', 'u', 'U', 'R', 'RR', 'lR', 'lRR', 'E', 'e', 'ai', 'O', 'o', 'au', 'aE', 'AE', 'aO', 'aM', 'aH', 'a~']
    script1 = request.json['script1']
    script2 = request.json['script2']

    if script1 == 'Tamil':
        pp = 'RemoveDiacriticsTamil'
    else:
        pp = 'RemoveDiacritics'

    vowelsScript1 = list(unique_everseen([convert('HK', script1, x, False,[],[pp]) for x in vowelsAll]))
    vowelsScript1_hk = [convert(script1, 'HK', x, False,[],[]) for x in vowelsScript1]

    actual_vowels = sorted(set(vowelsAll) & set(vowelsScript1_hk), key=vowelsAll.index)

    if script1 == 'Tamil':
        actual_vowels = [x for x in actual_vowels if x not in ['aE', 'AE', 'aO']]

    vowelsScript1 = list(unique_everseen([convert('HK', script1, x, False,[],[pp]) for x in actual_vowels]))
    vowelsScript2 = [convert(script1, script2, x, False,[],[]) for x in vowelsScript1]

    vowelsUnique = [convert(script1, 'HK', x, False,[],[]) for x in vowelsScript1]

    consonantsAll = ['k', 'kh', 'g', 'gh', 'G',
        'c', 'ch', 'j', 'jh', 'J',
        'T', 'Th', 'D', 'Dh', 'N',
        't', 'th', 'd', 'dh', 'n',
        'p', 'ph', 'b', 'bh', 'm',
        'y', 'r', 'l', 'v',
        'z', 'S', 's', 'h',
        'Z', 'L', 'r2', 'n2',
        'q', 'qh', 'g2', 'z2', 'r3', 'r3h', 'f', 'Y']

    if script1 == 'Sinhala' or  script1 == 'Rejang':
        consonantsAll = consonantsAll + ['n*g', 'n*j', 'n*D', 'n*d', 'm*b']

    consonantsScript1 = list(unique_everseen([convert('HK', script1, x+'a', False,[],[pp]) for x in consonantsAll]))
    consonantsScript1_hk = map(removeA, [convert(script1, 'HK', x, False,[],[]) for x in consonantsScript1])
    actual_consonants = sorted(set(consonantsAll) & set(consonantsScript1_hk), key=consonantsAll.index)

    # print(actual_consonants)

    consonantsScript1 = list(unique_everseen([convert('HK', script1, x+'a', False,[],[pp]) for x in actual_consonants]))

    consonantsScript2 = [convert(script1, script2, x, False,[],[]) for x in consonantsScript1]

    consonantUnique = [convert(script1, 'HK', x, False,[],[pp]) for x in consonantsScript1]
    consonantUnique = [x.replace('a','') for x in consonantUnique]

    compound = []

    if script1 == 'BatakSima':
        vowelsUnique.append('e')
        vowelsUnique.append('o')
        vowelsUnique.append('au')

    elif script1 == 'BatakManda':
        vowelsUnique.append('e')
        vowelsUnique.append('o')

    elif script1 == 'BatakPakpak':
        vowelsUnique.append('e')
        vowelsUnique.append('aE')
        vowelsUnique.append('o')

    elif script1 == 'BatakToba':
        vowelsUnique.append('e')
        vowelsUnique.append('o')

    elif script1 == 'BatakKaro':
        vowelsUnique.append('e')
        vowelsUnique.append('aE')
        vowelsUnique.append('o')
        vowelsUnique.append('aO')

    elif script1 == 'Khojki':
        vowelsUnique.append('I')

    vowelsUnique = [x for x in sorted(vowelsUnique, key=vowelsAll.index) if x !='a']

    for cons in consonantUnique:
        for vow in vowelsUnique:
            compound.append(cons + vow)

        compound.append(cons)
        compound.append('&' + cons)

    if script1 == 'Multani' or script1 == 'Mahajani':
        compound = []

    compoundsScript1 = list(unique_everseen([convert('HK', script1, x, False,[],[pp]) for x in compound]))
    compoundsScript1 = [x for x in compoundsScript1  if x not in consonantsScript1]
    compoundsScript2 = [convert(script1, script2, x, False,[],[]) for x in compoundsScript1]

    results['vowelsScript1'] = vowelsScript1
    results['vowelsScript2'] = vowelsScript2
    results['consonantsScript1'] = consonantsScript1
    results['consonantsScript2'] = consonantsScript2
    results['compoundsScript1'] = compoundsScript1
    results['compoundsScript2'] = compoundsScript2

    return jsonify(results)

@app.route('/api/conjuncts', methods=['POST', 'GET'])
def conjuncts_list():
    results = {}
    script1 = request.json['script1']
    script2 = request.json['script2']
    conj = request.json['conj']
    postoptions = request.json['postoptions']

    for key, value in conj.items():
        result_script1 = list(unique_everseen([convert('IAST', script1, x, False,[],[]) for x in value]))
        result_iast = [convert(script1, 'IAST', x, False,['removeChillus'],[]) for x in result_script1]
        actual_result = sorted(set(value) & set(result_iast), key=value.index)

        results[key] = [convert('IAST', script1, x, False,[], postoptions) for x in actual_result]
        results[key[:-1] + '2'] = [convert('IAST', script2, x, False,[], []) for x in actual_result]

    return jsonify(results)

@app.route('/api/scriptmatrix', methods=['POST', 'GET'])
def scriptmatrix_list():
    results_final = {}
    results = {}
    results_hk = {}
    guide = request.json['guide']
    scripts = request.json['scripts']
    chars = request.json['chars']

    for script in scripts:
        results[script] = convert('HK', script, json.dumps(chars).replace(' ',''), False,[],[])
        results_hk[script] = convert(script, 'HK', results[script], False,[],[])

    guide_chars = convert('HK', guide, json.dumps(chars).replace(' ',''), False,[],[])

    results_final['results'] = results
    results_final['resultsHK'] = results_hk
    results_final['guideChars'] = guide_chars

    return jsonify(results_final)

@app.route('/api/describe', methods=['POST', 'GET'])
def describe_list():
    results = {}
    results['script1'] = convert('HK', request.json['script1'], json.dumps(request.json['text']).replace(' ',''), False,[],[])
    results['script2'] = convert('HK', request.json['script2'], json.dumps(request.json['text']).replace(' ',''), False,[],[])
    results['script1hk'] = convert(request.json['script1'], 'HK', results['script1'], False,[],[])
    return jsonify(results)

@app.route('/api/website', methods=['POST', 'GET'])
def fetch_site():
    url = request.args['url']
    r = requests.get(url)
    if "UTF-8" not in r.encoding:
        r.encoding = r.apparent_encoding

    htmlcontent = r.text

    #htmlcontent = htmlcontent.replace('href="/', 'href="' + url + '/')

    baseurl = re.sub('(https*://)([^/]+)/*.*', r'\1'+ r'\2', url,flags=re.IGNORECASE)
    baseurl = baseurl.replace('‍','')

    #print('Base URL')
    #print(baseurl)

    htmlcontent = convert(request.args['source'], request.args['target'], htmlcontent, json.loads(request.args['nativize']),
        json.loads(request.args['preOptions']), json.loads(request.args['postOptions']))

    # Replace relative paths with absolute paths
    htmlcontent=re.sub("(\")/",r"\1"+baseurl+"/",htmlcontent)
    htmlcontent=re.sub("(\.\")/",r"\1"+baseurl+"/",htmlcontent)
    htmlcontent=re.sub("(url\()\/",r"\1"+baseurl+"/",htmlcontent)

    ## Parameters

    params = 'source=' + request.args['source'] + '&target=' + request.args['target'] + '&preOptions=' + request.args['preOptions'] + '&postOptions=' + request.args['postOptions'] + '&nativize=' + request.args['nativize']

    transurl = html.escape("http://aksharamukha.appspot.com/api/website?"+params+'&url=')

    # fix double dot
    urlparts = url.split("/")
    doubledot =""
    for  i in range(0, len(urlparts)-2):
        doubledot = doubledot + urlparts[i]+ "/"

    htmlcontent=htmlcontent.replace("../",doubledot)

    ## Replace links

    htmlcontent=re.sub("(<a href\=\"?)",r"\1"+transurl,htmlcontent)
    htmlcontent=re.sub("(<a class=.*? href\=\"?)",r"\1"+transurl,htmlcontent)
    htmlcontent=re.sub("(<a target\=\"\_blank\" href\=\")",r"\1"+transurl,htmlcontent)
    htmlcontent=re.sub("(<a target\=\"\_self\" href\=\")",r"\1"+transurl,htmlcontent)

    ## Replace with native numerals

    htmlcontent = PostProcess.RetainIndicNumerals(htmlcontent, request.args['target'], True)

    ## Retain Dandas

    htmlcontent = PostProcess.RetainDandasIndic(htmlcontent, request.args['target'], True)

    return htmlcontent


@app.route('/api/convert', methods=['POST', 'GET'])
def convert_post():
    #print('There requests are')
    #print(request.json)

    if 'text' in request.json:
        text = convert(request.json['source'], request.json['target'], request.json['text'], request.json['nativize'],
            request.json['preOptions'], request.json['postOptions'])
    else:
        text = ''

    text = text.replace('\n', '<br/>')

    #print(text)

    return text


@app.route('/api/convert_loop_tgt', methods=['POST', 'GET'])
def convert_loop_tgt_post():
    # print('There requests are')
    # print(request.json)

    results = {}

    for target in request.json['targets']:
        text = convert(request.json['source'], target, request.json['text'], request.json['nativize'],
            request.json['preOptions'], request.json['postOptions'])
        text = text.replace('\n', '<br/>')
        results[target] = text

    # print(results)

    return jsonify(results)

@app.route('/api/convert_loop_src', methods=['POST', 'GET'])
def convert_loop_src_post():
    # print('There requests are')
    # print(request.json)

    results = {}

    # print('hereee')
    texts = json.loads(request.json['text'])

    for i, source in enumerate(request.json['sources']):
        # print(texts[source])
        text = convert(source, request.json['target'], json.dumps(texts[source],ensure_ascii=False), request.json['nativize'],
            request.json['preOptions'], request.json['postOptions'])
        text = text.replace('\n', '<br/>')
        try:
            results[source] = json.loads(text)
        except:
            print('finding')
            #print(text)
            #print(texts[source])
            #print('Exception')

    # print(results)

    return jsonify(results)


def convert(src, tgt, txt, nativize, preoptions, postoptions):
    txt = PreProcess.PreProcess(txt,src,tgt)

    if 'siddhamUnicode' in postoptions and tgt == 'Siddham':
        tgt = 'SiddhamUnicode'
    if 'LaoNative' in postoptions and tgt == 'Lao':
        tgt = 'Lao2'
    if 'siddhamUnicode' in preoptions and src == 'Siddham':
        src = 'SiddhamUnicode'
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


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8085, debug=True)
