# -*- coding: utf-8 -*-

from aksharamukha import Convert as cn
import xml.etree.ElementTree as ET
from aksharamukha import GeneralMap as GM
import re

def GetSyllables(Strng,Script):

    if Script not in GM.IndicScripts:

        ListV = '|'.join(sorted(GM.CrunchSymbols(GM.Vowels,Script),key=len,reverse=True))
        ListC = '|'.join(sorted(GM.CrunchSymbols(GM.Consonants,Script),key=len,reverse=True))
        ListA = '|'.join(sorted(GM.CrunchSymbols(GM.CombiningSigns,Script),key=len,reverse=True))

        Sylbl = re.compile('(('+ListC+')*'+'(('+ListV+')('+ListA+')?)?)')

        ListSyl = [Mtch[0] for Mtch in Sylbl.findall(Strng) if Mtch[0] != '']

    return ListSyl

def GetSidRanCh(Char,Script,reverse=False):

    if Script is 'Siddham':
        tree = ET.parse('C:\Personal Projects\\aksharamukha\ScriptMap\EastIndic\siddham.xml')
        tbl = 'tbl_siddham'
        defChar = '袎'
    elif Script is 'Ranjana':
        tree = ET.parse('C:\Personal Projects\\aksharamukha\ScriptMap\EastIndic\\ranjana.xml')
        tbl = 'tbl_lantsa'
        defChar = '跬'

    root = tree.getroot()
    fnd = False

    for mapng in root.findall(tbl):
        for ch in mapng:
            if ch.text == Char:
                fndmap = mapng
                fnd = True
        if fnd:
            break

    if fnd:
        if not reverse:
            return fndmap.find('chars').text
        else:
            return fndmap.find('ime').text
    else:
        return defChar

def SiddhRanjConv(Strng,Script,reverse=False):
    if not reverse:
        Sylbl = sorted(GetSyllables(Strng,'HK'),key=len,reverse=True)

        SylblCon = [GetSidRanCh(x,Script) for x in Sylbl if x != '']

        for x,y in zip(Sylbl,SylblCon):
            Strng = Strng.replace(x,y)

        Strng = Strng.replace('_','')

    else:
        CharList = list(set(Strng.replace(" ","")))
        if Script == "Siddham":
            Strng = Strng.replace("袎","(.)")
        else:
            Strng = Strng.replace("跬","(.)")
        for char in CharList:
            Strng = Strng.replace(char,GetSidRanCh(char,Script,reverse=True))

    return Strng

if __name__ == "__main__":
    print(cn.convertScript("namo", "HK", "Siddham"))
    print(cn.convertScript("巧伕", "Siddham", "Telugu"))
    print(cn.convertScript("巧伕", "Siddham", "Ranjana"))
    print(cn.convertScript("呣呺","Ranjana","Kannada"))
