# -*- coding: utf-8 -*-

from . import GeneralMap as GM, PreProcess as PrP, ConvertFix as CF
from . import PostProcess as PP
import aksharamukha.ScriptMap.EastIndic.SiddhamRanjana as SR
import string
import re
from functools import cmp_to_key


### Mapping : https://viss.wordpress.com/2015/05/17/how-to-transcribe-pa%E1%B8%B7i-in-lanna-and-burmese/ ###
### Assmae kva -> becomes kba ## Check Assamese Wikipedia
### ITRANS features like comments implement
### Check Aksharamukha Todo list... and cross check and implement that
### Add HK-Itrans Option of Vishvas Vasuki
### Remove Diacritics
### Add space before punctiations and then remove it

# Sort Functions

def TamilSort(x,y):
    if('\u0B83' in x[0] and len(x[0]) != 1):
        return -1
    elif(x[0] < y[0]):
        return 1
    else:
        return 0

def lenSort(x,y):
    if(len(x[0]) > len(y[0])):
        return -1
    else:
        return 0

def convertInter(Strng,Source):
    ScriptAll = GM.Vowels+GM.Consonants+GM.CombiningSigns+GM.Numerals+GM.Signs+GM.Aytham
    SourceScript = GM.CrunchSymbols(ScriptAll,Source)
    TargetScript = GM.CrunchSymbols(ScriptAll,GM.Inter)
    ScriptMapAll = sorted(zip(SourceScript,TargetScript),key=cmp_to_key(lenSort))

    for x,y in ScriptMapAll:
        Strng = Strng.replace(x,y)

    return Strng

# Conversion Module
def convertScript(Strng,Source,Target):
    #print(Target)
    #print(Target in GM.IndicScripts)

    charPairs=[];
    Schwa = '\uF000'
    DepV = '\u1E7F'

    if Source in GM.LatinScripts and Target in GM.IndicScripts:
        try:
            Strng = getattr(CF,"Fix"+Source)(Strng,reverse=True)
        except AttributeError:
            pass
            #print #"Fix"+Target+" doesn't exist - Reverse"

        ## Joiners {} : ZWNJ : () : ZWJ
        Strng = Strng.replace("{}", "\u200C")
        Strng = Strng.replace("()", "\u200D")

        Strng = CF.VedicSvarasLatinIndic(Strng, Source)

        punc =  '(' + '|'.join(["\u005C"+x for x in list(string.punctuation)]+ ['\s']
                    + [x.replace('.', '\.') for x in GM.CrunchSymbols(GM.Signs,Source)[1:3]]) + ')'

        sOm, tOm = GM.CrunchList('OmMap', Source)[0],GM.CrunchList('OmMap', Target)[0]

        Strng = re.sub(punc + sOm + punc, r'\1' + tOm + r'\2', Strng)
        Strng = re.sub('^' + sOm + punc, tOm + r'\1', Strng)
        Strng = re.sub(punc + sOm + '$', r'\1' + tOm, Strng)
        Strng = re.sub('^' + sOm + '$', tOm, Strng)

        punc = '(\s)'

        Strng = re.sub(punc + sOm + punc, r'\1' + tOm + r'\2', Strng)
        Strng = re.sub('^' + sOm + punc, tOm + r'\1', Strng)
        Strng = re.sub(punc + sOm + '$', r'\1' + tOm, Strng)
        Strng = re.sub('^' + sOm + '$', tOm, Strng)

        SourceOld = Source

        Strng = convertInter(Strng,Source)
        Source = GM.Inter
        Strng = PrP.RomanPreFix(Strng,Source)

        ## HK l_R l_RR

        Strng = Strng.replace("ṿ×_","ṿ")
        Strng = Strng.replace("ṿ×_","ṿ")

        ha = GM.CrunchSymbols(GM.Consonants,Source)[32]
        charPairs=[]

        for charList in GM.ScriptAll:
            # Crunch all related characters into a list
            TargetScript = GM.CrunchSymbols(GM.retCharList(charList),Target)
            if charList == 'VowelSigns':
                # Add DepVSign to all VowelSigns to differentiate from Independent Vowels
                SourceScript = [DepV+x for x in GM.CrunchSymbols(GM.VowelSigns,Source)]
            else:
                SourceScript = GM.CrunchSymbols(GM.retCharList(charList),Source)
            # Create a Tuple for the conversion pair
            ScriptMap = list(zip(SourceScript,TargetScript))
            # Sort the mapping in descending order. Longer Characters are to be replaced first. ऍˇ > ऍ
            ScriptMap.sort(reverse=True);
            charPairs= charPairs + ScriptMap

        charPairs = sorted(charPairs,key=cmp_to_key(lenSort))

        # Perform replacement sequentially for each character group
        for x,y in charPairs:
            #print x,y
            Strng = Strng.replace(x,y)

        ## a_i => a<dev>i<dev> ; a_u = a<dev>u<dev>
        Strng=Strng.replace('_' + GM.CrunchSymbols(GM.Vowels,Target)[2],  GM.CrunchSymbols(GM.Vowels,Target)[2])
        Strng=Strng.replace('_' + GM.CrunchSymbols(GM.Vowels,Target)[4],  GM.CrunchSymbols(GM.Vowels,Target)[4])

        ## Joiners Vir + ZWJ
        vir = GM.CrunchList('ViramaMap', Target)[0]
        Strng = Strng.replace(vir + "[]", "\u200D" + vir)

        #print Strng

        #print(Strng)

        # Apply Fixes on the Output based on the Script
        Strng = CF.FixIndicOutput(Strng, Source, Target)

        #print(Strng)

    elif Source in GM.LatinScripts and Target in GM.LatinScripts:
        try:
            Strng = getattr(CF,"Fix"+Source)(Strng,reverse=True)
        except AttributeError:
            pass
            #print #"Fix"+Target+" doesn't exist - Reverse"

        ScriptAll = GM.Vowels+GM.Consonants+GM.CombiningSigns+GM.Numerals+GM.Signs+GM.Aytham

        Strng = convertInter(Strng,Source)

        SourceScript = GM.CrunchSymbols(ScriptAll,GM.Inter)
        TargetScript = GM.CrunchSymbols(ScriptAll, Target)
        ScriptMapAll = list(zip(SourceScript,TargetScript))

        for x,y in ScriptMapAll:
            Strng = Strng.replace(x,y)

        Strng = CF.PostFixRomanOutput(Strng,Source,Target)

    elif Source in GM.IndicScripts and Target in GM.IndicScripts:
        Strng = PrP.RemoveJoiners(Strng)

        Strng = CF.ShiftDiacritics(Strng,Source,reverse=True)
        try:
            Strng = getattr(CF,"Fix"+Source)(Strng,reverse=True)
        except AttributeError:
            pass
            #print #"Fix"+Target+" doesn't exist - Reverse"

        punc =  '(' + '|'.join(["\u005C"+x for x in list(string.punctuation)]+ ['\s']
                    + [x.replace('.', '\.') for x in GM.CrunchSymbols(GM.Signs,Source)[1:3]]) + ')'

        sOm, tOm = GM.CrunchList('OmMap', Source)[0],GM.CrunchList('OmMap', Target)[0]

        if len(sOm) != 1:
            Strng = re.sub(punc + sOm + punc, r'\1' + tOm + r'\2', Strng)
            Strng = re.sub('^' + sOm + punc, tOm + r'\1', Strng)
            Strng = re.sub(punc + sOm + '$', r'\1' + tOm, Strng)
            Strng = re.sub('^' + sOm + '$', tOm, Strng)

        if len(sOm) == 1:
            Strng = Strng.replace(sOm, tOm)

        # Iterate for each character group
        for charList in GM.ScriptAll:
            # Crunch all related characters into a list
            SourceScript = GM.CrunchSymbols(GM.retCharList(charList),Source)
            TargetScript = GM.CrunchSymbols(GM.retCharList(charList),Target)
            # Create a Tuple for the conversion pair
            ScriptMap = list(zip(SourceScript,TargetScript))
            # Sort the mapping in descending order. why ?
            ScriptMap.sort(reverse=True)
            charPairs= charPairs + ScriptMap

        #Sort based on Length - Longest first
        charPairs = sorted(charPairs,key=cmp_to_key(lenSort))

        # Perform replacement sequentially for each character group
        for x,y in charPairs:
            #print x,y
            Strng = Strng.replace(x,y)
            #print Strng

        #Strng = Strng.replace(GM.CrunchList('OmMap', Source)[0],GM.CrunchList('OmMap', Target)[0])
        # Apply Fixes on the Output based on the Script

        Strng = CF.FixIndicOutput(Strng, Source, Target)

    elif Source in GM.IndicScripts and Target in GM.LatinScripts:
        Strng = PrP.RemoveJoiners(Strng)
        Strng = CF.ShiftDiacritics(Strng, Source, reverse=True)
        try:
            Strng = getattr(CF,"Fix"+Source)(Strng,reverse=True)
        except AttributeError:
            pass
            #print #"Fix"+Target+" doesn't exist - Reverse"

        sOm, tOm = GM.CrunchList('OmMap', Source)[0],GM.CrunchList('OmMap', Target)[0]

        Strng = Strng.replace(sOm, tOm)

        # Iterate for each character group
        for charList in GM.ScriptAll:
            # Crunch all related characters into a list
            SourceScript = GM.CrunchSymbols(GM.retCharList(charList),Source)
            if charList == 'Consonants':
                # Add Schwa to all Roman consonants. Basically, the Roman script is "Indianized"
                TargetScript = [x+Schwa for x in GM.CrunchSymbols(GM.Consonants,Target)]
            elif charList == 'Vowels':
                # Add DepVSign to all Independent vowel to differentiate from vowel sign.
                TargetScript = [DepV+x for x in GM.CrunchSymbols(GM.Vowels,Target)]
            else:
                TargetScript = GM.CrunchSymbols(GM.retCharList(charList),Target)
            # Create a Tuple for the conversion pair
            ScriptMap = list(zip(SourceScript,TargetScript))
            # Sort the mapping in descending order. Longer Characters are to be replaced first. ऍˇ > ऍ
            ScriptMap.sort(reverse=True);
            charPairs= charPairs + ScriptMap

        charPairs = sorted(charPairs,key=cmp_to_key(lenSort))

        # Perform replacement sequentially for each character group
        for x,y in charPairs:
            Strng = Strng.replace(x,y)

        # Remove all intermediate characters and fix Output
        Strng = CF.FixRomanOutput(Strng,Target)

        Strng = CF.VedicSvarsIndicLatin(Strng)

        Strng = CF.PostFixRomanOutput(Strng,Source,Target)

        # Convert Syllabic lR -> l_R Important !!!
    elif Source in GM.SiddhamRanjana:
        Strng = SR.SiddhRanjConv(Strng,Source,reverse=True)
        Strng = convertScript(Strng,"HK",Target)

    elif Target in GM.SiddhamRanjana:
        Strng = convertScript(Strng,Source,"HK")
        Strng = SR.SiddhRanjConv(Strng,Target)

    Strng = PP.default(Strng)

    return Strng