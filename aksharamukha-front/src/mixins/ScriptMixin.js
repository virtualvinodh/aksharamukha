export const ScriptMixin = {
  data () {
    return {
      apiCall: this.$axios.create({
        baseURL: 'https://aksharamukha.appspot.com/api/',
        // baseURL: 'http://localhost:8085/api',
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
          { label: 'E/O for long, e/o for short', value: 'swapEe' }
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
          { label: 'Siddham Unicode', value: 'siddhamUnicode' }
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
        'Siddham': [
          { label: 'Siddham Unicode', value: 'siddhamUnicode' },
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
          value: 'Ahom'
        },
        {
          label: 'Assamese',
          value: 'Assamese'
        },
        {
          label: 'Avestan',
          value: 'Avestan'
        },
        {
          label: 'Balinese',
          value: 'Balinese'
        },
        {
          label: 'Batak Karo',
          value: 'BatakKaro',
          sublabel: 'Beta'
        },
        {
          label: 'Batak Mandailing',
          value: 'BatakManda',
          sublabel: 'Beta'
        },
        {
          label: 'Batak Pakpak',
          value: 'BatakPakpak',
          sublabel: 'Beta'
        },
        {
          label: 'Batak Toba',
          value: 'BatakToba',
          sublabel: 'Beta'
        },
        {
          label: 'Batak Simalungan',
          value: 'BatakSima',
          sublabel: 'Beta'
        },
        {
          label: 'Bengali',
          value: 'Bengali'
        },
        {
          label: 'Brahmi',
          value: 'Brahmi'
        },
        {
          label: 'Bhaiksuki',
          value: 'Bhaiksuki'
        },
        {
          label: 'Buginese (Lontara)',
          value: 'Buginese'
        },
        {
          label: 'Buhid',
          value: 'Buhid'
        },
        {
          label: 'Burmese (Myanmar)',
          value: 'Burmese'
        },
        {
          label: 'Chakma',
          value: 'Chakma'
        },
        {
          label: 'Cham',
          value: 'Cham',
          sublabel: 'Beta'
        },
        {
          label: 'Devanagari',
          value: 'Devanagari'
        },
        {
          label: 'Grantha',
          value: 'Grantha'
        },
        {
          label: 'Pandya Grantha',
          value: 'GranthaPandya'
        },
        {
          label: 'Gujarati',
          value: 'Gujarati'
        },
        {
          label: 'Hanunoo',
          value: 'Hanunoo'
        },
        {
          label: 'Javanese',
          value: 'Javanese'
        },
        {
          label: 'Kaithi',
          value: 'Kaithi'
        },
        {
          label: 'Kannada',
          value: 'Kannada'
        },
        {
          label: 'Kharoshthi',
          value: 'Kharoshthi'
        },
        {
          label: 'Khojki',
          value: 'Khojki'
        },
        {
          label: 'Khudawadi',
          value: 'Khudawadi'
        },
        {
          label: 'Khmer (Cambodian)',
          value: 'Khmer'
        },
        {
          label: 'Lao',
          value: 'Lao'
        },
        {
          label: 'Lao (Pali)',
          value: 'LaoPali'
        },
        {
          label: 'Lepcha',
          value: 'Lepcha'
        },
        {
          label: 'Limbu',
          value: 'Limbu'
        },
        {
          label: 'Malayalam',
          value: 'Malayalam'
        },
        {
          label: 'Mahajani',
          value: 'Mahajani'
        },
        {
          label: 'Meetei Mayek',
          value: 'MeeteiMayek'
        },
        {
          label: 'Modi',
          value: 'Modi'
        },
        {
          label: 'Multani',
          value: 'Multani'
        },
        {
          label: 'Newa (Nepal Bhasa)',
          value: 'Newa'
        },
        {
          label: 'Old Persian',
          value: 'OldPersian'
        },
        {
          label: 'Oriya',
          value: 'Oriya'
        },
        {
          label: 'PhagsPa',
          value: 'PhagsPa'
        },
        {
          label: 'Punjabi (Gurmukhi)',
          value: 'Gurmukhi'
        },
        {
          label: 'Rejang',
          value: 'Rejang'
        },
        {
          label: 'Santali (Ol Chiki)',
          value: 'Santali'
        },
        {
          label: 'Saurashtra',
          value: 'Saurashtra'
        },
        {
          label: 'Siddham',
          value: 'Siddham'
        },
        {
          label: 'Sharada',
          value: 'Sharada'
        },
        // {
        //   label: 'Siddham',
        //   value: 'Siddham'
        // },
        {
          label: 'Sinhala',
          value: 'Sinhala'
        },
        {
          label: 'Sora Sompeng',
          value: 'SoraSompeng'
        },
        {
          label: 'Sundanese',
          value: 'Sundanese'
        },
        {
          label: 'Syloti Nagari',
          value: 'SylotiNagri'
        },
        {
          label: 'Tagbanwa',
          value: 'Tagbanwa'
        },
        {
          label: 'Tagalog',
          value: 'Tagalog'
        },
        {
          label: 'Tai Tham (Lanna)',
          sublabel: 'Beta',
          value: 'TaiTham'
        },
        {
          label: 'Takri',
          value: 'Takri'
        },
        {
          label: 'Tamil',
          value: 'Tamil'
        },
        {
          label: 'Tamil (with full Grantha)',
          value: 'TamilGrantha'
        },
        {
          label: 'Tamil Brahmi',
          value: 'TamilBrahmi'
        },
        {
          label: 'Telugu',
          value: 'Telugu'
        },
        // Font not working
        // {
        //  label: 'Tolong Siki',
        //  value: 'TolongSiki'
        // },
        {
          label: 'Thaana (Dhivehi)',
          value: 'Thaana'
        },
        {
          label: 'Thai',
          value: 'Thai'
        },
        {
          label: 'Tibetan',
          value: 'Tibetan'
        },
        {
          label: 'Tirhuta (Maithili)',
          value: 'Tirhuta'
        },
        {
          label: 'Urdu',
          value: 'Urdu'
        },
        {
          label: 'Vatteluttu',
          value: 'Vatteluttu'
        },
        {
          label: 'Warang Citi (Varang Kshiti)',
          value: 'WarangCiti'
        },
        {
          label: 'Zanabazar Square',
          value: 'ZanabazarSquare'
        }
      ],
      scriptsLatin: [
        {
          label: 'Harvard-Kyoto',
          value: 'HK'
        },
        {
          label: 'ITRANS',
          value: 'Itrans'
        },
        {
          label: 'IAST',
          value: 'IAST'
        },
        {
          label: 'IPA',
          value: 'IPA'
        },
        {
          label: 'ISO 15919',
          value: 'ISO'
        },
        {
          label: 'Titus',
          value: 'Titus'
        },
        {
          label: 'Velthuis',
          value: 'Velthuis'
        },
        {
          label: 'Cyrillic (Russian)',
          value: 'RussianCyrillic'
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
      return this.scriptsIndic.slice().concat(this.scriptsLatin.slice())
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
    getOutputClass: function (tgt, postOptions = []) {
      if (postOptions.includes('siddhamap') && tgt === 'Siddham') {
        return 'siddhamap'
      } else if (postOptions.includes('tradOrtho') && tgt === 'Malayalam') {
        return 'malayalamold'
      } else if (postOptions.includes('siddhamUnicode') && tgt === 'Siddham') {
        return 'siddhamunicode'
      } else if (postOptions.includes('LimbuDevanagariConvention') && tgt === 'Devanagari') {
        return 'limbudeva'
      } else if (postOptions.includes('egrantamil') && tgt === 'Grantha') {
        return 'granthagrantamil'
      } else if (postOptions.includes('nepaldevafont') && tgt === 'Newa') {
        return 'nepaldevafont'
      } else {
        return tgt.toLowerCase()
      }
    },
    getInputClass: function (src, preOptions = []) {
      if (preOptions.includes('siddhamUnicode') && src === 'Siddham') {
        return 'siddhamunicode'
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
