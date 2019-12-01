from flask import Flask, jsonify, request, redirect
from flask_cors import CORS
import re
from aksharamukha import Convert,PostOptions,PostProcess,PreProcess, GeneralMap
import json
import requests
import html
import itertools
from collections import Counter
import unicodedata
import io

from aksharamukha.transliterate import convert, unique_everseen, removeA, auto_detect, detect_preoptions

app = Flask(__name__)
CORS(app)

try:
  import googleclouddebugger
  googleclouddebugger.enable()
except ImportError:
  pass

@app.route('/demo', methods=['POST', 'GET'])
def main_site():
    return redirect("http://aksharamukha-api.appspot.com/spa-mat")
    # return "This is a backend for <a href=\"http://aksharamukha.appspot.com\">Aksharamukha</a>."

@app.route('/api/autodetect', methods=['POST', 'GET'])
def auto_detect_request():
    return auto_detect(request.json['text'])

@app.route('/api/detectpre', methods=['POST', 'GET'])
def detect_pre_request():
    return jsonify(detect_preoptions(request.json['text'], request.json['source']))

@app.route('/api/commonletters', methods=['POST', 'GET'])
def common_letters():
    script1 = request.json['script1']
    script2 = request.json['script2']

    """
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
    """
    script_sort = sorted([script1, script2])
    suffix = script_sort[0] + '_' + script_sort[1]

    if 'Soyombo' in suffix:
        index = '5'
    elif script_sort[0] <= 'BatakToba':
        index = '1'
    elif script_sort[0] <= 'Grantha':
        index = '2'
    elif script_sort[0] <= 'Khudawadi':
        index = '3'
    else:
        index = '4'

    f = open ('resources/common_letters' + index + '/common_letters_' + suffix + '.json', 'r', encoding='utf-8')
    commonletters = json.loads(f.read())
    f.close()

    results = {}

    results['script1'] = commonletters[script1]
    results['script2'] = commonletters[script2]

    return jsonify(results)

@app.route('/api/latinmatrix', methods=['POST', 'GET'])
def latinmatrix_list():
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


@app.route('/api/syllabary', methods=['POST', 'GET'])
def syllabary_list():
    """
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
    """


    script1 = request.json['script1']
    script2 = request.json['script2']

    f = open ('resources/syllabary/syllabary_' + script1 + '.json', 'r', encoding='utf-8')
    syllabary = f.read()
    syllabary = syllabary.replace('،', ',').replace(" ", "")
    f.close()

    if script2 != 'Velthuis':
        syllabary_guide = convert(script1, script2, syllabary, False,[],[])
        syllabary_guide = json.loads(syllabary_guide.replace('،', ','))
    else:
        syllabary_guide = convert(script1, script2, syllabary, False,[],[]).replace('""', '"\\"').replace('&"', '&\\"')
        syllabary_guide = json.loads(syllabary_guide)

    syllabary = json.loads(syllabary)

    results = {}

    results['vowelsScript1'] = syllabary['vowels']
    results['vowelsScript2'] = syllabary_guide['vowels']
    results['consonantsScript1'] = syllabary['consonants']
    results['consonantsScript2'] = syllabary_guide['consonants']
    results['compoundsScript1'] = syllabary['compounds']
    results['compoundsScript2'] = syllabary_guide['compounds']

    return jsonify(results)

@app.route('/api/conjuncts', methods=['POST', 'GET'])
def conjuncts_list():
    script1 = request.json['script1']
    script2 = request.json['script2']
    vowel = request.json['vowel']

    postoptions = request.json['postoptions']

    print('The post options are :: ')
    print(postoptions)

    if script1[0:3] < 'Mod':
        index = '1'
    else:
        index = '2'

    """
    for key, value in conj.items():
        result_script1 = list(unique_everseen([convert('IAST', script1, x, False,[],[]) for x in value]))
        result_iast = [convert(script1, 'IAST', x, False,['removeChillus'],[]) for x in result_script1]
        actual_result = sorted(set(value) & set(result_iast), key=value.index)

        results[key] = [convert('IAST', script1, x, False,[], postoptions) for x in actual_result]
        results[key[:-1] + '2'] = [convert('IAST', script2, x, False,[], []) for x in actual_result]
    """

    if script1 == 'Sinhala':
        if 'SinhalaConjuncts' in postoptions:
            file = 'resources/conjuncts'+ index + '/conjuncts_' + script1 + '_' + vowel + '_all' + '.json'
        else:
            file = 'resources/conjuncts'+ index + '/conjuncts_' + script1 +  '_' + vowel + '.json'
    elif script1 == 'Chakma':
        if 'ChakmaEnableAllConjuncts' in postoptions:
            file = 'resources/conjuncts'+ index + '/conjuncts_' + script1 + '_' + vowel + '_all' + '.json'
        else:
            file = 'resources/conjuncts'+ index + '/conjuncts_' + script1 +  '_' + vowel + '.json'
    else:
        file = 'resources/conjuncts'+ index + '/conjuncts_' + script1 +  '_' + vowel + '.json'

    f = open (file, 'r', encoding='utf-8')
    conjuncts = f.read()
    conjuncts = conjuncts.replace('،', ',').replace(" ", "")
    f.close()

    if script2 != 'Velthuis':
        conjuncts_guide = convert(script1, script2, conjuncts, False,[],[])
        conjuncts_guide = PostProcess.RetainIndicNumerals(conjuncts_guide, script2, True)
        conjuncts_guide = json.loads(conjuncts_guide.replace('،', ','))
    else:
        conjuncts_guide = convert(script1, script2, conjuncts, False,[],[]).replace('""', '"\\"').replace('&"', '&\\"')
        conjuncts_guide = json.loads(PostProcess.RetainIndicNumerals(conjuncts_guide, script2, True))

    conjuncts = json.loads(conjuncts)

    results = {}

    results['conjuncts1S1'] = conjuncts['conjuncts1S1']
    results['conjuncts2S1'] = conjuncts['conjuncts2S1']
    results['conjuncts3S1'] = conjuncts['conjuncts3S1']
    results['conjuncts4S1'] = conjuncts['conjuncts4S1']
    results['conjuncts5S1'] = conjuncts['conjuncts5S1']

    results['conjuncts1S2'] = conjuncts_guide['conjuncts1S1']
    results['conjuncts2S2'] = conjuncts_guide['conjuncts2S1']
    results['conjuncts3S2'] = conjuncts_guide['conjuncts3S1']
    results['conjuncts4S2'] = conjuncts_guide['conjuncts4S1']
    results['conjuncts5S2'] = conjuncts_guide['conjuncts5S1']

    return jsonify(results)

@app.route('/api/scriptmatrix', methods=['POST', 'GET'])
def scriptmatrix_list():
    guide = request.json['guide']
    charnums = request.json['charnums']
    """
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
    """

    f = open ('resources/script_matrix/script_matrix_' + guide + charnums + '.json', 'r', encoding='utf-8')
    results_final = json.loads(f.read(), encoding = "utf-8")
    f.close()

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

@app.route('/api/public', methods=['POST', 'GET'])
def convert_public():
    #print('There requests are')
    #print(request.json)

    nativize = True
    preoptions = []
    postoptions = []

    if 'preoptions' in request.values:
        preoptions = request.values['preoptions'].split(',')

    if 'postoptions' in request.values:
        postoptions = request.values['postoptions'].split(',')

    if 'nativize' in request.values:
        if request.values['nativize'] == 'False' or request.values['nativize'] == 'false':
            nativize = False

    if 'source' not in request.values:
        source = auto_detect(request.values['text'])
        preoptions = detect_preoptions(request.values['text'], source)
    else:
        source = request.values['source']

    if 'text' in request.values:
        text = convert(source, request.values['target'], request.values['text'], nativize, preoptions, postoptions)
    else:
        text = ''

    return text

@app.route('/api/plugin', methods=['POST', 'GET'])
def convert_plugin():
    source = request.json['source']

    if request.json['source'] == 'autodetect':
        source = auto_detect(request.json['text'])
        preoptions = detect_preoptions(request.json['text'], source)

    print(source)

    if source not in GeneralMap.Transliteration:
        text = convert(source, request.json['target'], request.json['text'], request.json['nativize'], request.json['preOptions'], request.json['postOptions'])
    else:
        text = request.json['text']

    return text


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

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8085, debug=True)
