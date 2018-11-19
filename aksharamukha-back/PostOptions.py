# -*- coding: utf-8 -*-

## Include AnusvaraToNasal for Santali, TolongSikhi, Limbu, Lepcha

## Generate without Short Vowels - Only include for preserver "Source"

import PostProcess as PP
import GeneralMap as GM

def ApplyScriptDefaults(Strng,Source,Target):
    Options = []

    if Target in GM.IndicScripts:
        Options += []#['RemoveDiacritics'] #Sometimes you may wanna keep it. Adjust options

    if Target == 'Telugu' or Target == 'Kannada':
        Options += ['NasalToAnusvara','MToAnusvara']

    elif Target == 'Malayalam':
        Options += ['MalayalamAnusvaraNasal', 'MToAnusvara', 'MalayalamremoveHistorical']

    elif Target == 'Tamil':
        Options += ['TamilNaToNNa','AnusvaraToNasal']

    elif Target == 'Bengali':
        Options += ['VaToBa','YaToYYa','KhandaTa']

    elif Target == 'MeeteiMayek':
        Options += ['MeeteiMayekremoveHistorical']

    elif Target == 'Limbu':
        Options += ['LimburemoveHistorical']

    elif Target == 'Assamese':
        Options += ['YaToYYa','KhandaTa']

    elif Target == 'Oriya':
        Options += ['VaToBa','YaToYYa']

    elif Target == 'Sinhala':
        Options += []

    elif Target == 'Gurmukhi':
        Options += ['GurmukhiTippiBindu','GurmukhiTippiGemination']

    elif Target == 'Saurashtra':
        Options += ['SaurashtraHaru']

    elif Target == 'Thai':
        Options += []

    elif Target == 'Tibetan':
        Options += ['TibetanRemoveVirama', 'TibetanRemoveBa']

    elif Target == "Thaana":
        Options += ['ThaanaRemoveHistorical']

    elif Target == "Avestan":
        Options += ['AvestanConventions']

    elif Target == "Sundanese":
        Options += ['SundaneseRemoveHistoric']

    elif Target == "Multani":
        Options += ['MultaniAbjad']

    else:
        Options += []

    for Option in Options:
        if Option.find(Target) != -1:
            Strng = getattr(__import__('PostProcess'),Option)(Strng)
        else:
            Strng = getattr(__import__('PostProcess'),Option)(Strng,Target)

    return Strng