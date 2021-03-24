# -*- coding: utf-8 -*-
from . import GeneralMap as GM
from aksharamukha.ScriptMap.Roman import Avestan, IAST
from aksharamukha.ScriptMap.MainIndic import Ahom, Tamil,TamilGrantha, Limbu, MeeteiMayek, Urdu, Lepcha, Chakma, Kannada, Gurmukhi, Newa
from aksharamukha.ScriptMap.EastIndic import Lao, TaiTham,Tibetan,Burmese,Khmer,Balinese,Javanese,Thai, Sundanese, PhagsPa, Cham, Thaana, Rejang, ZanabazarSquare
from . import PostProcess
import re

## Test Syllable initial conjunct

## ListC check.. if LLA is there in ListC... just now it has only Consonant Map
### Rewrite all ListC, ListV as sorted(List,key=len,reverse=True)

def OriyaIPAFixPre(Strng):
    Strng = Strng.replace('ଂ', 'ଙ୍')
    Strng = Strng.replace('ଃ', 'ହ୍')

    return Strng

def SinhalaIPAFix(Strng):
    consonants = '(' + '|'.join(GM.CrunchSymbols(GM.Consonants, 'IPA')) + ')'

    Strng = re.sub('^' + consonants + '(ə)', r'\1ʌ', Strng)
    Strng = re.sub('(\s)' + consonants + '(ə)', r'\1\2ʌ', Strng)

    Strng = re.sub('^' + consonants + consonants +'(ə)', r'\1ʌ', Strng)
    Strng = re.sub('(\s)' + consonants + consonants +'(ə)', r'\1\2ʌ', Strng)

    Strng = re.sub('^' + consonants + consonants + consonants +'(ə)', r'\1ʌ', Strng)
    Strng = re.sub('(\s)' + consonants + consonants + consonants +'(ə)', r'\1\2ʌ', Strng)


    return Strng

def OriyaIPAFix(Strng):
    Strng = Strng.replace('ə', 'ɔ')
    Strng = Strng.replace('j', 'd͡ʒ')
    Strng = Strng.replace('\u1E8F', 'j')
    Strng = Strng.replace('kʂ', 'kʰ')
    Strng = Strng.replace('ʂ', 's̪')
    Strng = Strng.replace('ʃ', 's̪')
    Strng = Strng.replace('ʋ', 'u̯')

    Strng = Strng.replace('t͡s', 't͡ʃ')

    Strng = Strng.replace('ɪ', 'i')
    Strng = Strng.replace('iː', 'i')
    Strng = Strng.replace('uː', 'u')
    Strng = Strng.replace('eː', 'e')
    Strng = Strng.replace('oː', 'o')
    Strng = Strng.replace('ɾɨ', 'ɾu')
    Strng = Strng.replace('ɾɨː', 'ɾu')
    Strng = Strng.replace('lɨ', 'lu')
    Strng = Strng.replace('lɨː', 'lu')

    return Strng

def VedicSvarasLatinIndic(Strng, Source):
    ## Vedic Svaras
    Strng = Strng.replace('{\\m+}', 'ꣳ')
    Strng = Strng.replace('\\m++', 'ꣴ')
    Strng = Strng.replace('\\m+', 'ꣳ')

    Strng = Strng.replace('\\`', '\\_') ## Alternate form of Anudatta
    Strng = Strng.replace('\\\'\'', '\\"') ## Alternate form of Dirdha udatta

    Ayogavaha = GM.CrunchList('AyogavahaMap', Source)
    Svaras = ['\\_', '\\"', '\\\'']

    ## Svap the order of Svara + Ayogavaha -> Ayogaaha + Svara
    ## Indic syllable boundaries
    for x in Ayogavaha:
        for y in Svaras:
            Strng = Strng.replace(y + x, x + y)

    ### Introduce Vedic Svaras
    Strng = Strng.replace('\\"', '᳚')
    Strng = Strng.replace('\\\'', '॑')
    Strng = Strng.replace('\\_', '॒')

    return Strng

def VedicSvarsIndicLatin(Strng):
    Strng = Strng.replace('᳚', '\\"')
    Strng = Strng.replace('॑', '\\\'')
    Strng = Strng.replace('॒', '\\_')
    Strng = Strng.replace('ꣳ', '\\m+')
    Strng = Strng.replace('ꣴ', '\\m++')

    return Strng

def VedicSvarasOthers(Strng, Target):
    Strng = Strng.replace('\\"','↑↑').replace("\\_", '↓').replace("\\\'",'↑')
    anu = GM.CrunchList('AyogavahaMap', Target)[1]
    Strng = Strng.replace('\\m++', 'ꣴ')
    Strng = Strng.replace('\\m+', 'ꣳ')

    Ayogavaha = GM.CrunchList('AyogavahaMap', Target)

    return Strng

def VedicSvarasDiacrtics(Strng, Target):
    Strng = Strng.replace('\\\'', '̍')
    Strng = Strng.replace('\\"', '̎')
    Strng = Strng.replace('\\_', '̱')
    Strng = Strng.replace('\\m++', 'gͫ̄')
    Strng = Strng.replace('\\m+', 'gͫ')

    if (Target == 'ISO'):
        Strng = Strng.replace('\\’’', '̎')
        Strng = Strng.replace('\\’', '̍')


    Ayogavaha = GM.CrunchList('AyogavahaMap', Target)
    Svaras = ['̍', '̎', '̱']

    ## Svap the order of Svara + Ayogavaha -> Ayogaaha + Svara
    ## Indic syllable boundaries
    for x in Ayogavaha:
        for y in Svaras:
            Strng = Strng.replace(x + y, y + x)

    return Strng

def VedicSvarasCyrillic(Strng, Target):
    Strng = Strng.replace('\\\'', '̍')
    Strng = Strng.replace('\\"', '̎')
    Strng = Strng.replace('\\_', '̱')
    Strng = Strng.replace('\\м++', 'г\u0361м')
    Strng = Strng.replace('\\м+', 'г\u035Cм')
    Strng = Strng.replace('\\m++', 'г\u0361м')
    Strng = Strng.replace('\\m+', 'г\u035Cм')
    Ayogavaha = GM.CrunchList('AyogavahaMap', Target)
    Svaras = ['̍', '̎', '̱']

    ## Svap the order of Svara + Ayogavaha -> Ayogaaha + Svara
    ## Indic syllable boundaries
    for x in Ayogavaha:
        for y in Svaras:
            Strng = Strng.replace(x + y, y + x)

    return Strng

def VedicSvarasNonDiacritic(Strng):
    Strng = Strng.replace('̍', '\\\'')
    Strng = Strng.replace('̎', '\\"')
    Strng = Strng.replace('̱', '\\_')
    Strng = Strng.replace('gͫ̄', '\\m++')
    Strng = Strng.replace('gͫ', '\\m+')

    Strng = Strng.replace('г\u0361м', '\\m++')
    Strng = Strng.replace('г\u035Cм', '\\m+')


    return Strng

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

def FixVedic(Strng, Target):
    # Alternate Vedic Forms
    Strng = Strng.replace('{\\m+}', '\\m+')
    Strng = Strng.replace('\\`', '\\_') ## Alternate form of Anudatta
    Strng = Strng.replace('\\\'\'', '\\"') ## Alternate form of Dirdha udatta

    # Fix Malformed Input //m+, //++

    Strng = Strng.replace('\\\\м', '\\м')
    Strng = Strng.replace('\\\\m', '\\m')
    Strng = Strng.replace('\\\\\'', '\\\'')
    Strng = Strng.replace('\\\\"', '\\"')
    Strng = Strng.replace('\\\\_', '\\_')

    vedicDiacRoman = ["IAST", "IASTPali", "ISO", "Titus"]
    vedicnonDiacRoman = ["HK", "Itrans", "Velthuis", "SLP1", "WX"]

    if Target in vedicDiacRoman:
        Strng = VedicSvarasDiacrtics(Strng, Target)
    elif Target  == "IPA":
        Strng = Strng.replace('\\"','↑↑').replace("\\_", '↓').replace("\\\'",'↑')
        Strng = Strng.replace('\\m++', 'gͫ̄')
        Strng = Strng.replace('\\m+', 'gͫ')
    elif Target == "RomanReadable":
        Strng = Strng.replace('\\"','').replace("\\_", '').replace("\\\'",'')
        Strng = Strng.replace('\\m++', 'ggum')
        Strng = Strng.replace('\\m+', 'gum')
    elif Target in vedicnonDiacRoman:
        pass
    elif Target == "RussianCyrillic":
        Strng = VedicSvarasCyrillic(Strng, Target)
    else:
        Strng = VedicSvarasOthers(Strng, Target)

    return Strng

# PostFile ? why not fix !?
def PostFixRomanOutput(Strng,Source,Target):
    Strng = Strng.replace("\u02BD","")

    Strng = FixVedic(Strng, Target)

    if Source == 'Sinhala' and Target == 'IPA':
        Strng = SinhalaIPAFix(Strng)

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

    if Target == "Wancho":
        Strng = FixWancho(Strng)

    if Target == "Mro":
        Strng = FixMro(Strng)

    if Target == "RomanReadable":
        Strng = FixRomanReadable(Strng)

    if Target == "IAST" or Target == "IASTPali":
        Strng = Strng.replace("a_i", "aï")
        Strng = Strng.replace("a_u", "aü")

    if Target == "ISO":
        Strng = Strng.replace("\\’", "\\\'")
        Strng = Strng.replace("a_i", "a:i")
        Strng = Strng.replace("a_u", "a:u")


    if Target == "Velthuis" or Target == "Itrans":
        Strng = Strng.replace("\\.a", "\\\'")

    if Target == "Aksharaa":
        Strng = Strng.replace("\\a;", "\\\'")

    if Target == "HanifiRohingya":
        Strng = FixHanifiRohingya(Strng)

    if Target == "Mongolian":
        Strng = FixMongolian(Strng)

    return Strng

# Fixing the Indic Ouput for the standard corrections
# Indic Fix are mandatory corrections to the immediate ouput.
def FixIndicOutput(Strng,Source,Target):
    vir = GM.CrunchList('ViramaMap', Target)[0]

    Strng = Strng.replace(vir + '_', vir)

    try:
        Strng = globals()["Fix"+Target](Strng)
    except KeyError:
        pass
        #print #"Fix"+Target+" doesn't exist"

    Strng = Strng.replace('\u02BD','')
    # Shifting Vowel Signs and Diacritics
    # க²ா ->  கா²
    Strng = ShiftDiacritics(Strng,Target,reverse=False)

    ## Make the Vedic Signs readable
    vedicScripts = ['Assamese', 'Bengali', 'Devanagari', 'Gujarati', 'Kannada', 'Malayalam', 'Oriya', 'Gurmukhi', 'Tamil', 'Telugu', 'TamilExtended', 'Grantha']

    if Target not in vedicScripts:
        Strng = Strng.replace('॒','↓')
        Strng = Strng.replace('᳚','↑↑')
        Strng = Strng.replace('॑','↑')

    return Strng

def FixHebrew(Strng, reverse = False):
    vowelsigns = '(' + '|'.join(GM.CrunchSymbols(GM.VowelSigns, 'Hebrew')) + ')'
    consonants = '(' + '|'.join(GM.CrunchSymbols(GM.Consonants, 'Hebrew')) + ')'

    vowelsignsA = '(' + '|'.join(GM.CrunchSymbols(GM.VowelSigns, 'Hebrew') + ['ַ']) + ')'
    vowelsignsAD = '(' + '|'.join(GM.CrunchSymbols(GM.VowelSigns, 'Hebrew') + ['ַ', 'ּ']) + ')'

    vowelsignsADShin = '(' + '|'.join(GM.CrunchSymbols(GM.VowelSigns, 'Hebrew') + ['ַ', 'ּ', 'ׁ']) + ')'
    vowelsignsADShinG = '(' + '|'.join(GM.CrunchSymbols(GM.VowelSigns, 'Hebrew') + ['ַ', 'ּ', 'ׁ', '׳']) + ')'


    finalCons = ['כ', 'מ', 'נ', 'פ', 'צ', 'פּ', 'כּ']
    finals = ['ך', 'ם', 'ן', 'ף', 'ץ', 'ףּ', 'ךּ']

    otherCons = 'ב,ח,ע,צ,ש,ת'.split(',')
    consonantsAll = '(' + '|'.join(GM.CrunchSymbols(GM.Consonants, 'Hebrew') + finals  + otherCons + ['׳']) + ')'

    if not reverse:
        Strng = Strng.replace('\u02BD', '')

        # Fix Anusvara

        # mK, mG, mp, mC, md, mt
        Strng = re.sub('מְ' + '\u02BC' + '([גדזטכצקת])', 'נְ' + r'\1', Strng)
        Strng = re.sub('מְ' + '\u02BC', 'מְ', Strng)

        # insert a_sign
        Strng = re.sub(consonants + '(?!' + vowelsigns + ')', r'\1' + '\u05B7' + r'\2', Strng)

        # fix double a to single a
        Strng = Strng.replace('\u05b7\u05b7', '\u05B7')

        # Fix a appear with Dagesh and Shva.. k -> kaph + patau + dagesh + shva -> kaph + dagesh + shva
        Strng = Strng.replace('\u05b7\u05bc\u05B0', '\u05bc\u05B0')

        # fix order of vowel signs and vowels sign with ch/j
        Strng = re.sub('(׳)' + vowelsigns, r'\2\1', Strng)
        Strng = re.sub('(וֹ)(׳)', r'\2\1', Strng)
        Strng = re.sub('(וּ)(׳)', r'\2\1', Strng)
        Strng = re.sub('(׳)(\u05b7)', r'\2\1', Strng)
        Strng = re.sub('(׳)(\u05b7)', r'\1', Strng)

        # Fix Pateh appearing with vowel signs
        Strng = re.sub('(\u05b7)' + vowelsigns, r'\2', Strng)
        Strng = re.sub('(\u05b7)' + '(\u05BC)' + vowelsigns, r'\2\3', Strng)

        #Do gemination
        ## consonant doubling with Dagesh
        Strng = re.sub('([' + 'ושרקסנמליזטײ' + '])(ְ)' + r'\1', r'\1' + 'ּ', Strng)
        Strng = re.sub('(שׁ)(ְ)' + r'\1', r'\1' + 'ּ', Strng)

        # Fix Finals

        shortVowels = '(' + '|'.join(['\u05B7', '\u05B8', '\u05B4', '\u05BB', '\u05B5', '\u05B6', '\u05B9', '\u05B0']) + ')'

        vowelsAll = '(' + '|'.join(['\u05B7', '\u05B8', '\u05B4', '\u05BB', '\u05B5', '\u05B6', '\u05B9', '\u05B0', 'י', 'וֹ', 'וּ'] + ['׳']) + ')'

        for c, f in zip(finalCons, finals):
            Strng = re.sub(vowelsAll + '(' + c + ')' + shortVowels + '(׳?)' + '(?!' + consonantsAll + ')', r'\1' + f +  r'\3' + r'\4', Strng)

        # Fix Va + O
        Strng = Strng.replace('װ' + '\u05B9', '\u05D5\u05BA')

        Strng = Strng.replace('װ' , '\u05D5')
        Strng = Strng.replace('ײ' , 'י')

        Strng = Strng.replace('\u02BC', '')


    else:
        vowels = ['ְ','ֱ','ֲ','ֳ','ִ','ֵ','ֶ','ַ','ָ','ֹ','ֺ','ֻ','ׇ']
        vowelsR = '(' + '|'.join(vowels) + ')'

        for f,c in zip(finals, finalCons):
            Strng = Strng.replace(f, c)

        # Swap the order of diacritics
        Strng = re.sub(vowelsR + '([ּׁׂ])', r'\2\1', Strng)

        ## gimme, teh and other consonants  with Dagesh just replace themselves
        Strng = re.sub('([דתצ])(ּ)', r'\1', Strng)

        ## approx vowels

        # Short vowels with Schwa
        Strng = Strng.replace('אֲ', 'אַ')
        Strng = Strng.replace('עֲ', 'אַ')

        Strng = Strng.replace('\u05B1', '\u05B6').replace('\u05B3', '\u05B9').replace('\u05B2','')

        # replace malei forms
        Strng = re.sub('(?<=[ֵֶַָֹ])([א])'+'(?!' + vowelsignsA + ')', '', Strng)
        Strng = re.sub('(?<=[ִֵֶַָֹֻ])([ה])'+'(?!' + vowelsignsAD + ')', '', Strng)

        Strng = re.sub('(?<=[ֵֶ])([י])'+'(?!' + vowelsR + vowelsigns + ')', '', Strng)

        # ha + dagesh to normal ha
        Strng = Strng.replace('הּ', 'ה')

        ## consonant doubling with Dagesh
        Strng = re.sub('([' + 'שרקסנמליזט' + '])(ּ)', r'\1' + 'ְ' + 'ְ' + r'\1', Strng) ## twice to mark it specifically

        ## approx Cons
        Strng = Strng.replace('ת', 'ט').replace('ח', 'כ').replace('ע', 'א').replace('שׂ', 'ס')
        Strng = re.sub('ש(?![ׂׄ])', 'שׁ', Strng)

        Strng = Strng.replace('ׁׁ','ׁ')

        ## replace vet with double vav if not followed by dagesh
        Strng = re.sub('ב(?!ּ)', 'װ', Strng)

        # swap garesh and short vowels
        Strng = re.sub(vowelsR + "(׳)", r'\2\1', Strng)

        # tsa when not followed by gatresh with t+sa (including vowel signs)
        Strng = re.sub('צ' + '(?!׳)', 'טְְס', Strng)

        ## reinsert uo2dbc of vau based vowels
        Strng = re.sub('(\s|^|\.|,|א)' + '(וֹ|וּ)', r'\1\2' + '\u02BC', Strng)
        Strng = re.sub('(וּ)' + vowelsignsA, 'װְװ' + r'\2', Strng)

        ## vav, yod to double vav/yod if followed by short vowels or long vowels
        Strng = re.sub('י' + '(?=' + vowelsigns + '|ַ)', 'ײ', Strng)
        Strng = re.sub('ו' + '(?=' + '[ְִֵֶַָׇֺֻ]' +  '|ַ)', 'װ', Strng)

        ## replace vay ad yod in other cases when no preceded or succeeded by the vowels
        Strng  = re.sub('(?<!ִ)(י)', 'ײ' , Strng)
        Strng = re.sub('(ו)(?![ֹֺּ])', 'װ', Strng)

        ## Intrdouce Schva nach

        # Replva holem for vav with holem
        Strng = Strng.replace('ֺ','ֹ')

        # remove stray alephs
        Strng = re.sub('[א](?!' + vowelsR + ')', '', Strng)

        ## remove schwa at the end of vwords
        Strng = re.sub(consonantsAll + "(?!" + vowelsignsADShinG + ')', r'\1' + 'ְ' + r'\2', Strng)

        ## Aleph + Svha = a
        Strng = Strng.replace('אְ','')


        ## Hard Svha nakh
        if '௞' in Strng:
            # added in preoptions
            Strng = Strng.replace('௞', '')
            Strng = Strng.replace('ְ' + 'ְ','ְ')
        else:
            ## Schva nach
            # https://judaism.stackexchange.com/questions/92599/what-are-the-rules-for-shva-na
            # http://www.shailamorah.com/kriah-roundtable/teaching-shva-rules
            Strng = re.sub('(\s|\.|,|^)' + consonantsAll + '(ְ)', r'\1\2' + 'ֶ', Strng)
            Strng = re.sub('(ּ)' + '(ְ)', r'\1' + 'ֶ' , Strng)
            Strng = re.sub(consonantsAll + '(' 'ְ' + 'ְ' + ')' + '(' + r'\1' + ')(' + 'ְ' + ')', r'\1\2\3' +  'ֶ', Strng)
            Strng = re.sub(consonantsAll + '(ְ)' + '(' + r'\1' + ')'+ '(?!(\s|\.|\n|,|$))', r'\1' + 'ֶ' + r'\3', Strng)
            Strng = re.sub(consonantsAll + '(ְ)' + consonantsAll + '(ְ)' + '(?!(\s|\.|\n|,|$))', r'\1\2' + r'\3' + 'ֶ' , Strng)

            Strng = Strng.replace('ְ' + 'ְ','ְ') #two schva to one
            Strng = Strng.replace('ֶ' + 'ְ','ְ') #two schva to one

        ## remove patesh
        Strng = re.sub('(?<![אע])\u05B7', '', Strng)

    return Strng


def FixMongolian(Strng, reverse=False):
    vowels = '(' + '|'.join(GM.CrunchSymbols(GM.Vowels, 'Mongolian')) + ')'
    consonants = '(' + '|'.join(GM.CrunchSymbols(GM.Consonants, 'Mongolian')) + ')'

    if not reverse:
        #Strng = re.sub(consonants + '?' + vowels + '([\u1880\u1881])?', r'\1\2\3 ', Strng)
        Strng = re.sub('(\u180B)' + consonants, r'\2', Strng)
        Strng = re.sub('(\u180B)' + vowels, r'\2', Strng)

        Strng = re.sub(consonants + consonants + consonants + vowels + '(\u1880)', r'\5\1\2\3\4', Strng)
        Strng = re.sub(consonants + consonants + vowels + '(\u1880)', r'\4\1\2\3', Strng)
        Strng = re.sub(consonants + '?' + vowels + '(\u1880)', r'\3\1\2', Strng)
        Strng = Strng.replace(' \u02BC', '\u200B')
        Strng = Strng.replace('\u02BC', '\u200B')

    return Strng

def FixHanifiRohingya(Strng, reverse=False):
    consList = '(' + '|'.join(GM.CrunchSymbols(GM.Consonants, 'HanifiRohingya')+['\U00010D17', '\U00010D19']) + ')'
    vowList = '(' + '|'.join(GM.CrunchSymbols(GM.Vowels, 'HanifiRohingya')) + ')'

    vowListNotA = '(' + '|'.join(GM.CrunchSymbols(GM.Vowels, 'HanifiRohingya')[1:]) + ')'

    consListLookBehind = ''.join(map(lambda x: '(?<!' + x + ')', GM.CrunchSymbols(GM.Consonants, 'HanifiRohingya')))

    ## Add Urdu specific characters

    if not reverse:
        Strng = re.sub(consListLookBehind + vowList, '\U00010D00' + r'\1', Strng ) # Add Vowel Carrier
        Strng = re.sub(consList + r'\1', r'\1' + '\U00010D27', Strng) # Add Gemination

        Strng = re.sub(vowListNotA + '𐴀𐴟', r'\1' + '\U00010D17', Strng) # koi, kui etc
        Strng = re.sub(vowListNotA + '𐴀𐴞', r'\1' + '\U00010D19', Strng) # kou etc. using the dipthong character

        Strng = Strng.replace('\U00010D24\\', '\U00010D25') #swap tone 2
        Strng = Strng.replace('\U00010D24/', '\U00010D26') #swap tone 3

        Strng = Strng.replace('_', '\U00010D22') # Map Sukun

    else:
        tones = '([\U00010D24\U00010D25\U00010D26])'
        Strng = re.sub('(\U00010D00)' + tones + vowList, r'\1\3\2', Strng) # Swap Vowel-carrier + tone + vowelsign
        Strng = re.sub(consList + tones + vowList, r'\1\3\2', Strng) # swap cons + tone + vowel sign

        Strng = re.sub(vowListNotA.replace('\U00010D00', '') + '\U00010D17' , r'\1' + '𐴀𐴟', Strng) #swap tone 2
        Strng = re.sub(vowListNotA.replace('\U00010D00', '') +'\U00010D19', r'\1' + '𐴀𐴞' , Strng) #swap tone 3

        Strng = Strng.replace('\U00010D00', '') # remove vowel carrier
        Strng = re.sub('(.)' + '\U00010D27', r'\1\1' , Strng) # reverse gemination

        Strng = Strng.replace('\U00010D25', '\U00010D24\\') #swap tone 2
        Strng = Strng.replace('\U00010D26', '\U00010D24/') # swap tone 3

        Strng = re.sub(consList + '\U00010D17' , r'\1' + '\U00010D16\u02BE', Strng) # cons + dipth.y -> y + nukta

        Strng = re.sub(consList +'\U00010D19', r'\1' + '\U00010D18\u02BE', Strng) # cons + dipth.w -> v + nukta

        Strng = Strng.replace('\U00010D22', '_') #remove Sukun

        Strng = Strng.replace('𐴜', '𐴖') # v -> w; Archaic v is not used anyway

    # Punctuation
    if ( not reverse):
        for x,y in zip([',','?',';'],['،','؟','؛']):
            Strng = Strng.replace(x,y)
    else :
        for x,y in zip([',','?',';'],['،','؟','؛']):
            Strng = Strng.replace(y,x)


    return Strng

def FixMasaramGondi(Strng, reverse=False):
    consList = '(' + '|'.join(GM.CrunchSymbols(GM.Consonants, 'MasaramGondi')) + ')'

    if not reverse:
        Strng = Strng.replace('𑴌𑵅𑴪','\U00011D2E') # KSSA
        Strng = Strng.replace('𑴓𑵅𑴕','\U00011D2F') # JNYA
        Strng = Strng.replace('𑴛𑵅𑴦','\U00011D30') # TRA

        Strng = re.sub(consList + '\U00011D45\U00011D26', r'\1' + '\U00011D47', Strng) # kra
        Strng = re.sub('\U00011D26\U00011D45' + consList, '\U00011D46' + r'\1', Strng) # rka

        ## remove final virama when not followed by a consonant
        Strng = re.sub('\U00011D45(?!' + consList + ')' , '\U00011D44', Strng)
    else:
        Strng = Strng.replace('\U00011D2E', '𑴌𑵅𑴪') # KSSA
        Strng = Strng.replace('\U00011D2F', '𑴓𑵅𑴕') # JNYA
        Strng = Strng.replace('\U00011D30', '𑴛𑵅𑴦') # TRA

        Strng = Strng.replace('\U00011D47', '\U00011D45\U00011D26',) # kra
        Strng = Strng.replace('\U00011D46', '\U00011D26\U00011D45') # rka

        Strng = Strng.replace('\U00011D44','\U00011D45')

    return Strng


def FixGunjalaGondi(Strng, reverse=False):
    consList = '(' + '|'.join(GM.CrunchSymbols(GM.Consonants, 'GunjalaGondi')) + ')'

    if not reverse:
        Strng = re.sub('(\U00011D7A\u02BE)([\U00011D7B\U00011D7C\U00011D80\U00011D81])', '\U00011D95' + r'\1', Strng)
        Strng = re.sub('(\U00011D7A\u02BF)([\U00011D7D\U00011D7E\U00011D82\U00011D83])', '\U00011D95' + r'\1', Strng)

        Strng = Strng.replace('\u02BE', '')
        Strng = Strng.replace('\u02BF', '')

        ## remove final virama when not followed by a consonant
        Strng = re.sub('\U00011D97(?!' + consList + ')' , '', Strng)
    else:
        pass

    return Strng

def FixSoyombo(Strng, reverse=False):
    finVir = ['\U00011A5E\U00011A99','\U00011A5C\U00011A99','\U00011A60\U00011A99','\U00011A6D\U00011A99','\U00011A6F\U00011A99','\U00011A72\U00011A99','\U00011A74\U00011A99','\U00011A7C\U00011A99','\U00011A7D\U00011A99','\U00011A7F\U00011A99','\U00011A81\U00011A99']
    fin = ['\U00011A8A','\U00011A8B','\U00011A8C','\U00011A8D','\U00011A8E','\U00011A8F','\U00011A90','\U00011A91','\U00011A92','\U00011A93','\U00011A94']
    consList = '(' + '|'.join(GM.CrunchSymbols(GM.Consonants, 'Soyombo')) + ')'

    if not reverse:
        Strng = Strng.replace('𑩜𑪙𑪀', '\U00011A83')  #KSSA
        Strng = re.sub('\U00011A7F\U00011A99' + '(?=' + consList + ')' , '\U00011A88', Strng) # Fix shka

        ## Gemination ##
        Strng = re.sub('(?<!𑪙)(.)𑪙' + r'\1', r'\1' + '\U00011A98', Strng)
        # final consonats
        if '\u02BE' in Strng:
            for x, y in zip (finVir, fin):
                Strng = re.sub(x + '(?!' + consList + ')' , y, Strng)

            Strng = re.sub('𑪈(?!' + consList + ')' , '\U00011A93', Strng)

            Strng = Strng.replace('\u02BE', '')

        ## remove final virama when not followed by a consonant
        Strng = re.sub('\U00011A99(?!' + consList + ')' , '', Strng)
    else:
        Strng = Strng.replace('\U00011A9A', ' ') ## Reverse Tsheg
        Strng = Strng.replace('\U00011A83', '𑩜𑪙𑪀')  #KSSA

        ## Gemination ##
        Strng = re.sub('(.)\U00011A98', r'\1' + '\U00011A99' + r'\1', Strng)

        viraCon = ['\U00011A7C\U00011A99', '\U00011A7D\U00011A99', '\U00011A81\U00011A99', '\U00011A7F\U00011A99']
        initial = ['\U00011A86', '\U00011A87', '\U00011A89', '\U00011A88']

        for x, y in zip(viraCon, initial):
            Strng = Strng.replace(y, x)

        tsaSeries = ['𑩵','𑩶','𑩷']
        caSeries = ['𑩡','𑩢','𑩣']

        for x, y in zip(tsaSeries,caSeries):
            Strng = Strng.replace(y, x)

        ## initial ##

        for x, y in zip(finVir, fin):
            Strng = Strng.replace(y, x)

    return Strng

def FixKharoshthi(Strng, reverse=False):
    Strng = KharoshthiNumerals(Strng, reverse)

    return Strng

def FixMarchen(Strng, reverse=False):
    subjoinCons = '𑱲 𑱳 𑱴 𑱵 𑱶 𑱷 𑱸 𑱹 𑱺 𑱻 𑱼 𑱽 𑱾 𑱿 𑲀 𑲁 𑲂 𑲃 𑲄 𑲅 𑲆 𑲇 𑲉 𑲊 𑲋 𑲌 𑲍 𑲎'.split(' ')
    subjoined = '𑲒 𑲓 𑲔 𑲕 𑲖 𑲗 𑲘 𑲙 𑲚 𑲛 𑲜 𑲝 𑲞 𑲟 𑲠 𑲡 𑲢 𑲣 𑲤 𑲥 𑲦 𑲧 𑲩 𑲪 𑲫 𑲬 𑲭 𑲮'.split(' ')

    if not reverse:
        for x, y in zip(subjoinCons, subjoined):
            Strng = Strng.replace('ʾ' + x, y)

        Strng = Strng.replace('ʾ', '')
        Strng = Strng.replace('\u02BF', '')

    else:
        tsaSeries = ['\U00011C82', '\U00011C83', '\U00011C84']
        jaSereis =  ['\U00011C76', '\U00011C77', '\U00011C78']

        for x, y in zip(tsaSeries, jaSereis):
            Strng = Strng.replace(y, x)

        for x, y in zip(subjoinCons, subjoined):
            Strng = Strng.replace(y, 'ʾ' + x)

    return Strng

def FixMro(Strng, reverse=False):
    # M2, K2, L2, L3, H2, t2
    extracons = ['\U00016A4E', '\U00016A59', '\U00016A5A', '\U00016A5B', '\U00016A5C', '\U00016A5E']
    consnormaldig = ['𖩃𖩢', '𖩌𖩢', '𖩍𖩢', '𖩍𖩣', '𖩉𖩢', '𖩀𖩢']
    consnormal = ['𖩃', '𖩌', '𖩍', '𖩍', '𖩉', '𖩀']

    if not reverse:
        for x, y in zip(consnormaldig, extracons):
            Strng = Strng.replace(x, y)
    else:
        for x, y in zip(extracons, consnormal):
            Strng = Strng.replace(x, y)

    return Strng

def FixWancho(Strng, reverse=False):
    tonemarks = ['\U0001E2EC', '\U0001E2ED', '\U0001E2EE', '\U0001E2EF']
    tonewri = ['\\_', '\\-', '\\!', '\\;']

    nasalization = ['\U0001E2E6', '\U0001E2E7', '\U0001E2E8', '\U0001E2EA'] # o, e, aa , u ; nasalization
    nasvowels = ['\U0001E2D5', '\U0001E2DB', '\U0001E2C0', '\U0001E2DE']

    Anusvaras = ['\U0001E2E2', '\U0001E2E3', '\U0001E2E4', '\U0001E2E5'] # o, aa, a, i
    AnusvaraVowels = ['\U0001E2D5', '\U0001E2C0', '\U0001E2C1', '\U0001E2DC']

    if not reverse:
        for x, y in zip(tonemarks, tonewri):
            Strng = Strng.replace(y, x)

        for x, y in zip(nasvowels, nasalization):
            Strng = Strng.replace(x + 'ʿ', y)

        Strng = Strng.replace('ʿ', '𞋉')

        for x, y in zip(AnusvaraVowels, Anusvaras):
            Strng = Strng.replace(x + 'ʾ', y)

        Strng = Strng.replace('ʾ', '𞋝')

        Strng = Strng.replace('𞋋𞋗', '\U0001E2E1')
        Strng = Strng.replace('𞋋𞋎', '\U0001E2E0')

        Strng = Strng.replace('𞋓Ø', '\U0001E2D2') ## WA
        Strng = Strng.replace('Ø', '')

    else:
        for x, y in zip(tonemarks, tonewri):
            Strng = Strng.replace(x, y)

        for x, y in zip(nasvowels, nasalization):
            Strng = Strng.replace(y, x + 'ʿ')

        for x, y in zip(AnusvaraVowels, Anusvaras):
            Strng = Strng.replace(y, x + 'ʾ')

        Strng = Strng.replace('\U0001E2E1', '𞋋𞋗')
        Strng = Strng.replace('\U0001E2E0', '𞋋𞋎')

        Strng = Strng.replace('\U0001E2D2', '𞋓Ø') ## WA


    return Strng

def FixSiddham(Strng, reverse=False):
    if not reverse:
        pass
    else:
        ## reverse the alternate forms
        Strng = Strng.replace('𑗜', '𑖲') # VS U
        Strng = Strng.replace('𑗝', '𑖳') # VS UU
        Strng = Strng.replace('𑗛', '𑖄') # VS U
        Strng = Strng.replace('𑗘', '𑖂') # VS I1
        Strng = Strng.replace('𑗙', '𑖂') # VS I2
        Strng = Strng.replace('𑗚', '𑖃') # VS II

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

    VedicSign = ['॑', '॒', '᳚']
    TamilDiacritic = ['ʼ', 'ˮ', '꞉']#, '²', '³', '⁴', '₂', '₃', '₄']

    if not reverse:
        Strng = Strng.replace(ava+ava,avaA)
        Strng = PostProcess.RetainDandasIndic(Strng, 'Tamil', True)
        Strng = PostProcess.RetainIndicNumerals(Strng, 'Tamil', True)

        for x in TamilDiacritic:
            for y in VedicSign:
                Strng = Strng.replace(x + y, y + x)

    else:
        Strng = Strng.replace(avaA,ava+ava)
        Strng = Strng.replace('ஷ²', 'ஶ')

        Strng = Strng.replace('𑌃', '꞉')

        for x in TamilDiacritic:
            for y in VedicSign:
                Strng = Strng.replace(y + x, x + y)

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

        Vedicomp = '([' + ''.join(GM.VedicSvarasList) + '])'

        Strng = re.sub(Vedicomp + '\u0A71' + '(.)', r'\1' + r'\2' + Gurmukhi.ViramaMap[0] + r'\2' , Strng)

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


def FixTamilExtended(Strng, reverse=False):
    if not reverse:
        Strng = Strng.replace('ക്‌ഷ', 'ക്ഷ')
        Strng = Strng.replace('ശ്‌ര', 'ശ്‍ര')
        Strng = Strng.replace('ൗ', 'ൌ')

        for svara in GM.VedicSvarasList:
            Strng = Strng.replace('\u200C' + svara, svara + '\u200C')
    else:
        for svara in GM.VedicSvarasList:
            Strng = Strng.replace(svara + '\u200C', '\u200C' + svara)

        Strng = Strng.replace('\u0D4D', '\u0D4D\u200C')

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

def FixKhamtiShan(Strng, reverse=False):
    if not reverse:
        Strng = Strng.replace('်ရ', 'ြ')
        Strng = Strng.replace('်ယ', 'ျ')
        Strng = Strng.replace('်ဝ', 'ွ')

        ## Maintain the order of the medials
        Strng = Strng.replace("\u103C\u103B", "\u103B\u103C")
        Strng = Strng.replace("\u103D\u103B", "\u103B\u103D")
        Strng = Strng.replace("ႂ\u103C", "\u103Cွ")
    else:
        Strng = Strng.replace('ꩳ', 'ရ')
        Strng = Strng.replace("\u103B\u103C", "\u103C\u103B")
        Strng = Strng.replace("\u103B\u103D", "\u103D\u103B")
        Strng = Strng.replace("\u103Cႂ", "ႂ\u103C")

        Strng = Strng.replace('ြ', '်ꩳ')
        Strng = Strng.replace('ꩳ', 'ရ')
        Strng = Strng.replace('ျ', '်ယ')
        Strng = Strng.replace('ွ', '်ဝ')

    return Strng

def FixTaiLaing(Strng, reverse=False):
    if not reverse:
        Strng = Strng.replace('်ꩺ', 'ြ')
        Strng = Strng.replace('်ယ', 'ျ')
        Strng = Strng.replace('်ဝ', 'ႂ')

        ## Maintain the order of the medials
        Strng = Strng.replace("\u103C\u103B", "\u103B\u103C")
        Strng = Strng.replace("\u103D\u103B", "\u103B\u103D")
        Strng = Strng.replace("ႂ\u103C", "\u103Cႂ")

        Strng = Strng.replace('ႂျ','်၀ျ')

    else:
        Strng = Strng.replace("\u103B\u103C", "\u103C\u103B")
        Strng = Strng.replace("\u103B\u103D", "\u103D\u103B")
        Strng = Strng.replace("\u103Cႂ", "ႂ\u103C")

        Strng = Strng.replace('ြ', '်ꩺ')
        Strng = Strng.replace('ျ', '်ယ')
        Strng = Strng.replace('ႂ', '်ဝ')

    return Strng

def FixShan(Strng, reverse=False):
    if not reverse:
        Strng = Strng.replace('်ရ', 'ြ')
        Strng = Strng.replace('်ယ', 'ျ')
        Strng = Strng.replace('်ဝ', 'ွ')
        Strng = Strng.replace('်ႁ', 'ှ')

        ## Maintain the order of the medials
        Strng = re.sub('(ှ)' + '([ျြွ])', r'\2\1', Strng)
        Strng = Strng.replace("\u103C\u103B", "\u103B\u103C")
        Strng = Strng.replace("\u103D\u103B", "\u103B\u103D")
        Strng = Strng.replace("ွ\u103C", "\u103Cွ")

    else:
        ## Reverse the order of the medials
        Strng = re.sub('([ျြွ])' + '(ှ)', r'\2\1', Strng)
        Strng = Strng.replace("\u103B\u103C", "\u103C\u103B")
        Strng = Strng.replace("\u103B\u103D", "\u103D\u103B")
        Strng = Strng.replace("\u103Cွ", "ွ\u103C")

        Strng = Strng.replace('ြ', '်ရ')
        Strng = Strng.replace('ျ', '်ယ')
        Strng = Strng.replace('ွ', '်ဝ')
        Strng = Strng.replace('ှ', '်ႁ')

    return Strng

def FixMon(Strng, reverse=False):
    pairs = [('င', 'ၚ'),('ဉ', 'ည'), ('ဈ', 'ၛ')]

    for x, y in pairs:
        Strng = Strng.replace(y, x)

    Strng = FixBurmese(Strng, reverse)

    Strng = Strng.replace('ည', '\uE001') #

    for x, y in pairs:
        Strng = Strng.replace(x, y)

    Strng = Strng.replace('\uE001', 'ည\u1039ည')

    medials_cons_mon = ['\u1039န', '\u1039မ', '\u1039လ']
    medials_mon = ['ၞ', 'ၟ', 'ၠ']

    if not reverse:
        for x, y in zip(medials_cons_mon, medials_mon):
            Strng = Strng.replace(x, y)

        Strng = Strng.replace('ၠြ', 'ြၠ')

        # Contigous Mon Medials
        for i, med1 in enumerate(medials_mon):
            for j, med2 in enumerate(medials_mon):
                Strng = Strng.replace(med1 + med2, medials_cons_mon[i] + medials_cons_mon[j])

        # Contiguous Medials + ya, ra and va
        for i, med in enumerate(medials_mon):
            Strng = Strng.replace(med + 'ျ', medials_cons_mon[i] + 'ျ')

            Strng = Strng.replace('ရ်' + med,  'ရ်' + medials_cons_mon[i])
            Strng = Strng.replace('ၚ်' + med,  'ၚ်' + medials_cons_mon[i])


        # RA + Medial
    else:
        Strng = Strng.replace('်ရၠ', 'ၠ်ရ')

        for x, y in zip(medials_cons_mon, medials_mon):
            Strng = Strng.replace(y, x)

        Strng = Strng.replace('\u1039', '်')

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

        Strng = re.sub('ျါ','ျာ', Strng)

        Strng = re.sub('(?<!ဂ)ြါ','ြာ', Strng)

        Strng = re.sub('ျေါ','ျော', Strng)

        Strng = re.sub('(?<!ဂ)ြေါ','ြော', Strng)


        Strng = Strng.replace("သ္သ", "ဿ")
        Strng = Strng.replace("ဉ္ဉ", "ည")

        Strng = Strng.replace("\u02F3", "့")
        Strng = Strng.replace("့်", "့်",)

        Strng = Strng.replace("ာ္", "ာ်")

        Strng = re.sub("(ရ်္င်္)" + "(" + ListC + ")", "ရ်္င္" + r'\2', Strng)

        Strng = Strng.replace("ါ္", "ါ်")

        Strng = Strng.replace("\u103A\u1039\u101A", "\u103B")
        Strng = Strng.replace('\u103C\u103A\u1039ဝ', "\u103Cွ")

        ## Maintain the order of the medials
        Strng = re.sub('(ှ)' + '([ျြွ])', r'\2\1', Strng)
        Strng = Strng.replace("\u103C\u103B", "\u103B\u103C")
        Strng = Strng.replace("\u103D\u103B", "\u103B\u103D")
        Strng = Strng.replace("ွ\u103C", "\u103Cွ")

        ## Introduce repha for ra and ga
        Strng = Strng.replace('ရျ', 'ရ်္ယ')
        Strng = Strng.replace('ငျ', 'င်္ယ')

        #Strng = Strng.replace("\u103A\u1039", "\u1039")
    else:
        ## Reverse the order of the medials
        Strng = re.sub('([ျြွ])' + '(ှ)', r'\2\1', Strng)
        Strng = Strng.replace("\u103B\u103C", "\u103C\u103B")
        Strng = Strng.replace("\u103B\u103D", "\u103D\u103B")
        Strng = Strng.replace("\u103Cွ", "ွ\u103C")

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

        Strng = Strng.replace('ཇྷ', 'ཛྷ') ## JHA -> DZHA

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
    a = GM.CrunchSymbols(GM.Vowels,Script)[0].split()[0]
    consa = "|".join(GM.CrunchSymbols(GM.Consonants,Script) + [a])

    if Script == "Thai":
        EAIO += "|ใ"
        cons = "|".join(GM.CrunchSymbols(GM.Consonants,Script) + ['ฮ','บ', 'ฝ', 'ด', 'ฦ', 'ฤ'])

    if Script == "Lao":
        cons = "|".join(GM.CrunchSymbols(GM.Consonants,Script) + ['ດ','ບ','ຟ'] )

    a = GM.CrunchSymbols(GM.Vowels,Script)[0]

    if not reverse:
        Strng = re.sub("("+consa+")("+EAIO+")",r"\2\1",Strng)
    else:
        Strng = re.sub("("+EAIO+")"+"("+consa+")",r'\2\1',Strng)

    return Strng

def FixKhomThai(Strng, reverse=False):

    if not reverse:
        Strng = Strng.replace('โ','เา')
        Strng = ThaiReverseVowelSigns(Strng,reverse)
        Strng = re.sub('(.\u0E3A)(.\u0E3A)(ใ)', r'\3\1\2', Strng) # reversed
        Strng = re.sub('(.\u0E3A)(ใ)', r'\2\1', Strng) # reversed

        Strng = re.sub('((.\u0E3A)+)(เ)', r'\3\1', Strng) # reversed
        Strng = re.sub('(.\u0E3A)?(.)(ฺร)', r'\3\1\2', Strng) # reversed
        Strng = Strng.replace('เอา', 'โอ')

        Strng = Strng.replace("เอำ", 'เาอํ')
        Strng = Strng.replace('เาอํ', 'โอํ')
    else:
        Strng = re.sub('(ใ)(.\u0E3A)(.\u0E3A)', r'\2\3\1', Strng)
        Strng = re.sub('(ใ)(.\u0E3A)', r'\2\1', Strng)

        Strng = re.sub('(ฺร)(.\u0E3A)?(.)', r'\2\3\1', Strng)
        Strng = re.sub('(เ)((.\u0E3A)+)', r'\2\1', Strng)
        Strng = ThaiReverseVowelSigns(Strng,reverse)
        Strng = Strng.replace('เา', 'โ')

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

        #print('I am here')

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
        Strng = Strng.replace('ə', '\U000110E6\U000110E8')
    else:
        ListV = "(" + "|".join(GM.CrunchSymbols(GM.Vowels, 'SoraSompeng')) + ')'
        Strng = re.sub(ListC + '(?!' + ListV + ')', r'\1' + 'ə', Strng)

        Strng = Strng.replace('𑃔ə𑃨', '𑃔𑃨ə')

        Strng = Strng.replace('𑃦𑃨', 'ə')
        Strng = Strng.replace('ə𑃨', '𑃨')

    return Strng


def FixRomanReadable(Strng, reverse = False):
    if not reverse:
        Strng = re.sub('([aiueo])nj([aeiou])', r'\1' + 'ny' + r'\2', Strng)
        Strng = re.sub('(\W)nj([aeiou])', r'\1' + 'ny' + r'\2', Strng)
        Strng = re.sub('^nj([aeiou])', 'ny' + r'\1', Strng)

        Strng = Strng.replace("njnj", "nny")

        Strng = Strng.replace("Mk", "ngk")
        Strng = Strng.replace("Mg", "ngg")
        Strng = Strng.replace("Mc", "njc")
        Strng = Strng.replace("Mj", "njj")
        Strng = Strng.replace("Md", "nd")
        Strng = Strng.replace("Mt", "nt")
        Strng = Strng.replace("M", 'm')

        Strng = Strng.replace("ngk", "nk")
        Strng = Strng.replace("ngg", "ng")
        Strng = Strng.replace("njc", "nc")
        Strng = Strng.replace("njj", "nj")

        Strng = Strng.replace("jnj", "jny")
    else:
        pass

    return Strng


def FixWarangCiti(Strng, reverse = False):
    ListC = "(" + "|".join(GM.CrunchSymbols(GM.Consonants, 'WarangCiti')) + ')'
    ListV = "(" + "|".join(GM.CrunchSymbols(GM.Vowels, 'WarangCiti') + ['\u200D']) + ')'

    if not reverse:
        Strng = re.sub(ListC + ListC, r'\1' + '\u200D' + r'\2', Strng)

        # Remove the inherent vowel
        Strng = re.sub(ListC + '(\U000118C1\U000118D9\u02BE)', r'\1' + '\u00BD', Strng)

        Strng = re.sub(ListC + '(\U000118C1)', r'\1', Strng)

        Strng = re.sub(ListV + '(\U000118C0)', r'\1' + '\u200D' + r'\2', Strng)

        Strng = Strng.replace('\u02BE', '')

        Strng = Strng.replace("𑣟\u02BF", "𑣙𑣗") # Remove Warang Citi Nukta

        # Brining back 'AA'

        Strng = Strng.replace('\u00BD', '\U000118C1')

    else:
        Strng = Strng.lower()
        ## Replace hb -> vQ
        Strng = Strng.replace("𑣙𑣗", "𑣟\u02BF") # Introduce Warang Citi Nukta
        Strng = Strng.replace('\u00D7', '\u200D')

        ## Reintroduce vowel AA
        Strng = re.sub(ListC + '(\U000118C1)', r'\1' + '\u00BD',Strng)
        Strng = re.sub('(\u02BF)' + '(\U000118C1)', r'\1' + '\U000118C1\u00BD',Strng)

        # Introduce the inhernt  Vowel
        Strng = re.sub(ListC + '(?!' + ListV + ')', r'\1' + '\U000118C1', Strng)

        ## Retain Aspirates
        Strng = re.sub('([\U000118D4\U000118D5\U000118CC\U000118CB\U000118CF\U000118CE\U000118D2\U000118D1\U000118D5\U000118D4\U000118D8\U000118D7\U000118DB])(\u200D)(𑣙)', r'\1' + '\u00D6' + r'\3', Strng)
        Strng = Strng.replace('\u200D', '')
        Strng = Strng.replace('\u00D6', '\u200D')

        ## Move vowel signs and nUkta viQ -> vQi
        Strng = re.sub('(𑣁)' + '(\u02BF)' + ListV , r'\2\3', Strng)

        ## Remove a if necessary
        Strng = Strng.replace('𑣁' + '\u02BB', '')

        Strng = Strng.replace('\U000118C1\u00BD', '\U000118C1\U000118D9\u02BE')

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
        Strng = Strng.replace("\u193A\u1922", "\u1922\u193A")
        Strng = re.sub('(' + '|'.join(FinalCons) + ')' + '(?=[ᤕᤖᤘ])', r'\1' + '\u200C', Strng)
        Strng = re.sub('([ᤀᤁᤂᤃᤄᤅᤆᤇᤈᤉᤊᤋᤌᤍᤎᤏᤐᤑᤒᤓᤔᤕᤖᤗᤘᤚᤛᤜᤠᤣᤥᤧᤨᤩᤪᤫ])᤺', r'\1' + '꞉', Strng)
        ## Modifying letter colon ## Fix this only with aH ᤆᤠ᤺ᤣ
    else:
        Strng = Strng.replace("\u1922\u193A", "\u193A\u1922")
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

        Strng = Strng.replace('ऱ्', 'ऱ्‌') ## Prevent RRA from forming conjuncts

        ## Except for YA and HA

        Strng = Strng.replace('ऱ्‌य', 'ऱ्य')
        Strng = Strng.replace('ऱ्‌ह', 'ऱ्ह')


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

        Strng = Strng.replace('𑄣𑄳𑄦', '𑅄')
        Strng = Strng.replace('𑄣𑄴𑄦', '𑅄')

        ## Ai => kai
        Strng = re.sub("("+listC+")"+"(𑄃𑄨)", r'\1' + '\U0001112D', Strng)
        ## ei' => kei
        Strng = Strng.replace('\U0001112C𑄃𑄨ʼ', '\U00011146', )


    else:
        Strng = PostProcess.ChakmaGemination(Strng, reverse = True)

        Strng = Strng.replace('𑅄', '𑄣𑄳𑄦')

        Strng = Strng.replace('\U00011133\U00011103', '\U00011145')
        Strng = Strng.replace('\U00011133\U00011104', '\U00011146')

        Strng = Strng.replace('\U0001112D', '𑄃𑄨')
        Strng = Strng.replace('\U00011146', '\U0001112C𑄃𑄨ʼ')

        Strng = Strng.replace("\U00011127","\u02BE")
        Strng = re.sub("("+listC+")"+"(?!"+listV+'|\u02BE'+")",r'\1''\U00011127',Strng)
        Strng = Strng.replace("\u02BE","")

    yrlvn = "("+"|".join(Chakma.ConsonantMap[19:20]+Chakma.ConsonantMap[26:29])+")"

    if not reverse:
        # Subjoined consonants
        # Usual convention
        Strng = re.sub("\U00011134"+"(?="+yrlvn+")","\U00011133",Strng)

        Strng = PostProcess.ChakmaGemination(Strng)
    else:
        # Reverse above
        Strng = Strng.replace("\U00011133","\U00011134")

        # Reverse independetnet vowels to a-based vowels
        vowelDepA = ["𑄃𑄨", "𑄃𑄪", "𑄃𑄬"]
        vowelIndep = ["\U00011104", "\U00011105" , "\U00011106"]

        for x, y in zip(vowelDepA, vowelIndep):
            Strng = Strng.replace(y, x)

    ###  O/Sub-va lookign similar; check

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
        Strng = Strng.replace('ə̸ə̸', 'ɑ̷ː')
    else:
        Strng = Strng.replace('ɑ̷ː', 'ə̸ə̸')
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
    else:
        Strng = Strng.replace('ఁ', 'ఀ')

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

    # Ra/La + vira -> Subjoined
    for x,y in zip(Cons,Sub):
        if not reverse:
            Strng = Strng.replace(x,y)
        else:
            Strng = Strng.replace(y,x)

    if not reverse:
        # Strng = Strng.replace("\u1A63\u1A74","\u1A74\u1A63") # kAM -> kMA (Like Thai ำ )
        # Check above in Pali texts
        pass
    else:
        #Strng = Strng.replace("\u1A74\u1A63","\u1A63\u1A74") # kAM <- kMA
        pass

    ListC ='|'.join(GM.CrunchSymbols(GM.Consonants,'TaiTham'))
    ng = TaiTham.ConsonantMap[4]+vir

    if not reverse:
        # Mai Kang Lai
        Strng = re.sub('('+ng+')'+'('+ListC+')','\u1A58'+r'\2',Strng)
        # Subjoining Virama
        Strng = re.sub(vir+'('+ListC+')','\u1A60'+r'\1',Strng)
        # Great Sa
        Strng = Strng.replace('ᩈ᩠ᩈ','ᩔ')

        # Fix Tall A
        TallACons = '|'.join(['ᩅ', 'ᨴ', 'ᨵ', 'ᨣ']) ## va da dha ga

        Strng = PostProcess.FixTallA(Strng, TallACons)

        Strng = Strng.replace('\u1A55\u1A60\u1A3F', '\u1A60\u1A3F\u1A55') # Fix krya

        Strng = Strng.replace('\u1A60\u1A47', vir + '\u1A47') ## Fonts don't support SSA conjunct

    else:
        AA = 'ᩣ'
        Strng = Strng.replace('ᩔ', 'ᩈ᩠ᩈ') ## Reverse great sa
        Strng = re.sub('('+ListC+')'+'\u1A58',r'\1' + ng,Strng) # Reverse: Kai mang Lai -> ng + virama
        Strng = Strng.replace('\u1A60',vir) # Regular Virama for Transliteration
        Strng = Strng.replace("ᩤ", AA) # Reverse Tall A

        Strng = Strng.replace('\u1A60\u1A3F\u1A55', '\u1A55\u1A60\u1A3F') # Rever krya


    return Strng

def FixLaoTham(Strng, reverse=False):
    Strng = FixTaiTham(Strng, reverse)

    return Strng

def FixLueTham(Strng, reverse=False):
    Strng = FixTaiTham(Strng, reverse)

    ListC ='|'.join(GM.CrunchSymbols(GM.Consonants,'TaiTham'))
    if not reverse:
        E = "ᩮ"
        AA = 'ᩣ'
        TallACons = '|'.join(['ᩅ', 'ᨴ', 'ᨵ', 'ᨣ']) ## va da dha ga
        Strng = re.sub('('+TallACons+')(᩠)('+ListC +')'+'('+E+'?)'+AA,r'\1\2\3\4'+'ᩤ',Strng)
        Strng = re.sub('('+TallACons+')(᩠)('+ListC +')'+'(᩠)('+ListC +')'+'('+E+'?)'+AA,r'\1\2\3\4\5\6'+'ᩤ',Strng)
    else:
        pass

    return Strng

def FixKhuenTham(Strng, reverse=False):
    Strng = FixTaiTham(Strng, reverse)

    ListC ='|'.join(GM.CrunchSymbols(GM.Consonants,'TaiTham'))
    if not reverse:
        E = "ᩮ"
        AA = 'ᩣ'
        TallACons = '|'.join(['ᩅ', 'ᨴ', 'ᨵ', 'ᨣ']) ## va da dha ga
        Strng = re.sub('('+TallACons+')(᩠)('+ListC +')'+'('+E+'?)'+AA,r'\1\2\3\4'+'ᩤ',Strng)
        Strng = re.sub('('+TallACons+')(᩠)('+ListC +')'+'(᩠)('+ListC +')'+'('+E+'?)'+AA,r'\1\2\3\4\5\6'+'ᩤ',Strng)
    else:
        pass

    return Strng

# Transcription for Native Lao
def LaoTranscribe(Strng,reverse=False):
    from . import PostProcess as pp

    shortA, conjA = '\u0EB0', '\u0EB1'

    if not reverse:
        Strng = pp.ThaiLaoTranscription(Strng,"Lao",shortA,conjA)
    else:
        Strng = pp.ThaiLaoTranscription(Strng,"Lao",shortA, conjA,reverse=True)

    return Strng

# Transcription for Pali Lao
def LaoPaliTranscribe(Strng,reverse=False, anusvaraChange = True):
    from . import PostProcess as pp
    shortA, conjA = '\u0EB0', '\u0EB1'

    if not reverse:
        Strng = pp.ThaiLaoTranscription(Strng,"LaoPali",shortA,conjA, anusvaraChange = anusvaraChange)
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
        Strng = Strng.replace('ꣳ', '𑍞')
        Strng = Strng.replace('ꣴ', '𑍟')
        Strng = Strng.replace('𑌼𑍍', '𑌼𑍍\u200C')
    else:
        Strng = Strng.replace('𑌼𑍍\u200C', '𑌼𑍍')
        Strng = Strng.replace('॑', '᳚')
        Strng = Strng.replace('᳴', '॑')
        Strng = Strng.replace('𑍞', 'ꣳ')
        Strng = Strng.replace('𑍟', 'ꣴ')

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

        vir = Ahom.ViramaMap[0]
        anu = Ahom.AyogavahaMap[1]

        #reverse closed syllable e
        Strng = re.sub(anu + '\U00011727' + '(?!\U00011728)', '\U00011726\U00011727\U0001172A', Strng)
        Strng = re.sub('(\U00011726)(.)('+vir+')', '\U00011726\U00011727'+r'\2\3', Strng)

        #rever closed syllable o
        Strng = re.sub('(\U00011728)(.)('+vir+')', '\U00011726\U00011721'+r'\2\3', Strng)

        Strng = Strng.replace(anu + '\U00011728', '\U00011726\U00011721\U0001172A')

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
        Strng = Strng.replace('\U00011A41', ' ')

        tsaSeries = ['𑨣', '𑨤', '𑨥']
        caSeries = ['𑨐','𑨑','𑨒']

        for x, y in zip(tsaSeries,caSeries):
            Strng = Strng.replace(y, x)

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
        ## The default behavior of Repha has been proposed to change
        # Strng = re.sub(ra + vir + '(' + ListC + ')', ra + vir + '\u200D' + r'\1', Strng)
    else:
        pass

    return Strng