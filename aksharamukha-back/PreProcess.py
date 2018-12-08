# -*- coding: utf-8 -*-

import GeneralMap as GM
import re
import string
import PostProcess
from ScriptMap.EastIndic import PhagsPa
from ScriptMap.MainIndic import Tamil, Malayalam, Limbu
### Use escape char in all functions

def UrduShortNotShown(Strng):
    Strng += "\u02BB\u02BB"

    return Strng

def egrantamil(Strng):
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
    Nas = "([ंःँ]?)"
    ISyl = "((" + VowI + "|" + "(" + Cons + VowS + "?" + ")" + Nas + '))'
    Syl = "((" + Cons + VowS + ')' + Nas + ")"
    SylAny = "((" + Cons + VowS + "?" + ')' + Nas + ")"

    vir = GM.CrunchList("ViramaMap", Target)[0]
    Cons2 = '((' + Cons + vir + ')?' + Cons + ')'

    Strng = re.sub(ISyl+Cons2+"(?!" + Char + ")", r'\1\8' + vir, Strng) # kama -> kam
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
        AltForm = ['aa','ii','uu','RRi','RRI','LLi','LLI','N^','JN','chh','shh','x','GY','.n','.m','.h','AUM']
        NormForm = ['A','I','U','R^i','R^I','L^i','L^I','~N','~n','Ch','Sh','kSh','j~n','M','M','','OM']

        for x,y in zip(AltForm,NormForm):
            Strng = Strng.replace(x,y)

    ## Normalize Input Strings

    Strng = normalize(Strng,Source)

    ## Remove unsupported letters and replace with supported ones

    return Strng

def UnSupThaana(Strng):

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

    ## Remove Joiners

    Strng = Strng.replace("\u200D", "")
    Strng = Strng.replace("\u200C", "")

    ## Decomposed Limbu to precomposed

    Strng = Strng.replace("ᤠ᤺ᤣ", "ᤠᤣ᤺")
    Strng = Strng.replace("᤺ᤣ", "ᤣ᤺")
    Strng = Strng.replace("ᤠᤣ", "ᤥ")

    ## Replace Thai ฎ

    Strng = Strng.replace("ฎ", "ฏ")

    ## Replace


    #Strng = Strng.replace('', "ຣ\uE00A")

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

    ConNasalsSpace = '|'.join([ListC[x] for x in [4,9,19]])
    ConNasals = '|'.join([ListC[x] for x in [14,24]])

    ConMedials = '|'.join(ListC[25:28]+ListSC[0:2]+ListSC[3:4])
    Vowels = '|'.join(GM.CrunchSymbols(GM.Vowels+GM.VowelSignsNV, "Tamil"))
    Aytham = GM.CrunchList('Aytham',"Tamil")[0]
    Consonants = '|'.join(GM.CrunchSymbols(GM.Consonants,"Tamil"))
    NRA =ListSC[3] + vir + ListSC[2]
    NDRA = ListC[14] + vir + ListC[12] + vir + ListC[26]

    ### Check Siva Siva Mails
    ### Do something about Eyelash ra in Transliterated text

    for i in range(len(ConUnVoiced)):
        #Strng = re.sub('('+Vowels+Consonants+')'+ConUnVoiced[i]+'('+Vowels+Consonants+')',r'\1'+ConVoicedS[i]+r'\2',Strng)
        Strng = re.sub('('+Vowels+'|'+Consonants+'|'+Aytham+')'+ConUnVoiced[i]+'(?!'+vir+')',r'\1'+ConVoicedS[i],Strng)

        # Nasals + Unvoiced -> voiced
        # Rule applied even if spaced -> ulakaJ cuRRu -> ulakaJ juRRu; cenJu -> senju
        Strng = re.sub('('+ConNasalsSpace+')'+'('+vir+')'+'( ?)'+ConUnVoiced[i],r'\1\2\3'+ConVoicedJ[i],Strng)
        # Only without space : vampu -> vambu;  varim panam -> varim panam
        Strng = re.sub('('+ConNasals+')'+'('+vir+')'+ConUnVoiced[i],r'\1\2'+ConVoicedJ[i],Strng)

        # Medials + Unvoiced -> Voiced
        Strng = re.sub('('+ConMedials+')'+'('+vir+')'+ConUnVoiced[i]+'(?!'+vir+')',r'\1\2'+ConVoicedS[i],Strng)

    Strng = Strng.replace(NRA,NDRA)
    # Intervocalic S
    Strng = re.sub('(?<!'+'('+ListC[5]+'|'+ListSC[2]+')'+vir+')'+ListC[5]+'(?!'+vir+')',ListC[31],Strng)

    import string
    punct = "|".join(['\\'+x for x in list(string.punctuation.replace(".","").replace("?",""))])+"|\s"

    # CA + Spac | Punct + SA -> CCA
    Strng = re.sub('('+ListC[5]+vir+')'+'(('+punct+')+)'+'('+ListC[31]+')',r'\1\2'+ListC[5],Strng)

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
    Strng = Strng.replace(ListSC[2],ListC[26])

    return Strng

def IPAIndic(Strng):
    Strng = Strng.replace("ʊ","u")
    Strng = Strng.replace("ɛ","e")

    return
