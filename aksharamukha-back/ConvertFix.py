# -*- coding: utf-8 -*-
import GeneralMap as GM
from ScriptMap.Roman import Avestan, IAST
from ScriptMap.MainIndic import Tamil,TamilGrantha, Limbu, MeeteiMayek, Urdu, Lepcha, Chakma, Kannada, Gurmukhi, Newa
from ScriptMap.EastIndic import Lao, TaiTham,Tibetan,Burmese,Khmer,Balinese,Javanese,Thai, Sundanese, PhagsPa, Cham, Thaana, Rejang, ZanabazarSquare
import PostProcess
import re

## Test Syllable initial conjunct

## ListC check.. if LLA is there in ListC... just now it has only Consonant Map
### Rewrite all ListC, ListV as sorted(List,key=len,reverse=True)

def FixRomanOutput(Strng,Target):

    # Input:Devanagari & Output:ISO
    # Input: क् क्अ क का कृ क्ह ब़् ब़ ब़ो भ् भ भा कि कइ कई
    # Output: kʌ× kʌ×a kʌ kʌā kʌr̥ kʌ×hʌ bʌ̄× bʌ̄ bʌ̄ō bhʌ× bhʌ bhʌā kʌi kʌṿi kʌṿī

    Schwa = '\uF000'
    DepV = '\u1E7F'

    # Creating RegEx matches
    #Escape ^,. which appear in ITRANS & Velthuis
    VowelSignList = '|'.join(GM.CrunchSymbols(GM.VowelSigns,Target)).replace('^','\^').replace('.','\.') # OR of all Consonants - k|kh etc
    VowelList = '|'.join(GM.CrunchSymbols(GM.Vowels,Target)).replace('^','\^').replace('.','\.') # OR of all Vowels - a|A etc

    Virama = ''.join(GM.CrunchSymbols(['ViramaMap'],Target))
    Nukta = ''.join(GM.CrunchSymbols(['NuktaMap'],Target))

    VowelA = GM.CrunchSymbols(['VowelMap'],Target)[0] # Vowel Letter 'a'
    VowelIU = '|'.join(GM.CrunchSymbols(['VowelMap'],Target)[2]+GM.CrunchSymbols(['VowelMap'],Target)[4])

    TargetCons = GM.CrunchSymbols(['ConsonantMap'],Target)
    ConsH = TargetCons[32] # Consonant H
    UnAspCons = '|'.join([TargetCons[i] for i in [0,2,5,7,10,12,15,17,20,22]]).replace('^','\^').replace('.','\.') # All Unaspirated Plosives

    # कि कइ - ki -> k_i
    Strng = re.sub('(?<='+Schwa+DepV+')'+'('+VowelIU+')',r'_\1',Strng)
    # Output: kʌ× kʌ×a kʌ kʌā kʌr̥ kʌ×hʌ bʌ̄× bʌ̄ bʌ̄ō bhʌ× bhʌ bhʌā kʌi kʌṿ_i kʌṿī

    # अइ अउ --> a_i a_u
    # print(Strng)
    Strng = re.sub('(?<=ṿ'+VowelA+'ṿ)'+'('+VowelIU+')',r'_\1',Strng)

    # ब्ह -> b_h not bh
    Strng = re.sub('('+UnAspCons+')''('+Schwa+Virama+')('+ConsH+')',r'\1_\3',Strng)
    # Output: kʌ× kʌ×a kʌ kʌā kʌr̥ k_hʌ bʌ̄× bʌ̄ bʌ̄ō bhʌ× bhʌ bhʌā kʌi kʌṿ_i kʌṿī

    # क्अ -> k_a not ka
    Strng = re.sub('('+Schwa+')('+Virama+')(?='+VowelList+')',r'_\2',Strng)
    # Output: kʌ× k_×a kʌ kʌā kʌr̥ k_hʌ bʌ̄× bʌ̄ bʌ̄ō bhʌ× bhʌ bhʌā kʌi kʌṿ_i kʌṿī

    # Rearranging Nukta
    Strng = re.sub('('+Schwa+')('+Nukta+')',r'\2\1',Strng)
    # Output: kʌ× k_×a kʌ kʌā kʌr̥ k_hʌ b̄ʌ× b̄ʌ b̄ʌō bhʌ× bhʌ bhʌā kʌi kʌṿ_i kʌṿī

    # Removing Schwa if followed by VowelSigns
    Strng = re.sub('('+Schwa+')(?='+VowelSignList+')','',Strng)
    # Output: k× k_×a kʌ kā kr̥ k_hʌ b̄× b̄ʌ b̄ō bh× bhʌ bhā ki kʌṿ_i kʌṿī

    # Replace Schwa by Vowel 'a'
    Strng = Strng.replace(Schwa,VowelA)
    # Output: k× k_×a ka kā kr̥ k_ha b̄× b̄a b̄ō bh× bha bhā ki kaṿ_i kaṿī

    # Remove DepV
    Strng = Strng.replace(DepV,'')
    # Output: k× k_×a ka kā kr̥ k_ha b̄× b̄a b̄ō bh× bha bhā ki ka_i kaī

    # Remove Virama
    Strng = Strng.replace(Virama,'')
    # Output: k k_a ka kā kr̥ k_ha b̄ b̄a b̄ō bh bha bhā ki ka_i kaī

    return Strng

# PostFile ? why not fix !?
def PostFixRomanOutput(Strng,Source,Target):
    Strng = Strng.replace("\u02BD","")

    if Target == "IPA":
        Strng = FixIPA(Strng)

    if Target == 'Santali':
        Strng = FixSantali(Strng)

    if Target == "Avestan":
        Strng = FixAvestan(Strng)

    if Target == "SoraSompeng":
        Strng = FixSoraSompeng(Strng)

    if Target == "WarangCiti":
        Strng = FixWarangCiti(Strng)

    return Strng

# Fixing the Indic Ouput for the standard corrections
# Indic Fix are mandatory corrections to the immediate ouput.
def FixIndicOutput(Strng,Source,Target):
    try:
        Strng = getattr(__import__('ConvertFix'),"Fix"+Target)(Strng)
    except AttributeError:
        pass
        #print #"Fix"+Target+" doesn't exist"

    Strng = Strng.replace('\u02BD','')
    # Shifting Vowel Signs and Diacritics
    # க²ா ->  கா²
    Strng = ShiftDiacritics(Strng,Target,reverse=False)

    return Strng

def FixKharoshthi(Strng, reverse=False):
    Strng = KharoshthiNumerals(Strng, reverse)

    return Strng

def FixBhaiksuki(Strng, reverse=False):
    if not reverse:
        Strng = Strng.replace(' ', '𑱃')
    else:
        Strng = Strng.replace('𑱃', ' ')
    return Strng

def FixKhudawadi(Strng, reverse=False):
    sindhi = ['𑊽', '𑋃', '𑋉', '𑋕']
    sindhiapprox = ['ˍ𑊼', 'ˍ𑋂', 'ˍ𑋈', 'ˍ𑋔']

    if not reverse:
        for x, y in zip(sindhi, sindhiapprox):
            Strng = Strng.replace(y,x)
    else:
        for x, y in zip(sindhi, sindhiapprox):
            Strng = Strng.replace(x,y)

    return Strng

# Correct Ru2, Lu2 -> R, lR
def FixTamil(Strng,reverse=False):
    Strng = CorrectRuLu(Strng,"Tamil",reverse)

    ava = Tamil.SignMap[0]
    avaA = '\u0028\u0B86\u0029'

    if not reverse:
        Strng = Strng.replace(ava+ava,avaA)
        Strng = PostProcess.RetainDandasIndic(Strng, 'Tamil', True)
        Strng = PostProcess.RetainIndicNumerals(Strng, 'Tamil', True)
    else:
        Strng = Strng.replace(avaA,ava+ava)

        Strng = Strng.replace('𑌃', '꞉')

    return Strng

def FixOriya(Strng, reverse=False):
    if not reverse:
        pass
    else:
        Strng = Strng.replace('ଵ','ୱ')

    return Strng

# Correct Ru'', Lu'' -> R, lR
# Tippi/Bindu
def FixGurmukhi(Strng,reverse=False):
    Strng = CorrectRuLu(Strng,"Gurmukhi",reverse)

    ava = Gurmukhi.SignMap[0]
    avaA = '\u0028\u0A06\u0029'

    # Tippi/Bindu conversion options are optional. Look into PostProcess

    if not reverse:
        Strng = Strng.replace(ava+ava,avaA)
        Strng = PostProcess.InsertGeminationSign(Strng, 'Gurmukhi')
        Strng = PostProcess.RetainIndicNumerals(Strng, 'Gurmukhi', True)

    else:
        Strng = Strng.replace(avaA,ava+ava)
        Strng = PostProcess.ReverseGeminationSign(Strng, 'Gurmukhi')
        Strng = Strng.replace('ੰਨ','ਨ੍ਨ')
        Strng = Strng.replace('ੰਮ','ਮ੍ਮ')
        # Replace Tippi by Bindu
        Strng = Strng.replace('\u0A70','\u0A02')
        Strng = PostProcess.GurmukhiYakaash(Strng, True)

    return Strng

# Fix ru', ru'',lu',lu'' in Tamil & Gurmukhi
# रुʼ -> ऋ, रूʼ -> ॠ, लुʼ -> ऌ, लूʼ -> ॡ
def CorrectRuLu(Strng,Target,reverse=False):
    ra = GM.CrunchList('ConsonantMap', Target)[26]
    la = GM.CrunchList('ConsonantMap', Target)[27]
    uuu = GM.CrunchSymbols(GM.VowelSigns,Target)[4:6] #Vowel Signs u & U
    ap = '\u02BC'
    # Generate ru', rU', lu', lU'
    ruCons = [ra+x+ap for x in uuu ] + [la+x+ap for x in uuu]
    # Replace above with actual Vocalic Vowels
    for x,y in zip(ruCons,GM.CrunchSymbols(GM.Vowels,Target)[6:10]):
        if not reverse:
            Strng = Strng.replace(x,y)
        else:
            Strng = Strng.replace(y,x)

    return Strng

#Shift Diacritics after vowel signs
def ShiftDiacritics(Strng,Target,reverse=False):
    VS = '|'.join(GM.CrunchSymbols(GM.VowelSigns,Target))
    Diac = '|'.join(GM.Diacritics)

    if not reverse:
        Strng = re.sub('('+Diac+')'+'('+VS+')',r'\2\1',Strng)
    else:
        Strng = re.sub('('+VS+')'+'('+Diac+')',r'\2\1',Strng)

    return Strng

# Move Vowel Signs
def FixTamilGrantha(Strng,reverse=False):
    ListC = '|'.join(GM.CrunchSymbols(GM.Consonants, 'TamilGrantha'))
    ListEAI = '|'.join(TamilGrantha.VowelSignMap[9:11]+TamilGrantha.SouthVowelSignMap[0:1])
    ListOAU = TamilGrantha.VowelSignMap[11:13]+TamilGrantha.SouthVowelSignMap[1:2]

    if not reverse:
        # k + VS e/E/ai -> Joiners + VS e/E/ai + k
        Strng = re.sub('('+ListC+')'+'('+ListEAI+')','\u200B\u200C\u200D\u200C'+r'\2\1',Strng)
        # k + VS o/O/au -> Joiners + VS e/E + k + VS AA/La
        Strng = re.sub('('+ListC+')'+'('+ListOAU[0]+')','\u200B\u200C\u200D\u200C'+TamilGrantha.VowelSignMap[9]+r'\1'+TamilGrantha.VowelSignMap[0],Strng)
        Strng = re.sub('('+ListC+')'+'('+ListOAU[2]+')','\u200B\u200C\u200D\u200C'+TamilGrantha.SouthVowelSignMap[0]+r'\1'+TamilGrantha.VowelSignMap[0],Strng)
        Strng = re.sub('('+ListC+')'+'('+ListOAU[1]+')','\u200B\u200C\u200D\u200C'+TamilGrantha.SouthVowelSignMap[0]+r'\1'+Tamil.SouthConsonantMap[0],Strng)

        ## Reversing நே்ˆদ
        Strng = re.sub('(\u200B\u200C\u200D\u200C.)'+'('+ListC+')'+'(்ˆ)',r'\2\3\1',Strng)

    else:
        #print('I am here')
        # k + VS o/O/au <- Joiners + VS e/E + k + VS AA/La
        Strng = re.sub('\u200B'+TamilGrantha.VowelSignMap[9]+'('+ListC+')'+TamilGrantha.VowelSignMap[0],r'\1'+ListOAU[0],Strng)
        Strng = re.sub('\u200B'+TamilGrantha.SouthVowelSignMap[0]+'('+ListC+')'+TamilGrantha.VowelSignMap[0],r'\1'+ListOAU[2],Strng)
        Strng = re.sub('\u200B'+TamilGrantha.SouthVowelSignMap[0]+'('+ListC+')'+Tamil.SouthConsonantMap[0],r'\1'+ListOAU[1],Strng)
        # k + VS e/E/ai <- Joiners + VS e/E/ai + k
        Strng = re.sub('\u200B'+'('+ListEAI+')'+'('+ListC+')',r'\2\1',Strng)

    return Strng

# Khmer - Subjoining Consonants and Repha
def FixKhmer(Strng,reverse=False):
    ListC ='|'.join(GM.CrunchSymbols(GM.Consonants,'Khmer'))
    ra = Khmer.ConsonantMap[26]
    vir = Khmer.ViramaMap[0]

    if not reverse:
        # Replace Explicit Virama + Cons -> Subjoining Virama + Cons
        Strng = re.sub(vir+'('+ListC+')','\u17D2'+r'\1',Strng)
        # Introduce Repha : ra + sub Virama + Cons -> Cons + Repha
        Strng = re.sub('(?<!\u17D2)('+ra+')'+'\u17D2'+'('+ListC+')',r'\2'+'\u17CC',Strng)
        # i + Anusara -> i-Anusvara ligature
        Strng = Strng.replace('\u1787\u17C6','\u17B9')
    else:
        # Replace Subjoining Virama with Explicit Virama
        Strng = Strng.replace('\u17D2',vir)
        Strng = re.sub(vir+'(?=[\u17AB\u17AC\u17AD\u17AE])','\u17D2',Strng)
        # Remove Repha : ra + sub Virama + Cons <- Cons + Repha
        Strng = re.sub('('+ListC+')'+'\u17CC',ra+vir+r'\1',Strng)
        # i + Anusara -> i-Anusvara ligature
        Strng = Strng.replace('\u17B9','\u1787\u17C6')

    return Strng

# Burmese - Tall A + Subjoning Consonants
def FixBurmese(Strng,reverse=False):
    ListC ='|'.join(GM.CrunchSymbols(GM.Consonants,'Burmese'))
    vir = Burmese.ViramaMap[0]
    AA = Burmese.VowelSignMap[0]
    E = Burmese.VowelSignMap[9]

    ## Check Rendering with Myanmar1 font buddho go gau

    yrvh = Burmese.ConsonantMap[25:27] + Burmese.ConsonantMap[28:29] + Burmese.ConsonantMap[32:33]
    yrvhsub = ['\u103B','\u103C','\u103D','\u103E']

    TallACons = '|'.join([Burmese.ConsonantMap[x] for x in [1,2,4,17,20,28]])

    if not reverse:
        # Replace Explicit Virama + Cons -> Subjoining Virama + Cons
        Strng = re.sub('(?<!ာ)' + vir+'('+ListC+')','\u1039'+r'\1',Strng)

        # Introduce Kinzi: ga + NGA + sub-Virama -> ga + NGA + exp-Virama + sub-Virama
        Strng = re.sub('('+Burmese.ConsonantMap[4]+')'+'('+'\u1039'+')',r'\1'+vir+r'\2',Strng)

        # Introduce Repha
        Strng = re.sub('(ရ)'+'('+'\u1039'+')',r'\1'+vir+r'\2',Strng)

        # Introduce Tall A: ka + AA -> ka + Tall A
        Strng = re.sub('(?<!\u1039)('+TallACons+')'+'('+E+'?)'+AA,r'\1\2'+'\u102B',Strng)

        ## buddho --> Tall A
        Strng = re.sub('('+TallACons+')(\u1039)('+ListC +')'+'('+E+'?)'+AA,r'\1\2\3\4'+'\u102B',Strng)
        Strng = re.sub('('+TallACons+')(\u1039)('+ListC +')'+'(\u1039)('+ListC +')'+'('+E+'?)'+AA,r'\1\2\3\4\5\6'+'\u102B',Strng)

        Strng = re.sub('(?<=်္)' + '('+TallACons+')'+'('+E+'?)'+AA,r'\1\2'+'\u102B',Strng)

        # Remove Tall a Kinzi

        for x,y in zip(yrvh,yrvhsub):
            # Introduce subjoining forms: sub-virama + y/r/v/h -> subjoining y/r/v/h
            Strng = re.sub('(?<!်)\u1039'+x,y,Strng)

        Strng = Strng.replace('ျါ','ျာ')
        Strng = Strng.replace('ြါ','ြာ')
        Strng = Strng.replace('ျေါ','ျော')
        Strng = Strng.replace('ြေါ','ြော')


        Strng = Strng.replace("သ္သ", "ဿ")
        Strng = Strng.replace("ဉ္ဉ", "ည")

        Strng = Strng.replace("\u02F3", "့")
        Strng = Strng.replace("့်", "့်",)

        Strng = Strng.replace("ာ္", "ာ်")

        Strng = Strng.replace("ရ်္င်္ဂ", "ရ်္င္ဂ")

        Strng = Strng.replace("ါ္", "ါ်")
    else:
        Strng = Strng.replace("ဿ","သ္သ")
        Strng = Strng.replace("ည", "ဉ္ဉ")

        Strng = Strng.replace("့်", "့်")
        Strng = Strng.replace("့","\u02F3")

        # Replace sub Virama with explicit Virama
        Strng = Strng.replace('\u1039',vir)
        # Replace Tall AA with AA
        Strng = Strng.replace('\u102B',AA)
        # Replace Kinzi with NGA + Virama
        Strng = Strng.replace(Burmese.ConsonantMap[4]+vir+vir,Burmese.ConsonantMap[4]+vir)
        # Replace Repha
        Strng = Strng.replace('ရ'+vir+vir,'ရ'+vir)

        for x,y in zip(yrvh,yrvhsub):
            # Replace subjoining forms: exp-virama + y/r/v/h <- subjoining y/r/v/h
            Strng = Strng.replace(y,vir+x)

    return Strng

# Add Repha (Bali,Java,Sundanese)
# a + r + ka -> a<repha>ka
# r +ya -> rya (no repha if syllable first)
def AddRepha(Strng,Script,Repha,reverse=False):
    vir = GM.CrunchSymbols(GM.VowelSigns,Script)[0]
    ra = GM.CrunchSymbols(GM.Consonants,Script)[26]

    ListC = '|'.join(GM.CrunchSymbols(GM.Consonants,Script))
    ListV = '|'.join(GM.CrunchSymbols(GM.Vowels,Script))
    ListVS = '|'.join(GM.CrunchSymbols(GM.VowelSignsNV,Script))

    if not reverse:
        # Introduce Repha: ka/ki/A + ra + vira -> ka/ki/A + Repha
        # Check all ListC + ListV + ListVS etc if '|' is introduced
        Strng = re.sub('('+ListC+'|'+ListV+'|'+ListVS+')'+'('+ra+vir+')',r'\1'+Repha,Strng)
        ## Not working
    else:
        # Replace Repha with ra+vir
        Strng = Strng.replace(Repha,ra+vir)

    return Strng

def FixBuginese(Strng, reverse = False):

    if not reverse:
        Strng = Strng.replace("ᨂ\u02BEᨀ","ᨃ")
        Strng = Strng.replace("ᨆ\u02BEᨄ","ᨇ")
        Strng = Strng.replace("ᨊ\u02BEᨑ","ᨋ")
        Strng = Strng.replace("ᨎ\u02BEᨌ","ᨏ")

        Strng = Strng.replace('\u02BE', '')
    else:
        Strng = Strng.replace("ᨃ", "ᨂ\u02BEᨀ")
        Strng = Strng.replace("ᨇ", "ᨆ\u02BEᨄ")
        Strng = Strng.replace("ᨋ", "ᨊ\u02BEᨑ")
        Strng = Strng.replace("ᨏ", "ᨎ\u02BEᨌ")

    return Strng


# Balinese Repha
def FixBalinese(Strng,reverse=False):
    Repha = '\u1B03'

    Strng = AddRepha(Strng,"Balinese",Repha,reverse)

    return Strng

# Javanese - Reppha & Subjoining ra & ya
def FixJavanese(Strng,reverse=False):
    Repha = '\uA982'
    vir = Javanese.ViramaMap[0]
    ra, ya = Javanese.ConsonantMap[26], Javanese.ConsonantMap[25]
    SubRa, SubYa = '\uA9BF','\uA9BE'

    Strng = AddRepha(Strng,"Javanese",Repha,reverse)

    if not reverse:
        # Introduce subjoining Ra & Ya
        Strng = Strng.replace(vir+ra,SubRa).replace(vir+ya,SubYa)
    else:
        # Replace Subjoining forms with cons+vir
        Strng = Strng.replace(SubRa,vir+ra).replace(SubYa,vir+ya)

    return Strng

# Urdu - Shadda, Final E
def FixUrdu(Strng,reverse=False):
    Target = 'Urdu'

    # .replace(u'\u064E','')

    Strng = Strng.replace('\u02BD','')

    vir = GM.CrunchSymbols(GM.VowelSigns,Target)[0]

    ConUnAsp = [GM.CrunchList('ConsonantMap', Target)[x] for x in [0,2,5,7,10,12,15,17,20,22,4,9,14,19,24]+list(range(25,33))] # Add SemiVowels & Nukta Consonants
    ConUnAsp = ConUnAsp + GM.CrunchList('SouthConsonantMap',Target) + GM.CrunchList('NuktaConsonantMap',Target)

    ## Add word-final E, Short A sign

    ShortVowels = '|'.join(['\u0652','\u064E','\u0650','\u064F'])
    a = '\u064E'
    ya = '\u06CC'
    va  = '\u0648'
    yaBig = '\u06D2'
    Aa = Urdu.VowelSignMap[0]

    #Strng = Strng.replace(u'\u064E'+ya,ya)
    #Strng = Strng.replace(u'\u064E'+va,va)

    if not reverse:
        ## Fixing Hamza

        ListVS = '(' + '|'.join(GM.CrunchSymbols(GM.VowelSigns,'Urdu')) + ')'
        ListV = '(' + '|'.join(GM.CrunchSymbols(GM.Vowels,'Urdu')) + ')'

        hamzaFull = "\u0621"
        hamzaChair = "\u0626"

        Strng = re.sub(ListVS + ListV, r'\1' + hamzaFull + r'\2', Strng)
        Strng = re.sub(ListV + ListV, r'\1' + hamzaFull + r'\2', Strng)


        Strng = re.sub('('+a+')'+'('+ShortVowels+')',r'\2',Strng)
        Strng = re.sub('(?<!'+Aa+')'+'('+a+')'+'('+va+'|'+ya+')'+'(?!'+ ShortVowels +')',r'\2',Strng)
        ListC = '|'.join(GM.CrunchSymbols(GM.Consonants,'Urdu')).replace(a,'')
        Ayoga = '|'.join(Urdu.AyogavahaMap[0] + Urdu.AyogavahaMap[1])

        Strng = Strng.replace(ya,yaBig)
        Strng = re.sub('('+yaBig+')'+'(?='+'|'.join(ConUnAsp)+ShortVowels+')',ya,Strng)
        Strng = re.sub('('+yaBig+')'+'('+ListC+')',ya+r'\2',Strng)
        Strng = re.sub('('+yaBig+')'+'('+Ayoga+')',ya+r'\2',Strng)

        Strng = Strng.replace('\u0650'+yaBig,'\u0650'+ya)
        Strng = Strng.replace(a+Urdu.VowelSignMap[0],Urdu.VowelSignMap[0])

        ## ye ## yezu ## Fix this

        ## Adding Gemination of Consonant

        ConAsp   = [GM.CrunchList('ConsonantMap', Target)[x] for x in [1,3,6,8,11,13,16,18,21,23]]
        ConUnAsp_a =  [x.replace('\u064e','') for x in ConUnAsp]

        Strng = re.sub('('+'|'.join(ConUnAsp_a)+')'+'('+vir+')'+r'\1',r'\1'+GM.Gemination[Target],Strng)

        ## Fix

        Strng = Strng.replace('ےے', 'یے')
        Strng = Strng.replace('ےی', 'یی')
        Strng = Strng.replace('ےْ', 'یْ')

        Strng = Strng.replace('ءاِی', 'ئی')
        Strng = Strng.replace('ءاے', 'ئے')

        ## Fix

        Strng = Strng.replace('', '')
    else:
        if True:
            #print(Strng)

            ListC = GM.CrunchSymbols(GM.Consonants,'Urdu')

            ## Replacig Arabic with closest Indic counterparts

            Strng = Strng.replace('ص', 'س')
            Strng = Strng.replace('ث', 'س')

            Strng = Strng.replace('ح', 'ہ')
            Strng = Strng.replace('ۃ', 'ہ')

            Strng = Strng.replace('ذ', 'ز')
            Strng = Strng.replace('ض', 'ز')
            Strng = Strng.replace('ظ', 'ز')

            Strng = Strng.replace('ط', 'ت')

            Strng = Strng.replace('ژ', 'ز')

            Strng = Strng.replace('ع', 'اَ')

            Strng = Strng.replace('ً', 'نْ')

            Strng = Strng.replace('ئ', '_'+ya)

            Strng = Strng.replace('ؤ', '_'+'و')

            Strng = Strng.replace('ء‬', '_')

            Strng = Strng.replace('یٰ', 'ا')

            Strng = Strng.replace('ك', 'ک')

            Strng = Strng.replace('ي', 'ی')

            #print(Strng)

            ## Gemination ##

            Strng = re.sub('(' + ShortVowels + ')(ّ)', r'\2'+r'\1', Strng)
            Strng = re.sub('(.)(ّ)', r'\1'+'ْ'+r'\1', Strng)


            #print(Strng)

            if "\u02BB\u02BB" in Strng: ## Short Vowels not showm. INnsert /a/ to all consonats and approximate
                Strng = Strng.replace('ا', 'اَ')

                for c in ListC:
                    Strng = Strng.replace(c.replace(a, ''), c)
                    Strng = Strng.replace(c + 'اَ', c + 'ا')
                    Strng = Strng.replace(c + 'ا' + 'و', c + 'ا' + '\u200B' + 'و')
                    Strng = Strng.replace(c + 'ا' + 'ی', c + 'ا' + '\u200B' + 'ی')

                Strng = Strng.replace(a + 'ھ', 'ھ' + a)

                Strng = Strng.replace('ھ' + a + 'اَ' , 'ھ' + a + 'ا')

                ### Change this for dochashmee ha
                Strng = Strng.replace('ھ' + a + 'ا' + 'و', 'ھ' + a + 'ا' + '\u200B' + 'و')
                Strng = Strng.replace('ھ' + a + 'ا' + 'ی', 'ھ' + a + 'ا' + '\u200B' + 'ی')

                Strng = Strng.replace(a + a, a)

                Strng= Strng.replace(yaBig, ya)

                Strng = Strng.replace('\u02BB\u02BB', '')
            else:
                ShortVowelsR = '|'.join(['\u0652','\u0650','\u064F'])
                longVowels = '|'.join(['و', 'ا', ya])

                Strng= Strng.replace(yaBig, ya)

                ListCR = '|'.join(GM.CrunchSymbols(GM.Consonants,'Urdu')).replace(a,'')

                Strng = re.sub('(' + ListCR + ')' + '('+ShortVowelsR+')',r'\1' + a + r'\2',Strng)
                Strng = re.sub('(' + ListCR + ')' + '('+longVowels+')'  + '(?!' + ShortVowels + ')',r'\1' + a + r'\2',Strng)


            VowelVS = '|'.join(GM.CrunchSymbols(GM.VowelSigns,'Urdu'))


        # print(Strng)

#    for i in range(len(ConAsp)):
#        Strng = re.sub('('+ConAsp[i]+')'+'('+vir+')'+'('+ConAsp[i]+')',r'\3'+GM.Gemination[Target],Strng)

    # Add Hamza

    if not reverse:
        pass
    else:
        pass

    ### Todo

    # Punctuation
    if ( not reverse):
        for x,y in zip([',','?',';'],['،','؟','؛']):
            Strng = Strng.replace(x,y)
    else :
        for x,y in zip([',','?',';'],['،','؟','؛']):
            Strng = Strng.replace(y,x)

#    Strng = Strng.replace(Aa+Aa,Aa+hamzaFull+Aa)
#    Strng = re.sub("("+ListVS+")"+"(?="+iii+")",r'\1'+hamzaChair,Strng)
#
#    Strng = Strng.replace(u"\u02BE","")

    #Strng = re.sub('('+ListC+')'+'(?!'+ListVS+')',r'\1'+a,Strng)

    return Strng

### Anusvara to Nasal for Thanaa - Consider Add
# ThaanaVowelSign A
def FixThaana(Strng,reverse=False):
    ## Thaana other Arabic based consonants DD££
    ListC ='|'.join(GM.CrunchSymbols(GM.Consonants,'Thaana'))
    VowelVS = '|'.join(GM.CrunchSymbols(GM.VowelSigns,'Thaana'))
    aBase = '\u0787'

    if not reverse:
        # Replace VS-A + Vowel Sign -> Vowel Sign :
        Strng = PostProcess.InsertGeminationSign(Strng, 'Thaana')
        Strng = re.sub("(\u07A6)"+"(?=("+VowelVS+"))","",Strng)
        Strng = Strng.replace("\u02BE","")

        for x,y in zip([',','?',';'],['،','؟','؛']):
            Strng = Strng.replace(x,y)

        Strng = Strng.replace('ʔ', 'އް')

    else:
        # Add VS-A to all VowelSigns
        # Approximate
        Strng = Strng.replace('ޢ','އ')
        Strng = Strng.replace('ޡ','ތ')
        Strng = Strng.replace('ޥ','ވ') # waav to va
        Strng = Strng.replace('ޠ','ތ') # To to ta
        Strng = Strng.replace('ޟ','ސ')
        Strng = Strng.replace('ޞ','ސ')
        Strng = Strng.replace('ޜ','ށ')
        Strng = Strng.replace('ޛ','ދ')
        Strng = Strng.replace('ޘ','ތ')
        Strng = Strng.replace('ޛ','ދ')
        Strng = Strng.replace('ޙ', 'ހ')

        Strng = re.sub('(' + ListC.replace('ަ','') + ')' + '(?!' + VowelVS + '|ަ' + ')', r'\1' + 'ް', Strng)

        Strng = re.sub('(?<!'+aBase+')(?<!'+'\u02BD\u02BD\u02BD'+')('+VowelVS+')',"\u07A6"+r'\1',Strng)
        Strng = PostProcess.ReverseGeminationSign(Strng, 'Thaana')

        Strng = Strng.replace('އް','ʔ')

        for x,y in zip([',','?',';'],['،','؟','؛']):
            Strng = Strng.replace(y,x)

    return Strng

def FixSaurashtra(Strng, reverse = False):
    if not reverse:
        Strng = Strng.replace('ꢒ꣄ꢰ', 'ꢒ꣄‍ꢰ') # Ksha
    else:
        Strng = Strng.replace('ꢴ','꣄ꢲ')

    return Strng

# Tibetan Subjoining Consnants
def FixTibetan(Strng,reverse=False):
    ListC = [Tibetan.ViramaMap[0]+chr(x) for x in range(0x0F40,0x0F68)] # Consonants
    ListSubC = [chr(x+80) for x in range(0x0F40,0x0F68)] # Subjoined Consonants

    SubC = ["ཝྭ","ཡྱ","རྱ","རྭ", "ྺྭ"]
    SubMinC = ["ཝྺ","ཡྻ","ཪྻ","ཪྺ", "ྺྺ"]

    if not reverse:
        for x,y in zip(ListC,ListSubC):
            Strng = Strng.replace(x,y)

        for x,y in zip(SubC,SubMinC):
            Strng = Strng.replace(x,y)

        Strng = Strng.replace(' ', '\u0F0B')

        Strng = Strng.replace("ཛྷ༹", "ཞ")

        Strng = Strng.replace("(", "༺")
        Strng = Strng.replace(")", "༻")

        Strng = Strng.replace("{", "༼")
        Strng = Strng.replace("}", "༽")


    if reverse:
        AspirateDecom= ["གྷ", "ཌྷ", "དྷ", "བྷ", "ཛྷ", "ྒྷ", "ྜྷ", "ྡྷ", "ྦྷ", "ྫྷ"]
        AspirateAtomic = ["གྷ", "ཌྷ", "དྷ", "བྷ", "ཛྷ", "ྒྷ", "ྜྷ", "ྡྷ", "ྦྷ", "ྫྷ"]

        for x, y in zip(AspirateDecom, AspirateAtomic):
            Strng = Strng.replace(x, y)

        for x,y in zip(SubC,SubMinC):
            Strng = Strng.replace(y,x)

        for x,y in zip(ListC,ListSubC):
            Strng = Strng.replace(y,x)

        for x,y in zip(['྄རྀ','྄རཱྀ','྄ལྀ',"྄ལཱྀ"],['ྲྀ','ྲཱྀ', 'ླྀ','ླཱྀ']):
            Strng = Strng.replace(x,y)

        Strng = Strng.replace('་', ' ')
        Strng = Strng.replace("༔", "།")
        Strng = Strng.replace("༈", "།")

        Strng = Strng.replace("༺", "(")
        Strng = Strng.replace("༻", ")")

        Strng = Strng.replace("༼", "{")
        Strng = Strng.replace("༽", "}")

        Strng = Strng.replace("འ", "ཨ")
        Strng = Strng.replace("ཇ", "ཛ")

        Strng = Strng.replace("ཞ", "ཛྷ༹")

    return Strng

# Thai, Lao follow visual ordering of Vowels signs ; <e> + k => <e>k
# Other Indic scripts follow logical order ; k + <e> => <e>k
# Swapping Vowel Signs for conversion
def ReverseVowelSigns(Strng,Script,reverse=False):
    EAIO = "|".join(sorted(GM.CrunchSymbols(GM.VowelSignsNV,Script)[9:12]+GM.CrunchSymbols(GM.VowelSignsNV,Script)[17:],key=len,reverse=True))
    cons = "|".join(GM.CrunchSymbols(GM.Consonants,Script))

    if Script == "Lao":
        cons = "|".join(GM.CrunchSymbols(GM.Consonants,Script) + ['ດ','ບ','ຟ'])

    a = GM.CrunchSymbols(GM.Vowels,Script)[0]

    if not reverse:
        Strng = re.sub("("+cons+")("+EAIO+")(?!("+EAIO+")"+a+")",r"\2\1",Strng)
    else:
        Strng = re.sub("("+EAIO+")"+"("+cons+")",r'\2\1',Strng)

    return Strng

def FixThai(Strng,reverse=False):
    Strng = ThaiReverseVowelSigns(Strng,reverse)
    Strng = ThaiDigraphConjuncts(Strng,reverse)

    if "\u02BB\u02BB" in Strng:
        Strng = PostProcess.ThaiLaoTranscription(Strng,"Thai", '\u0E30', '\u0E31', True)
        Strng = Strng.replace("\u02BB\u02BB", '')

        Strng = Strng.replace("หฺ์","ห์")


    return Strng

def ThaiReverseVowelSigns(Strng,reverse=False):
#    EAIO = "".join(Thai.VowelSignMap[9:12])
#    cons = "|".join(GM.CrunchSymbols(GM.Consonants, "Thai"))
#    a = Thai.VowelMap[0]
#    Strng = re.sub("("+cons+")(["+EAIO+"])(?!["+EAIO+"]"+a+")",r"\2\1",Strng)

    Strng = ReverseVowelSigns(Strng,"Thai",reverse)
    if not reverse:
        # VS AA + Anusvara -> VS AM (Ligature)
        # VS I + Anusvara -> VS IM (Ligature)
        Strng = Strng.replace("\u0E32\u0E4D","\u0E33").replace("\u0E34\u0E4D","\u0E36")
    else:
        # Reverse above
        Strng = Strng.replace("\u0E33","\u0E32\u0E4D").replace("\u0E36","\u0E34\u0E4D")

    return Strng

def FixLaoPali(Strng,reverse=False):
    ## Check AU in Lao in THN file pdf in Lao-Pali text

    Strng = ReverseVowelSigns(Strng,"LaoPali",reverse)

    if "\u02BB\u02BB" in Strng:
        Strng = LaoPaliTranscribe(Strng, True)
        Strng = Strng.replace("\u02BB\u02BB", '')

        Strng = Strng.replace("ຫ຺໌","ຫ໌")

    if not reverse:
        # VS AA + Anusvara -> VS AM (Ligature)
        Strng = Strng.replace("\u0EB2\u0ECD","\u0EB3")
    else:
        # VS AA + Anusvara <- VS AM (Ligature)
        Strng= Strng.replace("\u0EB3","\u0EB2\u0ECD")

    return Strng

def FixAvestan(Strng, reverse=False):
    extraCons = ["\U00010B33","\U00010B32","\U00010B1D","\U00010B12", '𐬣', '𐬝']
    ListC = "|".join(GM.CrunchSymbols(GM.Consonants, "Avestan")+extraCons)
    ListV = "|".join(GM.CrunchSymbols(GM.Vowels,"Avestan"))

    ya = Avestan.ConsonantMap[25]
    va = Avestan.ConsonantMap[28]
    ii = Avestan.VowelMap[2] * 2
    uu = Avestan.VowelMap[4] * 2

    if not reverse:
        Strng = Strng.replace('𐬀𐬩', '𐬄') ## aM
        Strng = Strng.replace('𐬁𐬩', '𐬅') ## AM

        Strng = re.sub("(("+ListV+")"+"|"+"("+ListC+"))"+"("+ya+")",r'\1'+ii,Strng)
        Strng = re.sub("(("+ListV+")"+"|"+"("+ListC+"))"+"("+va+")",r'\1'+uu,Strng)

        Strng = Strng.replace(Avestan.ConsonantMap[15]  + '\u02BF', '\U00010B1D') ## TTE
        Strng = Strng.replace(va + '\u02BF', '\U00010B21') # BHA

        Strng = Strng.replace('𐬰\u02BF', '𐬲') ## ZHA
        Strng = Strng.replace('𐬢\u02BF','𐬤') ## NGVA
        Strng = Strng.replace('𐬁_𐬋', '𐬃') ## AO

        Strng = Strng.replace('\u02BF', '')

    else:
        Strng = Strng.replace('𐬄', '𐬀𐬩')
        Strng = Strng.replace('𐬅', '𐬁𐬩')

        Strng = Strng.replace(ii, ya).replace(uu, va)

        Strng = Strng.replace('\U00010B1D', Avestan.ConsonantMap[15]  + '\u02BF')
        Strng = Strng.replace('𐬣', Avestan.ConsonantMap[4])

        Strng = Strng.replace('\U00010B12', Avestan.ConsonantMap[1])
        Strng = Strng.replace('\U00010B33', Avestan.ConsonantMap[29])
        Strng = Strng.replace('𐬡', va + '\u02BF')

        Strng = Strng.replace('𐬲', '𐬰\u02BF') ## ZHA
        Strng = Strng.replace('𐬤', '𐬢\u02BF') ## NGVA
        Strng = Strng.replace('𐬃', '𐬁_𐬋') ## AO

        ## 𐬲𐬤𐬃  approximate this

        ### Replave JHA + Nukta as ZHA in Devanagari & Gujarati

    return Strng

def FixLao(Strng,reverse=False):
    if reverse:
        Strng = Strng.replace("ດ", "ທ\uEB0A")
        Strng = Strng.replace('ບ', "ປ\uEB0A")
        Strng = Strng.replace('ຟ', "ພ\uEB0A")
        Strng = Strng.replace('ັ','ະ')

    if not reverse:
        Strng = Strng.replace("ທ\uEB0A", "ດ")
        Strng = Strng.replace("ປ\uEB0A", 'ບ')
        Strng = Strng.replace("ພ\uEB0A",'ຟ')

        Strng = re.sub("(?<!ດ)(?<!ບ)(?<!ຟ)\uEB0A", "", Strng)

    Strng = ReverseVowelSigns(Strng,"Lao",reverse)
    Strng = LaoTranscribe(Strng,reverse)

    if not reverse:
        # VS AA + Anusvara -> VS AM (Ligature)
        Strng = Strng.replace("\u0EB2\u0ECD","\u0EB3")

        # Remove the Pseduo Nukta
        Strng = Strng.replace("\uEB0A", "")

    else:
        # VS AA + Anusvara <- VS AM (Ligature)
        Strng= Strng.replace("\u0EB3","\u0EB2\u0ECD")

        # Swap Nukta
        Strng = Strng.replace("\u0EBA\uEB0A","\uEB0A\u0EBA")

        ## Fix NHukt and vowe a short a

        Strng = Strng.replace('຺ະ', '')
        #Strng = Strng.replace('຺', '')

        Strng = Strng.replace('ອ\u0EBAົ','ອົ')

    return Strng

# Re-arrange Vowels Signs /E/, /AI/, /O/ for digraph <dv>, <mh> etc
# e.g dve -> เทฺว instead of ทฺเว
def ThaiDigraphConjuncts(Strng,reverse=False):
    EAIO = "".join(Thai.VowelSignMap[9:12])
    cons = "|".join(GM.CrunchSymbols(GM.Consonants, "Thai"))
    yrlvh = "|".join(GM.CrunchSymbols(GM.Consonants, "Thai")[25:29] + GM.CrunchSymbols(GM.Consonants, "Thai")[32:33])
    sh = "|".join(Thai.ConsonantMap[31:33])
    vir = Thai.ViramaMap[0]

    #Replace \s with all punctuations
    if not reverse:
        # Comments
        Strng = re.sub("(?<=\s)("+cons+")"+"("+vir+")"+"(["+EAIO+"])"+"("+cons+")",r"\3\1\2\4",Strng)
        Strng = re.sub("("+cons+")"+"("+vir+")"+"(["+EAIO+"])"+"("+yrlvh+")",r"\3\1\2\4",Strng)
        Strng = re.sub("("+sh+")"+"("+vir+")"+"(["+EAIO+"])"+"("+cons+")",r"\3\1\2\4",Strng)
    else:
        ## Reverse the above.
        Strng = re.sub("(["+EAIO+"])"+"("+vir+")"+"("+cons+")",r"\2\3\1",Strng)

    return Strng

def FixOldPersian(Strng,reverse=False):
    Strng = OldPersianSyllable(Strng,reverse)
    Strng = OldPersianNumeral(Strng,reverse)

    return Strng

# Syllabization of Persian
# d<a> +i -> d<i> + i
# d<a> + u -> d<u> + u
def OldPersianSyllable(Strng,reverse=True):
    ICons = [x+'\U000103A1' for x in ['\U000103AD','\U000103B6','\U000103A9','\U000103BA','\U000103AB','\U000103B4','\U000103BC']]
    ICons_ = [x+'_\U000103A1' for x in ['\U000103AD','\U000103B6','\U000103A9','\U000103BA','\U000103AB','\U000103B4','\U000103BC']]
    ISyll = [x+'\U000103A1' for x in ['\U000103AE','\U000103B7','\U000103AA','\U000103BB','\U000103AB','\U000103B4','\U000103BC']]

    UCons = [x+'\U000103A2' for x in ['\U000103AD','\U000103B6','\U000103A3','\U000103A5','\U000103AB','\U000103B4','\U000103BC']]
    UCons_ = [x+'_\U000103A2' for x in ['\U000103AD','\U000103B6','\U000103A3','\U000103A5','\U000103AB','\U000103B4','\U000103BC']]
    USyll = [x+'\U000103A2' for x in ['\U000103AF','\U000103B8','\U000103A4','\U000103A6','\U000103AC','\U000103B5','\U000103BD']]

    ACons = [x+'<\U000103A0' for x in ['\U000103AD','\U000103B6','\U000103A3','\U000103A5','\U000103A9','\U000103BA','𐎼','𐎴','𐎫']]
    ASyll = ['\U000103AD','\U000103B6','\U000103A3','\U000103A5','\U000103A9','\U000103BA','𐎼','𐎴','𐎫']

    SylAlpha = '([𐎧𐎨𐏂𐎰𐎱𐎳𐎲𐎹𐎾𐎿𐏀𐏁𐏃])'

    ListC = '(' + '|'.join(GM.CrunchSymbols(GM.Consonants, 'OldPersian')) + ')'

    if not reverse:
        #print(Strng)
        Strng = Strng.replace(" ","\U000103D0").replace("_","").replace("<","")
        for x,y in zip(ICons+UCons+ACons,ISyll+USyll+ASyll):
            Strng = Strng.replace(x,y)
        #print(Strng)
    else:
        Strng = re.sub('𐎻(?!\U000103A1)', '𐎻\U000103A1', Strng)

        for x,y in zip(ICons_+UCons_,ISyll+USyll):
            Strng = Strng.replace(y,x)

        Strng = re.sub(SylAlpha + '(𐎠𐎡)', r'\1<\2', Strng)
        Strng = re.sub(SylAlpha + '(𐎠𐎢)', r'\1<\2', Strng)

        Strng = re.sub(ListC + '\U000103A0', r'\1' + '_\U000103A0', Strng)
        Strng = re.sub(SylAlpha + '([\U000103A1\U000103A2])', r'\1_\2', Strng)

        Strng = re.sub('([' + "".join(ASyll) + '])' + '([\U000103A1\U000103A2])', r'\1' + '<' + '\U000103A0' + r'\2' , Strng)

        Strng = Strng.replace('𐏐',' ')



    if not reverse:
        # Replace Space with Word Sperator
        # Remove _ - (why :-/ )
        pass
        #Strng = Strng.replace(" ","\U000103D0").replace("_","").replace("<","")
    else:
        pass
        #Strng = re.sub('([\U000103AD\U000103B6\U000103A3\U000103A5\U000103A9\U000103BA])_\U000103A0(?![𐎡𐎢])',r"\1",Strng)


    ## Fix dai Vs tai

    return Strng

# Convert numbers into Persinal Numeral System
def OldPersianNumeral(Strng,reverse=False):
    One = '\U000103D1'
    Two = '\U000103D2'
    Ten = '\U000103D3'
    Twenty = '\U000103D4'
    Hundred = '\U000103D5'

    Numbers = sorted(map(int,re.findall("\d+", Strng)),reverse=True)

    if not reverse:
        for num in Numbers:
            hN = int(num / 100)
            tW = int((num - (hN*100)) / 20)
            tN = int((num - (hN*100) - (tW*20)) /10)
            t2 = int((num - (hN*100) - (tW*20) - (tN*10)) /2)
            n1 = int(num - (hN*100) - (tW*20) - (tN*10) - (t2*2))

            perNum = (Hundred*hN) + (Twenty*tW) + (Ten*tN) + (Two*t2) + (One*n1)

            Strng = Strng.replace(str(num),perNum)
    else:
        Strng = Strng.replace(One, '1#')
        Strng = Strng.replace(Two, '2#')
        Strng = Strng.replace(Ten, '10#')
        Strng = Strng.replace(Twenty, '20#')
        Strng = Strng.replace(Hundred, '100#')

    return Strng

def KharoshthiNumerals(Strng, reverse=False):
    Numbers = sorted(map(int,re.findall("\d+", Strng)),reverse=True)

    if not reverse:
        for num in Numbers:
             Strng = Strng.replace(str(num),kharoshthiNumber(num))
    else:
        one = '𐩀'
        two = '𐩁'
        three = '𐩂'
        four = '𐩃'
        ten = '𐩄'
        twenty = '𐩅'
        hundred = '𐩆'
        thousand = '𐩇'

        Strng = Strng.replace(one, '1#')
        Strng = Strng.replace(two, '2#')
        Strng = Strng.replace(three, '3#')
        Strng = Strng.replace(four, '4#')
        Strng = Strng.replace(ten, '10#')
        Strng = Strng.replace(twenty, '20#')
        Strng = Strng.replace(hundred, '100#')
        Strng = Strng.replace(thousand, '1000#')


    return Strng

def kharoshthiNumber(Strng):
    one = '𐩀'
    two = '𐩁'
    three = '𐩂'
    four = '𐩃'
    ten = '𐩄'
    twenty = '𐩅'
    hundred = '𐩆'
    thousand = '𐩇'

    num = int(Strng)
    kharnum = ''
    thou = int(num/1000)
    if thou > 0:
        if thou > 1:
            kharnum += kharoshthiNumber(thou)
        kharnum += thousand
    hund = int((num - (thou*1000))/100)
    if hund > 0:
        if hund > 1:
            kharnum += kharoshthiNumber(hund)
        kharnum += hundred
    twen = int((num - (thou*1000) - (hund * 100))/20)
    if twen > 0:
        kharnum += twenty * twen
    tenn = int((num - (thou*1000) - (hund * 100) - (twen*20))/10)
    if tenn > 0:
        if tenn > 1:
            kharnum += kharoshthiNumber(tenn)
        kharnum += ten
    ones = int((num - (thou*1000) - (hund * 100) - (twen*20) - (tenn * 10)))
    if ones > 0:
        if ones == 1:
            kharnum += one
        elif ones == 2:
            kharnum += two
        elif ones == 3:
            kharnum += three
        elif ones == 4:
            kharnum += four
        elif ones == 5:
            kharnum += four + one
        elif ones == 6:
            kharnum += four + two
        elif ones == 7:
            kharnum += four + three
        elif ones == 8:
            kharnum += four + four
        elif ones == 9:
            kharnum += four + four + one

    return kharnum

def FixSinhala(Strng,reverse=False):
    Strng = PostProcess.SinhalaDefaultConjuncts(Strng)

    if not reverse:
        #Sinhala JNA
        Strng = Strng.replace("\u0DA2\u0DCA\u0DA4","\u0DA5")
        #sinhala
        Strng = Strng.replace("(අ)(අ)","(ආ)")
    else:
        Strng = Strng.replace("\u0DA5","\u0DA2\u0DCA\u0DA4")
        ## Remove joiners
        Strng = Strng.replace("‍","")
        Strng = Strng.replace("(ආ)","(අ)(අ)")


    return Strng

def FixSantali(Strng, reverse=False):
    if not reverse:
        Strng = Strng.replace('ᱹᱸ', 'ᱺ')
        Strng = Strng.replace('ᱻᱸ', 'ᱸᱻ')
    else:
        Strng = Strng.replace('ᱺ', 'ᱹᱸ')
        Strng = Strng.replace('ᱽ','’')
        Strng = Strng.replace('ᱸᱻ', 'ᱻᱸ')

    return Strng

def FixSoraSompeng(Strng, reverse = False):
    ListC = "(" + "|".join(GM.CrunchSymbols(GM.Consonants, 'SoraSompeng')) + ')'

    if not reverse:
        Strng = re.sub(ListC + '(ə)', r'\1', Strng)
        Strng = Strng.replace('ə', '\U000110E6')
    else:
        ListV = "(" + "|".join(GM.CrunchSymbols(GM.Vowels, 'SoraSompeng')) + ')'
        Strng = re.sub(ListC + '(?!' + ListV + ')', r'\1' + 'ə', Strng)

    return Strng

def FixWarangCiti(Strng, reverse = False):
    ListC = "(" + "|".join(GM.CrunchSymbols(GM.Consonants, 'WarangCiti')) + ')'

    if not reverse:
        Strng = re.sub(ListC + '(\U000118C1)', r'\1', Strng)
    else:
        ListV = "(" + "|".join(GM.CrunchSymbols(GM.Vowels, 'WarangCiti')) + ')'
        Strng = re.sub(ListC + '(?!' + ListV + ')', r'\1' + '\U000118C1', Strng)

    return Strng

#Subojined & Final
def FixLimbu(Strng,reverse=False):
    vir = Limbu.ViramaMap[0]

    SCons = [vir+x for x in [Limbu.ConsonantMap[x] for x in [25,26,28]]]  # /ya/, /ra/, /va/
    SubCons = ['\u1929','\u192A','\u192B']

    for x,y in zip(SCons,SubCons):
        if not reverse:
            # Replace Subjoined Consonants
            Strng = Strng.replace(x,y)
        else:
            # Reverse above
            Strng = Strng.replace(y,x)

    signAll = '|'.join(GM.CrunchSymbols(GM.Consonants+GM.Vowels+GM.VowelSignsNV, "Limbu"))

    FCons = [x+vir for x in [Limbu.ConsonantMap[x] for x in[0,4,15,19,20,24,26,27]]]
    FinalCons = ['\u1930','\u1931','\u1933','\u1934','\u1935','\u1936','\u1937','\u1938']

    ### ZWNJ with finalcons + ya/ra/la/va (perhaps do this for other scripts)ˍ
    if reverse:
        Strng = re.sub('(' + '|'.join(FinalCons) + ')' + '(?=[ᤕᤖᤘ])', r'\1' + '\u200C', Strng)
        Strng = re.sub('([ᤀᤁᤂᤃᤄᤅᤆᤇᤈᤉᤊᤋᤌᤍᤎᤏᤐᤑᤒᤓᤔᤕᤖᤗᤘᤚᤛᤜᤠᤣᤥᤧᤨᤩᤪᤫ])᤺', r'\1' + '꞉', Strng)
        ## Modifying letter colon ## Fix this only with aH ᤆᤠ᤺ᤣ
    else:
        Strng = Strng.replace('꞉', '᤺')

    for x,y in zip(FCons,FinalCons):
        if not reverse:
            # Replace Final pure consonants
            Strng = re.sub('('+signAll+')'+ '(\u193A?)' + '('+x+')',r'\1\2'+y,Strng)
        else:
            # Reverse above
            Strng = Strng.replace(y,x)

    if not reverse:
        Strng = Strng.replace('ʔ','᤹')
        Strng = Strng.replace('!','᥄')
        Strng = Strng.replace('?','᥅')
    else:
        Strng = Strng.replace('᤹', 'ʔ')
        Strng = Strng.replace('᥄', '!')
        Strng = Strng.replace('᥅', '?')
    ## Add proper support for Limbu e,o to Devanagari
    ## Limbu Question mark and exclamation mark?
    ## LImbu to devanagari conventions
    ## Limbu Danda

    return Strng


def FixDevanagari(Strng, reverse=False):
    Sindhi = ['ॻ','ॼ','ॾ','ॿ']
    SindhiApprox = ['ˍग','ˍज','ˍड','ˍब']
    if not reverse:
        Strng = Strng.replace('ʔ', 'ॽ')

        for x, y in zip(Sindhi, SindhiApprox):
            Strng = Strng.replace(y, x)

        Strng = Strng.replace('ज़़','ॹ')

    else:
        Strng = PostProcess.DevanagariPrishtamatra(Strng, reverse=True)
        Strng = Strng.replace('ॽ', 'ʔ')
        Strng = Strng.replace('ॹ', 'ज़़')

        for x, y in zip(Sindhi, SindhiApprox):
            Strng = Strng.replace(x, y)

    return Strng

def FixKaithi(Strng, reverse=False):
    if not reverse:
        Strng = Strng.replace(' ', '⸱')
    else:
        Strng = Strng.replace("⸱",' ')
        # Strng = re.sub('', '', Strng)

    return Strng

def FixLao2(Strng, reverse = False):
    return FixLao(Strng, reverse)

#Subjoined, final and la-ligatures
# Fix aH -> a ;
def FixLepcha(Strng,reverse=False):
    vir = Lepcha.ViramaMap[0]
    la = Lepcha.ConsonantMap[27]

    conLa = [x+vir+la for x in [Lepcha.ConsonantMap[c] for c in [0,2,20,22,24,32]]+[Lepcha.NuktaConsonantMap[6]]]
    conL = ['\u1C01','\u1C04','\u1C0F','\u1C14','\u1C16','\u1C1E','\u1C12']

    for x,y in zip(conLa,conL):
        if not reverse:
            # Replace k + vira + la -> kla
            Strng = Strng.replace(x,y)
        else:
            # Reverse above
            Strng = Strng.replace(y,x)

    yr = [vir+x for x in Lepcha.ConsonantMap[25:27]]
    yrSub = ['\u1C24','\u1C25']

    for x,y in zip(yr,yrSub):
        if not reverse:
            # sbjoined ya and ra
            Strng = Strng.replace(x,y)
        else:
            # reverse above
            Strng = Strng.replace(y,x)

    ## Word Final Consonants

    ## Consider adding -u instead of mass replacement [for Cham too] !

    listNF = [Lepcha.ConsonantMap[x] for x in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,21,22,23,29,30,31]]
    listF = [(Lepcha.ConsonantMap+Lepcha.AyogavahaMap)[x] for x in [0,0,0,34,0,0,0,0,19,15,15,15,15,19,15,15,15,20,20,20,15,15,15]]

    listNF += Lepcha.ConsonantMap[25:26]+Lepcha.ConsonantMap[28:29]
    listF += Lepcha.VowelMap[2:3] + Lepcha.VowelMap[4:5]

    if not reverse:
        # Remove Nukta if it appears with Virama
        # ka + Q + Viramam -> ka + virama
        Strng = Strng.replace(Lepcha.NuktaMap[0]+vir,vir)
        Strng = Strng.replace(Lepcha.ConsonantMap[32]+vir,'') # Remove <h> ; sihma -> sima
        consAll = "(" + "|".join(Lepcha.ConsonantMap + Lepcha.VowelMap + Lepcha.VowelSignMap) + ")"
        for x,y in zip(listNF,listF):
            Strng = re.sub(consAll+"(" + x+vir + ")",r'\1'+y+vir,Strng)


    else:
        pass # Irreversible

    conFinal = [x+vir for x in [Lepcha.ConsonantMap[c] for c in [0,15,19,20,24,26,27]]]
    conF = ['\u1C2D','\u1C33','\u1C30','\u1C31','\u1C2E','\u1C32','\u1C2F',]

    signAll = '|'.join(GM.CrunchSymbols(GM.Consonants+GM.Vowels+GM.VowelSignsNV, "Lepcha"))

    for x,y in zip(conFinal,conF):
        if not reverse:
            # Replace final consonants
            Strng = re.sub('('+signAll+')'+'('+x+')',r'\1'+y,Strng)
        else:
            Strng = Strng.replace(y,x)

    # Remove Virama - Lepcha doesn't have virama ?

    signVow = '|'.join(GM.CrunchSymbols(GM.VowelSignsNV,"Lepcha"))

    if not reverse:
        Strng = Strng.replace(vir,'') ## Removing faux Virama
        # Using Sign Kang with Vowel Signs
        # Inherent Consonant uses 1C34
        # kiM -> ki + 1C35 ; kaM -> ka + 1C34
        Strng = re.sub("("+signVow+')'+'('+Lepcha.AyogavahaMap[1]+')',r'\1'+'\u1C35',Strng)
        Strng = Strng.replace("ᰧᰶᰵ", "ᰧᰵᰶ") ## Fiximg IM issues kIM swap the Ran and M to display it better
    else:
        Strng = Strng.replace('\u1C35',Lepcha.AyogavahaMap[1])
        Strng = Strng.replace("ᰧᰵᰶ","ᰧᰶᰵ") ## Fiximg IM issues kIM swap the Ran and M to display it better

    return Strng

# Repha & Subjoined
def FixSundanese(Strng,reverse=False):
    vir = Sundanese.ViramaMap[0]

    r = Sundanese.ConsonantMap[26] + vir
    ListC = '|'.join(GM.CrunchSymbols(GM.Consonants + GM.Vowels + GM.VowelSignsNV,'Sundanese'))
    #print(ListC)


    if not reverse:
        # Sundanese Repha
        Strng = re.sub('(' + ListC + ')' + r, r'\1' + '\u1B81', Strng)
    else:
        # Reverse above
        Strng = Strng.replace('\u1B81',r)
        Strng = PostProcess.SundaneseHistoricConjuncts(Strng, reverse)

    yrl = [vir+x for x in Sundanese.ConsonantMap[25:28]]
    yrlSub = ['\u1BA1','\u1BA2','\u1BA3']

    for x,y in zip(yrl,yrlSub):
        if not reverse:
            # Subjoined consonants
            Strng = Strng.replace(x,y)
        else:
            # Reverse above
            Strng = Strng.replace(y,x)

    return Strng

# Repha & Subjoined
def FixRejang(Strng,reverse=False):
    vir = Rejang.ViramaMap[0]

    r = Rejang.ConsonantMap[26] + vir
    n = Rejang.ConsonantMap[19] + vir
    ListC = '|'.join(GM.CrunchSymbols(GM.Consonants + GM.Vowels + GM.VowelSignsNV,'Rejang'))

    if not reverse:
        # Sundanese Repha
        Strng = re.sub('(' + ListC + ')' + r, r'\1' + '\uA951', Strng)
        Strng = re.sub('(' + ListC + ')' + n, r'\1' + '\uA950', Strng)
    else:
        # Reverse above
        Strng = Strng.replace('\uA951',r)
        Strng = Strng.replace('\uA950',n)

    return Strng

# Chakmaa VS A and Subjoined
def FixChakma(Strng,reverse=False):
    listC = '('+"|".join(sorted(GM.CrunchSymbols(GM.Consonants,"Chakma")+Chakma.VowelMap[:1],key=len,reverse=True))+')'
    listV = '('+"|".join(sorted(GM.CrunchSymbols(GM.VowelSigns,"Chakma")+Chakma.ViramaMap+['\U00011133'],key=len,reverse=True))+')'

    Strng = Strng.replace("\u02BD","")

    if not reverse:
        # Introduce vowel Sign A ; Chakma - Inharant vowel is AA
        Strng = re.sub("("+listC+")"+"(?!"+listV+")",r'\1''\u02BE',Strng)
        Strng = Strng.replace("\U00011127","")
        Strng = Strng.replace("\u02BE","\U00011127")
    else:
        Strng = Strng.replace("\U00011127","\u02BE")
        Strng = re.sub("("+listC+")"+"(?!"+listV+'|\u02BE'+")",r'\1''\U00011127',Strng)
        Strng = Strng.replace("\u02BE","")

    yrlvn = "("+"|".join(Chakma.ConsonantMap[19:20]+Chakma.ConsonantMap[25:29])+")"

    if not reverse:
        # Subjoined consonants
        # Usual convention
        Strng = re.sub("\U00011134"+"(?="+yrlvn+")","\U00011133",Strng)
    else:
        # Reverse above
        Strng = Strng.replace("\U00011133","\U00011134")

    ###  O/Sub-va lookign similar; check

    ###  Unique Independent vowels etc

    return Strng

def FixIAST(Strng,reverse=False):
    if reverse:
        Strng = Strng.replace("ṁ",IAST.AyogavahaMap[1])
        # ^ Some IAST publications use /ṁ/ instead of /m dot below/

    return Strng

def FixIPA(Strng,reverse=False):
    colon_tilde = "\u02D0\u0303"
    tilde_colon = "\u0303\u02D0"

    if not reverse:
        # ɑː̃ -> ɑ̃ː
        Strng = Strng.replace(colon_tilde,tilde_colon)
        # Add Visarga echo - kuH/kUH -> kuhŭ/kuːhŭ
        Strng = re.sub("(.)(\u02D0?)(\u0068)",r'\1\2\3\1'+'\u0306',Strng)
    else:
        # ɑː̃ <- ɑ̃ː
        Strng = Strng.replace(tilde_colon,colon_tilde)
        # Reverse Visarga echo - kuH/kUH <- kuhŭ/kuːhŭ
        Strng = re.sub("(.)(\u02D0?)(\u0068)"+r"\1"+"\u0306",r"\1\2\3",Strng)

    return Strng

# Rearrange PhagsPa Letters ; Subjoined Letters ;
def FixPhagsPa(Strng,reverse=False):
    candraBindu = PhagsPa.AyogavahaMap[0]
    ListC = "|".join(sorted(PhagsPa.ConsonantMap,key=len,reverse=True)) #Do this for all
    ListV = "|".join(sorted(PhagsPa.VowelMap,key=len,reverse=True))
    ListVS = "|".join(sorted(PhagsPa.VowelSignMap,key=len,reverse=True))

    vir  = PhagsPa.ViramaMap[0]
    Virrvy = [vir+x for x in [PhagsPa.ConsonantMap[c] for c in [25,26,28]]]
    Subrvy = ['\uA868','\uA871','\uA867']

    SubrvyE = ['ꡱꡨ'] + Subrvy


    if not reverse:
        # Removing Indep. Vowel Sign
        #ListV = ListV.replace("\u1E7F","")
        #Strng = Strng.replace("\u1E7F","")

        for x,y in zip(Virrvy,Subrvy):
            Strng = Strng.replace(x,y)

        Strng = re.sub("("+ListV+")"+"("+candraBindu+")",r'\2\1',Strng)

        # Move Chandrabindu - bhrUM
        Strng = re.sub("("+ListC+")"+"(("+"|".join(SubrvyE)+")?)"+"(("+ListVS+")?)"+"("+candraBindu+")",r'\6\1\2\4',Strng)
        # Move Sigh Candrabindu

        # Move Vowel Sign AA for subjoining vowels ## Not moving
       #  Strng = re.sub("(["+"".join(Subrvy[1])+"])"+"("+PhagsPa.VowelSignMap[0]+")",r'\2\1',Strng)

    else:
        ListV = ListV.replace("\u1E7F","")

        Strng = Strng.replace('ꡖꡘꡟ','ꡱꡖꡟ')

        Aspirate = [('\uA842\uA85C','\u1E7E\uA842\u1E7E\uA85C\u1E7E'), ('\uA852\uA85C','\u1E7E\uA852\u1E7E\uA85C\u1E7E'), ('\uA86B\uA85C','\u1E7E\uA86B\u1E7E\uA85C\u1E7E'),
            ('\uA84A\uA85C','\u1E7E\uA84A\u1E7E\uA85C\u1E7E'),('\uA84E\uA85C','\u1E7E\uA84E\u1E7E\uA85C\u1E7E')]

        for x,y in Aspirate:
            Strng = Strng.replace(x,y)

        Strng = re.sub("("+PhagsPa.VowelSignMap[0]+")"+"(["+"".join(Subrvy[1])+"])",r'\2\1',Strng)
        Strng = re.sub("("+candraBindu+')'+"("+ListC+')'+"(("+"|".join(SubrvyE)+")?)"+"(("+ListVS+')?)',r'\2\3\5\1',Strng)
        Strng = re.sub("("+candraBindu+')'+'('+ListV+')',r'\2\1',Strng)

        for x,y in zip(Virrvy,Subrvy):
            Strng = Strng.replace(y,x)

        # Fixing  + Indepdendent vowels.
        Strng = re.sub("("+ListV+")","\u1E7F"r"\1",Strng)
        Strng = re.sub("("+ListC+"|ꡖ)"+"("+"\u1E7F"+")",r'\1',Strng)

    ## Fix rka - superfixed ra ; rka used only for Specific Tibetan context.
    if not reverse:
        Strng = Strng.replace(" ", "᠂")
        Strng = Strng.replace("\u02BD","")

        ## separate syllables

        #Strng = re.sub("(?<!ꡖ)" + "(" + "(" + ListV +")" + ")" + "(?!" + ListCVir + ")", r'\1' + ' ', Strng)
        #Strng = re.sub("(" + "(" + ListC +")" + "(" + "|".join(Subrvy) + ")?" + "(" + ListVS + ")" + ")" + "(?!" + ListCVir + ")", r'\1' + ' ', Strng)
        #Strng = Strng.replace("")
        #Strng = re.sub("(" + "(" + ListC +")" + "(" + "|".join(Subrvy) + ")?" + "(?!" + ListCVir + ")" + ")", r'\1' + ' ', Strng)

        ## sakv sakr not changing properly
        Strng = re.sub("(("+candraBindu+")?"+"("+ListC+")"+"(("+"|".join(SubrvyE)+")?)"+"(("+ListVS+")?))" +
            "(("+candraBindu+")?"+"("+ListC+")"+"(("+"|".join(SubrvyE)+")?)"+"(("+ListVS+")?))" + "(?!" + vir + ")", r'\1 \8', Strng)
        Strng = re.sub("(("+candraBindu+")?"+"("+ListC+")"+"(("+"|".join(SubrvyE)+")?)"+"(("+ListVS+")?))" +
            "(("+candraBindu+")?"+"("+ListC+")"+"(("+"|".join(SubrvyE)+")?)"+"(("+ListVS+")?))" + "(?!" + vir + ")", r'\1 \8', Strng)

        Strng = re.sub("(("+candraBindu+")?"+"("+ListV+"))" +
            "(("+candraBindu+")?"+"("+ListC+")"+"(("+"|".join(SubrvyE)+")?)"+"(("+ListVS+")?))" + "(?!" + vir + ")", r'\1 \4', Strng)
        Strng = re.sub("(("+candraBindu+")?"+"("+ListV+"))" +
            "(("+candraBindu+")?"+"("+ListC+")"+"(("+"|".join(SubrvyE)+")?)"+"(("+ListVS+")?))" + "(?!" + vir + ")", r'\1 \4', Strng)

        Strng = re.sub("(("+candraBindu+")?"+"("+ListC+")"+"(("+"|".join(SubrvyE)+")?)"+"(("+ListVS+")?))" +
            "(("+candraBindu+")?"+"("+ListV+"))" + "(?!" + vir + ")", r'\1 \8', Strng)
        Strng = re.sub("(("+candraBindu+")?"+"("+ListC+")"+"(("+"|".join(SubrvyE)+")?)"+"(("+ListVS+")?))" +
            "(("+candraBindu+")?"+"("+ListV+"))" + "(?!" + vir + ")", r'\1 \8', Strng)

        Strng = re.sub("(("+candraBindu+")?"+"("+ListV+"))" + "(?!" + vir + ")" +
            "(("+candraBindu+")?"+"("+ListV+"))" + "(?!" + vir + ")", r'\1 \4', Strng)
        Strng = re.sub("(("+candraBindu+")?"+"("+ListV+"))" + "(?!" + vir + ")" +
            "(("+candraBindu+")?"+"("+ListV+"))" + "(?!" + vir + ")", r'\1 \4', Strng)

        Strng = Strng.replace("\n","\n")

        #Strng = "(" + "(" + ListC +")" + "(" + "|".join(Subrvy) + ")?" + "(" + ListVS + ")" + ")" + "(?!" + ListCVir + ")"

        Strng = '\u12BA᠂' + Strng

        ListCE = ListC + "|" + "|".join(SubrvyE)

        ## Probably add more punctuations
        Strng = re.sub('(?:(?<!\n)(?<!᠂)(?<![,\.\"\?\&\(\)]))' + "(?<!" + vir + ")" + '(' + ListC + ')' + vir + "((" + candraBindu +")?" + "("+ListC+"))",r"\1 \2", Strng) #\u02BF Virama
        Strng = re.sub('(?<!᠂)' + '(' + ListC + ')' + vir + "((" + candraBindu +")?" + "("+ListV+"))",r" \1", Strng) #\u02BF Virama

        Strng = Strng.replace(vir,"") #\u02BF Virama
        Strng = Strng.replace("\u1E7F","")
        Strng = Strng.replace("\u1E7E","")
        Strng = Strng.replace("\u12BA᠂","")

        Strng = Strng.replace("᠂", " ᠂ ")


        #print Strng
    else:
        Strng = Strng.replace("ꡆ","ꡒ")

        for x,y in zip(Virrvy,Subrvy):
            Strng = Strng.replace(x,y)

        #print(Strng)

        ## Fix splavya
        Strng = re.sub("((" + ListC + ")" + "(("+"|".join(SubrvyE)+")?)" + "(?!" + ListVS + "))"
            + "((("+ListC+")"+"(("+"|".join(SubrvyE)+")?)"+"(("+ListVS+"))" + "("+candraBindu+")?))"  , r"\1" + vir + r"\6", Strng)


        Strng = re.sub("((("+ListC+")"+"(("+"|".join(SubrvyE)+")?)"+"(("+ListVS+")?)" + "("+candraBindu+")?)"
            + "((" + ListC + ")" + "(("+"|".join(SubrvyE)+")?)" + "(?!" + ListVS + ")))" , r"\1" + vir, Strng)

        Strng = re.sub("((("+ListV+")" + "("+candraBindu+")?)"
            + "((" + ListC + ")" + "(("+"|".join(SubrvyE)+")?)" + "(?!" + ListVS + ")))" , r"\1" + vir, Strng)

        for x,y in zip(Virrvy,Subrvy):
            Strng = Strng.replace(y,x)

        Strng = Strng.replace(" ", "")
        Strng = Strng.replace("᠂"," ")
        Strng = Strng.replace("᠃"," ")

        Strng = Strng.replace(vir + vir, vir)

        # ꡳꡊꡞꡚ ꡩꡖ ꡗ ---> diMSTAya
        # Fix Aspirated add the extra character
        # Fix saphA -> sphA ; sata -> sat ; suda -> sud
        # Add options to retain space
        #Strng = Strng.replace("(" + ListC + ")")


    return Strng

# Meetei Mayek Final
# Think of a-k-ka vers a-ka+vir-ka, also ag to ak. (Virama extends to second letter... ag could be replaced by ak..
# since a+ga+vir woould orthographically wrong (it has no following consonant to extend to), considered replacing a+g+virama with a+k

def FixMalayalam(Strng, reverse=False):
    Strng = PostProcess.MalayalamChillu(Strng, reverse)
    if not reverse:
        Strng = PostProcess.RetainDandasIndic(Strng, 'Malayalam', True)
        Strng = PostProcess.RetainIndicNumerals(Strng, 'Malayalam', True)

    Chillus=['\u0D7A','\u0D7B','\u0D7C','\u0D7D','\u0D7E', 'ഩ‍്']

    Anu = GM.CrunchSymbols(GM.CombiningSigns,'Malayalam')[1]

    return Strng

def FixTelugu(Strng, reverse=False):
    if not reverse:
        Strng = PostProcess.RetainDandasIndic(Strng, 'Telugu', True)
        Strng = PostProcess.RetainIndicNumerals(Strng, 'Telugu', True)

    return Strng

def FixMeeteiMayek(Strng,reverse=False):
    vir = MeeteiMayek.ViramaMap[0]
    listC = [x+vir for x in [MeeteiMayek.ConsonantMap[x] for x in [0,27,24,20,19,15,4,25]]]
    finalC = ['\uABDB','\uABDC','\uABDD','\uABDE','\uABDF','\uABE0','\uABE1','\uABE2']

    for x,y in zip(listC,finalC):
        if not reverse:
            Strng = re.sub(x,y,Strng)
        else:
            Strng = Strng.replace(y, x)

    return Strng

## Reverse not working
## For other batak writings as well

## Consider replacement of Anusvara by Nasal for East Asian Sripts which don't ahve a Sanskrit writing Tradition

def FixBatakSima(Strng, reverse= False):
    if not reverse:
        Strng = Strng.replace('ᯙᯮ', 'ᯙᯯ')
    else:
        Strng = Strng.replace('ᯙᯯ', 'ᯙᯮ')

    return Strng

# Cham Final & Subjoined
def FixCham(Strng,reverse=False):
    Strng = Strng.replace("\u02BD","")

    ## Check Differences between Vietnamese Cham & Cambodian Cham

    ListCAll = '('+'|'.join(GM.CrunchSymbols(GM.Consonants,'Cham')) + ')'
    ListVow = '('+'|'.join(GM.CrunchSymbols(GM.Vowels,'Cham')) + ')'
    ListVowS = '('+'|'.join(GM.CrunchSymbols(GM.VowelSignsNV,'Cham')) + ')'

    ## http://www.youtube.com/watch?v=z2_8GMqbO6M - Prenasalized Consonants
    vir = Cham.ViramaMap[0]
    nja = Cham.ConsonantMap[9] + vir + Cham.ConsonantMap[7]

#    if not reverse:
#        Strng = Strng.replace(nja,u'\uAA12')
#    else:
#        Strng = Strng.replace(u'\uAA12',nja)

    ## Replace Mue with ma, nue with na ???  - Should it be done ???

    ## Subjoined Consonants

    listC = [vir+x for x in Cham.ConsonantMap[25:29]]
    SubC = ['\uAA33','\uAA34','\uAA35','\uAA36'] # Subjoined - /ya/, /ra/, /la/, /va/
    for x,y in zip(listC,SubC):
        if not reverse:
            # Subjoined consonants
            Strng = Strng.replace(x,y)
        else:
            # Reverse above
            Strng = Strng.replace(y,x)

    # Replace Consonants without Final forms to Consonts with Final Forms
    # vagh -> vag, prajJa -> pracJA etc

    listNF = [Cham.ConsonantMap[x] for x in [1,3,6,7,8,9,16,17,18,21,22,23,31,29]]  # Non Final
    listF = [Cham.ConsonantMap[x] for x in [0,2,5,5,5,19,15,15,15,20,20,20,30,30]]  # Final

    for x,y in zip(listNF,listF):
        if not reverse:
            Strng = Strng.replace(x+vir,y+vir)
        else:
            pass # Irreversible

    ## Fix Hma Hla - Word Initial
    ## hma  ꩍꨠ -> Becomes ःम

    ## Consonnant h

    listC = [x+vir for x in [Cham.ConsonantMap[x] for x in [0,2,4,5,15,19,20,25,26,27,30,24]]]
    finalC = ['\uAA40','\uAA41','\uAA42','\uAA44','\uAA45','\uAA46','\uAA47','\uAA48','\uAA49','\uAA4A','\uAA4B','\uAA4C']

    for x,y in zip(listC,finalC):
        # final consonants
        if not reverse:
            Strng = Strng.replace(x,y)
            Strng = re.sub('(' + ListCAll + '|' +  ListVow + '|' +  ListVowS + ')' + 'ꨨ' + vir, r'\1'+'ꩍ', Strng)

        else:
            Strng = Strng.replace('ꩍ','ꨨ' + vir)
            if y not in Cham.AyogavahaMap:
                Strng = Strng.replace(y,x)

    # Remove faux Virama:
    va = Cham.ConsonantMap[28]
    if not reverse:
        Strng = Strng.replace(va+vir,va)
        #Strng = Strng.replace('ʾ', '')
    else:
        pass # Irreversible

    return Strng

# Subjoined Consonants in Tai Tham
# Mai Kang Lai - /ng/
def FixTaiTham(Strng,reverse=False):
    vir = TaiTham.ViramaMap[0]
    Cons = [vir+x for x in [TaiTham.ConsonantMap[x] for x in [26,27]]] # /ra/ and /la/
    Sub =['\u1A55','\u1A56'] # Subjoined Forms of /ra/ and /la/

    ListC ='|'.join(GM.CrunchSymbols(GM.Consonants,'TaiTham'))
    E = "ᩮ"

    TallACons = '|'.join(['ᩅ']) ## Just va
    AA = 'ᩣ'

    # Ra/La + vira -> Subjoined
    for x,y in zip(Cons,Sub):
        if not reverse:
            Strng = Strng.replace(x,y)
        else:
            Strng = Strng.replace(y,x)

    if not reverse:
        Strng = Strng.replace("\u1A63\u1A74","\u1A74\u1A63") # kAM -> kMA (Like Thai ำ )
        # Check above in Pali texts

    else:
        Strng = Strng.replace("\u1A74\u1A63","\u1A63\u1A74") # kAM <- kMA

    ListC ='|'.join(GM.CrunchSymbols(GM.Consonants,'TaiTham'))
    ng = TaiTham.ConsonantMap[4]+vir

    if not reverse:
        # Mai Kang Lai
        Strng = re.sub('('+ng+')'+'('+ListC+')','\u1A58'+r'\2',Strng)
        # Subjoining Virama
        Strng = re.sub(vir+'('+ListC+')','\u1A60'+r'\1',Strng)
        # Great Sa
        Strng = Strng.replace('ᩈ᩠ᩈ','ᩔ')

        # Introduce Tall A: ka + AA -> ka + Tall A
        Strng = re.sub('(?<!᩠)('+TallACons+')'+'('+E+'?)'+AA,r'\1\2'+'ᩤ',Strng)
        ## buddho --> Tall A
        Strng = re.sub('('+TallACons+')(᩠)('+ListC +')'+'('+E+'?)'+AA,r'\1\2\3\4'+'ᩤ',Strng)
        Strng = re.sub('('+TallACons+')(᩠)('+ListC +')'+'(᩠)('+ListC +')'+'('+E+'?)'+AA,r'\1\2\3\4\5\6'+'ᩤ',Strng)

        ### Subjoined
        Strng = re.sub('('+TallACons+')' + "(" + "|".join(Sub) + ")" + '('+E+'?)'+AA, r'\1\2\3' + 'ᩤ', Strng)

        Strng = Strng.replace('ᩅ᩠ᨿᩤ','ᩅ᩠ᨿᩣ') ## vyA (Tall) to vyA (normal)

    else:
        Strng = Strng.replace('ᩔ', 'ᩈ᩠ᩈ') ## Reverse great sa
        Strng = re.sub('('+ListC+')'+'\u1A58',r'\1' + ng,Strng) # Reverse: Kai mang Lai -> ng + virama
        Strng = Strng.replace('\u1A60',vir) # Regular Virama for Transliteration
        Strng = Strng.replace("ᩤ", AA) # Reverse Tall A

    return Strng

# Transcription for Native Lao
def LaoTranscribe(Strng,reverse=False):
    import PostProcess as pp
    shortA, conjA = '\u0EB0', '\u0EB1'

    if not reverse:
        Strng = pp.ThaiLaoTranscription(Strng,"Lao",shortA,conjA)
    else:
        Strng = pp.ThaiLaoTranscription(Strng,"Lao",shortA, conjA,reverse=True)

    return Strng

# Transcription for Pali Lao
def LaoPaliTranscribe(Strng,reverse=False):
    import PostProcess as pp
    shortA, conjA = '\u0EB0', '\u0EB1'

    if not reverse:
        Strng = pp.ThaiLaoTranscription(Strng,"LaoPali",shortA,conjA)
    else:
        Strng = pp.ThaiLaoTranscription(Strng,"LaoPali",shortA, conjA,reverse=True)

    return Strng

# Assamese and Bengali have the same mapping file duplicated
# Replace Bengali /ra/ with Assamese /ra/
def FixBengali(Strng, reverse=False):
    Strng = PostProcess.KhandaTa(Strng, 'Bengali', reverse)

    return Strng

def FixAssamese(Strng,reverse=False):
    Ra = "\u09B0"
    AssRa = "\u09F0"

    Strng = PostProcess.KhandaTa(Strng, 'Assamese', reverse)

    if not reverse:
        Strng = Strng.replace(Ra,AssRa)
    else:
        Strng = Strng.replace(AssRa,Ra)

    return Strng

def FixKannada(Strng,reverse=False):
    if not reverse:
        Strng = PostProcess.RetainDandasIndic(Strng, 'Kannada', True)
        Strng = PostProcess.RetainIndicNumerals(Strng, 'Kannada', True)

    return Strng

def FixGrantha(Strng, reverse=False):
    if not reverse:
        Strng = Strng.replace('॑', '᳴')
        Strng = Strng.replace('᳚', '॑')
    else:
        Strng = Strng.replace('॑', '᳚')
        Strng = Strng.replace('᳴', '॑')

    return Strng

def FixMahajani(Strng, reverse=False):
    if not reverse:
        #print(Strng)
        Strng = Strng.replace('𑅰𑅳ʾ𑅭ʿ𑅑', '\U00011176')
        Strng = Strng.replace('\u02BE','').replace('\u02BF','')
    else:
        Strng = Strng.replace('\U00011176', '𑅰𑅳ʾ𑅭ʿ𑅑')

    return Strng

def FixAhom(Strng, reverse = False):
    ListVS = '(' + '|'.join(GM.CrunchSymbols(GM.VowelSignsNV, 'Ahom')) + ')'
    Anu = '('+ GM.CrunchList('AyogavahaMap', 'Ahom')[1] + ')'

    if not reverse:
        Strng = Strng.replace('\U0001172B\U0001170D', '\U0001171E')
        Strng = Strng.replace('\U0001172B\U0001170E', '\U0001171D')

        Strng = re.sub(ListVS + Anu, r'\2\1', Strng)
        Strng = re.sub(Anu + '(𑜦)', r'\2\1', Strng)

    else:
        Strng = Strng.replace('\U0001171E', '\U0001172B\U0001170D')
        Strng = Strng.replace('\U0001171D', '\U0001172B\U0001170E')

        Strng = re.sub(Anu + ListVS, r'\2\1', Strng)

    return Strng

def FixMultani(Strng, reverse = False):
    if not reverse:
        Strng = Strng.replace('\u02BE','').replace('\u02BF','')
        Strng = Strng.replace('ˍ\U0001128C', '\U0001128D').replace('ˍ\U00011282','\U00011293') ## Plosives

    else:
        Strng = Strng.replace('\U0001128D','ˍ\U0001128C').replace('\U00011293','ˍ\U00011292') ## Plsosives

    return Strng


def FixGujarati(Strng,reverse=False):
    if not reverse:
        Strng = PostProcess.RetainDandasIndic(Strng, 'Gujarati', True)
        Strng = Strng.replace('જ઼઼', 'ૹ')
    else:
        pass
        Strng = Strng.replace('ૹ', 'જ઼઼')

    return Strng

def FixZanabazarSquare(Strng, reverse=False):
    ListC ='|'.join(GM.CrunchSymbols(GM.Consonants,'ZanabazarSquare'))
    yrlv = ZanabazarSquare.ConsonantMap[25:29]
    yrlv_sub = ['\U00011A3B', '\U00011A3C', '\U00011A3D', '\U00011A3E']

    vir = ZanabazarSquare.ViramaMap[0]

    if not reverse:
        Strng = re.sub(vir+'('+ListC+')','\U00011A47'+r'\1',Strng)
        # KSSA
        Strng = Strng.replace('𑨋𑩇𑨯','𑨲')
    else:
        # subjoining contextual y/r/l/v
        for x, y in zip(yrlv, yrlv_sub):
            Strng = Strng.replace(y, '\U00011A47' + x)

        # Repha
        Strng = Strng.replace('\U00011A3A', yrlv[1] + '\U00011A47')

        # KSSA
        Strng = Strng.replace('𑨲', '𑨋𑩇𑨯')

        # Alternate ai/au
        Strng = Strng.replace('\U00011A07', '\U00011A04\U00011A0A')
        Strng = Strng.replace('\U00011A08', '\U00011A06\U00011A0A')

        # Mongolian final -> Virama
        Strng = Strng.replace('\U00011A33', vir)

        # Subojin to Normal vir
        Strng = Strng.replace('\U00011A47', vir)

    return Strng

def FixKhojki(Strng, reverse=False):
    sindhi = ['\U0001120B', '\U00011211', '\U0001121C', '\U00011222']
    sindhiapprox = ['ˍ\U0001120A', 'ˍ\U00011210', 'ˍ\U00011216', 'ˍ\U00011221']

    if not reverse:
        for x, y in zip(sindhi, sindhiapprox):
            Strng = Strng.replace(y, x)
        Strng = PostProcess.InsertGeminationSign(Strng, 'Khojki')
        # Move Shadda after consonant
        Strng = re.sub('(\U00011237)(.)', r'\2\1', Strng)
        # Reverse : Shadda + Nukta
        Strng = Strng.replace('𑈷𑈶', '𑈶𑈷')
        #Strng = re.sub('(' + GM.Germination['Khojki'] + ')', r'\2', Strng)
        # WordSeparatror
        Strng = Strng.replace(' ', '\U0001123A')
    else:
        # Reverse Word Separator
        Strng = Strng.replace('\U0001123A', ' ')

        for x, y in zip(sindhi, sindhiapprox):
            Strng = Strng.replace(x, y)
        # Reverse : Nukta + Shadda
        Strng = Strng.replace('𑈶𑈷', '𑈷𑈶')
        # Move Shadda before consonant
        Strng = re.sub('(.)(\U00011237)', r'\2\1', Strng)
        Strng = PostProcess.ReverseGeminationSign(Strng, 'Khojki')

    return Strng

def FixNewa(Strng, reverse=False):
    if not reverse:
        ListC ='|'.join(GM.CrunchSymbols(GM.Consonants,'Newa'))
        ra = Newa.ConsonantMap[26]
        vir = Newa.ViramaMap[0]
        Strng = re.sub(ra + vir + '(' + ListC + ')', ra + vir + '\u200D' + r'\1', Strng)
    else:
        pass

    return Strng