import re
import json

def syllabify(inputtext):

    vowels = '\u0904-\u0914\u0960-\u0961\u0972-\u0977'
    consonants = '\u0915-\u0939\u0958-\u095F\u0978-\u097C\u097E-\u097F'
    glottal = '\u097D'

    vowel_signs = '\u093E-\u094C\u093A-\u093B\u094E-\u094F\u0955-\u0957\u1CF8-\u1CF9'
    nasals = '\u0900-\u0902\u1CF2-\u1CF6'
    visarga = '\u0903'
    nukta = '\u093C'
    avagraha = '\u093D'
    virama = '\u094D'

    vedic_signs = '\u0951-\u0952\u1CD0-\u1CE1\u1CED'
    visarga_modifiers = '\u1CE2-\u1CE8'
    combining = '\uA8E0-\uA8F1'

    om = '\u0950'

    accents = '\u0953-\u0954'
    dandas = '\u0964-\u0965'
    digits = '\u0966-\u096F'
    abbreviation = '\u0970'
    spacing = '\u0971'

    vedic_nasals = '\uA8F2-\uA8F7\u1CE9-\u1CEC\u1CEE-\u1CF1'
    fillers = '\uA8F8-\uA8F9'
    caret = '\uA8FA'
    headstroke = '\uA8FB'

    space = '\u0020'
    joiners = '\u200C-\u200D'

    syllables = []
    curr = ''

    # iterate over each character in the input. if a char belongs to a
    # class that can be part of a syllable, then add it to the curr
    # buffer. otherwise, output it to syllables[] right away.

    for char in inputtext:

        if re.match('[' + vowels + avagraha + glottal + om + ']', char):

            # need to handle non-initial independent vowel letters,
            # avagraha, and om

            if curr != '':
                syllables.append(curr)
                curr = char
            else:
                curr = curr + char

        elif re.match('[' + consonants + ']', char):

            # if last in curr is not virama, output curr as syllable
            # else add present consonant to curr

            if len(curr) > 0 and curr[-1] != virama:
                syllables.append(curr)
                curr = char
            else:
                curr = curr + char

        elif re.match('[' + vowel_signs + visarga + vedic_signs + ']', char):
            curr = curr + char

        elif re.match('[' + visarga_modifiers + ']', char):

            if len(curr) > 0 and curr[-1] == visarga:
                curr = curr + char
                syllables.append(curr)
                curr = ''
            else:
                syllables.append(curr)
                curr = ''

        elif re.match('[' + nasals + vedic_nasals + ']', char):

            # if last in curr is a vowel sign, output curr as syllable
            # else add present vowel modifier to curr and output as syllable

            vowelsign = re.match('[' + vowel_signs + ']$', curr)
            if vowelsign:
                syllables.append(curr)
                curr = ''
            else:
                curr = curr + char
                syllables.append(curr)
                curr = ''

        elif re.match('[' + nukta + ']', char):
            curr = curr + char

        elif re.match('[' + virama + ']', char):
            curr = curr + char

        elif re.match('[' + digits + ']', char):
            curr = curr + char

        elif re.match('[' + fillers + headstroke + ']', char):
            syllables.append(char)

        elif re.match('[' + joiners + ']', char):
            curr = curr + char

        else:
            pass
            #print ("unhandled: " + char + " ", char.encode('unicode_escape'))

    # handle remaining curr
    if curr != '':
        syllables.append(curr)
        curr = ''

    # return each syllable as item in a list
    return syllables

print('Vinodh')

file = open("aptedict.txt", encoding="utf-8")

words = file.read().split('|')[1:]

words = list(map(lambda x: x.strip(), words))

file = open("aptedict.txt", encoding="utf-8")

words = file.read().split('|')[1:]

words = list(map(lambda x: x.strip(), words))

simple = lambda x: len(syllabify(x)) > 1 and len(syllabify(x)) < 6 and '्' not in x

medium = lambda x: len(syllabify(x)) > 1 and len(syllabify(x)) < 6 and x.count('्') == 1 and x[-1] != '्'

compl  = lambda x: len(syllabify(x)) > 1 and len(syllabify(x)) < 6 and x.count('्') > 1 and x[-1] != '्'

words_simple = list(filter(simple, words))
words_medium = list(filter(medium, words))
words_compl = list(filter(compl, words))

with open('words_simple.json', 'w', encoding='utf8') as json_file:
    json.dump(words_simple, json_file, ensure_ascii=False)

with open('words_medium.json', 'w', encoding='utf8') as json_file:
    json.dump(words_medium, json_file, ensure_ascii=False)

with open('words_compl.json', 'w', encoding='utf8') as json_file:
    json.dump(words_compl, json_file, ensure_ascii=False)


