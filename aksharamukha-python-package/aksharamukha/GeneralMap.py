# -*- coding: utf-8 -*-

### Introduce Nasal to Anusvara for scripts lacking nasal letters but having Anusvara/Chandrabindu

import importlib, string
import re
from functools import reduce

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

MainIndic = ['TamilExtended','MasaramGondi','GunjalaGondi','Dogra', 'Ranjana', 'Khojki','GranthaGrantamil', 'Multani', 'Ahom', 'Mahajani','SiddhamDevanagari', 'Vatteluttu', 'GranthaPandya', 'Khudawadi', 'Bhaiksuki', 'Sharada', 'Newa', 'SylotiNagri', 'Takri', 'Tirhuta', 'Modi', 'Kaithi', 'Kharoshthi','Lepcha','Chakma','Brahmi','MeeteiMayek','Limbu','Assamese','Bengali','Devanagari','Grantha','Gujarati','Gurmukhi','Kannada','Malayalam','Oriya','Saurashtra','Sinhala','Tamil','TamilBrahmi','TamilGrantha','Telugu','Urdu']
EastIndic =['LaoTham', 'LueTham', 'KhuenTham', 'Marchen', 'Soyombo', 'KhomThai', 'KhamtiShan', 'TaiLaing', 'Mon', 'Shan', 'ZanabazarSquare','Rejang', 'Lao2','Buhid', 'Hanunoo', 'Siddham', 'Tibetan','Lao','TaiTham','Cham','BatakKaro','BatakPakpak','BatakSima','BatakToba','BatakManda','LaoPali','PhagsPa','Buginese','Tagbanwa','Tagalog','Sundanese','Balinese','Burmese','Javanese','Khmer','Siddham','Ranjana','Thaana','Thai']
NonIndic = ['OldPersian']
Roman =['Mongolian', 'SLP1', 'Wancho', 'Mro', 'IASTPali', 'HanifiRohingya', 'Ariyaka', 'RomanReadable', 'Aksharaa', 'WarangCiti', 'SoraSompeng',"WX-kok",'Avestan','HK','IAST','ISO','Itrans','Titus','Titus','Velthuis','WX','Inter','IPA','TolongSiki','Santali','RussianCyrillic']
RomanDiacritic = ['IAST','Titus','ISO','IPA']

ScriptCategory = {}

ScriptCategory['IndianMain'] = ['GranthaGrantamil','Assamese','Bengali','Devanagari','Gujarati','Gurmukhi','Kannada','Malayalam','Oriya','Sinhala','Tamil','Telugu','Urdu']
ScriptCategory['IndianMinority'] = ['Brahmi','Chakma','Grantha','Lepcha','Limbu','MeeteiMayek','Saurashtra','TamilBrahmi','TamilGrantha', 'Kaithi']
ScriptCategory['EastAsianPaliSans'] = ['Balinese','Burmese','Cham','Javanese','Khmer','LaoPali','Lao','PhagsPa','TaiTham','Thaana','Thai','Tibetan']
ScriptCategory['EastAsianIndFili'] = ['BatakKaro','BatakManda','BatakPakpak','BatakSima','BatakToba','Buginese','Sundanese','Tagalog','Tagbanwa']
ScriptCategory['IndianAlpha'] = ['Santali','TolongSiki']
ScriptCategory['RomanDiacritic'] = ['IAST','IPA','ISO','Titus']
ScriptCategory['RomanNonDiacritic'] = ['HK','Itrans','RussianCyrillic','Velthuis','WX']
ScriptCategory['NonIndic'] = ['Avestan','OldPersian']

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
               'ZanabazarSquare',
               'Rejang',
               'GranthaGrantamil',
               'Devanagari',
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
               'SylotiNagri',
               'Tirhuta',
               'Modi',
               'Kaithi',
               'Kharoshthi',
               'Telugu',
               'Kannada',
               'Malayalam',
               'Gujarati',
               'Bengali',
               'Oriya',
               'Gurmukhi',
               'Tamil',
               'Assamese',
               'Saurashtra',
               'TamilBrahmi',
               'Grantha',
               'TamilGrantha',
               'Sinhala',
               'Khmer',
               'Burmese',
               'Urdu',
               'Balinese',
               'Javanese',
               'Thaana',
               'Tibetan',
               'Thai',
               'OldPersian',
               'Limbu',
               'Lepcha',
               'Sundanese',
               'Tagalog',
               'Tagbanwa',
               'Buginese',
               'Chakma',
               'PhagsPa',
               'MeeteiMayek',
               'LaoPali',
               'BatakKaro','BatakPakpak','BatakSima','BatakToba','BatakManda',
               'Cham',
               'TaiTham',
               'Lao',
               'Brahmi'
               ]

SiddhamRanjana = ['Ranjana']

LatinScripts = ['Mongolian', 'SLP1', 'Wancho', 'Mro', 'IASTPali', 'HanifiRohingya','Ariyaka', 'RomanReadable', 'Aksharaa', 'WarangCiti', 'SoraSompeng','WX-kok','Avestan','ISO','IAST','HK','Titus','Itrans','Velthuis','WX','Inter','IPA','TolongSiki','Santali','RussianCyrillic']

Gemination =  {
               'Gurmukhi' : '\u0A71',
               'Thaana' : '\u0787\u07B0',
               'Urdu': '\u0651',
               'Grantha': '𑌂',
               'Malayalam': 'ം',
               'Khojki': '\U00011237'
              }

Transliteration = ['IASTPali', 'RomanReadable', 'Aksharaa', 'ISO', 'IAST', 'HK','Titus','Itrans','Velthuis','WX', 'IPA', 'RussianCyrillic']


