# -*- coding: utf-8 -*-

### Introduce Nasal to Anusvara for scripts lacking nasal letters but having Anusvara/Chandrabindu

import importlib, string
import re
from functools import reduce

GURMUKHI = 'Gurmukhi'

SINHALA = 'Sinhala'

ASSAMESE = 'Assamese'

DEVANAGARI = "Devanagari"

HK = 'HK'

ITRANS = 'Itrans'

IAST = 'IAST'

ISO = 'ISO'

TITUS = 'Titus'

URDU = 'Urdu'

ZANABAZAR_SQUARE = 'ZanabazarSquare'

RUSSIAN_CYRILLIC = 'RussianCyrillic'

SIDDHAM_UNICODE = 'siddhamUnicode'

WARANG_CITI = 'WarangCiti'

TAI_THAM = 'TaiTham'

SYLOTI_NAGRI = 'SylotiNagri'

SORA_SOMPENG = 'SoraSompeng'

SANTALI = 'Santali'

PHAGS_PA = 'PhagsPa'

OLD_PERSIAN = 'OldPersian'

MEETEI_MAYEK = 'MeeteiMayek'

BURMESE = 'Burmese'

MYANMAR = 'Myanmar'

BATAK_KARO = 'BatakKaro'

BATAK = 'Batak'

LAO_PALI = 'LaoPali'

LAO = 'Lao'

BENGALI = 'Bengali'

# Crunch Symbols

def ScriptPath(Script):
    if Script in MainIndic:
        return 'aksharamukha.ScriptMap.MainIndic.'+Script
    elif Script in EastIndic:
        return 'aksharamukha.ScriptMap.EastIndic.'+Script
    elif Script in Roman:
        return 'aksharamukha.ScriptMap.Roman.'+Script
    elif Script in NonIndic:
        return 'aksharamukha.ScriptMap.NonIndic.'+Script

def retCharList(charList):
    return globals()[charList]

def CrunchSymbols(Part,Script):
    ModScript = importlib.import_module(ScriptPath(Script))
    return reduce(lambda x,y : x+y,[getattr(ModScript,Var) for Var in Part])

def CrunchList(List,Script):
    try:
      ModScript = importlib.import_module(ScriptPath(Script))
    except:
      import logging
      logging.exception('The script ' + Script + ' cannot be found')
      return ''

    return getattr(ModScript,List)

#Introduce in all Latin Conversions
def EscapeChar(Strng):
    punct = "".join(['\\'+x for x in string.punctuation])

    return re.sub('('+punct+')',r'\\'+r'\1',Strng)


# Collection of Symbols

VedicSvaras = '('+ '|'.join(['᳚', '॑', '॒']) + ')?'
VedicSvarasList = ['᳚', '॑', '॒']

Vowels = ['VowelMap','SouthVowelMap','ModernVowelMap','SinhalaVowelMap']
VowelSignsNV = ['VowelSignMap','SouthVowelSignMap','ModernVowelSignMap','SinhalaVowelSignMap']
VowelSigns = ['ViramaMap','VowelSignMap','SouthVowelSignMap','ModernVowelSignMap','SinhalaVowelSignMap']
CombiningSigns = ['AyogavahaMap','NuktaMap']
Consonants = ['ConsonantMap','SouthConsonantMap','NuktaConsonantMap','SinhalaConsonantMap']

Signs = ['SignMap']
Numerals = ['NumeralMap']
Aytham =['Aytham']
om = ['OmMap']
virama = ['ViramaMap']

MainIndic = ['TamilExtended','MasaramGondi','GunjalaGondi','Dogra', 'Ranjana', 'Khojki','GranthaGrantamil', 'Multani', 'Ahom', 'Mahajani','SiddhamDevanagari', 'Vatteluttu', 'GranthaPandya', 'Khudawadi', 'Bhaiksuki', 'Sharada', 'Newa', SYLOTI_NAGRI, 'Takri', 'Tirhuta', 'Modi', 'Kaithi', 'Kharoshthi','Lepcha','Chakma','Brahmi', MEETEI_MAYEK,'Limbu',
             ASSAMESE, BENGALI, DEVANAGARI, 'Grantha', 'Gujarati', GURMUKHI, 'Kannada', 'Malayalam', 'Oriya', 'Saurashtra',
             SINHALA, 'Tamil', 'TamilBrahmi', 'TamilGrantha', 'Telugu', URDU]
EastIndic =['LaoTham', 'LueTham', 'KhuenTham', 'Marchen', 'Soyombo', 'KhomThai', 'KhamtiShan', 'TaiLaing', 'Mon', 'Shan', ZANABAZAR_SQUARE,'Rejang', 'Lao2','Buhid', 'Hanunoo', 'Siddham', 'Tibetan',LAO,TAI_THAM,'Cham',BATAK_KARO,'BatakPakpak','BatakSima','BatakToba','BatakManda',LAO_PALI,PHAGS_PA,'Buginese','Tagbanwa','Tagalog','Sundanese','Balinese',BURMESE,'Javanese','Khmer','Siddham','Ranjana','Thaana','Thai']
NonIndic = [OLD_PERSIAN]
Roman =['Mongolian', 'SLP1', 'Wancho', 'Mro', 'IASTPali', 'HanifiRohingya', 'Ariyaka', 'RomanReadable', 'Aksharaa', WARANG_CITI, SORA_SOMPENG,"WX-kok",'Avestan',HK,IAST,ISO,ITRANS,TITUS,TITUS,'Velthuis','WX','Inter','IPA','TolongSiki',SANTALI,RUSSIAN_CYRILLIC]
RomanDiacritic = [IAST,TITUS,ISO,'IPA']

ScriptCategory = {}

ScriptCategory['IndianMain'] = ['GranthaGrantamil', ASSAMESE, BENGALI, DEVANAGARI, 'Gujarati', GURMUKHI, 'Kannada', 'Malayalam', 'Oriya',
                                SINHALA, 'Tamil', 'Telugu', URDU]
ScriptCategory['IndianMinority'] = ['Brahmi','Chakma','Grantha','Lepcha','Limbu',MEETEI_MAYEK,'Saurashtra','TamilBrahmi','TamilGrantha', 'Kaithi']
ScriptCategory['EastAsianPaliSans'] = ['Balinese',BURMESE,'Cham','Javanese','Khmer',LAO_PALI,'Lao',PHAGS_PA,'TaiTham','Thaana','Thai','Tibetan']
ScriptCategory['EastAsianIndFili'] = [BATAK_KARO,'BatakManda','BatakPakpak','BatakSima','BatakToba','Buginese','Sundanese','Tagalog','Tagbanwa']
ScriptCategory['IndianAlpha'] = [SANTALI,'TolongSiki']
ScriptCategory['RomanDiacritic'] = [IAST,'IPA',ISO,TITUS]
ScriptCategory['RomanNonDiacritic'] = [HK,ITRANS,RUSSIAN_CYRILLIC,'Velthuis','WX']
ScriptCategory['NonIndic'] = ['Avestan',OLD_PERSIAN]

Inter = "Inter"

Characters = Vowels + VowelSigns + CombiningSigns + Consonants
CharactersNV = Vowels + VowelSignsNV + CombiningSigns + Consonants

Diacritics = ['ʽ', '\u00B7', '\u00B9','\u00B2','\u00B3','\u2074','\u2081','\u2082','\u2083','\u2084']
DiacriticsRemovable = ['ʼ', 'ˇ', 'ˆ', '˘', '\u00B7']
DiacriticsRemovableTamil = ['ˇ', 'ˆ', '˘', '\u00B7']

ScriptAll = ['Aytham', 'Signs', 'CombiningSigns', 'VowelSigns', 'Vowels', 'Consonants', 'Numerals']

IndicScripts = [
               'LaoTham',
               'LueTham',
               'KhuenTham',
               'TamilExtended',
               'Marchen',
               'MasaramGondi',
               'GunjalaGondi',
               'Soyombo',
               'Dogra',
               'KhomThai',
               'KhamtiShan',
               'TaiLaing',
               'Mon',
               'Khojki',
               'Shan',
               'Ranjana',
               ZANABAZAR_SQUARE,
               'Rejang',
               'GranthaGrantamil',
               DEVANAGARI,
               'Multani',
               'Ahom',
               'Mahajani',
               'Lao2',
               'Hanunoo',
               'Buhid',
               'Siddham',
               'SiddhamDevanagari',
               'GranthaPandya',
               'Vatteluttu',
               'Khudawadi',
               'Bhaiksuki',
               'Sharada',
               'Newa',
               'Takri',
               SYLOTI_NAGRI,
               'Tirhuta',
               'Modi',
               'Kaithi',
               'Kharoshthi',
               'Telugu',
               'Kannada',
               'Malayalam',
               'Gujarati',
               BENGALI,
               'Oriya',
    GURMUKHI,
               'Tamil',
    ASSAMESE,
               'Saurashtra',
               'TamilBrahmi',
               'Grantha',
               'TamilGrantha',
    SINHALA,
               'Khmer',
               BURMESE,
               URDU,
               'Balinese',
               'Javanese',
               'Thaana',
               'Tibetan',
               'Thai',
               OLD_PERSIAN,
               'Limbu',
               'Lepcha',
               'Sundanese',
               'Tagalog',
               'Tagbanwa',
               'Buginese',
               'Chakma',
               PHAGS_PA,
               MEETEI_MAYEK,
               LAO_PALI,
               BATAK_KARO,'BatakPakpak','BatakSima','BatakToba','BatakManda',
               'Cham',
               'TaiTham',
               'Lao',
               'Brahmi'
               ]

SiddhamRanjana = ['Ranjana']

LatinScripts = ['Mongolian', 'SLP1', 'Wancho', 'Mro', 'IASTPali', 'HanifiRohingya','Ariyaka', 'RomanReadable', 'Aksharaa', WARANG_CITI, SORA_SOMPENG,'WX-kok','Avestan',ISO,IAST,HK,TITUS,ITRANS,'Velthuis','WX','Inter','IPA','TolongSiki',SANTALI,RUSSIAN_CYRILLIC]

Gemination =  {
               GURMUKHI: '\u0A71',
               'Thaana' : '\u0787\u07B0',
               URDU: '\u0651',
               'Grantha': '𑌂',
               'Malayalam': 'ം',
               'Khojki': '\U00011237'
              }

Transliteration = ['IASTPali', 'RomanReadable', 'Aksharaa', ISO, IAST, HK,TITUS,ITRANS,'Velthuis','WX', 'IPA', RUSSIAN_CYRILLIC]


