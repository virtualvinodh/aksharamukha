# -*- coding: utf-8 -*-

from . import GeneralMap as GM
from . import ScriptMap
from aksharamukha.ScriptMap.Roman import Avestan
from aksharamukha.ScriptMap.MainIndic import Ahom, Tamil,Malayalam,Gurmukhi,Oriya,Saurashtra,Sinhala,Urdu,Devanagari, Chakma, Limbu, Takri, TamilExtended
from aksharamukha.ScriptMap.EastIndic import Tibetan, Thai, PhagsPa, ZanabazarSquare, Burmese, KhamtiShan
from . import ConvertFix as CF
import re
import functools

### Write Lotsssss of Comments
### Rewrite all ListC, ListV as sorted(List,key=len,reverse=True). Then Correctrulu may be unnecessary

### Consider Adding Options to ignore Nukta etc for Gujarati bengali by default

## Todo
## Fix Font links and names in description

def default(Strng):

    return Strng

def urduRemoveInherent(Strng):
    Strng = re.sub('\Ba', '', Strng)

    return Strng

def HebrewVetVav(Strng):
    shortVowels = '(' + '|'.join(['\u05B7', '\u05B8', '\u05B4', '\u05BB', '\u05B5', '\u05B6', '\u05B9', '\u05B0']) + ')'

    Strng = re.sub(shortVowels + '(' + 'ו' + ')' + '(?!\u05BC)', r'\1' + 'ב', Strng)

    # Bet with Holam for Vav with beth with holam

    Strng = Strng.replace('בֺ', 'בֹ')

    return Strng

def devanagariuttara(Strng):

    return Strng

def devanagarinepali(Strng):

    return Strng

def devanagaribalbodh(Strng):

    return Strng

def devanagarijain(Strng):

    return Strng

def HiraganaaunotDipthong(Strng):

    return Strng

def IASTISONasalTilde(Strng):

    return Strng

def HeberewQoph(Strng):
    Strng = Strng.replace('כּ', 'ק').replace('ךּ', 'ק')

    return Strng

def HebewShortO(Strng):
    Strng = re.sub('(?<!ו)\u05B9', '\u05C7', Strng)

    return Strng

def HebrewKatevMalei(Strng):
    Strng = Strng.replace('ָ', 'א') # long aa
    Strng = Strng.replace('ַ', 'א') # short a

    return Strng

def HebrewnonFinalShort(Strng):
    finals = ['ך', 'ם', 'ן', 'ף', 'ץ', 'ףּ', 'ךּ']
    finalCons = ['כ', 'מ', 'נ', 'פ', 'צ', 'פּ', 'כּ']

    otherCons = 'ב,ח,ע,צ,ש,ת'.split(',')
    consonantsAll = '(' + '|'.join(GM.CrunchSymbols(GM.Consonants, 'Hebrew') + finals  + ['׳', 'י', 'ו'] + otherCons) + ')'

    shortVowels = ['\u05B7', '\u05B8', '\u05B4', '\u05BB', '\u05B5', '\u05B6', '\u05B9', '\u05C7']
    shortVowelsR = '(' + '|'.join(['\u05B7', '\u05B8', '\u05B4', '\u05BB', '\u05B5', '\u05B6', '\u05B9', '\u05C7'] + ['׳']) + ')'

    for s in shortVowels:
        Strng = re.sub('(' + s + ')' + '(׳?)' + '(?!' + consonantsAll + ')', r'\1\2' + 'ה' + '\u02BE', Strng )

    for f, c in zip(finals, finalCons):
        Strng = re.sub('(' + f + ')' + shortVowelsR + '(׳?)' + 'ה' + '\u02BE', c + r'\2\3' + 'ה', Strng)

    for f in finals:
        Strng = Strng.replace(f + '\u05B0', f)

    Strng = Strng.replace('\u05B0' + '׳' + 'ה' + '\u02BE', '\u05B0' + '׳' )
    Strng = Strng.replace('וֹה' + '\u02BE', 'וֹ' )

    Strng = Strng.replace('\u02BE', '')

    uVowels = ['וֹ', 'וּ']

    for s in uVowels:
        Strng = re.sub('(' + s + ')' + '(׳?)' + '(?!' + consonantsAll + ')', r'\1\2' + 'א', Strng )

    return Strng

def DevanagariAnusvara(Strng):

    return NasalToAnusvara(Strng, 'Devanagari')

def jainomDevangari(Strng):
    Strng = Strng.replace('ॐ', 'ꣽ')

    return Strng

def GurmukhiCandrabindu(Strng):
    Strng = Strng.replace('ਁ', 'ਂ')

    return Strng

def mDotAboveToBelow(Strng):
    Strng = Strng.replace('ṃ', 'ṁ')

    return Strng

def noLongEO(Strng):
    Strng = Strng.replace('ē', 'e').replace('ō', 'o')

    return Strng

def TamilStyleUUCore(Strng):
    Strng = re.sub('([ഖഗഘഛഝഠഡഢഥദധഫബഭ])' + '([ുൂ])', r'\1' + '\u200D' + r'\2', Strng)

    return Strng

def TamilStyleUUOther(Strng):
    Strng = re.sub('([ജശഷസഹ])' + '([ുൂ])', r'\1' + '\u200D' + r'\2', Strng)
    Strng = re.sub('(ശ്ര)' + '([ുൂ])', r'\1' + '\u200D' + r'\2', Strng)
    Strng = re.sub('(ശ്‍ര)' + '([ുൂ])', r'\1' + '\u200D' + r'\2', Strng)


    return Strng

def ContextualLLa(Strng):
    ListVS = '|'.join(GM.CrunchSymbols(GM.VowelSigns, 'Tamil'))
    ListC = '|'.join(GM.CrunchSymbols(GM.Consonants, 'Tamil'))

    Strng = re.sub('(ஆவ|ாவ)'+ 'ல', r'\1' +  'ள', Strng)
    Strng = re.sub('(்ரவா|்ரவ|ர|பவ|வி|ரா|ஷ்க|த⁴வ)'+ 'ல', r'\1' +  'ள', Strng)
    Strng = re.sub('(யா|யாம|கோம)'+ 'ல', r'\1' +  'ள', Strng)
    Strng = re.sub('(மௌ)'+ 'ல', r'\1' +  'ள', Strng)
    Strng = re.sub('([\s^])(ந)'+ 'ல', r'\1' +  'ள', Strng)
    Strng = Strng.replace('கலத்ர', 'களத்ர')
    Strng = Strng.replace('ஶீதல', 'ஶீதள')
    Strng = Strng.replace('ஸுதல', 'ஸுதள')
    Strng = Strng.replace('காலி', 'காளி')
    Strng = Strng.replace('காலீ', 'காளீ')
    Strng = Strng.replace('கலேவர', 'களேவர')
    Strng = Strng.replace('கலேவர', 'களேவர')
    Strng = Strng.replace('ப³ஹுல', 'ப³ஹுள')
    Strng = Strng.replace('கஶ்மல', 'கஶ்மள')

    Strng = re.sub('([கத])' + '(' + ListVS + ')?' + '([³⁴])'+ 'ல', r'\1\2\3' +  'ள', Strng)
    Strng = re.sub('(ஜு)'+ 'ல', r'\1' +  'ள', Strng)
    Strng = re.sub('(து)'+ 'லசி', r'\1' +  'ளசி', Strng)
    Strng = re.sub('(ரிம)'+ 'ல', r'\1' +  'ள', Strng)

    Strng = Strng.replace('ள்ய', 'ல்ய')

    return Strng

def FinalNNa(Strng):
    Strng = re.sub('ன', 'ந', Strng)

    Strng = re.sub('ந்' + '([\.।॥,!-])', 'ன்' + r'\1', Strng)
    Strng = re.sub('ந்' + '(\s)', 'ன்' + r'\1', Strng)
    Strng = re.sub('ந்$', 'ன்', Strng)

    return Strng

def TamilpredictDentaNaExtended(Strng):
    listDentalNa = '''ഩഖ
ഩഗര
ഩകുല
ഩഗ്‌ഩ
ഩക്ഷത്‌ര
ഩടരാജ
ഩടീ
ഩദീ
ഩന്‌ദഩ
ഩപുംസക
ഩഭ**
ഩമ**
ഩമശ്‌
ഩമസ്‌
ഩമാമ
ഩമാമി
ഩമാമോ
ഩമുചി
ഩമോ
ഩമോനമ
ഩമോനമോ
ഩമോസ്‌തു
ഩമോസ്‌തുതേ
ഩമഃ
ഩയഩ
ഩര**
ഩരക
ഩര്‌തക
ഩര്‌തഩ
ഩര്‌മദ
ഩല**
ഩലിഩ
ഩവ**
ഩവീഩ
ഩവ്‌യ
ഩശ്‌**
ഩഷ്‌ട
ഩാരായണ
ഩാഗ
ഩാടക
ഩാഡീ
ഩാട്‌യ
ഩാഡ്‌യ
ഩാഥ
ഩാദ
ഩാരത
ഩാഩാ***
ഩാഩ്‌യ**
ഩാഩൃത
ഩാഭ
ഩാമ
ഩായക
ഩായികാ
ഩാരദ
ഩാരസിംഹ
ഩാരി
ഩാരീ
ഩാവ***
ഩാശ
ഩാസിക
ഩിഗമ
ഩികട
ഩികര
ഩികാമ
ഩികായ
ഩിഖില
ഩികുഞ്‌ജ
ഩിഘൂഩ
ഩികേത
ഩിഗ്‌രഹ
ഩിഗൃഹ
ഩികൃന്‌ത
ഩിഗ്‌രന്‌ത
ഩിക്ഷിപ
ഩിക്ഷേപ
ഩിഘ്‌ഩ
ഩിജ
ഩിദര്‌ശ
ഩിതമ്‌ബ
ഩിതര
ഩിദാഘ
ഩിദാഩ
ഩിതാന്‌ത
ഩിധാഩ
ഩിധായ
ഩിധ
ഩിധേഹി
ഩിദ്‌ര
ഩിത്‌യ
ഩിന്‌ദാ
ഩിബദ്‌ധ
ഩിബധ്‌
ഩിബന്‌ധഩ
ഩിപട
ഩിപതിത
ഩിപത്‌യ
ഩിപപാത
ഩിപാതിത
ഩിപാത്‌യ
ഩിപുണ
ഩിബോധ
ഩിഭൃത
ഩിമഗ്‌ഩ
ഩിമിത്‌ത
ഩിമിഷ
ഩിയത
ഩിയന്‌ത
ഩിയന്‌ത്‌ര
ഩിയമ
ഩിയുക്‌ത
ഩിയുജ്‌യ
ഩിയോ
ഩിര
ഩിര്‌
ഩിലയ
ഩിവര്‌
ഩിവസ
ഩിവാര
ഩിവാസ
ഩിവിഷ്‌ട
ഩിവേദ
ഩിവേശ
ഩിവൃ
ഩിശ
ഩിശ്‌
ഩിഷ
ഩിഷ്‌
ഩിസ
ഩിസ്‌
ഩിഹിത
ഩിഃശ
ഩിഃഷ
ഩിഃസ
ഩീച
ഩീതി
ഩീര
ഩീല
ഩൂതഩ
ഩൂപുര
ഩേത്‌ര
ഩേയ**
ഩൈമിത്‌ത
ഩൈമിഷ
ഩൈരാശ്‌യ
ഩൈരൃത
ഩൈവേദ്‌യ
ഩൈഷ്‌
ഩ്‌യായ
ഩ്‌യാസ
ഩ്‌യൂഩ
ഩൃ'''.split('\n')

    vir = Tamil.ViramaMap[0]

    for wordNna in listDentalNa:
        wordNa = re.sub('^ഩ', 'ന', wordNna)
        if '²' in wordNna[-1] or '³' in wordNna[-1] or '⁴' in wordNna[-1]:
            number = wordNna[-1]

            wordNnaN = wordNna[:-1]
            wordNaN = wordNa[:-1]
            for vow in GM.CrunchSymbols(GM.VowelSigns, 'Tamil'):
                Strng = Strng.replace(wordNnaN + vow + number, wordNaN + vow + number)

        Strng = Strng.replace(wordNna, wordNa)

        for wordNna in ['ഩാമ','ഩര']:
            wordNa = re.sub('^ഩ', 'ന', wordNna)
            Strng = Strng.replace(wordNa + vir, wordNna + vir)

        Strng = Strng.replace('ഩ്‌ന', 'ന്‌ന')

    return Strng

def TamilpredictDentaNa(Strng):
    listDentalNa = '''னக²
னக³ர
னகுல
னக்³ன
னக்ஷத்ர
னடராஜ
னடீ
னதீ³
னந்த³ன
னபும்ʼஸக
னப⁴**
னம**
னமஶ்
னமஸ்
னமாம
னமாமி
னமாமோ
னமுசி
னமோ
னமோநம
னமோநமோ
னமோஸ்து
னமோஸ்துதே
னம꞉
னயன
னர**
னரக
னர்தக
னர்தன
னர்மத³
னல**
னலின
னவ**
னவீன
னவ்ய
னஶ்**
னஷ்ட
னாராயண
னாக³
னாடக
னாடீ³
னாட்ய
னாட்³ய
னாத²
னாத³
னாரத
னானா***
னான்ய**
னான்ருʼத
னாப⁴
னாம
னாயக
னாயிகா
னாரத³
னாரஸிம்ʼஹ
னாரி
னாரீ
னாவ***
னாஶ
னாஸிக
னிக³ம
னிகட
னிகர
னிகாம
னிகாய
னிகி²ல
னிகுஞ்ஜ
னிகூ⁴ன
னிகேத
னிக்³ரஹ
னிக்³ருʼஹ
னிக்ருʼந்த
னிக்³ரந்த
னிக்ஷிப
னிக்ஷேப
னிக்⁴ன
னிஜ
னித³ர்ஶ
னிதம்ப³
னிதர
னிதா³க⁴
னிதா³ன
னிதாந்த
னிதா⁴ன
னிதா⁴ய
னித⁴
னிதே⁴ஹி
னித்³ர
னித்ய
னிந்தா³
னிப³த்³த⁴
னிப³த்⁴
னிப³ந்த⁴ன
னிபட
னிபதித
னிபத்ய
னிபபாத
னிபாதித
னிபாத்ய
னிபுண
னிபோ³த⁴
னிப்⁴ருʼத
னிமக்³ன
னிமித்த
னிமிஷ
னியத
னியந்த
னியந்த்ர
னியம
னியுக்த
னியுஜ்ய
னியோ
னிர
னிர்
னிலய
னிவர்
னிவஸ
னிவார
னிவாஸ
னிவிஷ்ட
னிவேத³
னிவேஶ
னிவ்ருʼ
னிஶ
னிஶ்
னிஷ
னிஷ்
னிஸ
னிஸ்
னிஹித
னி꞉ஶ
னி꞉ஷ
னி꞉ஸ
னீச
னீதி
னீர
னீல
னூதன
னூபுர
னேத்ர
னேய**
னைமித்த
னைமிஷ
னைராஶ்ய
னைர்ருʼத
னைவேத்³ய
னைஷ்
ன்யாய
ன்யாஸ
ன்யூன
ன்ருʼ'''.split('\n')

    vir = Tamil.ViramaMap[0]

    Tamillist = '²³⁴ஃஅஆஇஈஉஊஎஏஐஒஓஔகஙசஜஞடணதநனபமயரறலளழவஷஸஹாிீுூெேைொோௌ்ௗ'

    for wordNna in listDentalNa:
        wordNa = re.sub('^ன', 'ந', wordNna)
        if '²' in wordNna[-1] or '³' in wordNna[-1] or '⁴' in wordNna[-1]:
            number = wordNna[-1]

            wordNnaN = wordNna[:-1]
            wordNaN = wordNa[:-1]
            for vow in GM.CrunchSymbols(GM.VowelSigns, 'Tamil'):
                Strng = Strng.replace(wordNnaN + vow + number, wordNaN + vow + number)

        Strng = Strng.replace(wordNna, wordNa)

        for wordNna in ['னாம','னர']:
            wordNa = re.sub('^ன', 'ந', wordNna)
            Strng = re.sub('([' + Tamillist +'])('+wordNa + vir +')', r'\1' + wordNna + vir, Strng)

        Strng = Strng.replace('ன்ந', 'ந்ந')

        Strng = Strng.replace('னாம்ன', 'நாம்ன')

    return Strng

def AhomClosed(Strng):
    vir = Ahom.ViramaMap[0]
    anu = Ahom.AyogavahaMap[1]

    #closed i
    Strng = Strng.replace('\U00011722', '\U00011723')
    Strng = re.sub('(\U00011723)(.)('+vir+')', '\U00011722'+r'\2\3', Strng)
    Strng = Strng.replace(anu + '\U00011723', anu + '\U00011722')

    #closed u
    Strng = Strng.replace('\U00011724', '\U00011725')
    Strng = re.sub('(\U00011725)(.)('+vir+')', '\U00011724'+r'\2\3', Strng)
    Strng = Strng.replace(anu + '\U00011725', anu + '\U00011724')

    #closed e
    Strng = re.sub('(\U00011726\U00011727)(.)('+vir+')', '\U00011726'+r'\2\3', Strng)
    Strng = Strng.replace('\U00011726\U0001172A\U00011727', anu + '\U00011727')

    #closed o
    Strng = re.sub('(\U00011726\U00011721)(.)('+vir+')', '\U00011728'+r'\2\3', Strng)
    Strng = Strng.replace('\U00011726\U0001172A\U00011721', anu + '\U00011728')

    return Strng

def TeluguTamilZha(Strng):

    return Strng

def TeluguTamilRra(Strng):
    Strng = Strng.replace('ఱ్ఱ', 'ౘ్ౘ')
    Strng = Strng.replace('ఱ', 'ౘ')

    return Strng

def ThaiNativeConsonants(Strng):
    Strng = Strng.replace('ท', 'ด')
    Strng = Strng.replace('พ', 'บ')
    Strng = Strng.replace("\u0E36","\u0E34\u0E4D")
    Strng = Strng.replace('ํ', 'งฺ')

    Strng = re.sub('(\u0E3A)([ยรลวห])', '\u035C'+ r'\2', Strng)
    Strng = Strng.replace('ห\u0E3A', 'ห\u035C')

    Strng = re.sub('([ยรลวห])' + '\u035C' + r'\1', r'\1' + '\u0E3A' + r'\1', Strng)

    Strng = re.sub('(า)(.)(ฺ)', '็' + r'\1\2\3', Strng)
    Strng = re.sub('([เโ])(.)(.)(ฺ)',  r'\1\2' + '็' +  r'\3\4', Strng)

    Strng = ThaiTranscription(Strng, False)

    Strng = Strng.replace('ะ͜', '\u035C')
    Strng = Strng.replace('ะ็', '็')
    Strng = re.sub('([เโไ])(.)(\u035C)(.)([ะ\u0E31])', r'\1\2\3\4', Strng)

    Strng = Strng.replace('ค', 'ก\u0325')
    Strng = Strng.replace('ช', 'จ\u0325')

    Strng = Strng.replace('ง', 'งํ')

    Strng = Strng.replace('ะงํ\u035C', '\u0E31งํ')

    Strng = re.sub('([เโไ])(งํ)([าัะ])', r'\1' + 'ง' + r'\2', Strng)
    Strng = re.sub('([เโไ])(งํ)', r'\1' + 'ง', Strng)
    Strng = re.sub('(งํ)([าัะ])', 'ง' + r'\2', Strng)

    return Strng

def KhamiShanMyanmarNumerals(Strng):
    for x, y in zip(KhamtiShan.NumeralMap, Burmese.NumeralMap):
        Strng = Strng.replace(x, y)

    return Strng

def KhamtiShanRa(Strng):

    Strng = Strng.replace('ရ', 'ꩳ')

    return Strng

def granthafinal(Strng):

    return Strng

def Dot2Dandas(Strng):
    Strng = Strng.replace('..', '॥')
    Strng = Strng.replace('.', '।')

    return Strng

def SaurastraHaaruColon(Strng):
    vir = Tamil.ViramaMap[0]
    ha = Tamil.ConsonantMap[-1]

    Strng = Strng.replace(vir + ha, ':')

    ListVS = '|'.join(GM.CrunchSymbols(GM.VowelSigns, 'Tamil'))

    Strng = re.sub('(:)' + '(' + ListVS + ')', r'\2\1', Strng)

    Strng = re.sub('(\s)(ன)', r'\1' + 'ந', Strng)
    Strng = re.sub('^ன', 'ந', Strng)

    return Strng

def TamilExtendedNNA(Strng):
    na = TamilExtended.ConsonantMap[19]
    nna = TamilExtended.SouthConsonantMap[3]
    vir = TamilExtended.ViramaMap[0]
    ta = TamilExtended.ConsonantMap[15]

    ListV = '|'.join(GM.CrunchSymbols(GM.Vowels+GM.VowelSigns+GM.Consonants,'TamilExtended')+[TamilExtended.SignMap[0]])

    Strng = re.sub('('+ListV+')'+ GM.VedicSvaras + '('+na+')' + '(?!' + vir + ')',r'\1\2'+nna,Strng)
    Strng = re.sub('('+ListV+')'+ GM.VedicSvaras + '('+na+')' + '(?!' + vir + ')',r'\1\2'+nna,Strng)

    Strng = re.sub('(ന്‌)(?![തഥദധ])', 'ഩ്‌', Strng)

    Strng = re.sub('(\s)ഩ്', r'\1' + 'ന്‌', Strng)
    Strng = re.sub('^ഩ്', r'' + 'ന്‌', Strng)

    Strng = TamilpredictDentaNaExtended(Strng)

    return Strng

def TakriRemoveGemination(Strng):

    Strng = re.sub('(.)' + Takri.ViramaMap[0] + r'\1', r'\1', Strng)

    return Strng

def MongolianSyllabize(Strng):
    vowels = '(' + '|'.join(GM.CrunchSymbols(GM.Vowels, 'Mongolian')+['\u1820']) + ')'
    consonants = '(' + '|'.join(GM.CrunchSymbols(GM.Consonants, 'Mongolian')) + ')'

    Strng = re.sub(consonants + '?' + vowels, r'\1\2' + ' ', Strng)
    Strng = re.sub('(\u180E\u1820)' + consonants, r'\1 \2', Strng)
    Strng = re.sub('\u1820 ', '\u1820\u180B ', Strng)
    Strng = Strng.replace('ᠣᠸᠠ᠋', 'ᠣᠸᠠ')
    Strng = Strng.replace('ᠣᠸᠸᠠ᠋', 'ᠣᠸᠸᠠ')
    Strng = Strng.replace(' \u180E', '\u180E')
    Strng = Strng.replace(' ' + '\u200B', '')
    Strng = Strng.replace(' ᢁ', 'ᢁ')

    return Strng

def TibetanSyllabize(Strng):
    vowels = '(' + '|'.join(GM.CrunchSymbols(GM.Vowels, 'Tibetan')) + ')'
    consonants = '(' + '|'.join(GM.CrunchSymbols(GM.Consonants, 'Tibetan')+['ཨ','ཅ','ཆ','ཇ','ཇྷ']) + ')'
    vowelsigns = '(' + '|'.join(GM.CrunchSymbols(GM.VowelSigns, 'Tibetan')+['\u0F80']) + ')'
    combiningSigns = '(' + '|'.join(GM.CrunchSymbols(GM.CombiningSigns, 'Tibetan')+['\u0F82']) + ')'
    ListSubC = '(' + '|'.join([chr(x+80) for x in range(0x0F40,0x0F68)] + ['ྻ','ྺ','ྼ']) + ')' # Subjoined Consonants

    Strng = re.sub(vowelsigns + combiningSigns + '?', r'\1\2་', Strng)
    Strng = re.sub(consonants , r'\1་', Strng)
    Strng = re.sub(ListSubC, r'\1་', Strng)
    Strng = re.sub('་' + vowelsigns, r'\1', Strng)
    Strng = re.sub('་' + ListSubC, r'\1', Strng)
    Strng = re.sub('་' + combiningSigns, r'\1', Strng)
    Strng = re.sub(combiningSigns, r'\1་', Strng)

    Strng = Strng.replace('་་', '་')

    return Strng

def SoyomboSyllabize(Strng):
    vowels = '(' + '|'.join(GM.CrunchSymbols(GM.Vowels, 'Soyombo')) + ')'
    consonants = '(' + '|'.join(GM.CrunchSymbols(GM.Consonants, 'Soyombo')+['𑩐', '\U00011A83']) + ')'
    vowelsigns = '(' + '|'.join(GM.CrunchSymbols(GM.VowelSigns, 'Soyombo')) + ')'
    combiningSigns = '(' + '|'.join(GM.CrunchSymbols(GM.CombiningSigns, 'Soyombo')) + ')'

    fin = '(' + '|'.join(['\U00011A8A','\U00011A8B','\U00011A8C','\U00011A8D','\U00011A8E','\U00011A8F','\U00011A90','\U00011A91','\U00011A92','\U00011A93','\U00011A94']) + ')'

    Strng = re.sub(vowelsigns + combiningSigns + '?', r'\1\2 ', Strng)
    Strng = re.sub(consonants , r'\1 ', Strng)
    Strng = re.sub(' ' + vowelsigns, r'\1', Strng)
    Strng = re.sub(' ' + combiningSigns, r'\1', Strng)
    Strng = re.sub('\U00011A99' + ' ', '\U00011A99', Strng)
    Strng = re.sub(combiningSigns, r'\1 ', Strng)
    Strng = re.sub(' 𑪘', '\U00011A98', Strng)
    Strng = re.sub(fin, r'\1 ', Strng)
    Strng = re.sub('( )' + fin, r'\2 ', Strng)
    #Strng = re.sub(combiningSigns, r'\1་', Strng)

    return Strng


def TakriArchaicKha(Strng):

    return Strng.replace('𑚸', '𑚋')

def TeluguReph(Strng):
    consonants = '(' + '|'.join(GM.CrunchSymbols(GM.Consonants, 'Telugu')) + ')'
    Strng = re.sub('ర్' + consonants, 'ర్‍' + r'\1', Strng)
    Strng = Strng.replace('\u0C4Dర్‍', '\u0C4Dర్')

    return Strng

def PhagsPaTib(Strng):

    return Strng

def PhagsPaSeal(Strng):

    return Strng

def TamilExtendedAnusvara(Strng):
    Strng = AnusvaraToNasal(Strng, 'TamilExtended')
    Strng = Strng.replace('\u0D02', 'മ്‌')

    return Strng

def RomanReadableLongEO(Strng):

    Strng = Strng.replace('o', 'oa')
    Strng = Strng.replace('oa\'', 'o')

    Strng = Strng.replace('e', 'ae')
    Strng = Strng.replace('ae\'', 'e')

    Strng = Strng.replace('aeae', 'ee')
    Strng = Strng.replace('oaoa', 'oo')

    return Strng

def TeluguArasunnaChandrabindu(Strng):
    Strng = Strng.replace('ఀ', 'ఁ')

    return Strng

def MarchenSanskritPalatals(Strng):
    tsaSeries = ['\U00011C82', '\U00011C83', '\U00011C84']
    jaSereis =  ['\U00011C76', '\U00011C77', '\U00011C78']

    for x, y in zip(tsaSeries, jaSereis):
        Strng = Strng.replace(x, y)

    return Strng


def SoyomboSanskritPalatals(Strng):
    tsaSeries = ['𑩵','𑩶','𑩷']
    caSeries = ['𑩡','𑩢','𑩣']

    for x, y in zip(tsaSeries,caSeries):
        Strng = Strng.replace(x, y)

    return Strng

def TibetanSanskritPalatals(Strng):
    caSeries = ['ཅ','ཆ','ཇ','ཇྷ']
    tsaSeries = ['ཙ','ཚ','ཛ','ཛྷ']

    for x, y in zip(tsaSeries,caSeries):
        Strng = Strng.replace(x, y)

    return Strng

def ZanabazarSanskritPalatals(Strng):
    tsaSeries = ['𑨣', '𑨤', '𑨥']
    caSeries = ['𑨐','𑨑','𑨒']

    for x, y in zip(tsaSeries,caSeries):
        Strng = Strng.replace(x, y)

    return Strng

def SoyomboFinals(Strng):

    return Strng

def SoyomboInitials(Strng):
    viraCon = ['\U00011A7C\U00011A99', '\U00011A7D\U00011A99', '\U00011A81\U00011A99']
    initial = ['\U00011A86', '\U00011A87', '\U00011A89']

    for x, y in zip(viraCon, initial):
        Strng = Strng.replace(x, y)

    return Strng

def ZanzabarSpaceTsheg(Strng):
    Strng = Strng.replace(' ', '\U00011A41')

    return Strng

def SoyomboSpaceTscheg(Strng):
    Strng = Strng.replace(' ', '\U00011A9A')

    return Strng

def NasaltoAnsvaraIASTISO(Strng):
    Strng = Strng.replace('ṁ', 'ṃ')

    Strng = re.sub('(ṃ)(k|g)', 'ṅ' + r'\2', Strng)
    Strng = re.sub('(ṃ)(c|j)', 'ñ' + r'\2', Strng)
    Strng = re.sub('(ṃ)(ṭ|ḍ)', 'ṇ' + r'\2', Strng)
    Strng = re.sub('(ṃ)(t|d)', 'n' + r'\2', Strng)
    Strng = re.sub('(ṃ)(p|b)', 'm' + r'\2', Strng)

    return Strng

def removeDiacritics(Strng):
    diacritics = ['\u0331', '\u0306', '\u0323', '\u035F', '\u0324', '\u035F', '\u0307', '\u0301', '\u0303', '\u0310', '\u0306', '\u0302', '\u0304']

    for dia in diacritics:
        Strng = Strng.replace(dia, '')

    vowelDia = ['а̄', 'ӣ', 'ӯ', 'ӗ']
    vowel = ['\u0430', '\u0438', '\u0443', '\u044D']

    for x, y in zip(vowelDia, vowel):
        Strng = Strng.replace(x, y)

    return Strng

def ranjanalantsa(Strng):
    Strng = Strng.replace('་', ' ')
    return Strng

def ranjanawartu(Strng):
    Strng = Strng.replace('་', '࿎ ')
    return Strng

def TaiKuen(Strng):
    return Strng

def TaiThamLao(Strng):
    return Strng

def egrantamil(Strng):
    return Strng

def tibetandbumed(Strng):
    return Strng

def oldtamilortho(Strng):
    return Strng

def nepaldevafont(Strng):
    return Strng

def granthaserif(Strng):
    return Strng

def ChakmaPali(Strng):
    listC = '('+"|".join(sorted(GM.CrunchSymbols(GM.Consonants,"Chakma")+Chakma.VowelMap[:1],key=len,reverse=True))+')'
    listV = '('+"|".join(sorted(GM.CrunchSymbols(GM.VowelSigns,"Chakma")+Chakma.ViramaMap+['\U00011133'],key=len,reverse=True))+')'

    Strng = ChakmaGemination(Strng, reverse = True)

    Strng = Strng.replace('𑄤', '\U00011147') # Replace Ya
    Strng = Strng.replace('𑄡', '𑄠') # Replace vA

    ## reverse A introduction

    Strng = Strng.replace("\U00011127","\u02BE")
    Strng = re.sub("("+listC+")"+"(?!"+listV+'|\u02BE'+")",r'\1''\U00011127',Strng)
    Strng = Strng.replace("\u02BE","")

    ## Replace A with Visarga as per Pali

    Strng = Strng.replace('\U00011127', '\U00011102')

    ## Replace subjoining with Explicit Virama

    Strng = Strng.replace('\U00011133', '\U00011134')

    return Strng

def ThaiSajjhayawithA(Strng):
    Strng = ThaiSajjhayaOrthography(Strng)
    Strng = Strng.replace('ัง','ังฺ')
    Strng = ThaiTranscription(Strng, anusvaraChange = True)

    Strng = Strng.replace('ะํ', 'ํ')
    Strng = Strng.replace('ะั', 'ั')
    Strng = Strng.replace('ะ๎', '๎')

    Strng = re.sub('([เโไ])(.๎)([ยรลวศษสหฬ])ะ', r'\1\2\3', Strng)

    Strng = Strng.replace("\u0E32\u0E4D", "\u0E33").replace("\u0E34\u0E4D", "\u0E36") # reverse AM, iM

    return Strng

def LaoSajjhaya(Strng):
    Strng = ThaiSajjhayaOrthography(Strng, Script = "LaoPali")

    return Strng

def LaoSajjhayawithA(Strng):
    Strng = ThaiSajjhayaOrthography(Strng, Script = "LaoPali")
    Strng = Strng.replace('ັງ', 'ັງ຺')
    Strng = CF.LaoPaliTranscribe(Strng, anusvaraChange = True)

    Strng = Strng.replace('ະໍ', 'ໍ')
    Strng = Strng.replace('ະັ', 'ັ')
    Strng = Strng.replace('ະ๎', '๎')

    Strng = Strng.replace('ະ໌', '໌')
    Strng = Strng.replace('ະົ', 'ົ')

    Strng = re.sub('([ເໂໄ])(.๎)([ຍຣລວຨຩສຫຬ])ະ', r'\1\2\3', Strng)

    Strng = Strng.replace('າໍ', 'ຳ')

    return Strng

def UseAlternateVSU(Strng):
    Strng = Strng.replace('𑖲', '𑗜')

    return Strng

def UseAlternateVSUU(Strng):
    Strng = Strng.replace('𑖳', '𑗝')

    return Strng

def UseAlternateU(Strng):
    Strng = Strng.replace('𑖄', '𑗛')

    return Strng

def UseAlternateI1(Strng):
    Strng = Strng.replace('𑖂', '𑗘')

    return Strng

def UseAlternateI2(Strng):
    Strng = Strng.replace('𑖂', '𑗙')

    return Strng

def UseAlternateII(Strng):
    Strng = Strng.replace('𑖃',  '𑗚')

    return Strng

def GranthaOldau(Strng):
    Strng = Strng.replace('𑍗', '𑍌')

    return Strng

def DevanagariACandra(Strng):
    Strng = Strng.replace('ऍ', 'ॲ')

    return Strng

def WarangCitiModernOrthogaphy(Strng):
    Strng = re.sub('([\U000118D4\U000118D5\U000118CC\U000118CB\U000118CF\U000118CE\U000118D2\U000118D1\U000118D5\U000118D4\U000118D8\U000118D7\U000118DB])(\u200D)(𑣙)', r'\1', Strng)
    Strng = Strng.replace('𑣝', '𑣞')

    Strng = Strng.replace('\u200D', '')

    return Strng

def ChakmaEnableAllConjuncts(Strng):
    listC = '('+"|".join(sorted(GM.CrunchSymbols(GM.Consonants,"Chakma")+Chakma.VowelMap[:1],key=len,reverse=True))+')'
    Strng = re.sub("\U00011134"+'('+listC+')',"\U00011133"+r'\1',Strng)

    Strng = ChakmaGemination(Strng)

    return Strng

def ChakmaGemination(Strng, reverse = False):
    ListC = "(" + "|".join(GM.CrunchSymbols(GM.Consonants, 'Chakma')) + ")"
    virs = "([\U00011134\U00011133])"
    virExp = "\U00011134"
    virDep = "\U00011133"
    ListV = '('+"|".join(sorted(GM.CrunchSymbols(GM.VowelSignsNV,"Chakma"), key=len, reverse = True)) + ")"

    if not reverse:
        Strng = re.sub(ListC + virs + r'\1' + ListV, r'\1' + virExp + r'\3' , Strng)

        Strng = re.sub(ListC + virExp + r'\1' + virDep + ListC, r'\1' + virExp + virDep + r'\2' , Strng)
        Strng = re.sub(ListC + virDep + r'\1' + virDep + ListC, r'\1' + virExp + virDep + r'\2' , Strng)

        Strng = re.sub(virDep + ListC + virExp + ListV, virExp + r'\1' + virExp + r'\2' , Strng)

        # Strng = re.sub(ListC + virExp + virExp, r'\1' + virExp + r'\1' + virExp, Strng)
    else:
        Strng = re.sub(ListC + virExp + ListV, r'\1' + virExp + r'\1' + r'\2', Strng)
        Strng = re.sub(ListC + virExp + virDep, r'\1' + virExp + r'\1' + virDep, Strng)


    return Strng

def ChakmaVowelsIndependent(Strng):
    vowelDepA = ["𑄃𑄨", "𑄃𑄪", "𑄃𑄬"]
    vowelIndep = ["\U00011104", "\U00011105" , "\U00011106"]

    for x, y in zip(vowelDepA, vowelIndep):
        Strng = Strng.replace(x, y)

    return Strng

def MultaniAbjad(Strng):
    ListAll = "(" + "|".join(GM.CrunchSymbols(GM.Characters, 'Multani') + ["𑊓", "𑊍"]) + ")"
    ListC = "(" + "|".join(GM.CrunchSymbols(GM.Consonants, 'Multani') + ["𑊓", "𑊍"]) + ")"
    ListV = "(" + "|".join(GM.CrunchSymbols(GM.Vowels, 'Multani') + ["𑊓", "𑊍"]) + ")"

    Strng = re.sub(ListC + ListV + ListC, r'\1\3', Strng)
    Strng = re.sub('('+ ListC + '{2,})' + ListV, r'\1', Strng)
    Strng = re.sub(ListV + ListC + ListV, r'\1\2', Strng)


    return Strng

def LaoNative(Strng):

    Strng = re.sub('ຕ([ເແໂໄ]?)ຕ', 'ດ' + r'\1' + 'ຕ', Strng)
    Strng = re.sub('ຕ([ເແໂໄ]?)ຖ', 'ດ' + r'\1' + 'ຖ', Strng)
    Strng = re.sub('ທ([ເແໂໄ]?)ທ', 'ດ' + r'\1' + 'ທ', Strng)
    Strng = re.sub('ສ([ເແໂໄ]?)ສ', 'ດ' + r'\1' + 'ສ', Strng)

    Strng = re.sub('ປ([ເແໂໄ]?)ປ', 'ບ' + r'\1' + 'ປ', Strng)
    Strng = re.sub('ພ([ເແໂໄ]?)ພ', 'ບ' + r'\1' + 'ພ', Strng)

    return Strng

def SundaneseHistoricConjuncts(Strng, reverse = False):
    ListC = '|'.join(GM.CrunchSymbols(GM.Consonants + GM.Vowels + GM.VowelSignsNV,'Sundanese'))

    if not reverse:
        Strng = Strng.replace('᮪ᮙ', '\u1BAC') # Subjoined m
        Strng = Strng.replace('᮪ᮝ', '\u1BAD') # Subjoined w

        ListC = '|'.join(GM.CrunchSymbols(GM.Consonants + GM.Vowels + GM.VowelSignsNV,'Sundanese'))
        Strng = re.sub('(' + ListC + ')' + 'ᮊ᮪', r'\1' + 'ᮾ', Strng) # Final K
        Strng = re.sub('(' + ListC + ')' + 'ᮙ᮪', r'\1' + 'ᮿ', Strng) # Final M

    else:
        Strng = Strng.replace('\u1BAC', '᮪ᮙ') # Subjoined m
        Strng = Strng.replace('\u1BAD', '᮪ᮝ') # Subjoined w
        Strng = Strng.replace('ᮾ','ᮊ᮪') # Final K
        Strng = Strng.replace('ᮿ','ᮙ᮪') # Final M

    return Strng

def LimbuSpellingSaI(Strng):
    vir = Limbu.ViramaMap[0]

    FCons = [x+vir for x in [Limbu.ConsonantMap[x] for x in[0,4,15,19,20,24,26,27]]]
    FinalCons = ['\u1930','\u1931','\u1933','\u1934','\u1935','\u1936','\u1937','\u1938']

    for x, y in zip(FCons, FinalCons):
        Strng = Strng.replace('\u193A' + y, x)
        Strng = Strng.replace('\u193A\u1922' + y, '\u1922' + x)

    return Strng

def siddhammukta(Strng):
    return Strng

def tradOrtho(Strng):
    return Strng

def siddhamap(Strng):
    return Strng

def KhojkiRetainSpace(Strng):
    Strng = Strng.replace('\U0001123A', ' ')

    return Strng

def BhaiksukiRetainSpace(Strng):
    Strng = Strng.replace('𑱃', ' ')

    return Strng

def KaithiRetainSpace(Strng):
    Strng = Strng.replace('⸱', ' ')

    return Strng

def MedievalTamilOrthography(Strng):
    OldEO = ['எ்', 'ெ்', 'ஒ்', 'ெ்ா', 'எ', 'ெ', 'ஒ', 'ொ']
    NewEO = ['எ', 'ெ', 'ஒ', 'ொ', 'ஏ', 'ே', 'ஓ', 'ோ']

    for x,y in zip(NewEO, OldEO):
        Strng = Strng.replace(x,y)

    return Strng

def AmbigousTamilOrthography(Strng):

    return Strng

def NewaMurmurConsonants(Strng):
    murmur = ['𑐓','𑐙','𑐤', '𑐪', '𑐭', '𑐯']
    connsh = ['𑐴𑑂𑐒', '𑐴𑑂𑐘', '𑐴𑑂𑐣', '𑐴𑑂𑐩', '𑐴𑑂𑐬', '𑐴𑑂𑐮']

    for x, y in zip(murmur, connsh):
        Strng = Strng.replace(y, x)

    return Strng

def ModiRemoveLong(Strng):
    Strng = Strng.replace('𑘂', '𑘃')
    Strng = Strng.replace('𑘅','𑘄')
    Strng = Strng.replace('𑘱', '𑘲')
    Strng = Strng.replace('𑘴','𑘳')

    Strng = Strng.replace('𑘆', '𑘨𑘲')
    Strng = Strng.replace('𑘇', '𑘨𑘲')
    Strng = Strng.replace('𑘈', '𑘩𑘲')
    Strng = Strng.replace('𑘉', '𑘩𑘲')

    Strng = Strng.replace('𑘵', '𑘿𑘨𑘲')
    Strng = Strng.replace('𑘶', '𑘿𑘨𑘲')
    Strng = Strng.replace('𑘷', '𑘿𑘩𑘲')
    Strng = Strng.replace('𑘸', '𑘿𑘩𑘲')

    return Strng

def LimbuDevanagariConvention(Strng):
    Strng = Strng.replace('ऎ', 'ए़')
    Strng = Strng.replace('ऒ', 'ओ़')
    Strng = Strng.replace('ॆ', 'े़')
    Strng = Strng.replace('ॊ', 'ो़')
    Strng = Strng.replace('꞉', 'ः')

    return Strng

def DevanagariPrishtamatra(Strng, reverse = False):
    if not reverse:
        Strng = Strng.replace('े','ॎ')
        Strng = Strng.replace('ै','ॎे')
        Strng = Strng.replace('ो','ॎा')
        Strng = Strng.replace('ौ','ॎो')
    else:
        Strng = Strng.replace('ॎे', 'ै')
        Strng = Strng.replace('ॎो', 'ौ')
        Strng = Strng.replace('ॎा', 'ो')
        Strng = Strng.replace('ॎ', 'े')

    return Strng

def ThaanaRemoveHistorical(Strng):
    return Strng.replace('ޱ','ނ')

def OriyaVaAlt(Strng):
    return  Strng.replace('ୱ','ଵ')

def GurmukhiYakaash(Strng, reverse=False):
    if not reverse:
        Strng = Strng.replace('੍ਯ','ੵ')
    else:
        Strng = Strng.replace('ੵ', '੍ਯ')

    return Strng

def dotReph(Strng):
    ListC = '('+"|".join(sorted(GM.CrunchSymbols(GM.Consonants,"Malayalam"))) + ')'

    Strng = re.sub('(?<!്)' + 'ർ' + ListC,'ൎ' + r'\1', Strng)
    Strng = re.sub('(?<!്)' +'ര്' + ListC,'ൎ' + r'\1', Strng)

    return Strng

def TamilGranthaVisarga(Strng):
    Strng = Strng.replace('꞉', '𑌃')

    return Strng

def archaicAIAU(Strng):
    Strng = Strng.replace('ൗ', 'ൌ')
    Strng = Strng.replace('ഈ', 'ൟ')

    return Strng

def MalayalamremoveHistorical(Strng):
    Strng = Strng.replace('\u0D29','\u0D28')
    Strng = Strng.replace('ന‍്', 'ൻ')

    return Strng

def LimburemoveHistorical(Strng):
    removePairs = [("ᤉ", "ᤈ"), ("ᤊ","ᤏ"), ("ᤚ", "ᤙ"), ("ᤲ", "ᤱ")]

    for x,y in removePairs:
        Strng = Strng.replace(x,y)

    return Strng

def MalayalamPrakrit(Strng):
    ## Replace Anusvara with Anusvara above
    Strng = Strng.replace("ം", "ഀ")
    Strng = InsertGeminationSign(Strng, 'Malayalam')

    return Strng

def GranthaPrakrit(Strng):
    ## Replace Anusvara with Anusvara above
    Strng = Strng.replace("𑌂", "𑌀")
    Strng = InsertGeminationSign(Strng, 'Grantha')

    ## not at the beginning of words
    pat = r'\s𑌂.'
    Strng = functools.reduce(lambda s, m: s.replace(m, ReverseGeminationSign(m, 'Grantha')), re.findall(pat, Strng), Strng)

    pat = r'𑍍𑌂.'
    Strng = functools.reduce(lambda s, m: s.replace(m, ReverseGeminationSign(m, 'Grantha')), re.findall(pat, Strng), Strng)

    return Strng
    ## Insert Gemination Sign

def MeeteiMayekremoveHistorical(Strng):
    removePairs = [('ꫢ', 'ꯆ'), ('ꫣ', 'ꯅ'), ('ꫤ','ꯇ'), ('ꫥ','ꯊ'), ('ꫦ','ꯗ'), ('ꫧ','ꯙ'), ('ꫨ','ꯅ'),
                   ('ꫩ','ꯁ'), ('ꫪ','ꯁ'), ('\uAAF5','ꯍ꯭'), ('ꯑꫫ','ꯏ'), ('ꯑꫬ','ꯎ'), ('ꫫ','ꯤ'), ('ꫬ','ꯨ')]

    for x,y in removePairs:
        Strng = Strng.replace(x,y)

    return Strng

def TamilOmDisable(Strng):
    return Strng.replace("ௐ", "ஓம்")

def TamilSHADisable(Strng):
    return Strng.replace("ஶ", "ஸ²")

def TamilNaToNNa(Strng):
    na = Tamil.ConsonantMap[19]
    nna = Tamil.SouthConsonantMap[3]
    vir = Tamil.ViramaMap[0]
    ta = Tamil.ConsonantMap[15]

    ListV = '|'.join(GM.CrunchSymbols(GM.Vowels+GM.VowelSigns+GM.Consonants,'Tamil')+[Tamil.SignMap[0].replace('(','\(').replace(')','\)')])

    Strng = re.sub('('+ListV+')'+ GM.VedicSvaras + '('+na+')' + '(?!' + vir + ta + ')',r'\1\2'+nna,Strng)
    Strng = re.sub('('+ListV+')'+ GM.VedicSvaras + '('+na+')' + '(?!' + vir + ta + ')',r'\1\2'+nna,Strng)

    Strng = re.sub('(²|³|⁴)'+ GM.VedicSvaras + '('+na+')' + '(?!' + vir + ta + ')',r'\1\2'+nna,Strng)
    Strng = re.sub('(²|³|⁴)'+ GM.VedicSvaras + '('+na+')' + '(?!' + vir + ta + ')',r'\1\2'+nna,Strng)

    #Strng = re.sub('(²|³|⁴)'+'('+na+')',r'\1'+nna,Strng)

    #Strng = re.sub('(\s)(ன)', r'\1' + 'ந', Strng)
    #Strng = re.sub('(\.)(ன)', r'\1' + 'ந', Strng)
    #Strng = re.sub('^ன', 'ந', Strng)

    Strng = re.sub("(?<=ஶ்ரீ)(ன)(?!" + vir + ")", "ந", Strng)

    return Strng

# കൽന് കത്ല് ക്ഷേത്ര് കൻല് - Check this

def MalayalamChillu(Strng, reverse=False, preserve=False):

    Chillus=['\u0D7A','\u0D7B','\u0D7C','\u0D7D','\u0D7E', 'ഩ‍്']

    ListC = '(' + '|'.join(GM.CrunchSymbols(GM.CharactersNV,'Malayalam') + ['ഽ']) + ')'

    vir = Malayalam.ViramaMap[0]
    ConVir =[
             Malayalam.ConsonantMap[14]+vir,
             Malayalam.ConsonantMap[19]+vir,
             Malayalam.ConsonantMap[26]+vir,
             Malayalam.ConsonantMap[27]+vir,
             Malayalam.SouthConsonantMap[0]+vir,
             'ഩ്'
            ]

    ## may be include ha ?
    CList = [
            Malayalam.ConsonantMap[10:15]+Malayalam.ConsonantMap[24:26]+Malayalam.ConsonantMap[28:29],
            Malayalam.ConsonantMap[15:20]+Malayalam.ConsonantMap[24:27]+Malayalam.ConsonantMap[28:29],
            Malayalam.ConsonantMap[25:27],
            Malayalam.ConsonantMap[20:21] + Malayalam.ConsonantMap[24:26] + Malayalam.ConsonantMap[27:29],
            Malayalam.SouthConsonantMap[0:1]+Malayalam.ConsonantMap[25:27],
            Malayalam.ConsonantMap[15:20]+Malayalam.ConsonantMap[24:27]+Malayalam.ConsonantMap[28:29]
            ]

    if not reverse:
        for i in range(len(Chillus)):
            #print '(?<!'+'['+vir+''.join(Chillus)+']'+')'+'('+ConVir[i]+')'+'(?!['+''.join(CList[i])+'])'
            Strng = re.sub(ListC + GM.VedicSvaras + '('+ConVir[i]+')'+'(?!['+''.join(CList[i])+'])',r'\1\2' + Chillus[i],Strng)
            Strng = re.sub(ListC + GM.VedicSvaras + '('+ConVir[i]+')'+'(?=(['+''.join(CList[i])+'])' + vir + r'\4' + ')',r'\1\2' + Chillus[i],Strng)


    else:
        if preserve:
            for x,y in zip(Chillus, ConVir):
                Strng = Strng.replace(x, y +'ˍ') ## Fix the reversal of characters of this
        else:
            for x,y in zip(Chillus, ConVir):
                Strng = Strng.replace(x, y) ## Fix the reversal of characters of this

    return Strng

def RemoveSchwa(Strng,Target):

    vir = GM.CrunchSymbols(GM.VowelSigns,Target)[0]
    ListC = '|'.join(GM.CrunchSymbols(GM.Consonants,Target))
    ListV = '|'.join(GM.CrunchSymbols(GM.Vowels,Target))
    ListVS = '|'.join(GM.CrunchSymbols(GM.VowelSignsNV,Target))
    ListAll = '|'.join(GM.CrunchSymbols(GM.Vowels+GM.VowelSigns+GM.Consonants+GM.CombiningSigns,Target))

    # Fix अपमही अपमाही

    Strng = re.sub('('+ListAll+')'+'('+ListC+')'+'(?!'+ListAll+')',r'\1\2'+vir,Strng)
    Strng = re.sub('('+ListAll+')'+'(?<!'+vir+')'+'('+ListC+')'+'('+ListC+')'+'('+ListVS+')',r'\1\2'+vir+r'\3\4',Strng)

    return Strng

def InsertGeminationSign(Strng,Target): #Fix this

    vir = GM.CrunchSymbols(GM.VowelSigns,Target)[0]
    ConUnAsp = [GM.CrunchList('ConsonantMap', Target)[x] for x in [0,2,5,7,10,12,15,17,20,22,4,9,14,19,24,25,26,27,28,29,30,31,32]]
    ConUnAsp = ConUnAsp + GM.CrunchList('SouthConsonantMap',Target) + GM.CrunchList('NuktaConsonantMap',Target)
    ConAsp   = [GM.CrunchList('ConsonantMap', Target)[x] for x in [1,3,6,8,11,13,16,18,21,23]]
    ConOthrs = [GM.CrunchList('ConsonantMap', Target)[x] for x in [0,2,5,7,10,12,15,17,20,22,4,9,14,19,24]]

    Strng = re.sub('('+'|'.join(ConUnAsp)+')'+'('+vir+')'+r'\1',GM.Gemination[Target]+r'\1',Strng)

    for i in range(len(ConAsp)):
        Strng = re.sub('('+ConUnAsp[i]+')'+'('+vir+')'+'('+ConAsp[i]+')',GM.Gemination[Target]+r'\3',Strng)

    return Strng

def ReverseGeminationSign(Strng,Target): #Fix this

    vir = GM.CrunchSymbols(GM.VowelSigns,Target)[0]
    ConUnAsp = [GM.CrunchList('ConsonantMap', Target)[x] for x in [0,2,5,7,10,12,15,17,20,22,4,9,14,19,24,25,26,27,28,29,30,31,32]]
    ConUnAsp = ConUnAsp + GM.CrunchList('SouthConsonantMap',Target) + GM.CrunchList('NuktaConsonantMap',Target)
    ConAsp   = [GM.CrunchList('ConsonantMap', Target)[x] for x in [1,3,6,8,11,13,16,18,21,23]]
    ConOthrs = [GM.CrunchList('ConsonantMap', Target)[x] for x in [0,2,5,7,10,12,15,17,20,22,4,9,14,19,24]]

    Strng = re.sub('(' + GM.Gemination[Target] + ')' + '('+'|'.join(ConUnAsp)+')', r'\2' + vir + r'\2', Strng)

    for i in range(len(ConAsp)):
        Strng = re.sub('(' + GM.Gemination[Target] + ')' + '(' + ConAsp [i] +')', ConUnAsp[i] + vir + r'\2', Strng)

    return Strng

def GurmukhiTippiBindu(Strng): # Check this Function
    Bindi = Gurmukhi.AyogavahaMap[1];
    Tippi = '\u0A70'
    ListTippi = '|'.join(GM.CrunchSymbols(GM.Consonants, 'Gurmukhi')+[Gurmukhi.VowelMap[x] for x in [0,2,3,4]]
        +[Gurmukhi.VowelSignMap[1]]+[Gurmukhi.VowelSignMap[3]])

    Char = '|'.join(GM.CrunchSymbols(GM.Consonants, 'Gurmukhi') + GM.CrunchSymbols(GM.Vowels, 'Gurmukhi'))

    Strng = re.sub('(' + Gurmukhi.VowelSignMap[4] +')' + Bindi + '(?!'+ Char + ')',  r'\1' + Tippi, Strng)

    # Strng = '(' + Gurmukhi.VowelSignMap[4] +')' + Bindi + '(=!'+ Char + ')'

    Strng = re.sub('('+ListTippi+')'+'('+Bindi+')',r'\1'+Tippi, Strng)

    return Strng

def GurmukhiTippiGemination(Strng):
    n = Gurmukhi.ConsonantMap[19]
    m = Gurmukhi.ConsonantMap[24]
    vir = Gurmukhi.ViramaMap[0]
    Addak = 'ੱ'
    Tippi = '\u0A70'

    #print(Strng)

    Strng = Strng.replace(Addak + m , Tippi + m)
    Strng = Strng.replace(Addak + n, Tippi + n)

    #print(Strng)

    return Strng

def KhandaTa(Strng,Target, reverse=False): #Check for Bhakt - Khanda Ta not formed

    ta = GM.CrunchSymbols(GM.Consonants, Target)[15]
    khandata = '\u09CE'
    vir = GM.CrunchSymbols(GM.VowelSigns,Target)[0]
    ListC = '|'.join([GM.CrunchList('ConsonantMap', Target)[x] for x in [15,16,19,22,27,24,25,26]] + ['ৰ'])
    #print ListC
    if not reverse:
        Strng = re.sub('(?<!' + vir + ')' + '('+ta+')'+'('+vir+')'+'(?!'+ListC+')',khandata, Strng)
    else:
        Strng = Strng.replace(khandata, ta + vir)

    return Strng

def NasalToAnusvara(Strng,Target):

    ListN = [GM.CrunchSymbols(GM.Consonants, Target)[x] for x in [4,9,14,19,24]]
    ListC = [
             '|'.join(GM.CrunchList('ConsonantMap', Target)[0:4]),
             '|'.join(GM.CrunchList('ConsonantMap', Target)[5:9]),
             '|'.join(GM.CrunchList('ConsonantMap', Target)[10:14]),
             '|'.join(GM.CrunchList('ConsonantMap', Target)[15:19]),
             '|'.join(GM.CrunchList('ConsonantMap', Target)[20:24]),
            ]
    ListCAll = '(' + '|'.join(GM.CrunchSymbols(GM.Characters, Target)) + ')'

    vir = GM.CrunchSymbols(GM.VowelSigns,Target)[0]
    Anu = GM.CrunchSymbols(GM.CombiningSigns,Target)[1]

    for i in range(len(ListN)):
        #print '('+ListN[i]+')'+'('+vir+')'+'('+ListC[i]+')'
        Strng = re.sub(ListCAll + GM.VedicSvaras + '(?<!' + vir + ')' + '('+ListN[i]+')' +'('+vir+')'+'('+ListC[i]+')',r'\1\2'+Anu+r'\5',Strng)
        Strng = re.sub(ListCAll + GM.VedicSvaras + '(?<!' + vir + ')' + '('+ListN[i]+')' +'('+vir+')'+'('+ListC[i]+')',r'\1\2'+Anu+r'\5',Strng)

    for svara in GM.VedicSvarasList:
        Strng = Strng.replace(svara + Anu, Anu + svara)

    return Strng

def AnusvaraToNasal(Strng,Target):

    ListN = [GM.CrunchSymbols(GM.Consonants, Target)[x] for x in [4,9,14,19,24]]
    ListC = [
             '|'.join(GM.CrunchList('ConsonantMap', Target)[0:4]),
             '|'.join(GM.CrunchList('ConsonantMap', Target)[5:9]),
             '|'.join(GM.CrunchList('ConsonantMap', Target)[10:14]),
             '|'.join(GM.CrunchList('ConsonantMap', Target)[15:19]),
             '|'.join(GM.CrunchList('ConsonantMap', Target)[20:24]),
            ]
    vir = GM.CrunchSymbols(GM.VowelSigns,Target)[0]
    Anu = GM.CrunchSymbols(GM.CombiningSigns,Target)[1]

    for i in range(len(ListN)):
        Strng = re.sub('('+Anu+')'+ GM.VedicSvaras + '('+ListC[i]+')',ListN[i]+vir+r'\2\3',Strng)

        if Target == "Tamil":
            Strng = re.sub('(ம்)'+ GM.VedicSvaras + '(ʼ)' + '('+ListC[i]+')',ListN[i]+vir+r'\2\4',Strng)

    return Strng

def MalayalamAnusvaraNasal(Strng):

    ListNNasal = [Malayalam.ConsonantMap[x] for x in [4,9,14,19,24]]
    ListCNasal = [
             '|'.join(Malayalam.ConsonantMap[0:1]),
             '|'.join(Malayalam.ConsonantMap[5:8]),
             '|'.join(Malayalam.ConsonantMap[10:14]),
             '|'.join(Malayalam.ConsonantMap[15:19]),
             '|'.join(Malayalam.ConsonantMap[20:21]),
            ]

    ListNAnu = [Malayalam.ConsonantMap[x] for x in [4,24]]
    ListCAnu = [
             '|'.join(Malayalam.ConsonantMap[1:4]),
             '|'.join(Malayalam.ConsonantMap[21:24]),
            ]

    vir = Malayalam.ViramaMap[0]
    Anu = Malayalam.AyogavahaMap[1]

    Chillus=['\u0D7A','\u0D7B','\u0D7C','\u0D7D','\u0D7E', 'ഩ‍്']

    for i in range(len(ListNNasal)):
        Strng = re.sub('('+Anu+')'+'('+ListCNasal[i]+')',ListNNasal[i]+vir+r'\2',Strng)

    for i in range(len(ListNAnu)):
        Strng = re.sub('(?<![' + ".".join(Chillus) + '])' + '('+ListNAnu[i]+')'+'('+vir+')'+'('+ListCAnu[i]+')',Anu+r'\3',Strng)

    return Strng

## Check Namna, ramya -> Malayalam; fix
def MToAnusvara(Strng,Target):

    M = GM.CrunchList('ConsonantMap', Target)[24] + GM.CrunchList('ViramaMap',Target)[0]
    vir = GM.CrunchList('ViramaMap',Target)[0]
    Anusvara = GM.CrunchList('AyogavahaMap',Target)[1]
    ListC = '|'.join(GM.CrunchSymbols(GM.Characters, Target))

    Chillus= '|'.join([vir, '\u0D7A','\u0D7B','\u0D7C','\u0D7D','\u0D7E'])

    ListCAll = '(' + '|'.join(GM.CrunchSymbols(GM.Characters, Target)) + ')'

    Strng = re.sub(ListCAll + GM.VedicSvaras + '(?<!' + vir + ')'+'('+M+')'+'(?!'+ListC+')',r'\1\2'+Anusvara,Strng)

    for svara in GM.VedicSvarasList:
        Strng = Strng.replace(svara + Anusvara, Anusvara + svara)

    #Strng = Strng.replace(M,Anusvara)

    return Strng

def OriyaYYA(Strng):
    return YYAEverywhere(Strng, 'Oriya')

def BengaliYYA(Strng):
    return YYAEverywhere(Strng, 'Bengali')

def YYAEverywhere(Strng, Target):
    Ya = GM.CrunchList('ConsonantMap', Target)[25]
    YYa = GM.CrunchList('NuktaConsonantMap',Target)[7]

    Strng = Strng.replace(Ya, YYa)

    return Strng

def YaToYYa(Strng,Target):
    YYa = GM.CrunchList('NuktaConsonantMap',Target)[7]

    ListC = '|'.join(GM.CrunchSymbols(GM.Characters, Target)+[GM.CrunchList('SignMap',Target)[0]] + ['ৰ'])

    ListS = '(' + '|'.join(GM.CrunchSymbols(GM.VowelSignsNV,Target)) + ')'

    Ya = GM.CrunchList('ConsonantMap', Target)[25]
    vir = GM.CrunchSymbols(GM.VowelSigns,Target)[0]

    ListVarga = '|'.join(GM.CrunchList('ConsonantMap',Target)[0:25])

    if Target in ['Assamese','Bengali', 'Oriya', "Chakma"]:
        Strng = re.sub('('+ListC+')'+ GM.VedicSvaras + Ya,r'\1\2'+YYa,Strng)

        if Target in ['Assamese', 'Bengali']:
            Strng = Strng.replace(vir+YYa,vir+Ya)

        if Target == "Chakma":
            Strng = Strng.replace("𑄠𑄡", "𑄠𑄠")
            Strng = Strng.replace(vir + YYa, "\U00011133" + YYa)

    #print(Target)
    '''
    if Target == 'Oriya':
        #print('I am here for you')
        Strng = re.sub('('+ListVarga+')'+ Ya+'('+ListC+')',r'\1'+YYa+r'\2',Strng)
        Strng = re.sub('('+ListVarga+')'+ ListS + Ya+'('+ListC+')',r'\1'+ r'\2' + YYa+r'\3',Strng)
        Strng = re.sub(Ya + '(?!' + ListC + ')', YYa, Strng)

        Strng = Strng.replace(vir+Ya,vir+YYa)
    '''

    return Strng

#def TamilTranscribe(Strng,Target):
#
#    CM = GM.CrunchList('ConsonantMap',Target)
#    SM = GM.CrunchList('SouthConsonantMap',Target)
#    vir = GM.CrunchSymbols(GM.VowelSigns,Target)[0]
#
#    ConUnVoiced = [CM[x] for x in [0,5,10,15,20]]
#    ConVoicedJ =  [CM[x] for x in [2,7,12,17,22]]
#    ConVoicedS =  [CM[x] for x in [2,31,12,17,22]]
#    ConNasals = '|'.join([CM[x] for x in [4,9,14,19,24]])
#    ConMedials = '|'.join(CM[25:28]+SM[0:2]+SM[3:4])
#    Vowels = '|'.join(GM.CrunchSymbols(GM.Vowels+GM.VowelSignsNV, Target))
#    Aytham = GM.CrunchList('Aytham',Target)[0]
#    Consonants = '|'.join(GM.CrunchSymbols(GM.Consonants,Target))
#    NRA =SM[3] + vir + SM[2]
#    NDRA = CM[14] + vir + CM[12] + vir + CM[26]
#
#    ### Check Siva Siva Mails
#    ### Do something about Eyelash ra in Transliterated text
#
#    for i in range(len(ConUnVoiced)):
#        #Strng = re.sub('('+Vowels+Consonants+')'+ConUnVoiced[i]+'('+Vowels+Consonants+')',r'\1'+ConVoicedS[i]+r'\2',Strng)
#        Strng = re.sub('('+Vowels+'|'+Consonants+'|'+Aytham+')'+ConUnVoiced[i]+'(?!'+vir+')',r'\1'+ConVoicedS[i],Strng)
#        Strng = re.sub('('+ConNasals+')'+'('+vir+')'+'( ?)'+ConUnVoiced[i],r'\1\2\3'+ConVoicedJ[i],Strng)
#        Strng = re.sub('('+ConMedials+')'+'('+vir+')'+ConUnVoiced[i]+'(?!'+vir+')',r'\1\2'+ConVoicedS[i],Strng)
#
#    Strng = Strng.replace(NRA,NDRA)
#    Strng = re.sub('(?<!'+'('+CM[5]+'|'+SM[2]+')'+vir+')'+CM[5]+'(?!'+vir+')',CM[31],Strng)
#
#    Strng = Strng.replace(CM[5]+vir+' '+CM[31],CM[5]+vir+' '+CM[5])
#
#    return Strng

def VaToBa(Strng,Target):

    va = GM.CrunchSymbols(GM.Consonants, Target)[28]
    ba = GM.CrunchSymbols(GM.Consonants, Target)[22]

    Strng = Strng.replace(va,ba)

    return Strng

def RetainDandasIndic(Strng, Target, reverse=False):
    Dandas = GM.CrunchList('SignMap', Target)[1:3]

    if not reverse:
        Strng = Strng.replace('..', Dandas[1])
        Strng = Strng.replace('.', Dandas[0])
    else:
        Strng = Strng.replace(Dandas[0], '.')
        Strng = Strng.replace(Dandas[1], '..')

    return Strng

def RetainIndicNumerals(Strng,Target, reverse=False):
    NativeNumerals = GM.CrunchList('NumeralMap', Target)
    ArabicNumerals = GM.CrunchList('NumeralMap', 'ISO')

    if not reverse:
        for x,y in zip(ArabicNumerals, NativeNumerals):
            Strng = re.sub('(?<!h)' + x, y, Strng)
    else:
        for x,y in zip(NativeNumerals, ArabicNumerals):
            Strng = Strng.replace(x, y)

    return Strng

def RetainTeluguDanda(Strng):
    return RetainDandasIndic(Strng, 'Telugu')

def RetainTeluguNumerals(Strng):
    return RetainIndicNumerals(Strng, 'Telugu')

def RetainTamilDanda(Strng):
    return RetainDandasIndic(Strng, 'Tamil')

def RetainTamilNumerals(Strng):
    return RetainIndicNumerals(Strng, 'Tamil')

def RetainKannadaDanda(Strng):
    return RetainDandasIndic(Strng, 'Kannada')

def RetainKannadaNumerals(Strng):
    return RetainIndicNumerals(Strng, 'Kannada')

def RetainMalayalamDanda(Strng):
    return RetainDandasIndic(Strng, 'Malayalam')

def RetainMalayalamNumerals(Strng):
    return RetainIndicNumerals(Strng, 'Malayalam')

def RetainGujaratiDanda(Strng):
    return RetainDandasIndic(Strng, 'Gujarati')

def RetainGurmukhiNumerals(Strng):
    return RetainIndicNumerals(Strng, 'Gurmukhi')

def SundaneseRemoveHistoric(Strng):
    Strng = Strng.replace('᮪ᮻ', 'ᮢᮩ')
    Strng = Strng.replace('᮪ᮼ', 'ᮣᮩ')
    Strng = Strng.replace('ᮻ', 'ᮛᮩ')
    Strng = Strng.replace('ᮼ', 'ᮜᮩ')
    Strng = Strng.replace('\u1BBD','\u1B98')

    return Strng

def OriyaVa(Strng):

    va = Oriya.ConsonantMap[28]
    OriyaVa = '\u0B2C'

    Strng =  re.sub('(?<!୍)' + va, OriyaVa, Strng)

    return Strng

def RemoveDiacritics(Strng):
    for x in GM.DiacriticsRemovable:
        Strng = Strng.replace(x,'')

    return Strng

def RemoveDiacriticsTamil(Strng):
    for x in GM.DiacriticsRemovableTamil:
        Strng = Strng.replace(x,'')

    return Strng

def TamilSubScript(Strng):

    SuperScript = ['\u00B9', '\u00B2', '\u00B3','\u2074']
    SubScript = ['\u2081','\u2082','\u2083','\u2084']

    for x,y in zip(SuperScript,SubScript):
        Strng = Strng.replace(x,y)

    return Strng

def TamilAddFirstVarga(Strng):

    ## Re-order rules correct stuff

    CM = GM.CrunchList('ConsonantMap','Tamil')
    ConUnVoiced = '|'.join([CM[x] for x in [0,5,10,15,20]])
    SuperScript = '|'.join(['\u00B2', '\u00B3','\u2074'])

    Strng = re.sub('('+ConUnVoiced+')'+'(?!'+SuperScript+')',r'\1'+'\u00B9',Strng)

    return Strng

def SaurashtraHaru(Strng):

    ListC = '|'.join([Saurashtra.ConsonantMap[x] for x in [19,24,26,27]])
    vir = Saurashtra.ViramaMap[0]
    ha = Saurashtra.ConsonantMap[32]

    Strng = re.sub('('+ListC+')'+vir+ha,r'\1'+'\uA8B4',Strng)

    return Strng

def SinhalaDefaultConjuncts(Strng):
    vir = Sinhala.ViramaMap[0]
    YR = '|'.join(Sinhala.ConsonantMap[25:27])

    Strng = re.sub('('+vir+')'+'('+YR+')',r'\1'+'\u200D'+r'\2',Strng)
    Strng = re.sub('('+YR[2]+')'+'('+vir+')'+'('+'\u200D'+')'+'('+YR[0]+')',r'\1\3\2\3\4',Strng)

    Strng = Strng.replace(Sinhala.ConsonantMap[7]+Sinhala.ViramaMap[0]+Sinhala.ConsonantMap[9],'\u0DA5')
    Strng = Strng.replace(Sinhala.ConsonantMap[0]+vir+Sinhala.ConsonantMap[30],Sinhala.ConsonantMap[0]+vir+'\u200D'+Sinhala.ConsonantMap[30])

    ## KSHA

    Strng = Strng.replace('ර‍්‍ය', 'ර්ය')
    Strng = Strng.replace('ර්‍ර', 'ර්ර')

    return Strng

def IASTPali(Strng):
    Strng = Strng.replace('l̤', 'ḷ')

    return Strng

def CyrillicPali(Strng):
    Strng = Strng.replace('л̤', 'л̣')

    return Strng

def SinhalaConjuncts(Strng):
    ListC = Sinhala.ConsonantMap + [Sinhala.SouthConsonantMap[0]]
    vir = Sinhala.ViramaMap[0]
    ZWJ ="\u200D"

    conjoining =[(0, 28), (2, 18), (9, 5), (10, 11), (15, 16), (15, 28), (17, 18), (17, 28), (19, 16), (19, 17), (19, 18), (19, 28) ]

    for x, y in conjoining:
        Strng = Strng.replace(ListC[x] + vir + ListC[y], ListC[x] + vir + ZWJ + ListC[y])

    for x in ListC:
        Strng = Strng.replace(ListC[26] + vir + x, ListC[26] + vir + ZWJ + x)

    for x in ListC:
        for y in ListC:
            Strng = Strng.replace(x + vir + y, x + ZWJ + vir + y)

    Strng = Strng.replace('ර‍්‍ය', 'ර්‍ය')

    return Strng

def SinhalaPali(Strng, reverse = False):
    EOLong = Sinhala.VowelMap[10:11]+Sinhala.VowelMap[12:13]+Sinhala.VowelSignMap[9:10]+Sinhala.VowelSignMap[11:12]
    EOShort = Sinhala.SouthVowelMap+Sinhala.SouthVowelSignMap

    for x,y in zip(EOLong,EOShort):
        if not reverse:
            Strng = Strng.replace(x,y)
        else:
            Strng = Strng.replace(y,x)

    return Strng

def UrduAlternateUU(Strng):
    Strng = Strng.replace("\\u064F\\u0648","\u0648\u0657")

    return Strng

def TibetanNada(Strng):
    Strng = Strng.replace('\u0F83','\u0F82')

    return Strng

def TibetanTsheg(Strng):
    Strng = Strng.replace('\u0F0B', ' ')

    return Strng

def TibetanRemoveVirama(Strng):
    Strng = Strng.replace(Tibetan.ViramaMap[0],'')

    return Strng

def TibetanRemoveBa(Strng):
    Strng = VaToBa(Strng,'Tibetan')

    Strng = Strng.replace('ཪྺ', 'རྦ')
    Strng = Strng.replace('བྺ', 'བྦ')
    Strng = Strng.replace('ྦྺ', 'ྦྦ')

    return Strng

def ThaiLaoTranscription(Strng,Script,shortA,shortAconj,reverse=False, anusvaraChange=True):
    ## For Native lao: aMDa give an'da as intermediate (N doesn't exist in Native Lao )
    ## Hence issues with nasal conversion

    Strng = Strng.replace("\u02BD","")

    cons = "|".join(GM.CrunchSymbols(GM.Consonants, Script)+GM.CrunchList('VowelMap',Script)[0:1])

    if Script == 'Thai':
        cons = "|".join(GM.CrunchSymbols(GM.Consonants, Script)+GM.CrunchList('VowelMap',Script)[0:1] + ['ฮ', 'บ', 'ฝ', 'ด'])

    if Script == 'Lao':
        cons = "|".join(GM.CrunchSymbols(GM.Consonants, Script) + GM.CrunchList('VowelMap',Script)[0:1] + ['ດ','ບ','ຟ'])

    consnA = cons[:-2]
    listVS = "|".join(GM.CrunchSymbols(GM.VowelSignsNV,Script))
    vir = GM.CrunchList('ViramaMap',Script)[0]
    AIUVir = "".join(GM.CrunchList('VowelSignMap',Script)[0:5]+[vir])
    EAIO = "".join(GM.CrunchList('VowelSignMap',Script)[9:12]+GM.CrunchList('SinhalaVowelSignMap',Script)[:])
    Anu = GM.CrunchList('AyogavahaMap',Script)[1]
    ng = GM.CrunchList('ConsonantMap',Script)[4]

    vowA = GM.CrunchList('VowelMap',Script)[0]

    if anusvaraChange:
        Strng = AnusvaraToNasal(Strng,Script)

    if not reverse:
        if Script == 'Thai':
            Strng = re.sub("(["+EAIO+"])"+"("+cons+")"+"("+vir+")",r'\2\3\1',Strng) #Reverse bre, bro etc
            Strng = Strng.replace("\u0E33","\u0E32\u0E4D").replace("\u0E36","\u0E34\u0E4D") # reverse AM, iM
        if Script == 'LaoPali':
            Strng = Strng.replace('ຳ', 'າໍ')

        if anusvaraChange:
            Strng = Strng.replace(Anu, ng + vir)

        Strng = re.sub("(?<!["+EAIO+"])"+"("+cons+")"+"(?!["+AIUVir+"])",r'\1'+shortA,Strng)
        Strng = re.sub("("+shortA+")"+"(?=("+cons+")"+"("+vir+"))",shortAconj,Strng)
        Strng = Strng.replace(vir, '')

        ## Fix Purevowels

    else:
        consOnly = "|".join(GM.CrunchSymbols(GM.Consonants, Script))
        aVow = GM.CrunchList('VowelMap',Script)[0]

        Strng = re.sub('('+consnA+')'+'(?!'+listVS+'|'+shortA+'|'+shortAconj+')',r'\1'+vir,Strng)

        if Script == "Lao":
            Strng = re.sub('(?<!ໂ)' + '(?<!ແ)'+'(?<!ເ)' + '('+aVow+')' + '(?<!ເ)' + shortA+"|"+shortAconj, r"\1",Strng)
            Strng = re.sub('(' + consOnly + ')' + '(?<!າ|ໂ|ແ|ເ)' + shortA+"|"+shortAconj, r"\1",Strng)

            Strng = Strng.replace("຺ຳ", "ຳ") ## Fixing for Lao

        else:
            Strng = re.sub('(?<!โ)' + '(?<!แ)'+'(?<!เ)' + '('+aVow+')' + '(?<!เ)' + shortA+"|"+shortAconj, r"\1",Strng)
            Strng = re.sub('(' + consOnly + ')' + '(?<!า|โ|แ|เ)' + shortA+"|"+shortAconj, r"\1",Strng)



    return Strng

def LaoTranscription(Strng):
    Strng = CF.LaoPaliTranscribe(Strng)

    Strng = Strng.replace('ະ໌', '໌')

    return Strng

def ThaiVisargaSaraA(Strng):
    Strng = Strng.replace('ห์','ะ')

    return Strng

def ThamTallADisable(Strng):
    Strng = Strng.replace('\u1A64', '\u1A63')

    return Strng

def ThamTallAOthers(Strng):
    TallACons = '|'.join(['ᨧ', 'ᨻ', 'ᩁ', 'ᨽ']) ## ca ba ra bha

    Strng = FixTallA(Strng, TallACons)

    return Strng

def LaoPhonetic(Strng):
    Strng = Strng.replace('ຄ', 'ກ')
    Strng = Strng.replace('ຊ', 'ຈ')
    Strng = Strng.replace('ທ', 'ດ')
    Strng = Strng.replace('ພ', 'ບ')
    Strng = Strng.replace('\u0ECD', 'ງໍ')

    return Strng

def ThamShiftMaiKangLai(Strng):
    Strng = re.sub('(\u1A58)(.)', r'\2\1', Strng)
    ListV = '(' + '|'.join(GM.CrunchSymbols(GM.VowelSigns,'TaiTham') + ['ᩤ']) + ')'

    Strng = re.sub('(\u1A58)([\u1A55\u1A56])', r'\2\1', Strng)
    Strng = re.sub('(\u1A58)(\u1A60.)', r'\2\1', Strng)
    Strng = re.sub('(\u1A58)' + ListV, r'\2\1', Strng)
    Strng = re.sub('(\u1A58)' + ListV, r'\2\1', Strng)

    return Strng

def FixTallA(Strng, TallACons):
    ListC ='|'.join(GM.CrunchSymbols(GM.Consonants,'TaiTham'))
    Sub =['\u1A55','\u1A56'] # Subjoined Forms of /ra/ and /la/

    E = "ᩮ"
    AA = 'ᩣ'

    # Introduce Tall A: ka + AA -> ka + Tall A
    Strng = re.sub('(?<!᩠)('+TallACons+')'+'('+E+'?)'+AA,r'\1\2'+'ᩤ',Strng)

    ## buddho --> Tall A
    Strng = re.sub('('+TallACons+')(᩠)('+ListC +')'+'('+E+'?)'+AA,r'\1\2\3\4'+'ᩤ',Strng)
    Strng = re.sub('('+TallACons+')(᩠)('+ListC +')'+'(᩠)('+ListC +')'+'('+E+'?)'+AA,r'\1\2\3\4\5\6'+'ᩤ',Strng)

    ### Subjoined
    Strng = re.sub('('+TallACons+')' + "(" + "|".join(Sub) + ")" + '('+E+'?)'+AA, r'\1\2\3' + 'ᩤ', Strng)

    ### reverse Tall-A for those with protruding subCons forms
    reverseSub = '([' + ''.join(['ᨥ', 'ᨫ', 'ᨬ', 'ᨰ', 'ᨸ', 'ᩈ', 'ᨿ', 'ᩇ', 'ᨹ']) + '])'
    Strng = re.sub('(\u1A60)'+ reverseSub + '(\u1A6E\u1A64)', r'\1\2' + '\u1A6E\u1A63', Strng) ## vyo (Tall) to vyo (normal)
    Strng = re.sub('(\u1A60)'+ reverseSub + '(\u1A64)', r'\1\2' + '\u1A63', Strng) ## vyA (Tall) to vyA (normal)

    return Strng

def ThaiSajjhayaOrthography(Strng, Script = "Thai"):
    ## reverse digraphs
    Strng = CF.ThaiReverseVowelSigns(Strng, True)
    Strng = CF.ThaiDigraphConjuncts(Strng, True)
    Strng = CF.ThaiReverseVowelSigns(Strng)

    if Script == "Thai":
        Strng = Strng.replace('ฺ', '์')
    if Script == "LaoPali":
        Strng = Strng.replace('຺', '์')

    cons = "|".join(GM.CrunchSymbols(GM.Consonants, Script)+GM.CrunchList('VowelMap',Script)[0:1])
    EAIO = "".join(GM.CrunchList('VowelSignMap',Script)[9:12]+GM.CrunchList('SinhalaVowelSignMap',Script)[:])

    # short a for conjuncts : t(a)ssa
    Strng = re.sub('(?<![' + EAIO + '])' + '(' + cons + ')' + '(' + cons + ')' + '(์)', r'\1' + 'ั' + r'\2\3', Strng)

    if Script == "Thai":
        cons_others  = '([ยรลวศษสหฬ])' # avarga
    if Script == "LaoPali":
        cons_others = '([ຍຣລວຨຩສຫຬ])' # avarga

    Strng = re.sub('(?<![' + EAIO + '])' + '(' + cons + ')' + '(' + cons + ')' + '(์)', r'\1' + 'ั' + r'\2\3', Strng)

    # varga + avaraga or avarga + varga add joiner
    # hma, mha etc.
    Strng = re.sub('(' + cons + ')' + '(์)' + '([' + EAIO + ']?)' + cons_others , r'\1' + '๎' + r'\3\4', Strng)
    Strng = re.sub(cons_others + '(์)' + '([' + EAIO + ']?)' + '(' + cons + ')', r'\1' + '๎' + r'\3\4', Strng)

    ## ssa, lla, nna do no add joiner
    Strng = re.sub(cons_others + '(๎)' + '([' + EAIO + ']?)' + r'\1' , r'\1' + '์' + r'\3\1', Strng)

    #reorder dve sme
    Strng = re.sub('(' + cons  + ')' + '(๎)' + '([' + EAIO + '])' + '(' + cons + ')', r'\3\1\2\4', Strng)

    if Script == "Thai":
        Strng = Strng.replace('ง์', 'ง')
        Strng = re.sub('(\u0E31)(.)(\u0E4E)', r'\2\3', Strng)

    if Script == "LaoPali":
        Strng = Strng.replace('ั', 'ັ')
        Strng = Strng.replace("ງ์", "ງ")
        Strng = Strng.replace("์", "໌")
        Strng = re.sub('(\u0EB1)(.)(\u0E4E)', r'\2\3', Strng)

    #Strng = re.sub('([ยรลวศษสหฬ])(์)', r'\1' + '๎', Strng)

    return Strng


def ThaiTranscription(Strng, anusvaraChange = True):

    ## reverse digraphs
    Strng = CF.ThaiReverseVowelSigns(Strng, True)
    Strng = CF.ThaiDigraphConjuncts(Strng, True)
    Strng = CF.ThaiReverseVowelSigns(Strng)

    Strng = ThaiLaoTranscription(Strng,"Thai", '\u0E30', '\u0E31', anusvaraChange = anusvaraChange)

    Strng = Strng.replace('ะ์','์')

    Strng = Strng.replace('ะงัง', '\u0E31งํ')

#    shortA = u'\u0E30'
#    shortAconj = u'\u0E31'
#    cons = "|".join(GM.CrunchSymbols(GM.Consonants, "Thai")+Thai.VowelMap[0:1])
#    vir = Thai.ViramaMap[0]
#    AIUVir = "".join(Thai.VowelSignMap[0:5]+[vir])
#    EAIO = "".join(Thai.VowelSignMap[9:12])
#    Anu = Thai.AyogavahaMap[1]
#    ng = Thai.ConsonantMap[4]
#
#    Strng = AnusvaraToNasal(Strng,"Thai")
#
#    Strng = re.sub("(["+EAIO+"])"+"("+cons+")"+"("+vir+")",r'\2\3\1',Strng) #Reverse bre, bro etc
#    Strng = Strng.replace(u"\u0E33",u"\u0E32\u0E4D").replace(u"\u0E36",u"\u0E34\u0E4D") # reverse AM, iM
#    Strng = re.sub("(?<!["+EAIO+"])"+"("+cons+")"+"(?!["+AIUVir+"])",r'\1'+shortA,Strng)
#    Strng = Strng.replace(Anu,ng)
#    Strng = Strng.replace(vir,"")
#    Strng = re.sub("("+shortA+")"+"(?=("+cons+")"+"("+cons+"|"+"["+EAIO+"]))",shortAconj,Strng)

    return Strng

def AvestanConventions(Strng):
    # Fix Nasalization, hma etc

    extraCons = ["\U00010B33","\U00010B32","\U00010B1D","\U00010B12", '𐬣', '𐬝']
    ListC = "|".join(GM.CrunchSymbols(GM.Consonants, "Avestan")+extraCons)
    ListV = "|".join(GM.CrunchSymbols(GM.Vowels,"Avestan"))
    ListA = "|".join(GM.CrunchSymbols(GM.Vowels + GM.Consonants,"Avestan")+extraCons+ ['𐬄','𐬅'])


    ii = Avestan.VowelMap[2] * 2
    uu = Avestan.VowelMap[4] * 2
    i = Avestan.VowelMap[2]
    a = Avestan.VowelMap[0]

    kha = Avestan.ConsonantMap[1]
    nga = Avestan.ConsonantMap[4]
    ya = Avestan.ConsonantMap[25]
    va = Avestan.ConsonantMap[28]
    ta = Avestan.ConsonantMap[15]
    tha = Avestan.ConsonantMap[16]
    dha = Avestan.ConsonantMap[18]
    na = Avestan.ConsonantMap[19]
    ma = Avestan.ConsonantMap[24]
    kb = "|".join([Avestan.ConsonantMap[0], Avestan.ConsonantMap[22]])
    nna = Avestan.ConsonantMap[14]
    sha = Avestan.ConsonantMap[29]

    VelarDental = "|".join(Avestan.ConsonantMap[0:4]+Avestan.ConsonantMap[15:19])

    Strng = Strng.replace(nga+i, '𐬣'+ i)

    ## Conventions from AVestan Combined Grammer

    Strng = re.sub(a + '([' + na + ma + '])' + '(?!' +  ListA + ')', '𐬆' + r'\1' , Strng) ## Soft -Ta end of words

    Strng = re.sub("("+na+")"+"("+VelarDental+")",nna+r'\2',Strng) ##

    Strng = re.sub("("+kha+")"+"(?="+ii+")","\U00010B12",Strng)
    Strng = re.sub("("+sha+")"+"(?="+ii+")","\U00010B33",Strng)

    Strng = re.sub("("+tha+"|"+dha+")"+"("+uu+")",r'\1'"𐬡",Strng)

    Strng = re.sub("("+ta+")"+"(?!"+"(("+ListV+")"+"|"+"("+ListC+"))"+")","\U00010B1D",Strng)
    Strng = re.sub("("+ta+")"+"(?="+"("+kb+")"+")",'\U00010B1D',Strng)

    return Strng

def TaiThamO(Strng):
    Strng = Strng.replace("\u1A6E\u1A63","\u1A70")

    return Strng

def TaiThamHighNga(Strng):
    Strng = Strng.replace('\u1A58','\u1A59')

    return Strng

def TaiThamMoveNnga(Strng):
    Strng = re.sub('(.)(\u1A58|\u1A50)',r'\2\1',Strng) # Probably its u1A59

    return Strng

def UrduRemoveShortVowels(Strng):
    ShortVowels = ['\u0652','\u064E','\u0650','\u064F']

    for vow in ShortVowels:
        Strng = Strng.replace(vow,"")

    return Strng

def LatinPipes(Strng):
    ###

    return Strng

def PhagsPaRearrange(Strng,Target):
    vir = GM.CrunchList('ViramaMap', Target)[0]
    ListC = '|'.join(GM.CrunchSymbols(GM.Consonants,Target))
    ListV = '|'.join(GM.CrunchSymbols(GM.Vowels,Target))
    ListVS = '|'.join(GM.CrunchSymbols(GM.VowelSignsNV,Target))

    Strng = re.sub("(?<!( |"+vir+"))"+"("+ListC+")"+"(?= )",r'\2'+vir,Strng)
    #print Strng

    Strng = Strng.replace(" ","").replace("᠂"," ").replace("᠃"," ")
    return Strng

def DevanagariAVowels(Strng):
    oldVowels = Devanagari.VowelMap[2:12]+Devanagari.SouthVowelMap[:1]
    a = Devanagari.VowelMap[0]
    newAVowels = [a+x for x in Devanagari.VowelSignMap[1:11]+Devanagari.SouthVowelSignMap[:1]]

    for x,y in zip(oldVowels,newAVowels):
        Strng = Strng.replace(x,y)

    return Strng

def AnusvaraToNasalIPA(Strng):

    Strng = Strng.replace("̃k","ŋk")
    Strng = Strng.replace("̃g","ŋg")

    Strng = Strng.replace("̃c","ɲc")
    Strng = Strng.replace("̃j","ɲj")

    Strng = Strng.replace("̃t̪","n̪t̪")
    Strng = Strng.replace("̃d̪","n̪d̪")

    Strng = Strng.replace("̃ɖ","ɳɖ")
    Strng = Strng.replace("̃ʈ","ɳʈ")

    Strng = Strng.replace("̃ːk","ːŋk")
    Strng = Strng.replace("̃ːg","ːŋg")

    Strng = Strng.replace("̃ːc","ːɲc")
    Strng = Strng.replace("̃ːj","ːɲj")

    Strng = Strng.replace("̃ːt̪","ːn̪t̪")
    Strng = Strng.replace("̃ːd̪","ːn̪d̪")

    Strng = Strng.replace("̃ːɖ","ːɳɖ")
    Strng = Strng.replace("̃ːʈ","ːɳʈ")

    return Strng

def IPARemoveCross(Strng):

    Strng = Strng.replace('×','')

    return Strng

def ChakmaAVowels(Strng):

    return Strng

def ZanabazarSquareContextual(Strng):
    yrlv = ZanabazarSquare.ConsonantMap[25:29]
    yrlv_sub = ['\U00011A3B', '\U00011A3C', '\U00011A3D', '\U00011A3E']

    for x, y in zip(yrlv, yrlv_sub):
        Strng = Strng.replace('\U00011A47' + x, y)
    # Repha
    Strng = re.sub('(?<!\U00011A47)' + yrlv[1] + '\U00011A47', '\U00011A3A', Strng)

    return Strng

def ZanabazarSquareAiAu(Strng):
    Strng = Strng.replace('\U00011A04\U00011A0A', '\U00011A07')
    Strng = Strng.replace('\U00011A06\U00011A0A', '\U00011A08')

    return Strng

def ZanabazarSquareMongolianFinal(Strng):
    Strng = Strng.replace(ZanabazarSquare.ViramaMap[0], '\U00011A33')

    return Strng

def TamilRemoveApostrophe(Strng):
    Strng = Strng.replace('ʼ', '')

    return Strng

def TamilRemoveNumbers(Strng):
    numerals = ['²', '³', '⁴', '₂', '₃', '₄']

    for num in numerals:
        Strng = Strng.replace(num, '')

    return Strng

def NewaSpecialTa(Strng):

    Strng = Strng.replace('𑐟𑑂', '𑐟𑑂‍') #Ta+virama -> ta + virama + ZWJ

    return Strng

def TamilDisableSHA(Strng):
    Strng = Strng.replace('ஶ', 'ஷ²')
    Strng = CF.ShiftDiacritics(Strng,'Tamil')

    return Strng

def swapEe(Strng):
    Strng = Strng.replace('e', 'X@X@')
    Strng = Strng.replace('e', 'E')
    Strng = Strng.replace('X@X@')

    return Strng

def capitalizeSentence(Strng):
    Strng = re.sub(r"(\A\w)|"+            # start of string
             "(?<!\.\w)([\.?!]\s*)\w|"+     # after a ?/!/. and a space,
             "\w(?:\.\w)|"+
             "(\n)\w|"+               # start/middle of acronym
             "(\n(\"|\“|\'|\‘))\w|"+
             "(?<=\w\.)\w",               # end of acronym
             lambda x: x.group().upper(),
             Strng)

    Strng = re.sub(r"(@)(.)", lambda x: x.groups()[1].upper(), Strng)

    return Strng

def NewaDisableRepha(Strng):
    Strng = Strng.replace('𑐬𑑂', '𑐬𑑂\u200D')

    return Strng