# -*- coding: utf-8 -*-

from . import GeneralMap as GM
import re
import string
from . import PostProcess
from . import ConvertFix as CF
from aksharamukha.ScriptMap.EastIndic import PhagsPa
from aksharamukha.ScriptMap.MainIndic import Tamil, Malayalam, Limbu, Chakma
### Use escape char in all functions

def ShowChillus(Strng):

    return PostProcess.MalayalamChillu(Strng, True, True)

def SanskritLexicaizeHK(Strng):

    return Strng

def ThaiPhonetic(Strng):
    Strng = Strng.replace('ด', 'ท')
    Strng = Strng.replace('บ', 'พ')
    Strng = Strng.replace('ก\u0325', 'ค')
    Strng = Strng.replace('จ\u0325', 'ช')
    Strng = Strng.replace('งํ', 'ง')

    Strng = Strng.replace('\u035C', '')

    Strng = Strng.replace('\u0E47', '')

    Strng += "\u02BB\u02BB"

    return Strng

def SaurastraHaaruColonTamil(Strng):
    Strng = Strng.replace('ன', 'ந')

    ListVS = '|'.join(GM.CrunchSymbols(GM.VowelSigns, 'Tamil'))

    Strng = re.sub('(' + ListVS + ')' + '(:)' , r'\2\1', Strng)

    chars = '([நமரல])'

    Strng = re.sub(chars + ':', r'\1' + '\uA8B4', Strng)

    return Strng

def ChakmaPali(Strng):
    Strng = Strng.replace('\U00011147', '𑄤') # Replace Ya
    Strng = Strng.replace('𑄠', '𑄡') # Replace vA

    listC = '('+"|".join(sorted(GM.CrunchSymbols(GM.Consonants,"Chakma")+Chakma.VowelMap[:1],key=len,reverse=True))+')'
    listV = '('+"|".join(sorted(GM.CrunchSymbols(GM.VowelSigns,"Chakma")+Chakma.ViramaMap+['\U00011133'],key=len,reverse=True))+')'

    Strng = Strng.replace("\u02BD","")

    Strng = Strng.replace('\U00011102', '\U00011127')

    # Introduce vowel Sign A ; Chakma - Inharant vowel is AA
    Strng = re.sub("("+listC+")"+"(?!"+listV+")",r'\1''\u02BE',Strng)
    Strng = Strng.replace("\U00011127","")
    Strng = Strng.replace("\u02BE","\U00011127")

    return Strng

def TakriArchaicKha(Strng):

    return Strng.replace('𑚋', '𑚸')

def UrduShortNotShown(Strng):
    Strng += "\u02BB\u02BB"

    return Strng

def AnuChandraEqDeva(Strng):

    return AnuChandraEq(Strng, 'Devanagari')

def AnuChandraEq(Strng, script):
    Chandrabindu = GM.CrunchList('AyogavahaMap', script)[0]
    Anusvara = GM.CrunchList('AyogavahaMap', script)[1]

    Strng = Strng.replace(Chandrabindu, Anusvara)

    return Strng

def TamilNumeralSub(Strng):
    ListC = '(' + '[கசடதபஜஸ]' + ')'
    ListV = '(' + '|'.join(GM.CrunchSymbols(GM.VowelSigns, 'Tamil')) + ')'

    Strng = re.sub(ListC + ListV + '2', r'\1\2' + '²', Strng)
    Strng = re.sub(ListC + ListV + '3', r'\1\2' + '³', Strng)
    Strng = re.sub(ListC + ListV + '4', r'\1\2' + '⁴', Strng)

    Strng = re.sub(ListC + '2', r'\1' + '²', Strng)
    Strng = re.sub(ListC + '3', r'\1' + '³', Strng)
    Strng = re.sub(ListC + '4', r'\1' + '⁴', Strng)

    Strng = Strng.replace('ரு\'', 'ருʼ')
    Strng = Strng.replace('ரு’', 'ருʼ')

    Strng = Strng.replace('ம்\'', 'ம்ʼ')
    Strng = Strng.replace('ம்’', 'ம்ʼ')

    return Strng

def swapEe(Strng):
    Strng = Strng.replace('E', 'X@X@')
    Strng = Strng.replace('e', 'E')
    Strng = Strng.replace('X@X@','e')

    Strng = Strng.replace('O', 'X@X@')
    Strng = Strng.replace('o', 'O')
    Strng = Strng.replace('X@X@','o')

    return Strng

def swapEeItrans(Strng):
    Strng = Strng.replace('^e', 'X@X@')
    Strng = Strng.replace('e', '^e')
    Strng = Strng.replace('X@X@','e')

    Strng = Strng.replace('^o', 'X@X@')
    Strng = Strng.replace('o', '^o')
    Strng = Strng.replace('X@X@','o')

    return Strng

def egrantamil(Strng):
    return Strng

def siddhammukta(Strng):
    return Strng

def TaiKuen(Strng):
    return Strng

def TaiThamLao(Strng):
    return Strng

def ThaiSajjhayaOrthography(Strng):
    Script = "Thai"

    #cons = "|".join(GM.CrunchSymbols(GM.Consonants, Script)+GM.CrunchList('VowelMap',Script)[0:1])
    #EAIO = "".join(GM.CrunchList('VowelSignMap',Script)[9:12]+GM.CrunchList('SinhalaVowelSignMap',Script)[:])
    ## Reorder dve
    #Strng = re.sub('([' + EAIO + '])' + '(' + cons  + ')' + '(๎)' + '(' + cons + ')', r'\2\3\1\4', Strng)

    Strng = Strng.replace('ัง', 'ังฺ')
    Strng = Strng.replace('์', 'ฺ')
    Strng = Strng.replace('๎', 'ฺ')
    Strng = Strng.replace('ั', '')

    return Strng

def ThaiSajjhayawithA(Strng):
    Strng = Strng.replace('ะ', '')
    Strng = ThaiSajjhayaOrthography(Strng)

    return Strng

def LaoSajhayaOrthography(Strng):
    Strng = Strng.replace('ັງ', 'ັງ຺')

    Strng = re.sub('([ເໂໄ])(.๎)([ຍຣລວຨຩສຫຬ])', r'\2\1\3', Strng)

    Strng = Strng.replace('໌', '຺')
    Strng = Strng.replace('๎', '຺')
    Strng = Strng.replace('ັ', '')

    return Strng

def LaoSajhayaOrthographywithA(Strng):
    Strng = Strng.replace('ະ', '')
    Strng = LaoSajhayaOrthography(Strng)

    return Strng

# consider adding an optional NUkta to the post consonantal position
def RemoveSchwaHindi(Strng):
    VowI = "(" + '|'.join(GM.CrunchSymbols(GM.Vowels,'Devanagari')) + ")"
    VowS = "(" + '|'.join(GM.CrunchSymbols(GM.VowelSignsNV, 'Devanagari')) + ")"
    Cons = "(" + '|'.join(GM.CrunchSymbols(GM.Consonants, 'Devanagari')) + ")"
    Char = "(" + '|'.join(GM.CrunchSymbols(GM.Characters, 'Devanagari')) + ")"
    Nas = "([ंःँ]?)"
    ISyl = "((" + VowI + "|" + "(" + Cons + VowS + "?" + "))" + Nas +')'
    Syl = "((" + Cons + VowS + ')' + Nas + ")"
    SylAny = "((" + Cons + VowS + "?" + ')' + Nas + ")"

    vir = '्'

    Cons2 = '((' + Cons + vir + ')?' + Cons + ')'

    Strng = re.sub(ISyl+Cons+Cons+SylAny+"(?!" + Char + ")", r'\1\8' + vir + r'\9\10', Strng) # bhAratIya --> bhArtIy
    Strng = re.sub(ISyl+Cons+Syl+SylAny+"(?!" + Char + ")", r'\1\8' + vir + r'\9\15', Strng) # bhAratIya --> bhArtIy
    Strng = re.sub(ISyl+Cons+Syl+"(?!" + Char + ")", r'\1\8' + vir + r'\9', Strng) # namakIn -> namkIn
    Strng = re.sub(ISyl+Cons2+"(?!" + Char + ")", r'\1\8' + vir, Strng) # kama -> kam
    #Strng = re.sub(VowI + Nas + Cons2+"(?!" + Char + ")", r'\1\2\3' + vir, Strng)

    return Strng

# consider adding an optional NUkta to the post consonantal position
def RemoveFinal(Strng, Target):
    VowI = "(" + '|'.join(GM.CrunchSymbols(GM.Vowels,Target)) + ")"
    VowS = "(" + '|'.join(GM.CrunchSymbols(GM.VowelSignsNV, Target)) + ")"
    Cons = "(" + '|'.join(GM.CrunchSymbols(GM.Consonants, Target)) + ")"
    Char = "(" + '|'.join(GM.CrunchSymbols(GM.Characters, Target)) + ")"

    Nas = "([" + '|'.join(GM.CrunchList('AyogavahaMap',Target)) + "]?)"

    ISyl = "((" + VowI + "|" + "(" + Cons + VowS + "?" + ")" + Nas + '))'
    Syl = "((" + Cons + VowS + ')' + Nas + ")"
    SylAny = "((" + Cons + VowS + "?" + ')' + Nas + ")"

    vir = GM.CrunchList("ViramaMap", Target)[0]
    Cons2 = '((' + Cons + vir + ')?' + Cons + ')'

    Strng = re.sub(ISyl + Cons2+"(?!" + Char + ")", r'\1\8' + vir, Strng) # kama -> kam

    #Strng = re.sub(VowI + Nas + Cons2+"(?!" + Char + ")", r'\1\2\3' + vir, Strng)

    return Strng

def SchwaFinalGurmukhi(Strng):

    Strng = RemoveFinal(Strng, 'Gurmukhi')

    return Strng

def SchwaFinalGujarati(Strng):

    Strng = RemoveFinal(Strng, 'Gujarati')

    return Strng

def SchwaFinalBengali(Strng):

    Strng = RemoveFinal(Strng, 'Bengali')

    return Strng

def SchwaFinalWarangCiti(Strng):
    Target = "WarangCiti"

    VowI = "(" + '|'.join(GM.CrunchSymbols(GM.Vowels,Target)) + ")"
    VowS = "(" + '|'.join(GM.CrunchSymbols(GM.VowelSignsNV, Target)) + ")"
    Cons = "(" + '|'.join(GM.CrunchSymbols(GM.Consonants, Target)) + ")"
    Char = "(" + '|'.join(GM.CrunchSymbols(GM.Characters, Target)) + ")"

    Nas = "([" + '|'.join(GM.CrunchList('AyogavahaMap',Target)) + "]?)"

    ISyl = "((" + VowI + "|" + "(" + Cons + VowS + "?" + ")" + Nas + '))'
    Syl = "((" + Cons + VowS + ')' + Nas + ")"
    SylAny = "((" + Cons + VowS + "?" + ')' + Nas + ")"

    vir = '\u02BB'
    Cons2 = '((' + Cons + vir + ')?' + Cons + ')'

    Strng = re.sub(ISyl+Cons2+"(?!" + Char + ")", r'\1\8' + vir, Strng) # kama -> kam

    return Strng

def siddhamUnicode(Strng):
    return Strng

def ThaiOrthography(Strng):
    Strng += "\u02BB\u02BB"

    return Strng

def LaoTranscription(Strng):
    Strng += "\u02BB\u02BB"

    return Strng

def LimbuDevanagariConvention(Strng):
    Strng = Strng.replace('ए़', 'ऎ')
    Strng = Strng.replace('ओ़', 'ऒ')
    Strng = Strng.replace('े़', 'ॆ')
    Strng = Strng.replace('ो़', 'ॊ')
    Strng = Strng.replace('ः', '꞉')

    return Strng

def LimbuSpellingSaI(Strng): ## Fix this not for all
    vir = Limbu.ViramaMap[0]

    FCons = [x+vir for x in [Limbu.ConsonantMap[x] for x in[0,4,15,19,20,24,26,27]]]
    FinalCons = ['\u1930','\u1931','\u1933','\u1934','\u1935','\u1936','\u1937','\u1938']

    for x, y in zip(FCons, FinalCons):
        Strng = Strng.replace(x, '\u193A' + y)

    return Strng


def removeChillus(Strng):
    Chillus=['\u0D7A','\u0D7B','\u0D7C','\u0D7D','\u0D7E']

    vir = Malayalam.ViramaMap[0]
    ConVir =[
             Malayalam.ConsonantMap[14]+vir,
             Malayalam.ConsonantMap[19]+vir,
             Malayalam.ConsonantMap[26]+vir,
             Malayalam.ConsonantMap[27]+vir,
             Malayalam.SouthConsonantMap[0]+vir,
            ]

    for x,y in zip(Chillus, ConVir):
        Strng = Strng.replace(x, y)

    return Strng

def SinhalaPali(Strng):
    Strng = PostProcess.SinhalaPali(Strng, reverse = True)

    return Strng

def IASTPali(Strng):
    Strng = Strng.replace('ḷ', 'l̤')

    return Strng

def CyrillicPali(Strng):
    Strng = Strng.replace('л̣', 'л̤',)

    return Strng

def MalayalamPrakrit(Strng):
    ## Reverse Gemination
    Strng = PostProcess.ReverseGeminationSign(Strng, 'Malayalam')
    Strng = Strng.replace("ഀ", "ം")

    return Strng

def GranthaPrakrit(Strng):
    ## Reverse Gemination
    Strng = PostProcess.ReverseGeminationSign(Strng, 'Grantha')

    Strng = Strng.replace("𑌀", "𑌂")

    return Strng

def RomanPreFix(Strng,Source):
    DepV = '\u1E7F'
    Asp = '\u02B0'

    Vir = GM.CrunchList("ViramaMap", Source)[0]
    Nuk = GM.CrunchList("NuktaMap", Source)[0]
    VowelA = GM.CrunchSymbols(['VowelMap'],Source)[0]

    ListV = '|'.join(GM.CrunchSymbols(GM.VowelSigns,Source))
    ListC = '|'.join(GM.CrunchSymbols(GM.Consonants,Source))

    Strng = re.sub('('+ListC+')'+'(?!'+ListV+'|'+VowelA+')',r'\1'+DepV+Vir,Strng)

    Strng = re.sub('('+ListC+'|'+Nuk+')'+'('+ListV+')',r'\1'+DepV+r'\2',Strng)
    #print Strng

    Strng = re.sub('(?<='+ListC+')'+'('+VowelA+')',r'',Strng)
    #print Strng

    #Fix Nukta त़् त़्अ त़्ा -->  त़् त़ त़ा
    Strng = Strng.replace(DepV+Vir+Nuk+VowelA,Nuk)
    Strng = re.sub(DepV+Vir+Nuk+'(?=['+DepV+'])',Nuk,Strng)
    Strng = Strng.replace(DepV+Vir+Nuk,Nuk+DepV+Vir)

    #print Strng

    return Strng

def PreProcess(Strng,Source,Target):
    if Source in GM.RomanDiacritic:
        Strng = Strng.lower()

    if Source == 'Itrans':
        sOm = 'OM'
        tOm = 'oM'

        punc =  '(' + '|'.join(["\u005C"+x for x in list(string.punctuation)]+ ['\s']
                    + [x.replace('.', '\.') for x in GM.CrunchSymbols(GM.Signs,Source)[1:3]]) + ')'

        Strng = re.sub(punc + sOm + punc, r'\1' + tOm + r'\2', Strng)
        Strng = re.sub('^' + sOm + punc, tOm + r'\1', Strng)
        Strng = re.sub(punc + sOm + '$', r'\1' + tOm, Strng)
        Strng = re.sub('^' + sOm + '$', tOm, Strng)

        punc = '(\s)'

        Strng = re.sub(punc + sOm + punc, r'\1' + tOm + r'\2', Strng)
        Strng = re.sub('^' + sOm + punc, tOm + r'\1', Strng)
        Strng = re.sub(punc + sOm + '$', r'\1' + tOm, Strng)
        Strng = re.sub('^' + sOm + '$', tOm, Strng)


        AltForm = ['O', 'aa','ii','uu','RRi','RRI','LLi','LLI','N^','JN','chh','shh','x','GY','.n','.m','.h', 'AUM', 'E']
        NormForm = ['^o', 'A','I','U','R^i','R^I','L^i','L^I','~N','~n','Ch','Sh','kSh','j~n','M','M','','oM', '^e']

        for x,y in zip(AltForm,NormForm):
            Strng = Strng.replace(x,y)

        Strng = Strng.replace('OM', 'oM')

    if Source == 'IAST':
        Strng = Strng.replace("aï", "a_i")
        Strng = Strng.replace("aü", "a_u")

    if Source == "ISO":
        Strng = Strng.replace('a:i', 'a_i')
        Strng = Strng.replace('a:u', 'a_u')

    if Source == "ISO" or Source == "IAST" or Source == "Titus" or "RussianCyrillic":
        Strng = CF.VedicSvarasNonDiacritic(Strng)

    if ('↓' in Strng or '↑' in Strng) and Target in GM.IndicScripts :
        Strng = Strng.replace('↓', '॒')
        Strng = Strng.replace('↑↑', '᳚')
        Strng = Strng.replace('↑', '॑')

    if ('↓' in Strng or '↑' in Strng) and Target in GM.LatinScripts :
        Strng = Strng.replace('↓', '\\_')
        Strng = Strng.replace('↑↑', '\\"')
        Strng = Strng.replace('↑', '\\\'')

    if Source == "WarangCiti":
        Strng = Strng.replace('\u200D', '\u00D7')

    ## Normalize Input Strings

    Strng = normalize(Strng,Source)

    ## Remove unsupported letters and replace with supported ones

    return Strng

def UnSupThaana(Strng):

    return Strng

def RemoveJoiners(Strng):
    Strng = Strng.replace("\u200D", "")
    Strng = Strng.replace("\u200C", "")

    return Strng

# Normalize Input
# ka + <nukta> -> qa etc
def normalize(Strng,Source):

    # Replace Decomposed Nukta Characters by pre-composed Nukta consonants

    #nuktaDecom = [u"क़",u"ख़",u"ग़",u"ज़",u"ड़",u"ढ़",u"फ़",u"य़",u"ਲ਼",u"ਸ਼",u"ਖ਼",u"ਗ਼",u"ਜ਼",u"ਫ਼",u"ড়",u"ঢ়",u"য়",u"ଡ଼",u"ଢ଼"]
    #nuktaPrecom = [u"क़",u"ख़",u"ग़",u"ज़",u"ड़",u"ढ़",u"फ़",u"य़",u"ਲ਼",u"ਸ਼",u"ਖ਼",u"ਗ਼",u"ਜ਼",u"ਫ਼",u"ড়",u"ঢ়",u"য়",u"ଡ଼",u"ଢ଼"]

    nuktaDecom = ["\u0915\u093C","\u0916\u093C","\u0917\u093C","\u091C\u093C","\u0921\u093C","\u0922\u093C","\u092B\u093C","\u092F\u093C","\u0A32\u0A3C","\u0A38\u0A3C","\u0A16\u0A3C","\u0A17\u0A3C","\u0A1C\u0A3C","\u0A2B\u0A3C","\u09A1\u09BC","\u09A2\u09BC","\u09AF\u09BC","\u0B21\u0B3C","\u0B22\u0B3C"]
    nuktaPrecom = ["\u0958","\u0959","\u095A","\u095B","\u095C","\u095D","\u095E","\u095F","\u0A33","\u0A36","\u0A59","\u0A5A","\u0A5B","\u0A5E","\u09DC","\u09DD","\u09DF","\u0B5C","\u0B5D"]

    if Source not in ["Grantha","TamilGrantha"]:
        for x,y in zip(nuktaDecom,nuktaPrecom):
            Strng = Strng.replace(x,y)

    # Sindhi C+Anudatta <- Sindhi Underscore characters
    # For easy Transliteration

    # Malayalam Chillu Characters

    chilluZwj=["ണ്‍","ന്‍","ര്‍","ല്‍","ള്‍","ക്‍"]
    chilluAtom=["ൺ","ൻ","ർ","ൽ","ൾ","ൿ"]

    for x,y in zip(chilluZwj,chilluAtom):
        Strng = Strng.replace(x,y)

    Strng = Strng.replace('ൌ', 'ൗ')
    Strng = Strng.replace('ൟ', 'ഈ')
    Strng = Strng.replace('ൎ', 'ര്')

    # Bengali Khanda Ta

    Strng = Strng.replace("ৎ","ত্‍")

    # Tamil

    tamAlt = ["ஸ்ரீ","க்‌ஷ","ர‌ி","ர‌ீ"]
    tamNorm = ["ஶ்ரீ","க்ஷ","ரி","ரீ"]

    # Burmese

    Strng = Strng.replace("ဿ", "သ္သ")

    # Tamil

    Strng.replace("ஸ²", "ஶ")

    ## The following is a reversal of custom options check !!!!

    subNum = ["¹","₁","₂","₃","₄"]
    supNum = ["","","²","³","⁴"]

    for x,y in zip(tamAlt+subNum,tamNorm+supNum):
        Strng = Strng.replace(x,y)

    # Tibetan Vowels

    oldVow = ["ྲྀ","ཷ","ླྀ","ཹ","ཱི","ཱུ","ཀྵ","ྐྵ"]
    newVow= ["ྲྀ","ྲཱྀ","ླྀ","ླཱྀ","ཱི","ཱུ","ཀྵ","ྐྵ"]

    for x,y in zip(oldVow,newVow):
        Strng = Strng.replace(x,y)

    ## Tibetan ca, ja

    Strng = Strng.replace('ཅ', 'ཙ')
    Strng = Strng.replace('ཆ', 'ཚ')

    # Decomposed to Precomposed Roman Characters

    latinDecom= ["ā","ī","ū","ē","ō","ṃ","ṁ","ḥ","ś","ṣ","ṇ","ṛ","ṝ","ḷ","ḹ","ḻ","ṉ","ṟ"]
    latinPrecom = ["ā","ī","ū","ē","ō","ṃ","ṁ","ḥ","ś","ṣ","ṇ","ṛ","ṝ","ḷ","ḹ","ḻ","ṉ","ṟ"]

    for x,y in zip(latinDecom,latinPrecom):
        Strng = Strng.replace(x,y)

    # Thai Decomposed AM to Precomposed AM

    Strng = Strng.replace("ํา","ำ")

    # For Lao

    Strng  = Strng.replace("ໍາ", 'ຳ')

    ## Two Single Danda to Double Danda

    Strng = Strng.replace("।।","॥")

    ## Decomposed Limbu to precomposed

    Strng = Strng.replace("ᤠ᤺ᤣ", "ᤠᤣ᤺")
    Strng = Strng.replace("᤺ᤣ", "ᤣ᤺")
    Strng = Strng.replace("ᤠᤣ", "ᤥ")

    ## Replace Thai ฎ

    Strng = Strng.replace("ฎ", "ฏ")

    ## Replace Grantha old au with new au

    Strng = Strng.replace('𑍌', '𑍗')

    ## Replace Tibetan Chandra with Nada to the normal one

    Strng = Strng.replace('\u0F82', '\u0F83')

    ## Replace Candra A iwht regualr AE

    Strng = Strng.replace('ॲ', 'ऍ')

    #Strng = Strng.replace('', "ຣ\uE00A")

    ## Normalization for Bengali, Tamil, Malayalam and Grantha

    # Bengali o/au

    Strng = Strng.replace('ো', 'ো')
    Strng = Strng.replace('াে', 'ো')

    Strng = Strng.replace('ৌ', 'ৌ')
    Strng = Strng.replace('ৗে', 'ৌ')

    # Tamil o, O, au

    Strng = Strng.replace('ொ', 'ொ')
    Strng = Strng.replace('ாெ', 'ொ')

    Strng = Strng.replace('ோ', 'ோ')
    Strng = Strng.replace('ாே', 'ோ')

    Strng = Strng.replace('ௌ', 'ௌ')
    Strng = Strng.replace('ௗெ', 'ௌ')

    # Malayalam

    Strng = Strng.replace('ൊ', 'ൊ')
    Strng = Strng.replace('ാെ', 'ൊ')

    Strng = Strng.replace('ോ', 'ോ')
    Strng = Strng.replace('ാേ', 'ോ')

    # Grantha

    Strng = Strng.replace('𑍋', '𑍋')
    Strng = Strng.replace('𑌾𑍇', '𑍋')

    return Strng

# Remove ZWJ/ZWNJ characters
def removeZW(Strng):
    Strng = Strng.replace("\u200C").replace("\u200D")

    return Strng

def PhagsPaArrange(Strng,Source):
    if Source in GM.IndicScripts:
        ListC = "|".join(sorted(GM.CrunchSymbols(GM.Consonants, Source),key=len,reverse=True)) #Do this for all
        ListV = "|".join(sorted(GM.CrunchSymbols(GM.Vowels, Source),key=len,reverse=True))
        ListVS = "|".join(sorted(GM.CrunchSymbols(GM.VowelSignsNV, Source),key=len,reverse=True))
        ListCS = "|".join(sorted(GM.CrunchSymbols(GM.CombiningSigns, Source),key=len,reverse=True))

        vir = GM.CrunchSymbols(GM.VowelSigns,Source)[0]

        yrv = "|".join([GM.CrunchSymbols(GM.Consonants, Source)[i] for i in [25,26,28]])

        Strng = re.sub("("+ListC+")"+"("+vir+")"+"("+yrv+")"+"("+"("+ListVS+")?"+"("+ListCS+")?"+")",r' \1\2\3\4',Strng)
        Strng = re.sub("("+ListC+ListV+")"+"("+"("+ListVS+")?"+"("+ListCS+")?"+")"+"("+ListC+")"+"("+vir+")"+"(?!\s)",r"\1\2\5\6 ",Strng)
        Strng = re.sub("("+ListC+ListV+")"+"("+"("+ListVS+")?"+"("+ListCS+")?"+")"+"("+ListC+")"+'(?!'+vir+')',r"\1\2 \5",Strng)
        Strng = re.sub("("+ListC+ListV+")"+"("+"("+ListVS+")?"+"("+ListCS+")?"+")"+"("+ListC+")"+'(?!'+vir+')',r"\1\2 \5",Strng)

    elif Source in GM.LatinScripts:
        pass

    return Strng

def TamilTranscribe(Strng):

    ListC = GM.CrunchList('ConsonantMap',"Tamil")
    ListSC = GM.CrunchList('SouthConsonantMap',"Tamil")
    vir = GM.CrunchSymbols(GM.VowelSigns,"Tamil")[0]

    ConUnVoiced = [ListC[x] for x in [0,5,10,15,20]]
    ConVoicedJ =  [ListC[x] for x in [2,7,12,17,22]]
    ConVoicedS =  [ListC[x] for x in [2,31,12,17,22]]

    ConNasalsAll = '|'.join([ListC[x] for x in [4, 9, 14, 19, 24]])
    conNasalCa = '|'.join([ListC[x] for x in [9]])
    ConNasalsGroup = [ConNasalsAll, conNasalCa, ConNasalsAll, ConNasalsAll, ConNasalsAll]

    ConMedials = '|'.join(ListC[25:28]+ListSC[0:2]+ListSC[3:4])
    Vowels = '|'.join(GM.CrunchSymbols(GM.Vowels+GM.VowelSignsNV, "Tamil"))
    Aytham = GM.CrunchList('Aytham',"Tamil")[0]
    Consonants = '|'.join(GM.CrunchSymbols(GM.Consonants,"Tamil"))
    NRA =ListSC[3] + vir + ListSC[2]
    NDRA = ListC[14] + vir + ListC[12] + vir + ListC[26]

    ### Check Siva Siva Mails
    ### Do something about Eyelash ra in Transliterated text

    for i in range(len(ConUnVoiced)):
        pass
        #Strng = re.sub('('+Vowels+Consonants+')'+ConUnVoiced[i]+'('+Vowels+Consonants+')',r'\1'+ConVoicedS[i]+r'\2',Strng)
        Strng = re.sub('('+Vowels+'|'+Consonants+'|'+Aytham+')'+ConUnVoiced[i]+'(?!'+vir+')',r'\1'+ConVoicedS[i],Strng)

        # Nasals + Unvoiced -> voiced
        # Rule applied even if spaced -> ulakaJ cuRRu -> ulakaJ juRRu; cenJu -> senju
        # Strng = re.sub('('+ConNasalsSpace+')'+'('+vir+')'+'( ?)'+ConUnVoiced[i],r'\1\2\3'+ConVoicedJ[i],Strng)

        # Only without space : vampu -> vambu;  varim panam -> varim panam
        Strng = re.sub('('+ConNasalsGroup[i]+')'+'('+vir+')'+ConUnVoiced[i],r'\1\2'+ConVoicedJ[i],Strng)

        # Medials + Unvoiced -> Voiced
        Strng = re.sub('('+ConMedials+')'+'('+vir+')'+ConUnVoiced[i]+'(?!'+vir+')',r'\1\2'+ConVoicedS[i],Strng)

    Strng = Strng.replace(NRA,NDRA)

    # Intervocalic S
    Strng = re.sub('(?<!'+'('+ListC[5]+'|'+ListSC[2] +'|' + 'ட' + ')'+vir+')'+ListC[5]+'(?!'+vir+')',ListC[31],Strng)

    import string

    punct = "|".join(['\\'+x for x in list(string.punctuation.replace(".","").replace("?",""))])+"|\s"

    # CA + Spac | Punct + SA -> CCA
    Strng = re.sub('('+ListC[5]+vir+')'+'(('+punct+')+)'+'('+ListC[31]+')',r'\1\2'+ListC[5],Strng)

    # JA + Spac | Punct + SA -> JCA
    Strng = re.sub('('+ListC[9]+vir+')'+'(('+punct+')+)'+'('+ListC[31]+')',r'\1\2'+ListC[7],Strng)

    # GA + Spac | Punct + KA ->
    Strng = re.sub('('+ListC[4]+vir+')'+'(('+punct+')+)'+'('+ListC[0]+')',r'\1\2'+ListC[2],Strng)

    # NA + Spac | Punct + TTA ->
    Strng = re.sub('('+ListC[14]+vir+')'+'(('+punct+')+)'+'('+ListC[10]+')',r'\1\2'+ListC[12],Strng)

    # NA + Spac | Punct + TA ->
    Strng = re.sub('('+ListC[19]+vir+')'+'(('+punct+')+)'+'('+ListC[15]+')',r'\1\2'+ListC[17],Strng)

    # K + k -> hh
    Strng = Strng.replace(Tamil.Aytham[0]+ListC[0],ListC[32]+vir+ListC[32])

    # K -> H
    Strng = Strng.replace(Tamil.Aytham[0],ListC[32]+vir)

    # RR + RRA -> TT+RA
    Strng = re.sub(ListSC[2]+vir+ListSC[2],ListC[10]+vir+ListC[26],Strng)

    # RR | TT + /s + SA -> RR + /s + CA
    Strng = re.sub("("+'['+ListC[10]+ListSC[2]+']'+vir+')'+'(\s)'+'('+ListC[31]+')',r'\1\2'+ListC[5],Strng)

    ## NNN to N, RR to R

    Strng = Strng.replace(ListSC[3],ListC[19])
    #Strng = Strng.replace(ListSC[2],ListC[26])

    return Strng

def IPAIndic(Strng):
    Strng = Strng.replace("ʊ","u")
    Strng = Strng.replace("ɛ","e")

    return
