export const ScriptMixin = {
  data () {
    return {
      apiCall: this.$axios.create({
        baseURL: 'https://aksharamukha.appspot.com/api/',
        // baseURL: 'http://localhost:8085/api',
        timeout: 100000
      }),
      wikipediaCall: this.$axios.create({
        // baseURL: 'https://aksharamukha.appspot.com/api/',
        baseURL: 'https://en.wikipedia.org/w',
        timeout: 100000
      }),
      scriptSourceCall: this.$axios.create({
        // baseURL: 'https://aksharamukha.appspot.com/api/',
        baseURL: 'http://scriptsource.org/cms/scripts/page.php?item_id=script_detail&key=Zanb',
        timeout: 100000
      }),
      vowels: ['a', 'A', 'i', 'I', 'u', 'U', 'R', 'E', 'e', 'ai', 'O', 'o', 'au'],
      consonants: ['k', 'kh', 'g', 'gh', 'G',
        'c', 'ch', 'j', 'jh', 'J',
        'T', 'Th', 'D', 'Dh', 'N',
        't', 'th', 'd', 'dh', 'n',
        'p', 'ph', 'b', 'bh', 'm',
        'y', 'r', 'l', 'v',
        'z', 'S', 's', 'h',
        'L', 'Z', 'r2', 'n2'],
      consonantsIndic: ['k', 'kh', 'g', 'gh', 'G',
        'c', 'ch', 'j', 'jh', 'J',
        'T', 'Th', 'D', 'Dh', 'N',
        't', 'th', 'd', 'dh', 'n',
        'p', 'ph', 'b', 'bh', 'm',
        'y', 'r', 'l', 'v',
        'z', 'S', 's', 'h',
        'L'],
      ayogavahas: ['aM', 'aH'],
      vowelsAll: ['a', 'A', 'i', 'I', 'u', 'U', 'R', 'RR', 'lR', 'lRR', 'E', 'e', 'ai', 'O', 'o', 'au', 'aE', 'AE', 'aO', 'aM', 'aH', 'a~'],
      consonantsAll: ['k', 'kh', 'g', 'gh', 'G',
        'c', 'ch', 'j', 'jh', 'J',
        'T', 'Th', 'D', 'Dh', 'N',
        't', 'th', 'd', 'dh', 'n',
        'p', 'ph', 'b', 'bh', 'm',
        'y', 'r', 'l', 'v',
        'z', 'S', 's', 'h',
        'Z', 'L', 'r2', 'n2',
        'q', 'qh', 'g2', 'z2', 'r3', 'r3h', 'f', 'Y'],
      consontantsSpecial: ['L', 'Z', 'r2', 'n2'],
      consonantsSinhala: ['n*g', 'n*j', 'n*D', 'n*d', 'm*b'],
      ayogavahasAll: ['~', 'M', 'H'],
      preOptionsGroup: {
        'Tamil': [
          { label: 'Transcribe Tamil', value: 'TamilTranscribe' }
        ],
        'Itrans': [
          { label: 'E/O for long, e/o for short', value: 'swapEeItrans' }
        ],
        'HK': [
          { label: 'E/O for long, e/o for short', value: 'swapEe' }
        ],
        'Velthuis': [
          { label: 'E/O for long, e/o for short', value: 'swapEe' }
        ],
        'Limbu': [
          { label: 'SA-I for vowel length', value: 'LimbuSpellingSaI' }
        ],
        'Thai': [
          { label: 'Thai Orthography', value: 'ThaiOrthography' }
        ],
        'LaoPali': [
          { label: 'Lao Orthography', value: 'LaoTranscription' }
        ],
        'Devanagari': [
          { label: 'Schwa deletion (Hindi)', value: 'RemoveSchwaHindi' }
        ],
        'Gujarati': [
          { label: 'Schwa deletion (Only word-final)', value: 'SchwaFinalGujarati' }
        ],
        'Bengali': [
          { label: 'Schwa deletion (Only word-final)', value: 'SchwaFinalBengali' }
        ],
        'Gurmukhi': [
          { label: 'Schwa deletion (Only word-final)', value: 'SchwaFinalGurmukhi' }
        ],
        'Grantha': [
          { label: 'Prakrit orthography', value: 'GranthaPrakrit' },
          { label: 'Use e-Grantamil encoding', value: 'egrantamil' }
        ],
        'Sinhala': [
          { label: 'Sanskrit/Pali Orthography', value: 'SinhalaPali' }
        ],
        'Malayalam': [
          { label: 'Prakrit orthography', value: 'MalayalamPrakrit' }
        ],
        'Siddham': [
          { label: 'Devanagari-based Siddham Font', value: 'siddhammukta' }
        ],
        'IAST': [
          { label: 'Pali Text', value: 'IASTPali' }
        ],
        'Urdu': [
          { label: 'Short vowels not shown', value: 'UrduShortNotShown' }
        ]
      },
      preOptionsGroupSpecific: {
        'DevanagariLimbu': [
          { label: 'Use Limbu Devanagari conventions', value: 'LimbuDevanagariConvention' }
        ]
      },
      postOptionsGroupSpecific: {
        'DevanagariLimbu': [
          { label: 'Use Limbu Devanagari conventions', value: 'LimbuDevanagariConvention' }
        ]
      },
      postOptionsGroup: {
        'Tamil': [
          { label: 'Old orthography', value: 'oldtamilortho' },
          { label: 'Use Grantha Visarga', value: 'TamilGranthaVisarga' },
          { label: 'Subscript numerals', value: 'TamilSubScript' },
          { label: 'Dandas', value: 'RetainTamilDanda' },
          { label: 'Disable ௐ', value: 'TamilOmDisable' },
          { label: 'Disable ஶ', value: 'TamilDisableSHA' },
          { label: 'Remove Apostrophe', value: 'TamilRemoveApostrophe' },
          { label: 'Remove Diacritic Numerals', value: 'TamilRemoveNumbers' },
          { label: 'Tamil Numerals', value: 'RetainTamilNumerals' },
          { label: 'Medieval e/o with Pulli', value: 'MedievalTamilOrthography' }
        ],
        'Chakma': [
          {
            label: 'Enable all conjuncts',
            value: 'ChakmaEnableAllConjuncts'
          },
          {
            label: 'Enable independent i, u and e',
            value: 'ChakmaVowelsIndependent'
          }
        ],
        'Newa': [
          { label: 'Enable murmured consonants', value: 'NewaMurmurConsonants' },
          { label: 'Disable Repha', value: 'NewaDisableRepha' },
          { label: 'Use Devanagari-based Newa font', value: 'nepaldevafont' }

        ],
        'Oriya': [
          { label: 'Use ଵ instead of ୱ', value: 'OriyaVaAlt' },
          { label: 'Use ୟ everywhere', value: 'OriyaYYA' }
        ],
        'Bengali': [
          { label: 'Use য় everywhere', value: 'BengaliYYA' }
        ],
        'Siddham': [
          { label: 'Variant vowel sign U <span class="siddham">𑗜</span>', value: 'UseAlternateVSU' },
          { label: 'Variant vowel sign UU <span class="siddham">𑗝</span>', value: 'UseAlternateVSUU' },
          { label: 'Variant I <span class="siddham">𑗘</span>', value: 'UseAlternateI1' },
          { label: 'Variant I <span class="siddham">𑗙</span>', value: 'UseAlternateI2' },
          { label: 'Variant II <span class="siddham">𑗚</span>', value: 'UseAlternateII' },
          { label: 'Variant U <span class="siddham">𑗛</span>', value: 'UseAlternateU' },
          { label: 'Use MuktamSiddham font', value: 'siddhammukta' },
          { label: 'Use ApDevSiddham font', value: 'siddhamap' }
        ],
        'Devanagari': [
          { label: 'Prishthamatra orthography', value: 'DevanagariPrishtamatra' }
        ],
        'Gurmukhi': [
          { label: 'Use Yakaash', value: 'GurmukhiYakaash' },
          { label: 'Gurmukhi Numerals', value: 'RetainGurmukhiNumerals' }

        ],
        'Thai': [
          { label: 'Thai Orthography', value: 'ThaiTranscription' },
          { label: 'Sara /a/ ะ as Visarga', value: 'ThaiVisargaSaraA' }

        ],
        'LaoPali': [
          { label: 'Lao Orthography', value: 'LaoTranscription' }
        ],
        'Lao': [
          { label: 'Lao Nativization', value: 'LaoNative' }
        ],
        'Tibetan': [
          { label: 'Use <i>Bindu with nada</i>', value: 'TibetanNada' },
          { label: 'Use space', value: 'TibetanTsheg' }
        ],
        'Sinhala': [
          { label: 'Sanskrit/Pali Orthography', value: 'SinhalaPali' },
          { label: 'Enable all conjuncts', value: 'SinhalaConjuncts' }
        ],
        'Ranjana': [
          { label: 'Lantsa style (Tibetan)', value: 'ranjanalantsa' },
          { label: 'Wartu style (Tibetan)', value: 'ranjanawartu' }
        ],
        'Telugu': [
          { label: 'Dandas', value: 'RetainTeluguDanda' },
          { label: 'Telugu Numerals', value: 'RetainTeluguNumerals' }
        ],
        'Gujarati': [
          { label: 'Dandas', value: 'RetainGujaratiDanda' }
        ],
        'Kannada': [
          { label: 'Dandas', value: 'RetainKannadaDanda' },
          { label: 'Kannada Numerals', value: 'RetainKannadaNumerals' }
        ],
        'Grantha': [
          { label: 'Use Grantha old AU vowel sign', value: 'GranthaOldau' },
          { label: 'Prakrit orthography', value: 'GranthaPrakrit' },
          { label: 'Use e-Grantamil encoding', value: 'egrantamil' }
        ],
        'Urdu': [
          { label: 'Remove short vowels', value: 'UrduRemoveShortVowels' }
        ],
        'IAST': [
          { label: 'Pali Text', value: 'IASTPali' },
          { label: 'Capitalize sentences', value: 'capitalizeSentence' }
        ],
        'ISO': [
          { label: 'Capitalize sentences', value: 'capitalizeSentence' }
        ],
        'Khojki': [
          { label: 'Retain spaces', value: 'KhojkiRetainSpace' }
        ],
        'Kaithi': [
          { label: 'Retain spaces', value: 'KaithiRetainSpace' }
        ],
        'Bhaiksuki': [
          { label: 'Retain spaces', value: 'BhaiksukiRetainSpace' }
        ],
        'Limbu': [
          { label: 'SA-I for vowel length', value: 'LimbuSpellingSaI' }
        ],
        'Sundanese': [
          { label: 'Sundanese historical conjuncts', value: 'SundaneseHistoricConjuncts' }
        ],
        'MeeteiMayek': [],
        'Malayalam': [
          { label: 'Dot Reph', value: 'dotReph' },
          { label: 'Archaic II & AU', value: 'archaicAIAU' },
          { label: 'Traditional orthography', value: 'tradOrtho' },
          { label: 'Prakrit orthography', value: 'MalayalamPrakrit' },
          { label: 'Dandas', value: 'RetainMalayalamDanda' },
          { label: 'Malayalam Numerals', value: 'RetainMalayalamNumerals' }
        ],
        'ZanabazarSquare': [
          { label: 'Contextual ya/ra/la/va & Repha', value: 'ZanabazarSquareContextual' },
          { label: 'Alternate ai/au', value: 'ZanabazarSquareAiAu' },
          { label: 'Mongolian final-mark', value: 'ZanabazarSquareMongolianFinal' }
        ]
      },
      autodetect: [
        {
          label: 'Auto-Detect',
          value: 'autodetect',
          icon: 'translate'
        }],
      scriptsIndic: [
        {
          label: 'Ahom',
          value: 'Ahom',
          sscode: 'Ahom',
          ssdesc: 'The Ahom script was used by members of the Tai Ahom community in India for writing the Ahom language, an extinct member of the Tai-Kadai language family. Ahom has been written for at least 500 years, and possibly much longer. The Ahom script is derived from Old Mon, ultimately of Brahmi origin. The Ahom language is occasionally used in religious rituals, and there have been some recent revival efforts by the ethnic Ahom community in Assam.',
          omnicode: 'ahom',
          wikicode: 'Ahom_alphabet',
          font: {
            'name': 'Noto Sans Ahom',
            'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSerifAhom/NotoSerifAhom-Regular.otf'
          }
        },
        {
          label: 'Assamese',
          value: 'Assamese',
          sscode: '',
          ssdesc: '',
          wikicode: 'Assamese_alphabet',
          wikidesc: 'The Assamese script is a writing system of the Assamese language. It used to be the script of choice in the Brahmaputra valley. It evolved from Kamarupi script. By the 17th century three styles of Assamese script could be identified (baminiya, kaitheli and garhgaya) that converged to the standard script following typesetting required for printing. The present standard is identical to the Bengali alphabet except for two letters, ৰ (ro) and ৱ (vo).',
          omnicode: 'assamese',
          font: {
            'name': '',
            'url': ''
          }
        },
        {
          label: 'Avestan',
          value: 'Avestan',
          sscode: 'Avst',
          ssdesc: 'The Avestan script was used from the 5th to the 13th century AD for writing the Avestan language, an Eastern Iranian language which is now only known from its use as the language of Zoroastrian religious texts called Avesta, although it is thought that at one time it was probably a natural language in everyday use. There are no surviving examples of written Avestan prior to its use as a liturgical language, and it is thought that the Avestan script was created particularly for the purpose of writing religious texts.',
          omnicode: 'avestan',
          wikicode: 'Avestan_alphabet',
          font: {
            'name': 'Noto Sans Avestan',
            'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/unhinted/NotoSansAvestan-Regular.ttf'
          }
        },
        {
          label: 'Balinese',
          value: 'Balinese',
          sscode: 'Bali',
          ssdesc: 'The Balinese script is used for writing the Balinese language spoken on the Indonesian islands of Java and Bali. It is derived from the Old Kawi script, and is ultimately of Brahmic descent. It is very similar to the Javanese script in form and behaviour; some consider them to be typological variants of one another. Historically, Balinese has been inscribed into stone, or written on palm leaves. Traditionally, the religious texts written on palm leaves were considered to be sacred and could not be read by everyone.',
          omnicode: 'balinese',
          wikicode: 'Balinese_script',
          font: {
            'name': 'Noto Serif Balinese',
            'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSerifBalinese/NotoSerifBalinese-Regular.otf'
          }
        },
        {
          label: 'Batak Karo',
          value: 'BatakKaro',
          sublabel: 'Beta',
          sscode: 'Batk',
          ssdesc: 'The Batak script is used to write the six Batak languages (Toba, Karo, Dairi, Mandailing, Simalungun and Angkola) spoken collectively by approximately 3 million people on the Indonesian island of Sumatra. It is one of several scripts indigenous to the Indonesian archipelago, descended from the Old Kawi script, which in turn is derived from the Pallava, and ultimately the Brahmi, script. This is the variant used by the Karo language.',
          omnicode: '',
          wikicode: '',
          font: {
            'name': 'Noto Sans Batak',
            'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/unhinted/NotoSansBatak-Regular.ttf'
          }
        },
        {
          label: 'Batak Mandailing',
          value: 'BatakManda',
          sublabel: 'Beta',
          sscode: 'Batk',
          ssdesc: 'The Batak script is used to write the six Batak languages (Toba, Karo, Dairi, Mandailing, Simalungun and Angkola) spoken collectively by approximately 3 million people on the Indonesian island of Sumatra. It is one of several scripts indigenous to the Indonesian archipelago, descended from the Old Kawi script, which in turn is derived from the Pallava, and ultimately the Brahmi, script. This is the variant used by the Mandailing language.',
          omnicode: 'batak',
          wikicode: 'Batak_script',
          font: {
            'name': 'Noto Sans Batak',
            'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/unhinted/NotoSansBatak-Regular.ttf'
          }
        },
        {
          label: 'Batak Pakpak',
          value: 'BatakPakpak',
          sublabel: 'Beta',
          sscode: 'Batk',
          ssdesc: 'The Batak script is used to write the six Batak languages (Toba, Karo, Dairi, Mandailing, Simalungun and Angkola) spoken collectively by approximately 3 million people on the Indonesian island of Sumatra. It is one of several scripts indigenous to the Indonesian archipelago, descended from the Old Kawi script, which in turn is derived from the Pallava, and ultimately the Brahmi, script. This is the variant used by the Pakpak language.',
          omnicode: 'batak',
          wikicode: 'Batak_script',
          font: {
            'name': 'Noto Sans Batak',
            'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/unhinted/NotoSansBatak-Regular.ttf'
          }
        },
        {
          label: 'Batak Toba',
          value: 'BatakToba',
          sublabel: 'Beta',
          sscode: 'Batk',
          ssdesc: 'The Batak script is used to write the six Batak languages (Toba, Karo, Dairi, Mandailing, Simalungun and Angkola) spoken collectively by approximately 3 million people on the Indonesian island of Sumatra. It is one of several scripts indigenous to the Indonesian archipelago, descended from the Old Kawi script, which in turn is derived from the Pallava, and ultimately the Brahmi, script. This is the variant used by the Toba language.',
          omnicode: 'batak',
          wikicode: 'Batak_script',
          font: {
            'name': 'Noto Sans Batak',
            'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/unhinted/NotoSansBatak-Regular.ttf'
          }
        },
        {
          label: 'Batak Simalungun',
          value: 'BatakSima',
          sublabel: 'Beta',
          sscode: 'Batk',
          ssdesc: 'The Batak script is used to write the six Batak languages (Toba, Karo, Dairi, Mandailing, Simalungun and Angkola) spoken collectively by approximately 3 million people on the Indonesian island of Sumatra. It is one of several scripts indigenous to the Indonesian archipelago, descended from the Old Kawi script, which in turn is derived from the Pallava, and ultimately the Brahmi, script. This is the variant used by the Simalungun language.',
          omnicode: 'batak',
          wikicode: 'Batak_script'
        },
        {
          label: 'Bengali',
          value: 'Bengali',
          sscode: 'Beng',
          ssdesc: 'The Bengali (also called Bangla) script is used for writing the Bengali language, spoken by over 180,000,000 people mostly in Bangladesh and India. It is also used for a number of other Indian languages including Sylheti and, with one or two modifications, Assamese. It is a Brahmic script although its exact derivation is disputed.',
          omnicode: 'batak',
          wikicode: 'Batak_script',
          font: {
            'name': '',
            'url': ''
          }
        },
        {
          label: 'Brahmi',
          value: 'Brahmi',
          sscode: 'Brah',
          ssdesc: 'The Brahmi script is ancestral to most of the scripts of South Asia, Southeast Asia, and to some Central Asian scripts. The name Brahmi actually does not refer to a single, discrete script as such; general practise is to use the term to refer to any script in the family now known as Brahmic, up until approximately 400 AD, at which point they became differentiated enough to be given their own names. Brahmic writing was originally used for writing early dialects of the Prakrit language, but spread widely during the period of Indian cultural expansion in the 1st millenium AD and has since provided the underlying design for over sixty scripts used by languages from the Indo-Aryan, Dravidian, Austro-Asiatic and Tibeto-Burman language families. ',
          omnicode: 'brahmi',
          wikicode: 'Brahmi_script',
          font: {
            'name': '',
            'url': ''
          }
        },
        {
          label: 'Bhaiksuki',
          value: 'Bhaiksuki',
          sscode: 'Bhks',
          ssdesc: 'Bhaiksuki is an extinct script used for writing Buddhist texts in the Indian state of Bihar. It is also known as the Arrow-Headed script due to the shape of the letters, many of which are capped with one or more triangular “arrows”. Little is known about this script.',
          omnicode: '',
          wikicode: 'Bhaiksuki_alphabet',
          font: {
            'name': 'Noto Sans Bhaiksuki',
            'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansBhaiksuki/NotoSansBhaiksuki-Regular.otf'
          }
        },
        {
          label: 'Buginese (Lontara)',
          value: 'Buginese',
          sscode: 'Bugi',
          ssdesc: 'The Buginese (also known as the Lontara) script is used for writing the Bugis, Makasar, and Mandar languages of Sulawesi in Indonesia. It is related to the other Brahmic scripts indigenous to the Indonesian archipelago.',
          omnicode: 'lontara',
          wikicode: 'Lontara_script',
          font: {
            'name': 'Noto Sans Buginese',
            'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/unhinted/NotoSansBuginese-Regular.ttf'
          }
        },
        {
          label: 'Buhid',
          value: 'Buhid',
          sscode: 'Buhd',
          ssdesc: 'The Buhid script is used to write the Buhid language, spoken by about 8,000 people in the Mindoro region of the Philippines. It is an indigenous abugida script of Brahmic origin. It is proposed that the Buhid, Hanunoo and Tagbanwa scripts share common origins with the Tagalog script, an extinct script from the same region, because of the many features they have in common.',
          omnicode: 'buhid',
          wikicode: 'Buhid_alphabet',
          font: {
            'name': 'Nnoto Sans Buhid',
            'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansBuhid/NotoSansBuhid-Regular.otf'
          }
        },
        {
          label: 'Burmese (Myanmar)',
          value: 'Burmese',
          sscode: 'Mymr',
          ssdesc: 'The Myanmar script was adapted from the Mon script, a descendent of Brahmi, and is found in stone inscriptions dating from the 12th century. It is used for writing the Burmese and Mon languages, both spoken in Myanmar (previously Burma). The two languages differ in how some phonemic values are assigned to letters. The script is also used, with character extensions, to write some of the Karen languages spoken in Myanmar and Thailand.',
          omnicode: 'burmese',
          wikicode: 'Burmese_alphabet',
          font: {
            'name': '',
            'url': ''
          }
        },
        {
          label: 'Chakma',
          value: 'Chakma',
          sscode: 'Cakm',
          ssdesc: 'The Chakma script (also called Ojhapath, Ojhopath, or Ajhapath) is used for writing the Chakma language spoken in the Chittagong Hill Tracts of Bangladesh and in the Seven Sister States of Northeastern India. There are slight variations in the forms of the letters used in the two countries. The script is related to Mon Khmer and Myanmar, and many of the letters closely resemble Myanmar letters. It is also being adapted and extended for writing Tanchangya, a related language spoken in Bangladesh.',
          omnicode: 'chakma',
          wikicode: 'Chakma_alphabet',
          font: {
            'name': 'Noto Sans Chakma',
            'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/unhinted/NotoSansChakma-Regular.ttf'
          }
        },
        {
          label: 'Cham',
          value: 'Cham',
          sublabel: 'Beta',
          sscode: 'Cham',
          ssdesc: 'The Cham script is a Brahmi-derived abugida used for writing the Cham language. There are two major dialects of Cham, spoken collectively by about 230,000 people in two isolated groups in Vietnam and Cambodia, both of which once had a thriving literary tradition dating from the 8th century. The Cambodian Cham population used to be much larger',
          omnicode: 'cham',
          wikicode: 'Cham_alphabet',
          font: {
            'name': 'Noto Sans Cham',
            'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/unhinted/NotoSansCham-Regular.ttf'
          }
        },
        {
          label: 'Devanagari',
          value: 'Devanagari',
          sscode: 'Deva',
          ssdesc: 'Devanagari is a Northern Brahmic script related to many other South Asian scripts including Gujarati, Bengali, and Gurmukhi, and, more distantly, to a number of South-East Asian scripts including Thai, Balinese, and Baybayin. The script is used for over 120 spoken Indo-Aryan languages, including Hindi, Nepali, Marathi, Maithili, Awadhi, Newari and Bhojpuri. It is also used for writing Classical Sanskrit texts.',
          omnicode: 'devanagari',
          wikicode: 'Devanagari',
          font: {
            'name': '',
            'url': ''
          }
        },
        {
          label: 'Grantha',
          value: 'Grantha',
          sscode: 'Gran',
          ssdesc: '',
          wikicode: 'Grantha_script',
          wikidesc: 'The Grantha script is an Indian script that was widely used between the sixth century and the 20th centuries by Tamil and Malayalam speakers in South India, particularly in Tamil Nadu and Kerala, to write Sanskrit and and is still in restricted use in traditional Vedic schools. Its complete replacement by the modern Tamil script (along with the promotion of Devanagari as a pan-Indian Sanskrit script) led to its gradual disuse and abandonment in Tamil Nadu in the early 20th century, except for specialised Hindu religious literature. Grantha script still lives in Tamil Nadu, albeit in reduced state.',
          omnicode: 'grantha',
          font: {
            'name': 'Noto Sans Grantha',
            'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansGrantha/NotoSansGrantha-Regular.otf'
          }
        },
        {
          label: 'Pandya Grantha',
          value: 'GranthaPandya',
          sscode: '',
          ssdesc: '',
          wikidesc: 'Pandya Grantha refers to the version of Grantha as used in the Velvikudi inscription. The Velvikudi inscription is an 8th-century bilingual copper-plate inscription from the Pandya kingdom of southern India. Inscribed in Sanskrit and Tamil languages, it records the Pandya king Nedunjadaiyan\'s renewal of a grant of the Velvikudi village to a brahmana.',
          omnicode: '',
          wikicode: 'Velvikudi_inscription',
          font: {
            'name': 'e-Pandya',
            'url': 'https://github.com/virtualvinodh/aksharamukha/blob/master/aksharamukha-front/src/statics/e-Pandya.ttf'
          }
        },
        {
          label: 'Gujarati',
          value: 'Gujarati',
          sscode: 'Gujr',
          ssdesc: 'The Gujarati script is used for writing the Gujarati and Chodri languages, together spoken by almost 47 million people. It is also used alongside the Devanagari script for writing a number of languages used by the Bhil people, one of India\'s largest indigenous groups. The script is related to Devanagari, with modifications to some of the letters, and without the headstroke which characterizes most of the Nagari scripts. The loss of the headstroke reflects the script\'s origins in informal writing; until the mid-19th century it was used primarily for bookkeeping and personal correspondence',
          omnicode: 'gujarati',
          wikicode: 'Gujarati_alphabet',
          font: {
            'name': 'Noto Serif Gujarati',
            'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSerifGujarati/NotoSerifGujarati-Regular.otf'
          }
        },
        {
          label: 'Hanunoo',
          value: 'Hanunoo',
          sscode: 'Hano',
          ssdesc: 'The Hanunóo script is used by the Mangyan people in the mountains of Mindoro, South Philippines, to write the Hanunóo language. Perhaps due to its inaccessible location, it is one of the few indigenous Philippine scripts which has not been replaced by the Latin script. It is of Brahmic origin, descended through Old Kawi, although its history is difficult to trace in detail due to the perishable nature of bamboo, the surface on which it is traditionally inscribed.',
          omnicode: 'hanunoo',
          wikicode: 'Hanunó%27o_alphabet',
          font: {
            'name': 'Noto Sans Hanunoo',
            'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansHanunoo/NotoSansHanunoo-Regular.otf'
          }
        },
        {
          label: 'Javanese',
          value: 'Javanese',
          sscode: 'Java',
          ssdesc: 'Javanese is Indonesia\'s oldest literary language, its literary history being traceable to the C4th. The present Javanese script is a modern variant of Old Kawi, an ancient Brahmic script from which many scripts in the Indonesian archipelago are derived. It is the pre-colonial script of the Javanese language spoken on the Indonesian islands of Java and Bali and is used to write the Tengger and Osing languages, also spoken in Java and Bali. The Javanese script is closely related to the Balinese script, although Javanese contains 4 consonant letters which are absent in the Balinese.',
          omnicode: 'javanese',
          wikicode: 'Javanese_script',
          font: {
            'name': 'Noto Sans Javanese',
            'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansJavanese/NotoSansJavanese-Regular.otf'
          }
        },
        {
          label: 'Kaithi',
          value: 'Kaithi',
          sscode: 'Kthi',
          ssdesc: 'The Kaithi script has been used predominantly in the Indian states of Bihar and Uttar Pradesh (but also in other North Indian states and the Nepali terai) for writing a group of Indo-Aryan languages. Kaithi has been used for writing the Bhojpuri, Maghadi, Urdu, Awadhi, Maithili, and Bengali languages since the 16th century. Its use was generally discouraged under British rule in India, except in the state of Bihar, where it was officially sanctioned for use in government offices. The script was widely used until the early 1900s, and there is some evidence that it is still used for personal correspondence in rural areas.',
          omnicode: 'kaithi',
          wikicode: 'Kaithi',
          font: {
            'name': 'Noto Sans Kaithi',
            'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansKaithi/NotoSansKaithi-Regular.otf'
          }
        },
        {
          label: 'Kannada',
          value: 'Kannada',
          sscode: 'Knda',
          ssdesc: 'The Kannada script is used for writing the Kannada language spoken by over 35 million people in southern India. It is also used for writing Konkani, a South Indian language with over 3 million speakers, Tulu, with almost 2 million speakers, and a number of south Indian minority languages including Badaga, Kudiya and Paniya. The script is closely related to Telugu writing; both languages were written using the Old Kanarese script until the 1500s when it diverged into two distinct varieties.',
          omnicode: 'kannada',
          wikicode: 'Kannada_alphabet',
          font: {
            'name': 'Noto Sans Kannada',
            'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansKannada/NotoSansKannada-Regular.otf'
          }
        },
        {
          label: 'Kharoshthi',
          value: 'Kharoshthi',
          sscode: 'Khar',
          ssdesc: 'Early writing in India is associated with three scripts; Indus (Harrapan), Brahmi and Kharoshthi. The Kharoshthi script descended from Aramaic and was used in what is now Northern Pakistan and Eastern Afghanistan during the 4th or 5th century BC. It was used for about 700 years for writing a group of vernacular middle Indo-Aryan dialects collectively termed \'Prakrit\'. There has been some evidence that local variants of Kharoshthi writing were used for even longer than this along the Silk Route, but these too later died out without leaving any descendants.',
          omnicode: 'kharosthi',
          wikicode: 'Kharosthi',
          font: {
            'name': '',
            'url': ''
          }
        },
        {
          label: 'Khmer (Cambodian)',
          value: 'Khmer',
          sscode: 'Khmr',
          ssdesc: 'The Khmer script is an abugida, descended from the Brahmic script Pallava. It is used for writing Khmer, the official language of Cambodia. The script is also sometimes used for writing minority languages in Cambodia, such as Brao and Mnong.',
          omnicode: 'khmer',
          wikicode: 'Khmer_alphabet',
          font: {
            'name': 'Noto Sans Khmer',
            'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSerifKhmer/NotoSerifKhmer-Regular.otf'
          }
        },
        {
          label: 'Khojki',
          value: 'Khojki',
          sscode: 'Khoj',
          ssdesc: 'Khojki is a Brahmi-derived abugida related to the Sharada script. It is used by the Khoja people - an ethnic group of largely Ismaili Shia Muslims - for recording religious literature in the Sindhi language. Khojki has been used since at least the 16th century, originally for manuscripts, but later in printed form also. The script has also been used to write other South Asian languages; however, in recent years its use has declined markedly.',
          omnicode: 'khojki',
          wikicode: 'Khojki_script',
          font: {
            'name': 'Noto Sans Khojki',
            'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansKhojki/NotoSansKhojki-Regular.otf'
          }
        },
        {
          label: 'Khudawadi',
          value: 'Khudawadi',
          sscode: 'Sind',
          ssdesc: 'The Khudawadi (also called Sindhi) script was used for writing the Indo-Aryan Sindhi language spoken by almost 20 million people in the Sindh province of Pakistan and in India. It is no longer used. It was used by traders and merchants to record their information and rose to importance as the script began to be used to record information kept secret from other groups and kingdoms.',
          omnicode: 'sindhi',
          wikicode: 'Khudabadi_script',
          font: {
            'name': 'Nodo Sans Khudawadi',
            'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansKhudawadi/NotoSansKhudawadi-Regular.otf'
          }
        },
        {
          label: 'Lao',
          value: 'Lao',
          sscode: 'Laoo',
          ssdesc: 'The Lao script is used for writing the Lao language, and is also the official script of a number of minority languages in Laos. The Lao language is closely related to Thai; there is a considerable Lao-speaking population in Thailand who write their language with the Thai script. However, the Lao script underwent a number of reforms which caused significant divergence from the Thai script.',
          omnicode: 'lao',
          wikicode: 'Lao_alphabet',
          font: {
            'name': '',
            'url': ''
          }
        },
        {
          label: 'Lao (Pali)',
          value: 'LaoPali',
          sscode: '',
          ssdesc: '',
          font: {
            'name': 'Lao Pali (Alpha)',
            'url': 'https://github.com/virtualvinodh/aksharamukha/blob/master/aksharamukha-front/src/statics/LaoPaliAlpha-Extralight.otf'
          },
          miscdesc: 'Lao (Pali) is the extended version of the Lao script to faithfully represent Pali and Sanskrit. Lao lacks several characters that are required to accurately express the phonology of those languages (unlike its neighbhouring scripts like Thai/Khmer). Therefore, Modern Lao cannot faithfully represent Pali words, and by extension, cannot transcript religious texts faithfully. In the 1930s, an additional set of characters were proposed to support Pali/Sanskrit by filling in the missing gaps. This also allows an etymological orthography for Lao (similar to Thai. The current Lao orthography is phonemic). But the addition met with little widespread support and finally by 1975, these additional characters were mostly out of use. But there is a revived interest in the characters. '
        },
        {
          label: 'Lepcha',
          value: 'Lepcha',
          sscode: 'Lepc',
          ssdesc: 'The Lepcha script is also called the Róng script - Lepcha people call themselves Róngkup, children of the Róng. It is used for writing the Lepcha language, a Tibeto-Burman language spoken by about 52,800 people in India, Nepal and Bhutan. The script is derived from Tibetan writing, probably motivated by Buddhist missionary activity in the 1700s. Early manuscripts were written in vertical columns but later and current texts are written horizontally. Many letters, when rotated back to their previous vertical position, closely resemble their Tibetan counterparts.',
          omnicode: 'lepcha',
          wikicode: 'Lepcha_script',
          font: {
            'name': 'Noto Sans Lepcha',
            'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/unhinted/NotoSansLepcha-Regular.ttf'
          }
        },
        {
          label: 'Limbu',
          value: 'Limbu',
          sscode: 'Limb',
          ssdesc: 'The Limbu script (also called Kiranti, Sirijonga or Sirijanga script) is used by about 400,000 people for writing the Limbu language spoken in Nepal and northern India. The Limbu language is also written in the Devanagari script. The origins of the script are unknown; it is evident from its structure that it is of Brahmic derivation, and appears to be closely related to the Lepcha script. Limbu folklore relates that in the 9th century the Limbu king Sirijanga prayed to the goddess Saravati for wisdom as to how to devise a script for his people, and in response she revealed the story of creation to him, written in the script.',
          omnicode: 'limbu',
          wikicode: 'Limbu_alphabet',
          font: {
            'name': 'Noto Sans Limbu',
            'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/unhinted/NotoSansLimbu-Regular.ttf'
          }
        },
        {
          label: 'Malayalam',
          value: 'Malayalam',
          sscode: 'Mlym',
          ssdesc: 'The Malayalam script is used for writing the Malayalam language, the official language of the Indian state of Kerala, and a number of minority languages spoken in India. Until the 16th century Malayalam was written in the vattezhuthu script, a Brahmic script which developed alongside Grantha writing, from which the modern Malayalam script descended.',
          omnicode: 'malayalam',
          wikicode: 'Malayalam_script',
          font: {
            'name': 'Noto Sans Malayalam',
            'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansMalayalam/NotoSansMalayalam-Regular.otf'
          }
        },
        {
          label: 'Mahajani',
          value: 'Mahajani',
          sscode: 'Mahj',
          ssdesc: 'The Mahajani script was a commercial script (महाजन mahajana is the Hindi word for ‘banker’) used across Northern India until the middle of the 20th century. It was used by speakers of a number of languages, including Hindi, Marwari and Punjabi, and was taught in special merchant- and business-focused schools alongside other skills required for conducting business.',
          omnicode: '',
          wikicode: 'Mahajani',
          font: {
            'name': 'Noto Sans Mahajani',
            'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansMahajani/NotoSansMahajani-Regular.otf'
          }
        },
        {
          label: 'Meetei Mayek (Manipuri)',
          value: 'MeeteiMayek',
          sscode: 'Mtei',
          ssdesc: 'The Meetei Mayek script is used for writing the Meetei (also called Manipuri) language spoken by about 1,400,000 people in India, primarily the state of Manipur, Bangladesh, and Myanmar. The language has been largely written in the Bengali script since the 18th century, but Meetei Mayek writing has experienced a resurgence in the last hundred years. The origins of the script are controversial, most of the early documents having been destroyed in the 18th century. Some sources claim it has been used for almost 4,000 years, and others suggest it derived from the Bengali script as recently as the 17th century.',
          omnicode: 'manipuri',
          wikicode: 'Meitei_script',
          font: {
            'name': 'Noto Sans Meetei Mayek',
            'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/unhinted/NotoSansMeeteiMayek-Regular.ttf'
          }
        },
        {
          label: 'Modi',
          value: 'Modi',
          sscode: 'Modi',
          ssdesc: 'The Modi script was used from the 17th century until the 1950s for writing Marathi, the state language of the Indian state of Maharashtra. The script developed from a cursive form of Devanagari, so shares a number of features with, and is visually similar to, that script. Modi is considered by many to be extinct, having been replaced by Devanagari after the 1950s. Efforts are underway to preserve knowledge of the script before the last generation of frequent users dies.',
          omnicode: 'modi',
          wikicode: 'Modi_script',
          font: {
            'name': 'Modi',
            'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansModi/NotoSansModi-Regular.otf'
          }
        },
        {
          label: 'Multani',
          value: 'Multani',
          sscode: 'Mult',
          ssdesc: 'The Multani script is used for writing the Saraiki language, spoken in the Punjab regions of India and Pakistan, and in northern Sindh in Pakistan. It is a commercial script, used mainly by merchants. Structurally, the script has characteristics of an abjad; vowels are generally not written unless they appear at the start of a word or in one-syllable V or CV clusters.',
          omnicode: '',
          wikicode: 'Multani_alphabet',
          font: {
            'name': 'Multani',
            'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansMultani/NotoSansMultani-Regular.otf'
          }
        },
        {
          label: 'Newa (Nepal Bhasa)',
          value: 'Newa',
          sscode: 'Newa',
          ssdesc: 'The Newa script, also known as Newar, or Prachalit (meaning popular), is used primarily for writing Newari, a Tibeto-Burman language of Nepal (also called Nepal-Bhasha, literally \'Nepal-Language\', but not to be confused with Nepali). This script has also been used, extensively in some cases, for writing the Sanskrit, Nepali, Hindi, Bengali, and Maithili languages. The script is also known as Nepalakshar, Newah Akhah and Pachumol. It is one of six scripts subsumed under the name Nepal-Lipi, literally \'Nepal-Script\'',
          omnicode: '',
          wikicode: 'Prachalit_Nepal_alphabet',
          font: {
            'name': 'Noto Sans Newa',
            'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansNewa/NotoSansNewa-Regular.otf'
          }
        },
        {
          label: 'Old Persian',
          value: 'OldPersian',
          sscode: 'Xpeo',
          ssdesc: 'Old Persian cuneiform was the main script for writing the Old Persian language from 525-330 BC. Visually it resembles Sumero-Akkadian cuneiform; most of the letters are arrangements of between two and five horizontal, vertical or angle-shaped wedges. However, there appears to be no derivational relationship between the sound-to-symbol mapping of individual letters in the two scripts, nor has any other script been found which links the forms of the scripts. For this reason, Old Persian cuneiform is generally believed to have been an independent invention.',
          omnicode: 'opcuneiform',
          wikicode: 'Old_Persian_cuneiform',
          font: {
            'name': 'Noto Sans Old Persian',
            'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansOldPersian/NotoSansOldPersian-Regular.otf'
          }
        },
        {
          label: 'Oriya',
          value: 'Oriya',
          sscode: 'Orya',
          ssdesc: 'The Odia (formerly Oriya) script is used for writing the Odia language, the official language of the Indian state of Orissa, as well as a number of Dravidian and Munda minority languages spoken in that region. It is also used in Orissa for transcribing Sanskrit texts. The earliest inscriptions in the Odia language have been dated to 1051 AD, written in the Kalinga script from which modern Odia writing is derived.',
          omnicode: 'oriya',
          wikicode: 'Odia_alphabet',
          font: {
            'name': '',
            'url': ''
          }
        },
        {
          label: 'PhagsPa',
          value: 'PhagsPa',
          sscode: 'Phag',
          ssdesc: 'The \'Phags-pa script, called hor gsar yig in Tibetan and dörbelǰin üsüg in Mongolian, is named for its creator, the Tibetan sage \'Phags-pa Lama. \'Phags-pa was appointed \'National Perceptor\' in 1264 by the emperor Khubila Khan, by whom he was ordered to devise a script in which all the languages of his empire - including Tibetan, Uyghur, Mongolian and Chinese - could be written. The new script met with limited success and only scanty accounts of its creation exist in the biographies written by \'Phags pa\'s disciples.',
          omnicode: 'phagspa',
          wikicode: '%27Phags-pa_script',
          font: {
            'name': '',
            'url': ''
          }
        },
        {
          label: 'Punjabi (Gurmukhi)',
          value: 'Gurmukhi',
          sscode: 'Guru',
          ssdesc: 'The Gurmukhi script is used primarily by followers of the Sikh religion in India to write the Punjabi language. Gurmukhi writing is historically derived from Brahmi, but its present form was developed in the 16th century by Guru Angad, successor to the founder of the Sikh religion, Guru Nanak. The word Gurmukhi means \'from the mouth of the guru\'. Muslims in the Pakistani Punjab write Punjabi in the Persian script; use of the Persian script for writing Punjabi is called Shahmukhi.',
          omnicode: 'punjabi',
          wikicode: 'Gurmukhi',
          font: {
            'name': '',
            'url': ''
          }
        },
        {
          label: 'Ranjana (Lantsa)',
          value: 'Ranjana',
          sscode: 'Qabb',
          ssdesc: 'The Ranjana script is used for writing the Newari language of Nepal. This language is also called Nepal-Bhasha. The script was derived from Brahmi via the Old Nepal script, both of which are now extinct, around the 12th century AD. It has been used since that time in a gradually decreasing capacity, but is still used for producing Hindu and Buddhist religious texts and taught in Buddhist monasteries. It is also used as a decorative script in much the same way as calligraphy is used in the West.',
          omnicode: 'ranjana',
          wikicode: 'Ranjana_alphabet',
          font: {
            'name': 'Ranjana Unicode',
            'url': 'https://github.com/virtualvinodh/aksharamukha/blob/master/aksharamukha-front/src/statics/RanjanaUNICODE1.0.TTF'
          }
        },
        {
          label: 'Rejang',
          value: 'Rejang',
          sscode: 'Rjng',
          ssdesc: 'The Rejang (also known as the Kaganga or Redjang) script is used to write the 5 Rejang dialects spoken collectively by about 200-250,000 people on the Indonesian island of Sumatra, and the Kerinci and Lampung languages of the same region. The script is thought to pre-date the introduction of Islam in the 12th century to the area, although the earliest attested document has been dated to the mid C18th. It is traditionally written on bamboo, buffalo horn, bark or copper plates',
          omnicode: 'redjang',
          wikicode: 'Rejang_script',
          font: {
            'name': 'Noto Sans Rejang',
            'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansRejang/NotoSansRejang-Regular.otf'
          }
        },
        {
          label: 'Santali (Ol Chiki)',
          value: 'Santali',
          sscode: 'Olck',
          ssdesc: 'The Ol Chiki script (also called Ol Cemet, Ol, or Santali) was created by Pandit Raghunath Murmu in the 1920s for writing the Santali language, which is spoken by just under 6 million people in India, Bangladesh and Nepal. The Santali language is also written in the Devanagari, Bengali, Oriya and Roman scripts, and most people who are literate in Ol Chiki are also literate in at least one of the others. For this reason, not all Santali speakers are agreed as to the necessity of a unique script for their language, but despite competition from surrounding scripts, Ol Chiki is becoming more widely accepted.',
          omnicode: 'santali',
          wikicode: 'Ol_Chiki_script',
          font: {
            'name': 'Noto Sans Old Chiki',
            'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansOlChiki/NotoSansOlChiki-Regular.otf'
          }
        },
        {
          label: 'Saurashtra',
          value: 'Saurashtra',
          sscode: 'Saur',
          ssdesc: 'The Saurashtra language is spoken by approximately 130,000 people in Southern India. The Saurashtra script is of Brahmic origin, although its exact derivation is not known. Unlike most of the surrounding Dravidian languages, Saurashtra is Indo-European. The language has its own script of the same name, but is also written in the Tamil, Telugu, and Devanagari scripts. There is some debate amongst speakers of the Saurashtra language as to which script is best suited to the language.',
          omnicode: 'saurashtra',
          wikicode: 'Saurashtra_alphabet',
          font: {
            'name': 'Noto Sans Saurashtra',
            'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansSaurashtra/NotoSansSaurashtra-Regular.otf'
          }
        },
        {
          label: 'Siddham',
          value: 'Siddham',
          sscode: 'Sidd',
          ssdesc: 'Siddham is an extinct Brahmic script which was used between 600-1200 AD for writing Sanskrit. The script travelled along the silk road to China, Japan and Korea in the form of Buddhist tantra texts. An adaptation of the script is still used in some esoteric Buddhist schools in Japan, where it is called Bonji.',
          omnicode: 'siddham',
          wikicode: 'Siddhaṃ_script',
          font: {
            'name': 'Noto Sans Siddham',
            'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansSiddham/NotoSansSiddham-Regular.otf'
          }
        },
        {
          label: 'Sharada',
          value: 'Sharada',
          sscode: 'Shrd',
          ssdesc: 'The Sharada script evolved from Gupta Brahmi in the 9th century AD. In its earlier forms it was widespread over the northwest parts of the Indian subcontinent and was the progenitor of the Gurmukhi script, but later it became restricted to Kashmir, where it was the principal means of writing until the 20th century. In the 1950s a Perso-Arabic script was made the official script of Kashmir. Sharada is now only used by Kashmiri Pandits - a Hindu, ethnically Aryan group who inhabited the Kashmiri valley until they were exiled in the 1990s - for religious and ceremonial purposes.',
          omnicode: 'sharda',
          wikicode: 'Sharada_script',
          font: {
            'name': 'Noto Sans Sharada',
            'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansSharada/NotoSansSharada-Regular.otf'
          }
        },
        // {
        //   label: 'Siddham',
        //   value: 'Siddham'
        // },
        {
          label: 'Sinhala',
          value: 'Sinhala',
          sscode: 'Sinh',
          ssdesc: 'The Sinhala script is used for writing the Sinhala language, spoken by approximately 15,500,000 people in Sri Lanka, and for transcribing the ancient Pali and Sanskrit languages. The script is derived from Brahmi, and shows close similarities to the Grantha script which was used in southern India until the 16th century. ',
          omnicode: 'sinhala',
          wikicode: 'Sinhalese_script',
          font: {
            'name': 'Noto Sans Sinhala',
            'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansSinhala/NotoSansSinhala-Regular.otf'
          }
        },
        {
          label: 'Sora Sompeng',
          value: 'SoraSompeng',
          sscode: 'Sora',
          ssdesc: 'The Sora Sompeng script is used for writing the Sora language spoken by about 310,000 people in India, predominantly in the eastern state of Orissa. Sora is in the Munda language family. It is also sometmes called Saora or Savara, but is not to be confused with the Savara language in the Dravidian family.',
          omnicode: 'sorangsompeng',
          wikicode: 'Sorang_Sompeng_alphabet',
          font: {
            'name': 'Noto Sans SoraSompeng',
            'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansSoraSompeng/NotoSansSoraSompeng-Regular.otf'
          }
        },
        {
          label: 'Sundanese',
          value: 'Sundanese',
          sscode: 'Sund',
          ssdesc: 'The Sundanese script is used to write the Sundanese language, spoken by about 27 million people on the Indonesian island of Java. Today, the language is generally written in either the Sundanese or the Latin script, but has historically also been written using other scripts. It is currently taught in schools and used for public signage.',
          omnicode: 'sundanese',
          wikicode: 'Sundanese_script',
          font: {
            'name': 'Noto Sans Sundanese',
            'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/unhinted/NotoSansSundanese-Regular.ttf'
          }
        },
        {
          label: 'Syloti Nagari',
          value: 'SylotiNagri',
          sscode: 'Sylo',
          ssdesc: 'The Syloti Nagri script (also called Sylheti Nagri) is the original script for the Sylheti language, spoken in Bangladesh. The script has been almost entirely replaced by the Bengali and, to a lesser extent, Latin, scripts. At its peak however, it was used by all literate Sylheti speakers for personal correspondence, record-keeping, business purposes and religious texts in the language. The script appears to be derived from the Kaithi script used in Bihar.',
          omnicode: 'syloti',
          wikicode: 'Sylheti_Nagari',
          font: {
            'name': 'Noto Sans SylotiNagri',
            'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansSylotiNagri/NotoSansSylotiNagri-Regular.otf'
          }
        },
        {
          label: 'Tagbanwa',
          value: 'Tagbanwa',
          sscode: 'Tagb',
          ssdesc: 'The Tagbanwa (also known as Apurahuano) script is one of the Brahmic scripts indigenous to the Philippines. It is used to write the Tagbanwa language, which is spoken by approximately 8,000 people living in scattered communities throughout the Palawan region; literacy in the script is low. Of the three living indigenous Philippine scripts - Hanunoo, Buhid and Tagbanwa - Tagbanwa is acknowledged to be the least widely used.',
          omnicode: 'tagbanwa',
          wikicode: 'Tagbanwa',
          font: {
            'name': 'Noto Sans Tagbanwa',
            'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/unhinted/NotoSansTagbanwa-Regular.ttf'
          }
        },
        {
          label: 'Tagalog',
          value: 'Tagalog',
          sscode: 'Tglg',
          ssdesc: 'The Tagalog script, also known as Baybayin, is an extinct script indigenous to the Philippines. It was used to write the Tagalog language, which is still spoken by 21 million people throughout the Philippines, although it is now written in the Latin script. The Tagalog script was an abugida which descended from the Oldl Kawi, and ultimately the Brahmic, scripts.',
          omnicode: 'tagalog',
          wikicode: 'Baybayin',
          font: {
            'name': 'Noto Sans Tagalog',
            'url': 'Noto Sans Tagalog'
          }
        },
        {
          label: 'Tai Tham (Lanna)',
          sublabel: 'Beta',
          value: 'TaiTham',
          sscode: 'Lana',
          ssdesc: 'The Lanna script is also known as the Tai Tham, Dham, Yuan, or Northern Thai script. It has been used for writing the Northern Thai, Lü and Khün languages. Northern Thai is the biggest language group which uses the script, with 6 million speakers, but literacy is low. The script has religious significance and is used in Buddhist monasteries.',
          omnicode: 'lanna',
          wikicode: 'Tai_Tham_script',
          font: {
            'name': 'Lamphun',
            'url': 'http://wrdingham.co.uk/lanna/renderer_test.htm#fonts'
          }
        },
        {
          label: 'Takri',
          value: 'Takri',
          sscode: 'Takr',
          ssdesc: 'The Takri script was used between the 16th and 19th centuries in what are now Jammu and Kashmir, Himachal Pradesh, the Punjab, and Uttarakhand. It was used for writing the Chambeali and Dogri languages, as well as a number of Pahari (Himalayan) languages including Jaunsari and Kulvi. The script is derived from Sharada, one of the Gupta scripts, and is related to the Gurmukhi and Lahnda scripts. It was widely used both in official and personal contexts.',
          omnicode: 'takri',
          wikicode: 'Takri_alphabet',
          font: {
            'name': 'Noto Sans Takri',
            'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansTakri/NotoSansTakri-Regular.otf'
          }
        },
        {
          label: 'Tamil',
          value: 'Tamil',
          sscode: 'Taml',
          ssdesc: 'The Tamil script is used for writing the Tamil language, a Dravidian language spoken by over 65,500,000 people in India, Sri Lanka, Singapore, Malaysia and Mauritius. Tamil is an official language in the south Indian state of Tamil Nadu as well as in Sri Lanka and Malaysia. The script is derived from Brahmi, so is related to many of the scripts used for writing Indian Indo-Aryan languages',
          omnicode: 'tamil',
          wikicode: 'Tamil_script',
          font: {
            'name': 'Noto Sans Tamil',
            'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansTamil/NotoSansTamil-Regular.otf'
          }
        },
        {
          label: 'Tamil (with full Grantha)',
          value: 'TamilGrantha',
          sscode: '',
          ssdesc: '',
          miscdesc: 'Tamil (with full Grantha) represents the attempts to use the full complimentary set of Grantha letters to fill the gaps in the Tamil script (as compared to the pan-Indic system). Modern Tamil only adopts /ja/, /śa/, /ṣa/, /ha/ and the compound /śrī/ from Grantha into its character reportoire. This was probably done instead of using superscript numerals to increase the readability of the text (and the possible wide-spread familiarity with Grantha script few decades ago).',
          omnicode: '',
          wikicode: '',
          font: {
            'name': 'e-Grantamil',
            'url': 'http://virtualvinodh.com/download/e-Grantamil.ttf'
          }
        },
        {
          label: 'Tamil Brahmi',
          value: 'TamilBrahmi',
          sscode: '',
          ssdesc: '',
          wikicode: 'Tamil-Brahmi',
          wikidesc: 'Tamil-Brahmi is a variant of the Brahmi script used to write the Tamil language. These are the earliest documents of a Dravidian language, and the script was well established in the Chera and Pandyan states, in what is now Tamil Nadu, Kerala and Sri Lanka. Inscriptions have been found on cave beds, pot sherds, Jar burials, coins, seals, and rings.',
          omnicode: '',
          font: {
            'name': '',
            'url': ''
          }
        },
        {
          label: 'Telugu',
          value: 'Telugu',
          sscode: 'Telu',
          ssdesc: 'The Telugu script is used for writing the Telugu language, a Dravidian language spoken by almost 70,000,000 people in South India. The Telugu script is also used for writing a number of minority languages in Southern India, including Chenchu, Savara and Manna-Dora to which the Telugu language is related. The script is closely related to the Kannada script.',
          omnicode: 'telugu',
          wikicode: 'Telugu_script',
          font: {
            'name': 'Lohit Telugu',
            'url': 'https://pagure.io/lohit/tree/master'
          }
        },
        // Font not working
        // {
        //  label: 'Tolong Siki',
        //  value: 'TolongSiki'
        // },
        {
          label: 'Thaana (Dhivehi)',
          value: 'Thaana',
          sscode: 'Thaa',
          ssdesc: 'The Thaana script is used for writing the Maldivian language, also known as Dhivehi, spoken by about 370,000 people in the Maldives and in Maldivian communities in India. It is one of the few alphabets in the world which does not have its roots in the Proto-Canaanite script. Rather, the first nine letters are derived from the shapes of the numerals used in Arabic writing, and the next nine from earlier forms of Maldivian letters.',
          omnicode: 'thaana',
          wikicode: 'Thaana',
          font: {
            'name': '',
            'url': ''
          }
        },
        {
          label: 'Thai',
          value: 'Thai',
          sscode: 'Thai',
          ssdesc: 'The Thai script is used primarily for writing the Thai language, as well as Northern Thai, Northeastern Thai, Southern Thai, and Thai Song, which are separate languages. It is also used to write a number of minority languages in Thailand, Laos and China, as well as Pali, which is widely used in Buddhist temples and monasteries. Both the Thai language and script are closely related to Laotian. The script is of Indic origin, derived from Old Khmer.',
          omnicode: 'thai',
          wikicode: 'Thai_alphabet',
          font: {
            'name': '',
            'url': ''
          }
        },
        {
          label: 'Tibetan',
          value: 'Tibetan',
          sscode: 'Tibt',
          ssdesc: 'The Tibetan script is used for writing the Tibetan, Dzongkha, Ladakhi and Sikkimese languages, spoken in Tibet, Bhutan, Nepal and India. It is also used for transcribing religious Sanskrit texts. Tibetan Buddhism traditionally ascribes its creation to Minister Thon mi Sambhota in Northeast India. What is generally agreed upon is that it is ultimately derived from the Brahmi script.',
          omnicode: 'tibetan',
          wikicode: 'Tibetan_alphabet',
          font: {
            'name': '',
            'url': ''
          }
        },
        {
          label: 'Tirhuta (Maithili)',
          value: 'Tirhuta',
          sscode: 'Tirh',
          ssdesc: 'The Tirhuta (also called Mithilakshar) script has historically been used for writing the Maithili language, an Indo-Aryan language spoken by almost 35 million people. Nowadays, the Maithili language is written almost exclusively in the Devanagari script, although Tirhuta is still sometimes used by religious pundits for writing ceremonial letters and documents, and efforts are underway to broaden the scope of its usage.',
          omnicode: 'maithili',
          wikicode: 'Tirhuta',
          font: {
            'name': 'Mithila Uni',
            'url': 'http://vedicastrology.wikidot.com/local--files/mithilakshara-font/MithilaUni.ttf'
          }
        },
        {
          label: 'Urdu',
          value: 'Urdu',
          sscode: '',
          ssdesc: '',
          wikicode: 'Urdu_alphabet',
          wikidesc: 'The Urdu alphabet is the right-to-left alphabet used for the Urdu language. It is a modification of the Persian alphabet known as Perso-Arabic, which is itself a derivative of the Arabic alphabet. The Urdu alphabet has up to 58 letters. With 39 basic letters and no distinct letter cases, the Urdu alphabet is typically written in the calligraphic Nastaʿlīq script, whereas Arabic is more commonly in the Naskh style.',
          omnicode: 'urdu',
          font: {
            'name': 'Noto Sans Nastaliq Urdu',
            'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoNastaliqUrdu/NotoNastaliqUrdu-Regular.otf'
          }
        },
        {
          label: 'Vatteluttu',
          value: 'Vatteluttu',
          sscode: '',
          ssdesc: '',
          wikicode: 'Vatteluttu_alphabet',
          font: {
            'name': 'e-Vatteluttu',
            'url': 'https://github.com/virtualvinodh/aksharamukha/blob/master/aksharamukha-front/src/statics/e-VatteluttuOT.ttf'
          },
          wikidesc: 'The Vaṭṭeḻuttu, also spelled Vattezhutthu (literally "Round Script") was an abugida writing system in southern India and Sri Lanka in the latter half of the 1st millennium AD. Vatteluttu was the common script for writing various forms of Tamil language in Pandya-Chera region till the 9th century and after that time it came to be replaced by the present-day Tamil script everywhere except in Kerala'
        },
        {
          label: 'Warang Citi (Varang Kshiti)',
          value: 'WarangCiti',
          sscode: 'Wara',
          ssdesc: 'The Warang Citi script is used for writing the Ho language spoken largely in the state of Jharkhand in eastern India. The script displays a number of similarities with other scripts including Latin and Brahmi; scholars generally believe it is the result of borrowing into it. ',
          omnicode: 'varangkshiti',
          wikicode: 'Warang_Citi',
          font: {
            'name': 'Noto Sans WarangCiti',
            'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansWarangCiti/NotoSansWarangCiti-Regular.otf'
          }
        },
        {
          label: 'Zanabazar Square',
          value: 'ZanabazarSquare',
          sscode: 'Zanb',
          ssdesc: 'The Zanabazar Square script is also known as the Mongolian Square script. It is named after its creator, Zanabazar, the first spiritual leader of Tibetan Buddhism in Mongolia, who also developed the Soyombo script. It was used for writing the Mongolian, Sanskrit and Tibetan languages. The Zanabazar Square script was inspired by the Tibetan script and has graphical similarities to Phags-pa and its variant forms.',
          wikicode: 'Horizontal_square_script',
          omnicode: 'mhss',
          font: {
            'name': 'Babel Stone Zanabazar',
            'url': 'http://www.babelstone.co.uk/Fonts/Download/BabelStoneZanabazar.ttf'
          }
        }
      ],
      scriptsLatin: [
        {
          label: 'Roman (Harvard-Kyoto)',
          value: 'HK'
        },
        {
          label: 'Roman (ITRANS)',
          value: 'Itrans'
        },
        {
          label: 'Roman (IAST)',
          value: 'IAST'
        },
        {
          label: 'Roman (IPA)',
          value: 'IPA',
          sscode: '',
          ssdesc: '',
          miscdesc: '',
          omnicode: '',
          wikicode: 'International_Phonetic_Alphabet',
          font: {
            'name': '',
            'url': ''
          },
          wikidesc: 'The International Phonetic Alphabet (IPA) is an alphabetic system of phonetic notation based primarily on the Latin alphabet. It was devised by the International Phonetic Association in the late 19th century as a standardized representation of the sounds of spoken language. The IPA is used by lexicographers, foreign language students and teachers, linguists, speech-language pathologists, singers, actors, constructed language creators and translators. The IPA is designed to represent only those qualities of speech that are part of oral language: phones, phonemes, intonation and the separation of words and syllables.'
        },
        {
          label: 'Roman (ISO 15919)',
          value: 'ISO'
        },
        {
          label: 'Roman (Titus)',
          value: 'Titus'
        },
        {
          label: 'Roman (Velthuis)',
          value: 'Velthuis'
        },
        {
          label: 'Cyrillic (Russian)',
          value: 'RussianCyrillic',
          sscode: '',
          ssdesc: '',
          miscdesc: '',
          omnicode: '',
          wikicode: 'Russian_alphabet',
          font: {
            'name': '',
            'url': ''
          },
          wikidesc: 'The Russian alphabet uses letters from the Cyrillic script. The modern Russian alphabet consists of 33 letters. The Cyrillic script is a writing system used for various alphabets across Eurasia, particularly in Eastern Europe, the Caucasus, Central Asia, and North Asia. It is based on the Early Cyrillic alphabet developed during the 9th century AD at the Preslav Literary School in the First Bulgarian Empire. It is the basis of alphabets used in various languages, especially those of Orthodox Slavic origin, and non-Slavic languages influenced by Russian.'
        }
      ],
      scriptsRomanization: [
        {
          label: 'Harvard-Kyoto',
          value: 'HK'
        },
        {
          label: 'ITRANS',
          value: 'Itrans'
        },
        {
          label: 'Velthuis',
          value: 'Velthuis'
        },
        {
          label: 'IAST',
          value: 'IAST'
        },
        {
          label: 'ISO',
          value: 'ISO'
        },
        {
          label: 'Titus',
          value: 'Titus'
        }
      ],
      scriptsIME: [
        {
          label: 'Harvard-Kyoto',
          value: 'HK'
        },
        {
          label: 'ITRANS',
          value: 'Itrans'
        },
        {
          label: 'Velthuis',
          value: 'Velthuis'
        },
        {
          label: 'Devanagari',
          value: 'Devanagari'
        }
      ]
    }
  },
  computed: {
    scriptsOutput: function () {
      return this.scripts.filter(function (el) {
        return el.value !== 'GranthaGrantamil'
      })
      // return this.scripts.slice(1)
    },
    scriptsInput: function () {
      return this.autodetect.slice().concat(this.scripts)
    },
    scripts: function () {
      var scriptAll = this.scriptsIndic.slice().concat(this.scriptsLatin.slice())
      scriptAll.sort(this.compareObjects)
      return scriptAll
    },
    compounds: function () {
      var compounds = []
      for (let i = 0; i < this.consonants.length; i++) {
        for (let j = 0; j < this.vowels.length; j++) {
          compounds.push(this.consonants[i] + this.vowels[j])
        }
      }
      compounds = compounds.concat(this.vowels)
      compounds = compounds.concat(this.consonants)
      compounds = compounds.concat(this.ayogavahas)

      return compounds
    }
  },
  methods: {
    compareObjects: function (a, b) {
      if (a.label < b.label) {
        return -1
      } else if (a.label > b.label) {
        return 1
      }
      return 0
    },
    getScriptObject: function (name) {
      for (const s of this.scripts) {
        if (s.value === name) {
          return s
        }
      }
      return null
    },
    getDescription: function (script, link = true) {
      var desc
      var omniext

      if (script.value === 'Sundanese') {
        omniext = '.php'
      } else {
        omniext = '.htm'
      }

      if (typeof script.miscdesc === 'string' && script.miscdesc !== '') {
        desc = script.miscdesc
      } else if (typeof script.wikidesc === 'string' && script.wikidesc !== '') {
        desc = script.wikidesc

        if (link) {
          desc += ' (<i>from <a href="http://en.wikipedia.org/wiki/' + script.wikicode + '" target="_blank">Wikipedia<a></i>)'
        } else {
          desc += ' (from Wikipedia)'
        }

        if (typeof script.sscode === 'string' && script.sscode !== '' && link) {
          desc += '. Also see: <a href="https://scriptsource.org/scr/' + script.sscode + '" target="_blank">ScriptSource<a>'
        }

        if (typeof script.omnicode === 'string' && script.omnicode !== '' && link) {
          desc += 'and <a href="https://www.omniglot.com/writing/' + script.omnicode + omniext + '" target="_blank">Omniglot<a>'
        }
      } else {
        desc = script.ssdesc

        if (link) {
          desc += ' (<i>from <a href="https://scriptsource.org/scr/' + script.sscode + '" target="_blank">ScriptSource<a></i>)'
        } else {
          desc += ' (from ScriptSource)'
        }

        if (typeof script.wikicode === 'string' && script.wikicode !== '' && link) {
          desc += '. Also see <a href="http://en.wikipedia.org/wiki/' + script.wikicode + '" target="_blank">Wikipedia<a>'
        }

        if (typeof script.omnicode === 'string' && script.omnicode !== '' && link) {
          desc += ' and <a href="https://www.omniglot.com/writing/' + script.omnicode + omniext + '" target="_blank">Omniglot<a>'
        }
      }

      return desc
    },
    getOutputClass: function (tgt, postOptions = []) {
      if (postOptions.includes('siddhamap') && tgt === 'Siddham') {
        return 'siddhamap'
      } else if (postOptions.includes('tradOrtho') && tgt === 'Malayalam') {
        return 'malayalamold'
      } else if (postOptions.includes('siddhammukta') && tgt === 'Siddham') {
        return 'siddhammukta'
      } else if (postOptions.includes('LimbuDevanagariConvention') && tgt === 'Devanagari') {
        return 'limbudeva'
      } else if (postOptions.includes('egrantamil') && tgt === 'Grantha') {
        return 'granthagrantamil'
      } else if (postOptions.includes('nepaldevafont') && tgt === 'Newa') {
        return 'nepaldevafont'
      } else if (postOptions.includes('ranjanalantsa') && tgt === 'Ranjana') {
        return 'ranjanalantsa'
      } else if (postOptions.includes('ranjanawartu') && tgt === 'Ranjana') {
        return 'ranjanawartu'
      } else if (postOptions.includes('oldtamilortho') && tgt === 'Tamil') {
        return 'tamilold'
      } else {
        return tgt.toLowerCase()
      }
    },
    getInputClass: function (src, preOptions = []) {
      if (preOptions.includes('siddhammukta') && src === 'Siddham') {
        return 'siddhammukta'
      } else if (preOptions.includes('egrantamil') && src === 'Grantha') {
        return 'granthagrantamil'
      } else if (preOptions.includes('LimbuDevanagariConvention') && src === 'Devanagari') {
        return 'limbudeva'
      } else {
        return src.toLowerCase()
      }
    },
    replaceCommaJSON: function (script, array2) {
      if (script === 'Urdu' || script === 'Thaana') {
        if (typeof array2 !== 'object') {
          array2 = JSON.parse(array2.replace(/،/g, ','))
        }
      }
      return array2
    },
    getRandomInt: function (min, max) {
      return Math.floor(Math.random() * (max - min + 1)) + min
    },
    scriptRandom: function () {
      return this.scriptsIndic[this.getRandomInt(0, this.scriptsIndic.length - 1)]
    },
    checkDiacritics: function (Strng) {
      var diac = false
      var diacritic = ['ˮ', 'ʼ', 'ˇ', 'ʽ', 'ˆ', '˘', '\u00B7', '\u00B9', '\u00B2', '\u00B3', '\u2074', '\u2081', '\u2082', '\u2083', '\u2084']
      diacritic.forEach(function (char) {
        if (Strng.includes(char)) {
          diac = true
        }
      })

      return diac
    },
    convertAsync: function (src, tgt, txt, sourcePreserve, optionsPost, optionsPre) {
      return new Promise(resolve => {
        var data = {
          source: src,
          target: tgt,
          text: txt,
          nativize: !sourcePreserve,
          postOptions: optionsPost,
          preOptions: optionsPre
        }
        this.apiCall.post('/convert', data)
          .then(function (response) {
            resolve(response.data)
          })
          .catch(function (error) {
            console.log(error)
          })
      })
    },
    convertLoopTgtAsync: function (src, tgts, txt, sourcePreserve, optionsPost, optionsPre) {
      return new Promise(resolve => {
        var data = {
          source: src,
          targets: tgts,
          text: txt,
          nativize: !sourcePreserve,
          postOptions: optionsPost,
          preOptions: optionsPre
        }
        this.apiCall.post('/convert_loop_tgt', data)
          .then(function (response) {
            resolve(response.data)
          })
          .catch(function (error) {
            console.log(error)
          })
      })
    },
    convertLoopSrcAsync: function (srcs, tgt, txt, sourcePreserve, optionsPost, optionsPre) {
      return new Promise(resolve => {
        var data = {
          sources: srcs,
          target: tgt,
          text: txt,
          nativize: !sourcePreserve,
          postOptions: optionsPost,
          preOptions: optionsPre
        }
        this.apiCall.post('/convert_loop_src', data)
          .then(function (response) {
            resolve(response.data)
          })
          .catch(function (error) {
            console.log(error)
          })
      })
    }
  }
}
