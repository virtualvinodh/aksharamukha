from aksharamukha import GeneralMap as GM
from aksharamukha import ScriptMap as SM
import importlib
import json
import io
import itertools
import os
from aksharamukha.transliterate import convert, unique_everseen, removeA

# Script Mapping JSON

scripts = '["Dogra", "KhomThai", "Ariyaka", "Shan", "KhamtiShan", "Mon", "TaiLaing", "Ahom","Assamese","Avestan","Balinese","BatakKaro","BatakManda","BatakPakpak","BatakToba","BatakSima","Bengali","Brahmi","Bhaiksuki","Buginese","Buhid","Burmese","Chakma","Cham","Devanagari","Grantha","GranthaPandya","Gujarati","Hanunoo","Javanese","Kaithi","Kannada","Kharoshthi","Khmer","Khojki","Khudawadi","Lao","LaoPali","Lepcha","Limbu","Malayalam","Mahajani","MeeteiMayek","Modi","Multani","Newa","OldPersian","Oriya","PhagsPa","Gurmukhi","Ranjana","Rejang","Santali","Saurashtra","Siddham","Sharada","Sinhala","SoraSompeng","Sundanese","SylotiNagri","Tagbanwa","Tagalog","TaiTham","Takri","Tamil","TamilGrantha","TamilBrahmi","Telugu","Thaana","Thai","Tibetan","Tirhuta","Urdu","Vatteluttu","WarangCiti","ZanabazarSquare"]'
scripts = json.loads(scripts)

roman = ["IAST", "IPA", "ISO", "RussianCyrillic", "Titus", "HK", "Itrans", "Velthuis"]

scriptsAll = scripts + roman

scripts_syllabary = scripts + ['RussianCyrillic']

def generate_script_map():
  NameVowels = ['main','south','modern','sinhala']
  NameVowelSigns = ['virama','main','south','modern','sinhala']
  NameCombiningSigns = ['ayogavaha','nukta']
  NameConsonants = ['main','south','persoarabic','sinhala']
  NameOthers = ['aytham', 'om', 'symbols']

  overallMap = {}

  for Script in GM.IndicScripts + GM.LatinScripts:
    ModScript = importlib.import_module(GM.ScriptPath(Script))
    characters = {}

    vowels = {}
    for i, typ in enumerate(GM.Vowels):
      vowels[NameVowels[i]] = getattr(ModScript, typ)

    vowelsigns = {}
    for i, typ in enumerate(GM.VowelSigns):
      vowelsigns[NameVowelSigns[i]] = getattr(ModScript, typ)

    combiningsigns = {}
    for i, typ in enumerate(GM.CombiningSigns):
      combiningsigns[NameCombiningSigns[i]] = getattr(ModScript, typ)

    consonants = {}
    for i, typ in enumerate(GM.Consonants):
      consonants[NameConsonants[i]] = getattr(ModScript, typ)

    others = {}
    for i, typ in enumerate(['Aytham', 'OmMap', 'SignMap']):
      others[NameOthers[i]] = getattr(ModScript, typ)

    characters['vowels'] = vowels
    characters['vowelsigns'] = vowelsigns
    characters['combiningsigns'] = combiningsigns
    characters['consonants'] = consonants
    characters['others'] = others
    characters['numerals'] = getattr(ModScript, 'NumeralMap')

    if Script not in ['TolongSiki', 'Vatteluttu', 'SiddhamDevanagari', 'Ranjana', 'GranthaPandya', 'GranthaGrantamil']:
      overallMap[Script.lower()] = characters

  f = io.open("resources/script_mapping/script_mapping.json", mode="w", encoding="utf-8")
  f.write(json.dumps(overallMap, ensure_ascii = False, sort_keys=True, indent=4))
  f.close()

## Script Matrix Files

def generate_script_matrix():
  chars5 = '[[["a","A","i","I","u","U","R","RR"],["lR","lRR","e","ai","o","au"]],[["E","O","aE","AE","aO"]],[["aM","aH","a~"]],[["ka","kha","ga","gha","Ga"],["ca","cha","ja","jha","Ja"],["Ta","Tha","Da","Dha","Na"],["ta","tha","da","dha","na"],["pa","pha","ba","bha","ma"]],[["ya","ra","la","va","za","Sa","sa","ha"]],[["La","Za","r2a","n2a"]],[["qa","qha","g2a","z2a","r3a","r3ha","fa","Ya"]],[["n*ga","n*ja","n*Da","n*da","m*ba"]],[["ka","kA","ki","kI","ku","kU","kR","kRR"],["klR","klRR","ke","kai","ko","kau"]],[["kE","kO","kaE","kAE","kaO"]],[["kaM","kaH","ka~","k"]],[["\'","oM",".",".."]]]'
  chars3 = '[[["a","A","i"],["I","u","U"],["R","RR","lR"],["lRR","e","ai"],["o","au"]],[["E","O","aE"],["AE","aO"]],[["aM","aH","a~"]],[["ka","kha","ga"],["gha","Ga","ca"],["cha","ja","jha"],["Ja","Ta","Tha"],["Da","Dha","Na"],["ta","tha","da"],["dha","na","pa"],["pha","ba","bha"],["ma"]],[["ya","ra","la"],["va","za","Sa"],["sa","ha"]],[["La","Za","r2a"],["n2a"]],[["qa","qha","g2a"],["z2a","r3a","r3ha"],["fa","Ya"]],[["n*ga","n*ja","n*Da"],["n*da","m*ba"]],[["ka","kA","ki"],["kI","ku","kU"],["kR","kRR","klR"],["klRR","ke","kai"],["ko","kau"]],[["kE","kO","kaE"],["kAE","kaO"]],[["kaM","kaH","ka~"],["k"]],[["\'","oM","."],[".."]]]'

  chars5 = json.dumps(json.loads(chars5), ensure_ascii = False).replace(" ", "")
  chars3 = json.dumps(json.loads(chars3), ensure_ascii = False).replace(" ", "")
  charsAll = [chars5, chars3]

  for i, chars in enumerate(charsAll):
    for guide in roman:
      results_final = {}
      results = {}
      results_hk = {}

      for script in scripts:
          results[script] = json.loads(convert('HK', script, chars, False,[],[]).replace('،', ','))
          results_hk[script] = json.loads(convert(script, 'HK', json.dumps(results[script], ensure_ascii = False), False,[],[]))

      if guide != 'Velthuis':
        guide_chars = json.loads(convert('HK', guide, chars, False,[],[]))
      else:
        guide_chars = json.loads(convert('HK', guide, chars, False,[],[]).replace('""', '"\\"'))

      results_final['results'] = results
      results_final['resultsHK'] = results_hk
      results_final['guideChars'] = guide_chars

      num = ["5", "3"]

      f = io.open("resources/script_matrix/script_matrix_" + guide + num[i] + ".json", mode="w", encoding="utf-8")
      f.write(json.dumps(results_final, ensure_ascii = False, sort_keys=True, indent=4))
      f.close()

## Generate Syllables
def generate_syllables():
    results = {}

    for script1 in scripts_syllabary:
      vowelsAll = ['a', 'A', 'i', 'I', 'u', 'U', 'R', 'RR', 'lR', 'lRR', 'E', 'e', 'ai', 'O', 'o', 'au', 'aE', 'AE', 'aO', 'aM', 'aH', 'a~']

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

      results['vowels'] = vowelsScript1
      results['consonants'] = consonantsScript1
      results['compounds'] = compoundsScript1

      f = io.open("resources/syllabary/syllabary_" + script1 + ".json", mode="w", encoding="utf-8")
      f.write(json.dumps(results, ensure_ascii = False, sort_keys=True, indent=4))
      f.close()

def generate_conjuncts():
  conj = '{"conjuncts1S1":["ak","akh","ag","agh","aṅ","ac","ach","aj","ajh","añ","aṭ","aṭh","aḍ","aḍh","aṇ","at","ath","ad","adh","an","ap","aph","ab","abh","am","ay","ar","al","av","aś","aṣ","as","ah","al̤"],"conjuncts2S1":["kka","kkha","kca","kcha","kṇa","kta","ktha","kna","kpa","kpha","kma","kya","kra","kla","kva","kśa","kṣa","ksa","khkha","khna","khya","khva","gga","ggha","gja","gḍa","gṇa","gda","gdha","gna","gba","gbha","gma","gya","gra","gla","gva","ghna","ghma","ghya","ghra","ghva","ṅka","ṅkha","ṅga","ṅgha","ṅṅa","ṅca","ṅja","ṅta","ṅda","ṅdha","ṅna","ṅpa","ṅbha","ṅma","ṅya","ṅra","ṅva","ṅśa","ṅsa","ṅha","cca","ccha","cña","cma","cya","cra","cva","chya","jja","jjha","jña","jma","jya","jra","jva","jha","jhña","cña","cha","ñja","ñjha","ñña","ñśa","ñha","ṭka","ṭkha","ṭca","ṭcha","ṭṭa","ṭṇa","ṭta","ṭpa","ṭpha","ṭma","ṭya","ṭva","ṭśa","ṭṣa","ṭsa","ṭhya","ḍga","ḍgha","ḍja","ḍḍa","ḍḍha","ḍda","ḍdha","ḍba","ḍbha","ḍma","ḍya","ḍra","ḍla","ḍva","ḍhya","ḍhra","ḍhva","ṇṭa","ṇṭha","ṇḍa","ṇḍha","ṇṇa","ṇna","ṇma","ṇya","ṇva","ṇha","tka","tkha","tta","ttha","tna","tpa","tpha","tma","tya","tra","tva","tṣa","tsa","thna","thya","thra","thva","dga","dgha","dda","ddha","dna","dba","dbha","dma","dya","dra","dva","dhna","dhma","dhya","dhra","dhva","nka","nkha","nga","ngha","nta","ntha","nda","ndha","nna","npa","npha","nba","nbha","nma","nya","nra","nva","nṣa","nsa","nha","pka","pkha","pca","pcha","pṭa","pṇa","pta","pna","ppa","ppha","pma","pya","pra","pla","pva","pśa","psa","bga","bja","bda","bdha","bba","bbha","bya","bra","bla","bva","bhṇa","bhna","bhma","bhya","bhra","bhla","bhva","mṇa","mna","mpa","mpha","mba","mbha","mma","mya","mra","mla","mva","mha","yya","yva","rka","rka","hra","gra","gha","rca","rcha","rja","rja","hra","ṭra","ḍra","ḍha","rṇa","rta","rtha","rda","rdha","rna","rpa","rpha","rba","rbha","rma","rya","rla","rva","rśa","rṣa","rsa","rha","lka","lga","lda","lpa","lpha","lba","lbha","lma","lya","lla","lva","lśa","lha","vṇa","vna","vya","vra","vla","śca","ścha","śna","śpa","śma","śya","śra","śla","śva","śśa","ṣka","ṣkha","ṣṭa","ṣṭha","ṣṇa","ṣpa","ṣpha","ṣma","ṣya","ṣra","ṣva","ṣṣa","ska","skha","sta","stha","sna","spa","spha","sma","sya","sra","sva","ssa","hṇa","hna","hma","hya","hra","hla","hva","l̤ha"],"conjuncts3S1":["kkra","kkla","kkva","kkṣa","ktya","ktra","ktva","kthna","kthya","knya","kpra","kpla","kmya","krya","klya","kśma","kśra","kśla","kśva","kṣṇa","kṣma","kṣya","kṣra","kṣva","ksta","kstha","ksna","kspa","kspha","ksma","ksya","ksra","ksva","ggra","gghya","gghra","gjña","gjya","gjva","gdya","gdra","gdva","gdhya","gdhra","gdhva","gnya","gbra","gbhya","gbhra","gmya","grya","grva","gvya","gvra","ghnya","ghrya","ghvya","ṅkta","ṅktha","ṅkya","ṅkra","ṅkla","ṅkva","ṅkṣa","ṅksa","ṅkhya","ṅgdha","ṅgya","ṅgra","ṅgva","ṅghna","ṅghya","ṅghra","ṅtra","ṅtva","ṅdhya","ṅnya","ṅnra","ṅpra","ṅvya","ṅvra","ṅsva","ccya","cchma","cchya","cchra","cchla","cchva","cñya","jjña","jjya","jjva","jjhya","jñya","jñva","jmya","jrya","jvya","ñcma","ñcya","ñcva","ñchna","ñchya","ñchra","ñchla","ñchva","ñjña","ñjma","ñjya","ñjva","ñśma","ñśya","ñśra","ñśla","ñśva","ṭkra","ṭkṣa","ṭṭya","ṭtra","ṭtva","ṭpra","ṭśra","ṭśla","ṭsta","ṭstha","ṭsna","ṭspa","ṭsva","ḍgya","ḍgra","ḍghra","ḍjña","ḍjya","ḍḍhya","ḍḍhva","ḍdva","ḍbra","ḍbhya","ḍbhra","ḍvya","ṇṭya","ṇṭhya","ṇḍḍha","ṇḍya","ṇḍra","ṇḍva","ṇḍhya","ṇḍhra","ṇvya","tkya","tkra","tkla","tkva","tkṣa","tkhya","ttna","ttma","ttya","ttra","ttva","ttsa","tthya","tnya","tnva","tpra","tpla","tmya","tyva","trya","trva","tvya","tska","tskha","tsta","tstha","tsna","tspa","tspha","tsma","tsya","tsra","tsva","thnya","thvya","dgra","dgla","dghna","dghra","ddya","ddra","ddva","ddhma","ddhya","ddhra","ddhva","dbra","dbhya","dbhra","dbhva","dmya","drya","drva","dvya","dvra","dhnya","dhrya","dhvya","dhvra","nkra","nkla","nkva","nkṣa","nkhya","ngra","ngla","nghna","nghra","ntta","nttha","ntma","ntya","ntra","ntva","ntsa","nthya","nddha","ndma","ndya","ndra","ndva","ndhma","ndhya","ndhra","ndhva","nnya","nnva","npra","npla","npsa","nbra","nbhra","nmya","nmra","nmla","nyva","nvya","nvra","nska","nskha","nsta","nstha","nsna","nspa","nspha","nsma","nsya","nsra","nsva","nhya","nhra","nhva","pkṣa","ptya","ptra","ptva","pnya","ppra","prya","pśya","psna","psya","psva","bgra","bjya","bdya","bdhya","bdhva","bbra","bbhya","bvya","bhrya","bhrva","bhvya","mnya","mpya","mpra","mpla","mpsa","mbya","mbra","mbva","mbhya","mbhra","mmya","mmra","mmla","mrya","rkca","rkta","rktha","rkpa","rkya","rkṣa","rksa","rkhya","rgga","rggha","rgja","rgbha","rgya","rgra","rgla","rgva","rghna","rghya","rghra","rṅkha","rṅga","rccha","rcya","rjña","rjma","rjya","rjva","rñja","rḍya","rḍhya","rṇṇa","rṇya","rṇva","rtta","rtna","rtma","rtya","rtra","rtva","rtsa","rthya","rddha","rdma","rdya","rdra","rdva","rdhna","rdhma","rdhya","rdhra","rdhva","rnya","rnva","rpya","rbra","rbhya","rbhra","rbhva","rmya","rmra","rmla","ryya","rvya","rvra","rvla","rśma","rśya","rśva","rṣṭa","rṣṭha","rṣṇa","rṣma","rṣya","rṣva","rsra","rsva","rhya","rhra","rhla","rhva","lkya","lgva","lpya","lbya","lbhya","llya","lvya","lhya","vnya","ścya","śnya","śmya","śrya","śrva","śvya","ṣkya","ṣkra","ṣkla","ṣkva","ṣkṣa","ṣṭya","ṣṭra","ṣṭva","ṣṭhya","ṣṭhva","ṣṇya","ṣṇva","ṣpya","ṣpra","ṣpla","ṣmya","skra","stma","stya","stra","stva","stsa","sthna","sthya","snya","spra","sphya","smya","srya","svya","ssya","ssva","hnya","hmya","hvya"],"conjuncts4S1":["ktrya","ktvya","kṣṇya","kṣmya","kstra","gdvya","gdhrya","ṅktya","ṅktra","ṅktva","ṅkṣṇa","ṅkṣma","ṅkṣya","ṅkṣva","ṅgdhya","ṅgdhva","ṅghrya","tkṣma","tkṣva","ttrya","tstra","tsthya","tspra","tsphya","ddvya","nttva","ntrya","ntvya","ntsta","ntstha","ntsna","ntspa","ntsya","ntsra","ntsva","nddhya","nddhva","ndrya","ndvya","ndhrya","nstra","nsphya","ptrya","psnya","rkṣṇa","rkṣya","rksva","rṅgya","rjmya","rttra","rtnya","rtrya","rtvya","rtsna","rtsya","rddhya","rdrya","rdvya","rdhnya","rśvya","rṣṭya","rṣṇya","lgvya","ṣṭrya","strya","sthnya"],"conjuncts5S1":["rtsnya"]}'
  vowels = ['a', 'ā', 'i', 'ī', 'u', 'ū', 'ṛ', 'ĕ', 'e', 'ai', 'ŏ', 'o', 'au', 'aṃ', 'aḥ']

  scripts = ['Dogra']

  total = len(scripts) * len(vowels)

  i = 0

  for script1 in scripts:
    results = {}
    postoptions = []

    if script1[0:3] < 'Mod':
        index = '1'
    else:
        index = '2'

    for vowel in vowels:
      i = i + 1

      print('Processing ' + str(i) + ' out of ' + str(total))

      conj2 = json.loads(conj.replace('a', vowel))

      for key, value in conj2.items():
          result_script1 = list(unique_everseen([convert('IAST', script1, x, False,[],[]) for x in value]))
          result_iast = [convert(script1, 'IAST', x, False,['removeChillus'],[]) for x in result_script1]
          actual_result = sorted(set(value) & set(result_iast), key=value.index)

          results[key] = [convert('IAST', script1, x, False,[], postoptions) for x in actual_result]

      print("resources/conjuncts"+ index + "/conjuncts_" + script1 + "_" + vowel + ".json")

      f = io.open("resources/conjuncts"+ index + "/conjuncts_" + script1 + "_" + vowel + ".json", mode="w", encoding="utf-8")
      f.write(json.dumps(results, ensure_ascii = False, sort_keys=True, indent=4))
      f.close()

      if (script1 == 'Sinhala' or script1 == 'Chakma'):
        postoptions = ['SinhalaConjuncts', 'ChakmaEnableAllConjuncts']

        for key, value in conj2.items():
            result_script1 = list(unique_everseen([convert('IAST', script1, x, False,[],[]) for x in value]))
            result_iast = [convert(script1, 'IAST', x, False,['removeChillus'],[]) for x in result_script1]
            actual_result = sorted(set(value) & set(result_iast), key=value.index)

            results[key] = [convert('IAST', script1, x, False,[], postoptions) for x in actual_result]

        f = io.open("resources/conjuncts"+ index + "/conjuncts_" + script1 + "_" + vowel + "_all.json", mode="w", encoding="utf-8")
        f.write(json.dumps(results, ensure_ascii = False, sort_keys=True, indent=4))
        f.close()

def generate_common_letters():
  letters = ["ka","kA","ki","kI","ku","kU","kR","kE","ke","kai","kO","ko","kau","kha","khA","khi","khI","khu","khU","khR","khE","khe","khai","khO","kho","khau","ga","gA","gi","gI","gu","gU","gR","gE","ge","gai","gO","go","gau","gha","ghA","ghi","ghI","ghu","ghU","ghR","ghE","ghe","ghai","ghO","gho","ghau","Ga","GA","Gi","GI","Gu","GU","GR","GE","Ge","Gai","GO","Go","Gau","ca","cA","ci","cI","cu","cU","cR","cE","ce","cai","cO","co","cau","cha","chA","chi","chI","chu","chU","chR","chE","che","chai","chO","cho","chau","ja","jA","ji","jI","ju","jU","jR","jE","je","jai","jO","jo","jau","jha","jhA","jhi","jhI","jhu","jhU","jhR","jhE","jhe","jhai","jhO","jho","jhau","Ja","JA","Ji","JI","Ju","JU","JR","JE","Je","Jai","JO","Jo","Jau","Ta","TA","Ti","TI","Tu","TU","TR","TE","Te","Tai","TO","To","Tau","Tha","ThA","Thi","ThI","Thu","ThU","ThR","ThE","The","Thai","ThO","Tho","Thau","Da","DA","Di","DI","Du","DU","DR","DE","De","Dai","DO","Do","Dau","Dha","DhA","Dhi","DhI","Dhu","DhU","DhR","DhE","Dhe","Dhai","DhO","Dho","Dhau","Na","NA","Ni","NI","Nu","NU","NR","NE","Ne","Nai","NO","No","Nau","ta","tA","ti","tI","tu","tU","tR","tE","te","tai","tO","to","tau","tha","thA","thi","thI","thu","thU","thR","thE","the","thai","thO","tho","thau","da","dA","di","dI","du","dU","dR","dE","de","dai","dO","do","dau","dha","dhA","dhi","dhI","dhu","dhU","dhR","dhE","dhe","dhai","dhO","dho","dhau","na","nA","ni","nI","nu","nU","nR","nE","ne","nai","nO","no","nau","pa","pA","pi","pI","pu","pU","pR","pE","pe","pai","pO","po","pau","pha","phA","phi","phI","phu","phU","phR","phE","phe","phai","phO","pho","phau","ba","bA","bi","bI","bu","bU","bR","bE","be","bai","bO","bo","bau","bha","bhA","bhi","bhI","bhu","bhU","bhR","bhE","bhe","bhai","bhO","bho","bhau","ma","mA","mi","mI","mu","mU","mR","mE","me","mai","mO","mo","mau","ya","yA","yi","yI","yu","yU","yR","yE","ye","yai","yO","yo","yau","ra","rA","ri","rI","ru","rU","rR","rE","re","rai","rO","ro","rau","la","lA","li","lI","lu","lU","lR","lE","le","lai","lO","lo","lau","va","vA","vi","vI","vu","vU","vR","vE","ve","vai","vO","vo","vau","za","zA","zi","zI","zu","zU","zR","zE","ze","zai","zO","zo","zau","Sa","SA","Si","SI","Su","SU","SR","SE","Se","Sai","SO","So","Sau","sa","sA","si","sI","su","sU","sR","sE","se","sai","sO","so","sau","ha","hA","hi","hI","hu","hU","hR","hE","he","hai","hO","ho","hau","La","LA","Li","LI","Lu","LU","LR","LE","Le","Lai","LO","Lo","Lau","Za","ZA","Zi","ZI","Zu","ZU","ZR","ZE","Ze","Zai","ZO","Zo","Zau","r2a","r2A","r2i","r2I","r2u","r2U","r2R","r2E","r2e","r2ai","r2O","r2o","r2au","n2a","n2A","n2i","n2I","n2u","n2U","n2R","n2E","n2e","n2ai","n2O","n2o","n2au","a","A","i","I","u","U","R","E","e","ai","O","o","au","k","kh","g","gh","G","c","ch","j","jh","J","T","Th","D","Dh","N","t","th","d","dh","n","p","ph","b","bh","m","y","r","l","v","z","S","s","h","L","Z","r2","n2","aM","aH"]

  script_combinations = list(itertools.combinations(scriptsAll, 2))

  script_combinations = [scriptC for scriptC in script_combinations if "Dogra" in scriptC]

  total = len(script_combinations)

  i = 0
  for script1, script2 in script_combinations:
    i = i + 1

    print('Processing ' + str(i) + ' out of ' + str(total))

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

    results[script1] = letters_script1_common
    results[script2] = letters_script2_common

    script_sort = sorted([script1, script2])
    suffix = script_sort[0] + '_' + script_sort[1]

    if script_sort[0] <= 'BatakToba':
        index = '1'
    elif script_sort[0] <= 'Grantha':
        index = '2'
    elif script_sort[0] <= 'Khudawadi':
        index = '3'
    else:
        index = '4'

    f = io.open("resources/common_letters" + index + "/common_letters_" + suffix + ".json", mode="w", encoding="utf-8")
    f.write(json.dumps(results, ensure_ascii = False, sort_keys=True, indent=4))
    f.close()

if __name__ == "__main__":
  print('Generating Script Mapping as Json')
  #generate_script_map()
  print('Generating Script Matrix')
  #generate_script_matrix()
  print('Generating Syllabary')
  #generate_syllables()
  print('Generating Conjuncts')
  generate_conjuncts()
  print('Generating Common Letters')
  #generate_common_letters()







