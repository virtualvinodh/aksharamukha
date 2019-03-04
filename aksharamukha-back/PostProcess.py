# -*- coding: utf-8 -*-

import GeneralMap as GM
from ScriptMap.Roman import Avestan
from ScriptMap.MainIndic import Tamil,Malayalam,Gurmukhi,Oriya,Saurashtra,Sinhala,Urdu,Devanagari, Chakma, Limbu
from ScriptMap.EastIndic import Tibetan, Thai, PhagsPa, ZanabazarSquare
import ConvertFix as CF
import re

### Write Lotsssss of Comments
### Rewrite all ListC, ListV as sorted(List,key=len,reverse=True). Then Correctrulu may be unnecessary

### Consider Adding Options to ignore Nukta etc for Gujarati bengali by default

def default(Strng):

    return Strng

def ranjanalantsa(Strng):
    Strng = Strng.replace('་', ' ')
    return Strng

def ranjanawartu(Strng):
    Strng = Strng.replace('་', '࿎ ')
    return Strng

def egrantamil(Strng):
    return Strng

def nepaldevafont(Strng):
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

def ChakmaEnableAllConjuncts(Strng):
    listC = '('+"|".join(sorted(GM.CrunchSymbols(GM.Consonants,"Chakma")+Chakma.VowelMap[:1],key=len,reverse=True))+')'
    Strng = re.sub("\U00011134"+'('+listC+')',"\U00011133"+r'\1',Strng)

    Strng = ChakmaGemination(Strng)

    return Strng

def ChakmaGemination(Strng, reverse = False):
    ListC = "(" + "|".join(GM.CrunchSymbols(GM.Consonants, 'Chakma')) + ")"
    virs = "([\U00011134 \U00011133])"
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
        Strng = Strng.replace('ौ','ॎाे')
    else:
        Strng = Strng.replace('ॎे', 'ै')
        Strng = Strng.replace('ॎाे', 'ौ')
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

    Strng = re.sub('('+ListV+')'+'('+na+')',r'\1'+nna,Strng)
    Strng = re.sub('(²|³|⁴)'+'('+na+')',r'\1'+nna,Strng)
    Strng = Strng.replace(nna+vir+ta,na+vir+ta)

    return Strng

# കൽന് കത്ല് ക്ഷേത്ര് കൻല് - Check this

def MalayalamChillu(Strng, reverse=False):

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
            Malayalam.ConsonantMap[10:15]+Malayalam.ConsonantMap[25:27]+Malayalam.ConsonantMap[28:29],
            Malayalam.ConsonantMap[15:20]+Malayalam.ConsonantMap[24:27]+Malayalam.ConsonantMap[28:29],
            Malayalam.ConsonantMap[25:27],
            Malayalam.ConsonantMap[25:28],
            Malayalam.SouthConsonantMap[0:1]+Malayalam.ConsonantMap[25:27],
            Malayalam.ConsonantMap[15:20]+Malayalam.ConsonantMap[24:27]+Malayalam.ConsonantMap[28:29]
            ]

    if not reverse:
        for i in range(len(Chillus)):
            #print '(?<!'+'['+vir+''.join(Chillus)+']'+')'+'('+ConVir[i]+')'+'(?!['+''.join(CList[i])+'])'
            Strng = re.sub(ListC + '('+ConVir[i]+')'+'(?!['+''.join(CList[i])+'])',r'\1' + Chillus[i],Strng)
    else:
        for x,y in zip(Chillus, ConVir):
            Strng = Strng.replace(x, y +'ˍ') ## Fix the reversal of characters of this

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
        Strng = re.sub(ListCAll + '(?<!' + vir + ')' + '('+ListN[i]+')'+'('+vir+')'+'('+ListC[i]+')',r'\1'+Anu+r'\4',Strng)

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
        Strng = re.sub('('+Anu+')'+'('+ListC[i]+')',ListN[i]+vir+r'\2',Strng)

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

    Strng = re.sub(ListCAll + '(?<!' + vir + ')'+'('+M+')'+'(?!'+ListC+')',r'\1'+Anusvara,Strng)

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
        Strng = re.sub('('+ListC+')'+Ya,r'\1'+YYa,Strng)

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
    print(ListC)
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

def ThaiLaoTranscription(Strng,Script,shortA,shortAconj,reverse=False):
    ## For Native lao: aMDa give an'da as intermediate (N doesn't exist in Native Lao )
    ## Hence issues with nasal conversion

    Strng = Strng.replace("\u02BD","")

    cons = "|".join(GM.CrunchSymbols(GM.Consonants, Script)+GM.CrunchList('VowelMap',Script)[0:1])

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

    Strng = AnusvaraToNasal(Strng,Script)

    if not reverse:
        if Script == Thai:
            Strng = re.sub("(["+EAIO+"])"+"("+cons+")"+"("+vir+")",r'\2\3\1',Strng) #Reverse bre, bro etc
            Strng = Strng.replace("\u0E33","\u0E32\u0E4D").replace("\u0E36","\u0E34\u0E4D") # reverse AM, iM

        Strng = re.sub("(?<!["+EAIO+"])"+"("+cons+")"+"(?!["+AIUVir+"])",r'\1'+shortA,Strng)
        Strng = Strng.replace(Anu,ng)
        Strng = Strng.replace(vir,"")
        Strng = re.sub("("+shortA+")"+"(?=("+cons+")"+"("+cons+"|"+"["+EAIO+"]))",shortAconj,Strng)
        Strng = re.sub("("+shortA+")"+"(?="+ng+")(?!["+AIUVir+"])",shortAconj,Strng)

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

def ThaiTranscription(Strng):

    ## reverse digraphs
    Strng = CF.ThaiReverseVowelSigns(Strng, True)
    Strng = CF.ThaiDigraphConjuncts(Strng, True)
    Strng = CF.ThaiReverseVowelSigns(Strng)

    Strng = ThaiLaoTranscription(Strng,"Thai", '\u0E30', '\u0E31')

    Strng = Strng.replace('ะ์','์')
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

    print('here')

    for num in numerals:
        print(num)
        Strng = Strng.replace(num, '')

    return Strng

def TamilDisableSHA(Strng):
    Strng = Strng.replace('ஶ', 'ஸ²')
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
             "(?<=\w\.)\w",               # end of acronym
             lambda x: x.group().upper(),
             Strng)

    return Strng

def NewaDisableRepha(Strng):
    Strng = Strng.replace('𑐬𑑂\u200D','𑐬𑑂')

    return Strng