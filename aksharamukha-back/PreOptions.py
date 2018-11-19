# -*- coding: utf-8 -*-

from . import PreProcess as PP

def ApplyPreProcessing(Strng,Source,Target):
    if Target == "PhagsPa":
        Options = ['PhagsPaArrange']
    else:
        Options = []
        
    for Option in Options:
        if Option.find(Target) != -1:
            Strng = getattr(__import__('PreProcess'),Option)(Strng,Source)
        else:
            Strng = getattr(__import__('PreProcess'),Option)(Strng,Target)
            
    return Strng        
