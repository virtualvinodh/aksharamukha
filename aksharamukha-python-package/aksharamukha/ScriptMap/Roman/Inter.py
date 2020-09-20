# -*- coding: utf-8 -*-

# Script Mapping for ISO


VowelMap =  [chr(0xE000+i) for i in range(0,14)]

SouthVowelMap = [chr(0xE100+i) for i in range(0,2)]

ModernVowelMap = [chr(0xE200+i) for i in range(0,2)]

SinhalaVowelMap = [chr(0xE300+i) for i in range(0,1)]
    
VowelSignMap =  VowelMap[1:]
               
SouthVowelSignMap = SouthVowelMap[:]

ModernVowelSignMap = ModernVowelMap[:]

SinhalaVowelSignMap = SinhalaVowelMap[:]

AyogavahaMap = [chr(0xE400+i) for i in range(0,3)]
    
ViramaMap =  [
             '\u00D7'
             ]

ConsonantMap =  [chr(0xE500+i) for i in range(0,33)]

SouthConsonantMap = [chr(0xE600+i) for i in range(0,4)]

NuktaConsonantMap =  [chr(0xE700+i) for i in range(0,8)]

NuktaMap = [chr(0xE800+i) for i in range(0,1)]
    
OmMap = [chr(0xE900+i) for i in range(0,1)]

SignMap = [chr(0xEA00+i) for i in range(0,3)]

SinhalaConsonantMap =[chr(0xEB00+i) for i in range(0,5)]

Aytham = [chr(0xEC00+i) for i in range(0,1)]

NumeralMap = [chr(0xED00+i) for i in range(0,10)]