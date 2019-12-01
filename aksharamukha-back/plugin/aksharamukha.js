const ScriptMixin = {
    data() {
        return {
            vowels: ['a', 'A', 'i', 'I', 'u', 'U', 'R', 'E', 'e', 'ai', 'O', 'o', 'au'],
            consonants: ['k', 'kh', 'g', 'gh', 'G', 'c', 'ch', 'j', 'jh', 'J', 'T', 'Th', 'D', 'Dh', 'N', 't', 'th', 'd', 'dh', 'n', 'p', 'ph', 'b', 'bh', 'm', 'y', 'r', 'l', 'v', 'z', 'S', 's', 'h', 'L', 'Z', 'r2', 'n2'],
            consonantsIndic: ['k', 'kh', 'g', 'gh', 'G', 'c', 'ch', 'j', 'jh', 'J', 'T', 'Th', 'D', 'Dh', 'N', 't', 'th', 'd', 'dh', 'n', 'p', 'ph', 'b', 'bh', 'm', 'y', 'r', 'l', 'v', 'z', 'S', 's', 'h', 'L'],
            ayogavahas: ['aM', 'aH'],
            vowelsAll: ['a', 'A', 'i', 'I', 'u', 'U', 'R', 'RR', 'lR', 'lRR', 'E', 'e', 'ai', 'O', 'o', 'au', 'aE', 'AE', 'aO', 'aM', 'aH', 'a~'],
            consonantsAll: ['k', 'kh', 'g', 'gh', 'G', 'c', 'ch', 'j', 'jh', 'J', 'T', 'Th', 'D', 'Dh', 'N', 't', 'th', 'd', 'dh', 'n', 'p', 'ph', 'b', 'bh', 'm', 'y', 'r', 'l', 'v', 'z', 'S', 's', 'h', 'Z', 'L', 'r2', 'n2', 'q', 'qh', 'g2', 'z2', 'r3', 'r3h', 'f', 'Y'],
            consontantsSpecial: ['L', 'Z', 'r2', 'n2'],
            consonantsSinhala: ['n*g', 'n*j', 'n*D', 'n*d', 'm*b'],
            ayogavahasAll: ['~', 'M', 'H'],
            preOptionsGroup: {
                'Tamil': [{
                    label: 'Transcribe Tamil <br/><small><span class="tamil">மதம், நகம்</span> → madam, nagam</small>',
                    value: 'TamilTranscribe'
                }, {
                    label: '<span class="tamil">க2 க3 க4 → க² க³ க⁴</span>',
                    value: 'TamilNumeralSub'
                }],
                'Itrans': [{
                    label: 'E/O for long, e/o for short',
                    value: 'swapEeItrans'
                }],
                'HK': [{
                    label: 'E/O for long, e/o for short',
                    value: 'swapEe'
                }],
                'Velthuis': [{
                    label: 'E/O for long, e/o for short',
                    value: 'swapEe'
                }],
                'Limbu': [{
                    label: 'SA-I for vowel length',
                    value: 'LimbuSpellingSaI'
                }],
                'Thai': [{
                    label: 'Thai orthography text <br/><small><div>e.g. พุทธะ</div></small>',
                    value: 'ThaiOrthography'
                }, {
                    label: 'Sajjhaya orthography text <br/><small><div>e.g. พุท์ธ</div></small>',
                    value: 'ThaiSajjhayaOrthography'
                }],
                'TaiTham': [{
                    label: 'Tai Tham Lao',
                    value: 'TaiThamLao'
                }, {
                    label: 'Tai Kuen',
                    value: 'TaiKuen'
                }],
                'LaoPali': [{
                    label: 'Lao orthography text<small><div class="laopali">e.g. ພຸທຘະ</div></small>',
                    value: 'LaoTranscription'
                }],
                'Devanagari': [{
                    label: 'Schwa deletion (Hindi) <small><div class="q-mt-sm">राम → rām, सबसे → sabse</div></small>',
                    value: 'RemoveSchwaHindi'
                }, {
                    label: 'Anusvara and Chandrabindu equivalent',
                    value: 'AnuChandraEqDeva'
                }],
                'Gujarati': [{
                    label: 'Schwa deletion (Only word-final) <br/><small><div class="q-mt-sm">राम → rām</div></small>',
                    value: 'SchwaFinalGujarati'
                }],
                'Bengali': [{
                    label: 'Schwa deletion (Only word-final) <br/><small><div class="q-mt-sm">রাম → rām</div></small>',
                    value: 'SchwaFinalBengali'
                }],
                'Gurmukhi': [{
                    label: 'Schwa deletion (Only word-final) <br/><small><div class="q-mt-sm">ਰਾਮ → rām</div</small>>',
                    value: 'SchwaFinalGurmukhi'
                }],
                'WarangCiti': [{
                    label: 'Schwa deletion (Only word-final) <br/><small><div class="q-mt-sm"><span class="warangciti">𑣜𑣁𑣖</span> → rām</div></small>',
                    value: 'SchwaFinalWarangCiti'
                }],
                'Grantha': [{
                    label: 'Prakrit orthography<br/><small><div class="grantha">e.g. 𑌬𑍁𑌂𑌧𑌀</div></small>'
                }, {
                    label: 'Use e-Grantamil encoding',
                    value: 'egrantamil'
                }],
                'Sinhala': [{
                    label: 'Sanskrit/Pali orthography text<br/><small><span class="sinhala">e.g. නමො භගවතෙ</span></small>',
                    value: 'SinhalaPali'
                }],
                'Malayalam': [{
                    label: 'Prakrit orthography text',
                    value: 'MalayalamPrakrit'
                }],
                'Siddham': [{
                    label: 'Devanagari-based Siddham font',
                    value: 'siddhammukta'
                }],
                'RussianCyrillic': [{
                    label: 'Pali Text',
                    value: 'CyrillicPali'
                }],
                'Urdu': [{
                    label: 'Short vowels not shown',
                    value: 'UrduShortNotShown'
                }]
            },
            preOptionsGroupSpecific: {
                'DevanagariLimbu': [{
                    label: 'Limbu Devanagari conventions<br/><small><span class="limbudev">e.g. ए़ ओ़ ए़ः के़ को़ के़ः</span></small>',
                    value: 'LimbuDevanagariConvention'
                }]
            },
            postOptionsGroupSpecific: {
                'DevanagariLimbu': [{
                    label: 'Use Limbu Devanagari conventions<small><br/><span class="limbu">ᤀᤧ ᤀᤨ ᤀᤧ᤺ ᤁᤧ ᤁᤨ ᤁᤧ᤺</span> → <span class="limbudev">ए़ ओ़ ए़ः के़ को़ के़ः</span></small>',
                    value: 'LimbuDevanagariConvention'
                }]
            },
            postOptionsGroup: {
                'Tamil': [{
                    label: 'Old orthography<br/><small><span class="tamil">லை னா</span> → <span class="tamilold">லை னா</span></small>',
                    value: 'oldtamilortho'
                }, {
                    label: 'Use Grantha Visarga<br/><small><span class="tamil">நம꞉ → நம𑌃</span></small>',
                    value: 'TamilGranthaVisarga'
                }, {
                    label: 'Subscript numerals<br/><small><span class="tamil">க²க³க⁴ → க₂க₃க₄</span></small>',
                    value: 'TamilSubScript'
                }, {
                    label: 'Dandas<br/><small><span class="tamil">. .. → । ॥</span></small>',
                    value: 'RetainTamilDanda'
                }, {
                    label: 'Disable ௐ<br/><small><span class="tamil">ௐ → ஓம்</span></small>',
                    value: 'TamilOmDisable'
                }, {
                    label: 'Disable ஶ<br/><small><span class="tamil">ஶ → ஸ²</span></small>',
                    value: 'TamilDisableSHA'
                }, {
                    label: 'Remove apostrophe<br/><small><span class="tamil">ருʼம்ʼ → ரும்</span></small>',
                    value: 'TamilRemoveApostrophe'
                }, {
                    label: 'Remove diacritic numerals<br/><small><span class="tamil">க²க³க⁴ → ககக</span></small>',
                    value: 'TamilRemoveNumbers'
                }, {
                    label: 'Tamil numerals<br/><small><span class="tamil">123 → ௧௨௩</span></small>',
                    value: 'RetainTamilNumerals'
                }, {
                    label: 'Medieval e/o with Pulli<br/><small><span class="tamil">ஒ ஓ கொ கோ → ஒ் ஒ கெ்ா கொ</span></small>',
                    value: 'MedievalTamilOrthography'
                }],
                'Chakma': [{
                    label: 'Enable all conjuncts<br/><small><span class="chakma">𑄇𑄴𑄈𑄧 𑄉𑄴𑄊𑄧 𑄚𑄴𑄖𑄧 → 𑄇𑄳𑄈𑄧 𑄉𑄳𑄊𑄧 𑄚𑄳𑄖𑄧</span></small>',
                    value: 'ChakmaEnableAllConjuncts'
                }, {
                    label: 'Enable independent i, u and e<br/><small><span class="chakma">𑄃𑄨 𑄃𑄪 𑄃𑄬 → 𑄄 𑄅 𑄆</span></small>',
                    value: 'ChakmaVowelsIndependent'
                }],
                'Newa': [{
                    label: 'Enable murmured consonants',
                    value: 'NewaMurmurConsonants'
                }, {
                    label: 'Disable Repha<br/><small><span class="newa">𑐢𑐬𑑂𑐩 → 𑐢𑐬𑑂‍𑐩</span></small>',
                    value: 'NewaDisableRepha'
                }, {
                    label: 'Use special /ta/ conjunct<br/><small><span class="newa">𑐟𑑂𑐥𑐟𑑂𑐩𑐟𑑂𑐰 → 𑐟𑑂‍𑐥𑐟𑑂‍𑐩𑐟𑑂‍𑐰</span></small>',
                    value: 'NewaSpecialTa'
                }, {
                    label: 'Use Devanagari-based Newa font<br/><small><span class="newa">𑐧𑐸𑐡𑑂𑐢𑑅</span> →<span class="nepaldevafont">बुद्धः</span></small>',
                    value: 'nepaldevafont'
                }],
                'Oriya': [{
                    label: 'Use ଵ instead of ୱ<br/><small>ଭୱତି → ଭଵତି</small>',
                    value: 'OriyaVaAlt'
                }, {
                    label: 'Use ୟ everywhere<br/><small>ଯୟାତି ଯଜ୍ଞ → ୟୟାତି ୟଜ୍ଞ</small>',
                    value: 'OriyaYYA'
                }],
                'Bengali': [{
                    label: 'Use য় everywhere<br/><small>যয়াতি যজ্ঞ → য়য়াতি য়জ্ঞ</small>',
                    value: 'BengaliYYA'
                }],
                'Siddham': [{
                    label: 'Variant vowel sign U <span class="siddham">𑗜</span><br/><small> <span class="siddham">𑖎𑖲𑖚𑖲𑖦𑖲 → 𑖎𑗜𑖚𑗜𑖦𑗜</span></small>',
                    value: 'UseAlternateVSU'
                }, {
                    label: 'Variant vowel sign UU <span class="siddham">𑗝</span><br/><small> <span class="siddham">𑖎𑖳𑖚𑖳𑖦𑖳 → 𑖎𑖳𑖚𑖳𑖦𑖳</span></small>',
                    value: 'UseAlternateVSUU'
                }, {
                    label: 'Variant I 1 <br/><small><span class="siddham">𑖂 → 𑗘</span></small>',
                    value: 'UseAlternateI1'
                }, {
                    label: 'Variant I 2 <br/><small><span class="siddham">𑖂 → 𑗙</span></small>',
                    value: 'UseAlternateI2'
                }, {
                    label: 'Variant II <br/><small><span class="siddham">𑖃 → 𑗚</span></small>',
                    value: 'UseAlternateII'
                }, {
                    label: 'Variant U <br/><small><span class="siddham">𑖄 → 𑗛</span></small>',
                    value: 'UseAlternateU'
                }, {
                    label: 'Use MuktamSiddham font',
                    value: 'siddhammukta'
                }, {
                    label: 'Use ApDevSiddham font',
                    value: 'siddhamap'
                }],
                'Devanagari': [{
                    label: 'Use ॲ instead of ऍ',
                    value: 'DevanagariACandra'
                }, {
                    label: 'Prishthamatra orthography<br/><small>के कै को कौ → कॎ कॎे कॎा कॎा</small>',
                    value: 'DevanagariPrishtamatra'
                }],
                'Gurmukhi': [{
                    label: 'Use Yakaash<br/><small>ਕ੍ਯ → ਕੵ</small>',
                    value: 'GurmukhiYakaash'
                }, {
                    label: 'Gurmukhi Numerals<br/><small>123 → ੧੨੩</small>',
                    value: 'RetainGurmukhiNumerals'
                }],
                'Thai': [{
                    label: 'Thai Orthography<br/><small><div>พุทฺธ → พุทธะ</div></small>',
                    value: 'ThaiTranscription'
                }, {
                    label: 'Sajjhaya Orthography<br/><small><div>พุทฺธ → พุท์ธ</div></small>',
                    value: 'ThaiSajjhayaOrthography'
                }, {
                    label: 'Sara a ะ as Visarga<br/><small><div>นมัห์ → นมะ</div></small>',
                    value: 'ThaiVisargaSaraA'
                }],
                'LaoPali': [{
                    label: 'Lao Orthography<br/><small><span class="laopali">ພຸທ຺ຘ → ພຸທຘະ</span></small>',
                    value: 'LaoTranscription'
                }],
                'Lao': [{
                    label: 'Lao Nativization<br/><small><span class="lao">ພຸທທັງ ຄັຈຈາມິ ສັພພັງ → ພຸດທັງ ຄັຈສາມິ ສັບພັງ</span></small>',
                    value: 'LaoNative'
                }],
                'TaiTham': [{
                    label: 'Tai Tham Lao<br/><small><span class="taitham">ᨻᩩᨴ᩠ᨵ</span> → <span class="taithamlao">ᨻᩩᨴ᩠ᨵ</span></small>',
                    value: 'TaiThamLao'
                }, {
                    label: 'Tai Kuen<br/><small><span class="taitham">ᨻᩩᨴ᩠ᨵ</span> → <span class="taikuen">ᨻᩩᨴ᩠ᨵ</span></small>',
                    value: 'TaiKuen'
                }],
                'Soyombo': [{
                    label: 'Use Sanskrit palatals<br/><small><span class="soyombo">𑩵 𑩶 𑩷 → 𑩡 𑩢 𑩣</span></small>',
                    value: 'SoyomboSanskritPalatals'
                }, {
                    label: 'Use Mongolian finals<br/><small><span class="soyombo">ak ag ad → 𑩐𑪋 𑩐𑪊 𑩐𑪍</span></small>',
                    value: 'SoyomboFinals'
                }, {
                    label: 'Use initial-form /ra/, /la/, /sa/<br/><small><span class="soyombo">𑩼𑪙𑩫 𑩽𑪙𑩫 𑪁𑪙𑩫 → 𑪆𑩫 𑪇𑩫 𑪉𑩫</span></small>',
                    value: 'SoyomboInitials'
                }, {
                    label: 'Use Tsheg<br/><small><span class="soyombo">𑩯 𑩴𑩖 → 𑩯𑪚𑩴𑩖</span></small>',
                    value: 'SoyomboSpaceTscheg'
                }],
                'Tibetan': [{
                    label: 'Use Sanskrit palatals<br/><small><span class="tibetan">ཙ ཚ ཛ ཛྷ → ཅ ཆ ཇ ཇྷ</span></small>',
                    value: 'TibetanSanskritPalatals'
                }, {
                    label: 'Use <i>Bindu with nada</i><br/><small><span class="tibetan">ཨྃ → ཨྂ</span></small>',
                    value: 'TibetanNada'
                }, {
                    label: 'Use space<br/><small><span class="tibetan">ན་མོ → ན མོ</span></small>',
                    value: 'TibetanTsheg'
                }, {
                    label: 'Use Dbu Med (Ume) style<br/><small><span class="tibetan">བུདྡྷཿ</span> → <span class="tibetandbumed">བུདྡྷཿ</span></small>',
                    value: 'tibetandbumed'
                }],
                'Sinhala': [{
                    label: 'Sanskrit/Pali Orthography<br/><small><span class="sinhala">නමෝ භගවතේ → නමො භගවතෙ</span></small>',
                    value: 'SinhalaPali'
                }, {
                    label: 'Enable all conjuncts<span><br/><small><span class="sinhala">බුද්ධස්ස → බුද්‍ධස‍්ස</span></small>',
                    value: 'SinhalaConjuncts'
                }],
                'Ranjana': [{
                    label: 'Lantsa style (Tibetan)<br/><small><span class="ranjana">बुद्धः</span> → <span class="ranjanalantsa">བུདྡྷཿ</span></small>',
                    value: 'ranjanalantsa'
                }, {
                    label: 'Wartu style (Tibetan)<br/><small><span class="ranjana">बुद्धः</span> → <span class="ranjanawartu">བུདྡྷཿ</span></small>',
                    value: 'ranjanawartu'
                }],
                'Telugu': [{
                    label: 'Dandas<br/><small><span class="telugu">. .. → । ॥</span></small>',
                    value: 'RetainTeluguDanda'
                }, {
                    label: 'Telugu Numerals<br/><small><span class="telugu">123 → ౧౨౩</span></small>',
                    value: 'RetainTeluguNumerals'
                }],
                'Gujarati': [{
                    label: 'Dandas<br/><small><span class="gujarati">. .. → । ॥</span></small>',
                    value: 'RetainGujaratiDanda'
                }],
                'Kannada': [{
                    label: 'Dandas<br/><small><span class="kannada">. .. → । ॥</span></small>',
                    value: 'RetainKannadaDanda'
                }, {
                    label: 'Kannada Numerals<br/><small><span class="kannada">123 → ೧೨೩</span></small>',
                    value: 'RetainKannadaNumerals'
                }],
                'Grantha': [{
                    label: 'Use Grantha old AU vowel sign <br/><small><div class="grantha">𑌕𑍗 → 𑌕𑍌</div></small>',
                    value: 'GranthaOldau'
                }, {
                    label: 'Prakrit orthography <br/><small><div class="grantha">𑌬𑍁𑌦𑍍𑌧𑌂 → 𑌬𑍁𑌂𑌧𑌀</div></small>',
                    value: 'GranthaPrakrit'
                }, {
                    label: 'Use e-Grantamil encoding',
                    value: 'egrantamil'
                }],
                'Urdu': [{
                    label: 'Remove short vowels<br/><small><span class="urdu">ہِنْدُوسْتانْ ← ہندوستان</span></small>',
                    value: 'UrduRemoveShortVowels'
                }],
                'IAST': [{
                    label: 'Capitalize sentences',
                    value: 'capitalizeSentence'
                }, {
                    label: 'Anusvara to Nasal<br/><small>gaṃgā → gaṅgā</small>',
                    value: 'NasaltoAnsvaraIASTISO'
                }],
                'IASTPali': [{
                    label: 'Capitalize sentences',
                    value: 'capitalizeSentence'
                }],
                'RussianCyrillic': [{
                    label: 'Pali Text',
                    value: 'CyrillicPali'
                }, {
                    label: 'Capitalize sentences',
                    value: 'capitalizeSentence'
                }, {
                    label: 'Remove Diacritics<br/><small><span class="russiancyrillic">сам̣кр̣там̣ → самкртам</span></small>',
                    value: 'removeDiacritics'
                }],
                'ISO': [{
                    label: 'Capitalize sentences',
                    value: 'capitalizeSentence'
                }, {
                    label: 'Anusvara to Nasal<br/><small>gaṁgā → gaṅgā</small>',
                    value: 'NasaltoAnsvaraIASTISO'
                }],
                'RomanReadable': [{
                    label: 'Capitalize sentences',
                    value: 'capitalizeSentence'
                }],
                'Khojki': [{
                    label: 'Retain spaces',
                    value: 'KhojkiRetainSpace'
                }],
                'WarangCiti': [{
                    label: 'Capitalize sentences',
                    value: 'capitalizeSentence'
                }],
                'Kaithi': [{
                    label: 'Retain spaces',
                    value: 'KaithiRetainSpace'
                }],
                'Bhaiksuki': [{
                    label: 'Retain spaces',
                    value: 'BhaiksukiRetainSpace'
                }],
                'Limbu': [{
                    label: 'SA-I for vowel length<small><br/><span class="limbu">ᤁ᤺ᤢᤰ → ᤁᤢᤁ᤻</span></small>',
                    value: 'LimbuSpellingSaI'
                }],
                'Sundanese': [{
                    label: 'Sundanese historical conjuncts<br/><small><span class="sundanese">ᮊ᮪ᮙ ᮊ᮪ᮝ ᮃᮊ᮪ ᮃᮙ᮪ → ᮊᮬ ᮊᮭ ᮃᮾ ᮃᮿ</span></small>',
                    value: 'SundaneseHistoricConjuncts'
                }],
                'Malayalam': [{
                    label: 'Dot Reph<br/><small><span class="malayalam">ധർമ → ധൎമ</span></small>',
                    value: 'dotReph'
                }, {
                    label: 'Archaic II & AU<br/><small><span class="malayalam">ഈ കൗ → ൟ കൌ</span></small>',
                    value: 'archaicAIAU'
                }, {
                    label: 'Traditional orthography<br/><small><span class="malayalam">തു തൂ</span> → <span class="malayalamold">തു തൂ</span></small>',
                    value: 'tradOrtho'
                }, {
                    label: 'Prakrit orthography<br/><small><span class="malayalam">ബുദ്ധ → ബുംധ</span></small>',
                    value: 'MalayalamPrakrit'
                }, {
                    label: 'Dandas<br/><small><span class="malayalam">. .. → । ॥</span></small>',
                    value: 'RetainMalayalamDanda'
                }, {
                    label: 'Malayalam Numerals<br/><small><span class="malayalam">123 → ൧൨൩</span></small>',
                    value: 'RetainMalayalamNumerals'
                }],
                'ZanabazarSquare': [{
                    label: 'Use Sanskrit palatals<br/><small><span class="zanabazarsquare">𑨣 𑨤 𑨥 → 𑨐 𑨑 𑨒</span></small>',
                    value: 'ZanabazarSanskritPalatals'
                }, {
                    label: 'Use Tsheg<br/><small><span class="zanabazarsquare">𑨝 𑨢𑨆 → 𑨝𑩁𑨢𑨆</span></small>',
                    value: 'ZanzabarSpaceTsheg'
                }, {
                    label: 'Contextual ya/ra/la/va & Repha<br/><small><span class="zanabazarsquare">𑨋𑩇𑨪 𑨋𑩇𑨫 𑨋𑩇𑨬 𑨋𑩇𑨭 𑨫𑩇𑨋 → 𑨋𑨻 𑨋𑨼 𑨋𑨽 𑨋𑨾 𑨺𑨋</span></small>',
                    value: 'ZanabazarSquareContextual'
                }, {
                    label: 'Alternate ai/au<br/><small><span class="zanabazarsquare">𑨀𑨄𑨊 𑨀𑨆𑨊 → 𑨀𑨇 𑨀𑨈</span></small>',
                    value: 'ZanabazarSquareAiAu'
                }, {
                    label: 'Mongolian final-mark<br/><small><span class="zanabazarsquare">𑨀𑨋𑨴 → 𑨀𑨋𑨳</span></small>',
                    value: 'ZanabazarSquareMongolianFinal'
                }]
            },
            autodetect: [{
                label: 'Auto-Detect',
                value: 'autodetect',
                icon: 'translate'
            }],
            scriptsIndic: [{
                    label: 'Ahom',
                    value: 'Ahom',
                    sscode: 'Ahom',
                    ssdesc: 'The Ahom script was used by members of the Tai Ahom community in India for writing the Ahom language, an extinct member of the Tai-Kadai language family. Ahom has been written for at least 500 years, and possibly much longer. The Ahom script is derived from Old Mon, ultimately of Brahmi origin. The Ahom language is occasionally used in religious rituals, and there have been some recent revival efforts by the ethnic Ahom community in Assam.',
                    omnicode: 'ahom',
                    wikicode: 'Ahom_alphabet',
                    font: {
                        'name': 'Noto Sans Ahom',
                        'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSerifAhom/NotoSerifAhom-Regular.otf'
                    },
                    language: ['Others'],
                    status: ['Living', 'Living: Minor'],
                    invented: ['Derived: Brahmi'],
                    region: ['East Indic', 'Indic']
                }, {
                    label: 'Ariyaka',
                    value: 'Ariyaka',
                    sscode: '',
                    ssdesc: '',
                    wikicode: '',
                    omnicode: 'ariyaka',
                    font: {
                        'name': 'Ariyaka',
                        'url': 'https://www.omniglot.com/fonts/ariyaka.zip'
                    },
                    language: ['Only Pali', 'Pali'],
                    status: ['Extinct', 'Extinct: Pre-Modern'],
                    invented: ['Invented'],
                    region: ['South East Asian: Mainland', 'South East Asian'],
                    miscsrc: '(from Omniglot)',
                    miscdesc: 'The Ariyaka alphabet was invented by King Mongkut Rama IV of Siam (1804-1868) as an alternative alphabet for Pali. He considered the Khmer alphabet, which was commonly used to write Pali, to be too complicated and decided to create an alphabet that was easier to use and more Western in appearance.'
                }, {
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
                    },
                    language: ['Sanskrit & Pali', 'Pali'],
                    status: ['Living', 'Living: Major'],
                    invented: ['Derived: Brahmi'],
                    region: ['East Indic', 'Indic']
                }, {
                    label: 'Avestan',
                    value: 'Avestan',
                    sscode: 'Avst',
                    ssdesc: 'The Avestan script was used from the 5th to the 13th century AD for writing the Avestan language, an Eastern Iranian language which is now only known from its use as the language of Zoroastrian religious texts called Avesta, although it is thought that at one time it was probably a natural language in everyday use. There are no surviving examples of written Avestan prior to its use as a liturgical language, and it is thought that the Avestan script was created particularly for the purpose of writing religious texts.',
                    omnicode: 'avestan',
                    wikicode: 'Avestan_alphabet',
                    font: {
                        'name': 'Noto Sans Avestan',
                        'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/unhinted/NotoSansAvestan-Regular.ttf'
                    },
                    language: ['Others'],
                    status: ['Extinct', 'Extinct: Ancient'],
                    invented: ['Derived: Aramaic'],
                    region: ['West Asian']
                }, {
                    label: 'Balinese',
                    value: 'Balinese',
                    sscode: 'Bali',
                    ssdesc: 'The Balinese script is used for writing the Balinese language spoken on the Indonesian islands of Java and Bali. It is derived from the Old Kawi script, and is ultimately of Brahmic descent. It is very similar to the Javanese script in form and behaviour; some consider them to be typological variants of one another. Historically, Balinese has been inscribed into stone, or written on palm leaves. Traditionally, the religious texts written on palm leaves were considered to be sacred and could not be read by everyone.',
                    omnicode: 'balinese',
                    wikicode: 'Balinese_script',
                    font: {
                        'name': 'Noto Serif Balinese',
                        'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSerifBalinese/NotoSerifBalinese-Regular.otf'
                    },
                    language: ['Sanskrit & Pali', 'Pali'],
                    status: ['Living', 'Living: Minor'],
                    invented: ['Derived: Brahmi', 'Derived: Pallava'],
                    region: ['South East Asian: Insular', 'South East Asian']
                }, {
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
                    },
                    language: ['Others'],
                    status: ['Living', 'Living: Minor'],
                    invented: ['Derived: Brahmi', 'Derived: Pallava'],
                    region: ['South East Asian: Insular', 'South East Asian']
                }, {
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
                    },
                    language: ['Others'],
                    status: ['Living', 'Living: Minor'],
                    invented: ['Derived: Brahmi', 'Derived: Pallava'],
                    region: ['South East Asian: Insular', 'South East Asian']
                }, {
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
                    },
                    language: ['Others'],
                    status: ['Living', 'Living: Minor'],
                    invented: ['Derived: Brahmi', 'Derived: Pallava'],
                    region: ['South East Asian: Insular', 'South East Asian']
                }, {
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
                    },
                    language: ['Others'],
                    status: ['Living', 'Living: Minor'],
                    invented: ['Derived: Brahmi', 'Derived: Pallava'],
                    region: ['South East Asian: Insular', 'South East Asian']
                }, {
                    label: 'Batak Simalungun',
                    value: 'BatakSima',
                    sublabel: 'Beta',
                    sscode: 'Batk',
                    ssdesc: 'The Batak script is used to write the six Batak languages (Toba, Karo, Dairi, Mandailing, Simalungun and Angkola) spoken collectively by approximately 3 million people on the Indonesian island of Sumatra. It is one of several scripts indigenous to the Indonesian archipelago, descended from the Old Kawi script, which in turn is derived from the Pallava, and ultimately the Brahmi, script. This is the variant used by the Simalungun language.',
                    omnicode: 'batak',
                    wikicode: 'Batak_script',
                    font: {
                        'name': 'Noto Sans Batak',
                        'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/unhinted/NotoSansBatak-Regular.ttf'
                    },
                    language: ['Others'],
                    status: ['Living', 'Living: Minor'],
                    invented: ['Derived: Brahmi', 'Derived: Pallava'],
                    region: ['South East Asian: Insular', 'South East Asian']
                }, {
                    label: 'Bengali',
                    value: 'Bengali',
                    sscode: 'Beng',
                    ssdesc: 'The Bengali (also called Bangla) script is used for writing the Bengali language, spoken by over 180,000,000 people mostly in Bangladesh and India. It is also used for a number of other Indian languages including Sylheti and, with one or two modifications, Assamese. It is a Brahmic script although its exact derivation is disputed.',
                    omnicode: 'batak',
                    wikicode: 'Batak_script',
                    font: {
                        'name': '',
                        'url': ''
                    },
                    language: ['Sanskrit & Pali', 'Pali'],
                    status: ['Living', 'Living: Major'],
                    invented: ['Derived: Brahmi'],
                    region: ['East Indic', 'Indic']
                }, {
                    label: 'Brahmi',
                    value: 'Brahmi',
                    sscode: 'Brah',
                    ssdesc: 'The Brahmi script is ancestral to most of the scripts of South Asia, Southeast Asia, and to some Central Asian scripts. The name Brahmi actually does not refer to a single, discrete script as such; general practise is to use the term to refer to any script in the family now known as Brahmic, up until approximately 400 AD, at which point they became differentiated enough to be given their own names. Brahmic writing was originally used for writing early dialects of the Prakrit language, but spread widely during the period of Indian cultural expansion in the 1st millenium AD and has since provided the underlying design for over sixty scripts used by languages from the Indo-Aryan, Dravidian, Austro-Asiatic and Tibeto-Burman language families. ',
                    omnicode: 'brahmi',
                    wikicode: 'Brahmi_script',
                    font: {
                        'name': '',
                        'url': ''
                    },
                    language: ['Sanskrit & Pali', 'Pali'],
                    status: ['Extinct', 'Extinct: Ancient'],
                    invented: ['Derived: Brahmi'],
                    region: ['Pan-Indic', 'Indic']
                }, {
                    label: 'Bhaiksuki',
                    value: 'Bhaiksuki',
                    sscode: 'Bhks',
                    ssdesc: 'Bhaiksuki is an extinct script used for writing Buddhist texts in the Indian state of Bihar. It is also known as the Arrow-Headed script due to the shape of the letters, many of which are capped with one or more triangular “arrows”. Little is known about this script.',
                    omnicode: '',
                    wikicode: 'Bhaiksuki_alphabet',
                    font: {
                        'name': 'Noto Sans Bhaiksuki',
                        'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansBhaiksuki/NotoSansBhaiksuki-Regular.otf'
                    },
                    language: ['Sanskrit & Pali', 'Pali'],
                    status: ['Extinct', 'Extinct: Ancient'],
                    invented: ['Derived: Brahmi'],
                    region: ['North Indic', 'Indic']
                }, {
                    label: 'Buginese (Lontara)',
                    value: 'Buginese',
                    sscode: 'Bugi',
                    ssdesc: 'The Buginese (also known as the Lontara) script is used for writing the Bugis, Makasar, and Mandar languages of Sulawesi in Indonesia. It is related to the other Brahmic scripts indigenous to the Indonesian archipelago.',
                    omnicode: 'lontara',
                    wikicode: 'Lontara_script',
                    font: {
                        'name': 'Noto Sans Buginese',
                        'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/unhinted/NotoSansBuginese-Regular.ttf'
                    },
                    language: ['Others'],
                    status: ['Living', 'Living: Minor'],
                    invented: ['Derived: Brahmi', 'Derived: Pallava'],
                    region: ['South East Asian: Insular', 'South East Asian']
                }, {
                    label: 'Buhid',
                    value: 'Buhid',
                    sscode: 'Buhd',
                    ssdesc: 'The Buhid script is used to write the Buhid language, spoken by about 8,000 people in the Mindoro region of the Philippines. It is an indigenous abugida script of Brahmic origin. It is proposed that the Buhid, Hanunoo and Tagbanwa scripts share common origins with the Tagalog script, an extinct script from the same region, because of the many features they have in common.',
                    omnicode: 'buhid',
                    wikicode: 'Buhid_alphabet',
                    font: {
                        'name': 'Nnoto Sans Buhid',
                        'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansBuhid/NotoSansBuhid-Regular.otf'
                    },
                    language: ['Others'],
                    status: ['Living', 'Living: Minor'],
                    invented: ['Derived: Brahmi', 'Derived: Pallava'],
                    region: ['South East Asian: Insular', 'South East Asian']
                }, {
                    label: 'Burmese (Myanmar)',
                    value: 'Burmese',
                    sscode: 'Mymr',
                    ssdesc: 'The Myanmar script was adapted from the Mon script, a descendent of Brahmi, and is found in stone inscriptions dating from the 12th century. It is used for writing the Burmese and Mon languages, both spoken in Myanmar (previously Burma). The two languages differ in how some phonemic values are assigned to letters. The script is also used, with character extensions, to write some of the Karen languages spoken in Myanmar and Thailand.',
                    omnicode: 'burmese',
                    wikicode: 'Burmese_alphabet',
                    font: {
                        'name': '',
                        'url': ''
                    },
                    language: ['Sanskrit & Pali', 'Pali'],
                    status: ['Living', 'Living: Major'],
                    invented: ['Derived: Brahmi', 'Derived: Pallava'],
                    region: ['South East Asian: Mainland', 'South East Asian']
                }, {
                    label: 'Chakma',
                    value: 'Chakma',
                    sscode: 'Cakm',
                    ssdesc: 'The Chakma script (also called Ojhapath, Ojhopath, or Ajhapath) is used for writing the Chakma language spoken in the Chittagong Hill Tracts of Bangladesh and in the Seven Sister States of Northeastern India. There are slight variations in the forms of the letters used in the two countries. The script is related to Mon Khmer and Myanmar, and many of the letters closely resemble Myanmar letters. It is also being adapted and extended for writing Tanchangya, a related language spoken in Bangladesh.',
                    omnicode: 'chakma',
                    wikicode: 'Chakma_alphabet',
                    font: {
                        'name': 'Noto Sans Chakma',
                        'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/unhinted/NotoSansChakma-Regular.ttf'
                    },
                    language: ['Only Pali', 'Pali'],
                    status: ['Living', 'Living: Minor'],
                    invented: ['Derived: Brahmi', 'Derived: Pallava'],
                    region: ['South East Asian: Mainland', 'South East Asian']
                }, {
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
                    },
                    language: ['Others'],
                    status: ['Living', 'Living: Minor'],
                    invented: ['Derived: Brahmi', 'Derived: Pallava'],
                    region: ['South East Asian: Insular', 'South East Asian']
                }, {
                    label: 'Devanagari',
                    value: 'Devanagari',
                    sscode: 'Deva',
                    ssdesc: 'Devanagari is a Northern Brahmic script related to many other South Asian scripts including Gujarati, Bengali, and Gurmukhi, and, more distantly, to a number of South-East Asian scripts including Thai, Balinese, and Baybayin. The script is used for over 120 spoken Indo-Aryan languages, including Hindi, Nepali, Marathi, Maithili, Awadhi, Newari and Bhojpuri. It is also used for writing Classical Sanskrit texts.',
                    omnicode: 'devanagari',
                    wikicode: 'Devanagari',
                    font: {
                        'name': 'Noto Sans Devanagari',
                        'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansDevanagari/NotoSansDevanagari-Regular.otf'
                    },
                    language: ['Sanskrit & Pali', 'Pali'],
                    status: ['Living', 'Living: Major'],
                    invented: ['Derived: Brahmi'],
                    region: ['North Indic', 'Indic']
                }, {
                    label: 'Dogra',
                    value: 'Dogra',
                    sscode: 'Dogr',
                    wikidesc: 'Dogri script is the original script of the Dogri language. It is very close to the Takri script.',
                    omnicode: '',
                    wikicode: 'Dogri_script',
                    font: {
                        'name': 'Noto Serif Dogra',
                        'url': 'https://github.com/googlefonts/noto-fonts/tree/master/phaseIII_only/unhinted/otf/NotoSerifDogra'
                    },
                    language: ['Sanskrit & Pali', 'Pali'],
                    status: ['Extinct', 'Extinct: Pre-Modern'],
                    invented: ['Derived: Brahmi'],
                    region: ['North Indic', 'Indic']
                }, {
                    label: 'Gondi (Gunjala)',
                    value: 'GunjalaGondi',
                    sscode: 'Gong',
                    ssdesc: 'The Gunjala Gondi script, also known as Koytura Gunjala Lipi, is named after the village of Gunjala in the Indian state of Telangana (formerly part of Andhra Pradesh) where manuscripts written in the script were recently found. The script is used to write the Gondi language and is distinct from the Masaram Gondi script designed in 1928 by Munshi Mangal Singh Masaram.\nGunjala Gondi manuscripts have been dated to 1750 and reference events as early as the 6th and 7th centuries. The script is cursive, hand-written sources showing syllables of a word connected using pen strokes. It does not appear to be genetically related to other scripts, although it strongly resembles the Modi script in appearance and style.',
                    omnicode: '',
                    wikicode: 'Gunjala_Gondi_Lipi',
                    font: {
                        'name': 'Noto Sans Gunjala Gondi',
                        'url': 'https://github.com/googlefonts/noto-fonts/tree/master/phaseIII_only/unhinted/otf/NotoSansGunjalaGondi'
                    },
                    language: ['Others'],
                    status: ['Living', 'Living: Minor'],
                    invented: ['Derived: Brahmi'],
                    region: ['North Indic', 'Indic']
                }, {
                    label: 'Gondi (Masaram)',
                    value: 'MasaramGondi',
                    sscode: 'Gonm',
                    ssdesc: 'The Gondi language belongs to the Central Dravidian group and is spoken by about 2 million people in the South Indian states of Madhya Pradesh, Gujarat, Andhra Pradesh, Maharashtra and Chhattisgarh. The language is usually written in the  Devanagari or  Telugu scripts, but, in 1928, Munshi Mangal Singh Masaram designed a script specifically for the Gondi language. An older script for writing Gondi,  Gunjala Gondi, is being revived in some places.',
                    omnicode: '',
                    wikicode: 'Gondi_writing',
                    font: {
                        'name': 'Noto Sans Masaram Gondi',
                        'url': 'https://github.com/googlefonts/noto-fonts/tree/master/phaseIII_only/unhinted/otf/NotoSansMasaramGondi'
                    },
                    language: ['Others'],
                    status: ['Living', 'Living: Minor'],
                    invented: ['Invented'],
                    region: ['North Indic', 'Indic']
                }, {
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
                    },
                    language: ['Sanskrit & Pali', 'Pali'],
                    status: ['Living', 'Living: Minor'],
                    invented: ['Derived: Brahmi', 'Derived: Pallava'],
                    region: ['South Indic', 'Indic']
                }, {
                    label: 'Grantha (Pandya)',
                    value: 'GranthaPandya',
                    sscode: '',
                    ssdesc: '',
                    wikidesc: 'Pandya Grantha refers to the version of Grantha as used in the Velvikudi inscription. The Velvikudi inscription is an 8th-century bilingual copper-plate inscription from the Pandya kingdom of southern India. Inscribed in Sanskrit and Tamil languages, it records the Pandya king Nedunjadaiyan\'s renewal of a grant of the Velvikudi village to a brahmana.',
                    omnicode: '',
                    wikicode: 'Velvikudi_inscription',
                    font: {
                        'name': 'e-Pandya',
                        'url': 'https://github.com/virtualvinodh/aksharamukha/blob/master/aksharamukha-front/src/statics/e-Pandya.ttf'
                    },
                    language: ['Sanskrit & Pali', 'Pali'],
                    status: ['Extinct', 'Extinct: Ancient'],
                    invented: ['Derived: Brahmi', 'Derived: Pallava'],
                    region: ['South Indic', 'Indic']
                }, {
                    label: 'Gujarati',
                    value: 'Gujarati',
                    sscode: 'Gujr',
                    ssdesc: 'The Gujarati script is used for writing the Gujarati and Chodri languages, together spoken by almost 47 million people. It is also used alongside the Devanagari script for writing a number of languages used by the Bhil people, one of India\'s largest indigenous groups. The script is related to Devanagari, with modifications to some of the letters, and without the headstroke which characterizes most of the Nagari scripts. The loss of the headstroke reflects the script\'s origins in informal writing; until the mid-19th century it was used primarily for bookkeeping and personal correspondence',
                    omnicode: 'gujarati',
                    wikicode: 'Gujarati_alphabet',
                    font: {
                        'name': 'Noto Serif Gujarati',
                        'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSerifGujarati/NotoSerifGujarati-Regular.otf'
                    },
                    language: ['Sanskrit & Pali', 'Pali'],
                    status: ['Living', 'Living: Major'],
                    invented: ['Derived: Brahmi'],
                    region: ['West Indic', 'Indic']
                }, {
                    label: 'Hanunoo',
                    value: 'Hanunoo',
                    sscode: 'Hano',
                    ssdesc: 'The Hanunóo script is used by the Mangyan people in the mountains of Mindoro, South Philippines, to write the Hanunóo language. Perhaps due to its inaccessible location, it is one of the few indigenous Philippine scripts which has not been replaced by the Latin script. It is of Brahmic origin, descended through Old Kawi, although its history is difficult to trace in detail due to the perishable nature of bamboo, the surface on which it is traditionally inscribed.',
                    omnicode: 'hanunoo',
                    wikicode: 'Hanunó%27o_alphabet',
                    font: {
                        'name': 'Noto Sans Hanunoo',
                        'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansHanunoo/NotoSansHanunoo-Regular.otf'
                    },
                    language: ['Others'],
                    status: ['Living', 'Living: Minor'],
                    invented: ['Derived: Brahmi', 'Derived: Pallava'],
                    region: ['South East Asian: Insular', 'South East Asian']
                }, {
                    label: 'Javanese',
                    value: 'Javanese',
                    sscode: 'Java',
                    ssdesc: 'Javanese is Indonesia\'s oldest literary language, its literary history being traceable to the C4th. The present Javanese script is a modern variant of Old Kawi, an ancient Brahmic script from which many scripts in the Indonesian archipelago are derived. It is the pre-colonial script of the Javanese language spoken on the Indonesian islands of Java and Bali and is used to write the Tengger and Osing languages, also spoken in Java and Bali. The Javanese script is closely related to the Balinese script, although Javanese contains 4 consonant letters which are absent in the Balinese.',
                    omnicode: 'javanese',
                    wikicode: 'Javanese_script',
                    font: {
                        'name': 'Noto Sans Javanese',
                        'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansJavanese/NotoSansJavanese-Regular.otf'
                    },
                    language: ['Sanskrit & Pali', 'Pali'],
                    status: ['Living', 'Living: Minor'],
                    invented: ['Derived: Brahmi', 'Derived: Pallava'],
                    region: ['South East Asian: Insular', 'South East Asian']
                }, {
                    label: 'Kaithi',
                    value: 'Kaithi',
                    sscode: 'Kthi',
                    ssdesc: 'The Kaithi script has been used predominantly in the Indian states of Bihar and Uttar Pradesh (but also in other North Indian states and the Nepali terai) for writing a group of Indo-Aryan languages. Kaithi has been used for writing the Bhojpuri, Maghadi, Urdu, Awadhi, Maithili, and Bengali languages since the 16th century. Its use was generally discouraged under British rule in India, except in the state of Bihar, where it was officially sanctioned for use in government offices. The script was widely used until the early 1900s, and there is some evidence that it is still used for personal correspondence in rural areas.',
                    omnicode: 'kaithi',
                    wikicode: 'Kaithi',
                    font: {
                        'name': 'Noto Sans Kaithi',
                        'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansKaithi/NotoSansKaithi-Regular.otf'
                    },
                    language: ['Only Pali', 'Pali'],
                    status: ['Extinct', 'Extinct: Pre-Modern'],
                    invented: ['Derived: Brahmi'],
                    region: ['North Indic', 'Indic']
                }, {
                    label: 'Kannada',
                    value: 'Kannada',
                    sscode: 'Knda',
                    ssdesc: 'The Kannada script is used for writing the Kannada language spoken by over 35 million people in southern India. It is also used for writing Konkani, a South Indian language with over 3 million speakers, Tulu, with almost 2 million speakers, and a number of south Indian Living: Minor languages including Badaga, Kudiya and Paniya. The script is closely related to Telugu writing; both languages were written using the Old Kanarese script until the 1500s when it diverged into two distinct varieties.',
                    omnicode: 'kannada',
                    wikicode: 'Kannada_alphabet',
                    font: {
                        'name': 'Noto Sans Kannada',
                        'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansKannada/NotoSansKannada-Regular.otf'
                    },
                    language: ['Sanskrit & Pali', 'Pali'],
                    status: ['Living', 'Living: Major'],
                    invented: ['Derived: Brahmi'],
                    region: ['South Indic', 'Indic']
                }, {
                    label: 'Khamti Shan',
                    value: 'KhamtiShan',
                    sscode: '',
                    ssdesc: '',
                    omnicode: '',
                    wikicode: '',
                    miscsrc: '(from <a href="https://www.unicode.org/L2/L2008/08181-n3423r.pdf">L2/08-181</a>)',
                    miscdesc: 'Khamti Shan is spoken by 50,000 people in Myanmar and India. The language has a long literary tradition which was lost as people forgot their script. In the last 5 years the script has undergone a resurgence in a new form and after a pilot literacy programme is to be taught throughout the region.',
                    font: {
                        'name': '',
                        'url': ''
                    },
                    language: ['Only Pali', 'Pali'],
                    status: ['Living', 'Living: Minor'],
                    invented: ['Derived: Brahmi', 'Derived: Pallava'],
                    region: ['South East Asian: Mainland', 'South East Asian']
                }, {
                    label: 'Kharoshthi',
                    value: 'Kharoshthi',
                    sscode: 'Khar',
                    ssdesc: 'Early writing in India is associated with three scripts; Indus (Harrapan), Brahmi and Kharoshthi. The Kharoshthi script descended from Aramaic and was used in what is now Northern Pakistan and Eastern Afghanistan during the 4th or 5th century BC. It was used for about 700 years for writing a group of vernacular middle Indo-Aryan dialects collectively termed \'Prakrit\'. There has been some evidence that local variants of Kharoshthi writing were used for even longer than this along the Silk Route, but these too later died out without leaving any descendants.',
                    omnicode: 'kharosthi',
                    wikicode: 'Kharosthi',
                    font: {
                        'name': '',
                        'url': ''
                    },
                    language: ['Sanskrit & Pali', 'Pali'],
                    status: ['Extinct', 'Extinct: Ancient'],
                    invented: ['Derived: Aramaic'],
                    region: ['West Indic', 'Indic']
                }, {
                    label: 'Khmer (Cambodian)',
                    value: 'Khmer',
                    sscode: 'Khmr',
                    ssdesc: 'The Khmer script is an abugida, descended from the Brahmic script Pallava. It is used for writing Khmer, the official language of Cambodia. The script is also sometimes used for writing Living: Minor languages in Cambodia, such as Brao and Mnong.',
                    omnicode: 'khmer',
                    wikicode: 'Khmer_alphabet',
                    font: {
                        'name': 'Noto Sans Khmer',
                        'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSerifKhmer/NotoSerifKhmer-Regular.otf'
                    },
                    language: ['Sanskrit & Pali', 'Pali'],
                    status: ['Living', 'Living: Major'],
                    invented: ['Derived: Brahmi', 'Derived: Pallava'],
                    region: ['South East Asian: Mainland', 'South East Asian']
                }, {
                    label: 'Khojki',
                    value: 'Khojki',
                    sscode: 'Khoj',
                    ssdesc: 'Khojki is a Brahmi-derived abugida related to the Sharada script. It is used by the Khoja people - an ethnic group of largely Ismaili Shia Muslims - for recording religious literature in the Sindhi language. Khojki has been used since at least the 16th century, originally for manuscripts, but later in printed form also. The script has also been used to write other South Asian languages; however, in recent years its use has declined markedly.',
                    omnicode: 'khojki',
                    wikicode: 'Khojki_script',
                    font: {
                        'name': 'Noto Sans Khojki',
                        'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansKhojki/NotoSansKhojki-Regular.otf'
                    },
                    language: ['Others'],
                    status: ['Living', 'Living: Minor'],
                    invented: ['Derived: Brahmi'],
                    region: ['West Indic', 'Indic']
                }, {
                    label: 'Khom Thai',
                    value: 'KhomThai',
                    sscode: '',
                    ssdesc: '',
                    miscdesc: 'This is an old Thai script sometimes found in religious documents, and still commonly used for labeling amulets, magical pictures (yantras) and Thai tattoos. It it mainly used for writing in the Pali language. Khom Thai has clear similarities with the Khmer script of Cambodia.',
                    miscsrc: '(from <a href="http://www.skyknowledge.com/khomthai.htm"> Skyknowledge</a>)',
                    omnicode: '',
                    wikicode: '',
                    font: {
                        'name': 'Patimokkha',
                        'url': 'https://github.com/virtualvinodh/aksharamukha/blob/master/aksharamukha-front/src/statics/Patimokkha.otf'
                    },
                    language: ['Sanskrit & Pali', 'Pali'],
                    status: ['Living', 'Living: Minor'],
                    invented: ['Derived: Brahmi', 'Derived: Pallava'],
                    region: ['South East Asian: Mainland', 'South East Asian']
                }, {
                    label: 'Khudawadi',
                    value: 'Khudawadi',
                    sscode: 'Sind',
                    ssdesc: 'The Khudawadi (also called Sindhi) script was used for writing the Indo-Aryan Sindhi language spoken by almost 20 million people in the Sindh province of Pakistan and in India. It is no longer used. It was used by traders and merchants to record their information and rose to importance as the script began to be used to record information kept secret from other groups and kingdoms.',
                    omnicode: 'sindhi',
                    wikicode: 'Khudabadi_script',
                    font: {
                        'name': 'Nodo Sans Khudawadi',
                        'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansKhudawadi/NotoSansKhudawadi-Regular.otf'
                    },
                    language: ['Only Pali', 'Pali'],
                    status: ['Extinct', 'Extinct: Pre-Modern'],
                    invented: ['Derived: Brahmi'],
                    region: ['West Indic', 'Indic']
                }, {
                    label: 'Lao',
                    value: 'Lao',
                    sscode: 'Laoo',
                    ssdesc: 'The Lao script is used for writing the Lao language, and is also the official script of a number of Living: Minor languages in Laos. The Lao language is closely related to Thai; there is a considerable Lao-speaking population in Thailand who write their language with the Thai script. However, the Lao script underwent a number of reforms which caused significant divergence from the Thai script.',
                    omnicode: 'lao',
                    wikicode: 'Lao_alphabet',
                    font: {
                        'name': '',
                        'url': ''
                    },
                    language: ['Others'],
                    status: ['Living', 'Living: Major'],
                    invented: ['Derived: Brahmi', 'Derived: Pallava'],
                    region: ['South East Asian: Mainland', 'South East Asian']
                }, {
                    label: 'Lao (Pali)',
                    value: 'LaoPali',
                    sscode: '',
                    ssdesc: '',
                    font: {
                        'name': 'Lao Pali (Alpha)',
                        'url': 'https://github.com/virtualvinodh/aksharamukha/blob/master/aksharamukha-front/src/statics/LaoPaliAlpha-Extralight.otf'
                    },
                    language: ['Only Pali', 'Pali'],
                    status: ['Living', 'Living: Minor'],
                    invented: ['Derived: Brahmi', 'Derived: Pallava'],
                    region: ['South East Asian: Mainland', 'South East Asian'],
                    miscsrc: '',
                    miscdesc: 'Lao (Pali) is the extended version of the Lao script to faithfully represent Pali and Sanskrit. Lao lacks several characters that are required to accurately express the phonology of those languages (unlike its neighbhouring scripts like Thai/Khmer). Therefore, Modern Lao cannot faithfully represent Pali words, and by extension, cannot transcript religious texts faithfully. In the 1930s, an additional set of characters were proposed to support Pali/Sanskrit by filling in the missing gaps. This also allows an etymological orthography for Lao (similar to Thai. The current Lao orthography is phonemic). But the addition met with little widespread support and finally by 1975, these additional characters were mostly out of use. But there is a revived interest in the characters. '
                }, {
                    label: 'Lepcha',
                    value: 'Lepcha',
                    sscode: 'Lepc',
                    ssdesc: 'The Lepcha script is also called the Róng script - Lepcha people call themselves Róngkup, children of the Róng. It is used for writing the Lepcha language, a Tibeto-Burman language spoken by about 52,800 people in India, Nepal and Bhutan. The script is derived from Tibetan writing, probably motivated by Buddhist missionary activity in the 1700s. Early manuscripts were written in vertical columns but later and current texts are written horizontally. Many letters, when rotated back to their previous vertical position, closely resemble their Tibetan counterparts.',
                    omnicode: 'lepcha',
                    wikicode: 'Lepcha_script',
                    font: {
                        'name': 'Noto Sans Lepcha',
                        'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/unhinted/NotoSansLepcha-Regular.ttf'
                    },
                    language: ['Others'],
                    status: ['Living', 'Living: Minor'],
                    invented: ['Derived: Brahmi'],
                    region: ['East Indic', 'Indic']
                }, {
                    label: 'Limbu',
                    value: 'Limbu',
                    sscode: 'Limb',
                    ssdesc: 'The Limbu script (also called Kiranti, Sirijonga or Sirijanga script) is used by about 400,000 people for writing the Limbu language spoken in Nepal and northern India. The Limbu language is also written in the Devanagari script. The origins of the script are unknown; it is evident from its structure that it is of Brahmic derivation, and appears to be closely related to the Lepcha script. Limbu folklore relates that in the 9th century the Limbu king Sirijanga prayed to the goddess Saravati for wisdom as to how to devise a script for his people, and in response she revealed the story of creation to him, written in the script.',
                    omnicode: 'limbu',
                    wikicode: 'Limbu_alphabet',
                    font: {
                        'name': 'Noto Sans Limbu',
                        'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/unhinted/NotoSansLimbu-Regular.ttf'
                    },
                    language: ['Others'],
                    status: ['Living', 'Living: Minor'],
                    invented: ['Derived: Brahmi'],
                    region: ['North Indic', 'Indic']
                }, {
                    label: 'Malayalam',
                    value: 'Malayalam',
                    sscode: 'Mlym',
                    ssdesc: 'The Malayalam script is used for writing the Malayalam language, the official language of the Indian state of Kerala, and a number of Living: Minor languages spoken in India. Until the 16th century Malayalam was written in the vattezhuthu script, a Brahmic script which developed alongside Grantha writing, from which the modern Malayalam script descended.',
                    omnicode: 'malayalam',
                    wikicode: 'Malayalam_script',
                    font: {
                        'name': 'Noto Sans Malayalam',
                        'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansMalayalam/NotoSansMalayalam-Regular.otf'
                    },
                    language: ['Sanskrit & Pali', 'Pali'],
                    status: ['Living', 'Living: Major'],
                    invented: ['Derived: Brahmi', 'Derived: Pallava'],
                    region: ['South Indic', 'Indic']
                }, {
                    label: 'Mahajani',
                    value: 'Mahajani',
                    sscode: 'Mahj',
                    ssdesc: 'The Mahajani script was a commercial script (महाजन mahajana is the Hindi word for ‘banker’) used across Northern India until the middle of the 20th century. It was used by speakers of a number of languages, including Hindi, Marwari and Punjabi, and was taught in special merchant- and business-focused schools alongside other skills required for conducting business.',
                    omnicode: '',
                    wikicode: 'Mahajani',
                    font: {
                        'name': 'Noto Sans Mahajani',
                        'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansMahajani/NotoSansMahajani-Regular.otf'
                    },
                    language: ['Others'],
                    status: ['Extinct', 'Extinct: Pre-Modern'],
                    invented: ['Derived: Brahmi'],
                    region: ['North Indic', 'Indic']
                }, {
                    label: 'Meetei Mayek (Manipuri)',
                    value: 'MeeteiMayek',
                    sscode: 'Mtei',
                    ssdesc: 'The Meetei Mayek script is used for writing the Meetei (also called Manipuri) language spoken by about 1,400,000 people in India, primarily the state of Manipur, Bangladesh, and Myanmar. The language has been largely written in the Bengali script since the 18th century, but Meetei Mayek writing has experienced a resurgence in the last hundred years. The origins of the script are controversial, most of the early documents having been destroyed in the 18th century. Some sources claim it has been used for almost 4,000 years, and others suggest it derived from the Bengali script as recently as the 17th century.',
                    omnicode: 'manipuri',
                    wikicode: 'Meitei_script',
                    font: {
                        'name': 'Noto Sans Meetei Mayek',
                        'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/unhinted/NotoSansMeeteiMayek-Regular.ttf'
                    },
                    language: ['Only Pali'],
                    status: ['Living', 'Living: Minor'],
                    invented: ['Derived: Brahmi'],
                    region: ['East Indic', 'Indic']
                }, {
                    label: 'Modi',
                    value: 'Modi',
                    sscode: 'Modi',
                    ssdesc: 'The Modi script was used from the 17th century until the 1950s for writing Marathi, the state language of the Indian state of Maharashtra. The script developed from a cursive form of Devanagari, so shares a number of features with, and is visually similar to, that script. Modi is considered by many to be extinct, having been replaced by Devanagari after the 1950s. Efforts are underway to preserve knowledge of the script before the last generation of frequent users dies.',
                    omnicode: 'modi',
                    wikicode: 'Modi_script',
                    font: {
                        'name': 'Modi',
                        'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansModi/NotoSansModi-Regular.otf'
                    },
                    language: ['Sanskrit & Pali', 'Pali'],
                    status: ['Extinct', 'Extinct: Pre-Modern'],
                    invented: ['Derived: Brahmi'],
                    region: ['North Indic', 'Indic']
                }, {
                    label: 'Mon',
                    value: 'Mon',
                    sscode: '',
                    ssdesc: '',
                    omnicode: 'mon',
                    miscsrc: '(from Omniglot)',
                    miscdesc: 'Mon is an Austroasiatic language spoken in parts of Myanmar/Burma and Thailand. In 2004 there were 850,000 speakers, mainly in Mon State, and also in the Tanintharyi Region and Kayin State in southern Myanmar.',
                    font: {
                        'name': '',
                        'url': ''
                    },
                    language: ['Sanskrit & Pali', 'Pali'],
                    status: ['Living', 'Living: Minor'],
                    invented: ['Derived: Brahmi', 'Derived: Pallava'],
                    region: ['South East Asian: Mainland', 'South East Asian']
                }, {
                    label: 'Multani',
                    value: 'Multani',
                    sscode: 'Mult',
                    ssdesc: 'The Multani script is used for writing the Saraiki language, spoken in the Punjab regions of India and Pakistan, and in northern Sindh in Pakistan. It is a commercial script, used mainly by merchants. Structurally, the script has characteristics of an abjad; vowels are generally not written unless they appear at the start of a word or in one-syllable V or CV clusters.',
                    omnicode: '',
                    wikicode: 'Multani_alphabet',
                    font: {
                        'name': 'Multani',
                        'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansMultani/NotoSansMultani-Regular.otf'
                    },
                    language: ['Others'],
                    status: ['Extinct', 'Extinct: Pre-Modern'],
                    invented: ['Derived: Brahmi'],
                    region: ['West Indic', 'Indic']
                }, {
                    label: 'Newa (Nepal Bhasa)',
                    value: 'Newa',
                    sscode: 'Newa',
                    ssdesc: 'The Newa script, also known as Newar, or Prachalit (meaning popular), is used primarily for writing Newari, a Tibeto-Burman language of Nepal (also called Nepal-Bhasha, literally \'Nepal-Language\', but not to be confused with Nepali). This script has also been used, extensively in some cases, for writing the Sanskrit, Nepali, Hindi, Bengali, and Maithili languages. The script is also known as Nepalakshar, Newah Akhah and Pachumol. It is one of six scripts subsumed under the name Nepal-Lipi, literally \'Nepal-Script\'',
                    omnicode: '',
                    wikicode: 'Prachalit_Nepal_alphabet',
                    font: {
                        'name': 'Noto Sans Newa',
                        'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansNewa/NotoSansNewa-Regular.otf'
                    },
                    language: ['Sanskrit & Pali', 'Pali'],
                    status: ['Living', 'Living: Minor'],
                    invented: ['Derived: Brahmi'],
                    region: ['North Indic', 'Indic']
                }, {
                    label: 'Old Persian',
                    value: 'OldPersian',
                    sscode: 'Xpeo',
                    ssdesc: 'Old Persian cuneiform was the main script for writing the Old Persian language from 525-330 BC. Visually it resembles Sumero-Akkadian cuneiform; most of the letters are arrangements of between two and five horizontal, vertical or angle-shaped wedges. However, there appears to be no derivational relationship between the sound-to-symbol mapping of individual letters in the two scripts, nor has any other script been found which links the forms of the scripts. For this reason, Old Persian cuneiform is generally believed to have been an independent invention.',
                    omnicode: 'opcuneiform',
                    wikicode: 'Old_Persian_cuneiform',
                    font: {
                        'name': 'Noto Sans Old Persian',
                        'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansOldPersian/NotoSansOldPersian-Regular.otf'
                    },
                    language: ['Others'],
                    status: ['Extinct', 'Extinct: Ancient'],
                    invented: ['Derived: Cuneiform'],
                    region: ['West Asian']
                }, {
                    label: 'Oriya',
                    value: 'Oriya',
                    sscode: 'Orya',
                    ssdesc: 'The Odia (formerly Oriya) script is used for writing the Odia language, the official language of the Indian state of Orissa, as well as a number of Dravidian and Munda Living: Minor languages spoken in that region. It is also used in Orissa for transcribing Sanskrit texts. The earliest inscriptions in the Odia language have been dated to 1051 AD, written in the Kalinga script from which modern Odia writing is derived.',
                    omnicode: 'oriya',
                    wikicode: 'Odia_alphabet',
                    font: {
                        'name': '',
                        'url': ''
                    },
                    language: ['Sanskrit & Pali', 'Pali'],
                    status: ['Living', 'Living: Major'],
                    invented: ['Derived: Brahmi'],
                    region: ['East Indic', 'Indic']
                }, {
                    label: 'PhagsPa',
                    value: 'PhagsPa',
                    sscode: 'Phag',
                    ssdesc: 'The \'Phags-pa script, called hor gsar yig in Tibetan and dörbelǰin üsüg in Mongolian, is named for its creator, the Tibetan sage \'Phags-pa Lama. \'Phags-pa was appointed \'National Perceptor\' in 1264 by the emperor Khubila Khan, by whom he was ordered to devise a script in which all the languages of his empire - including Tibetan, Uyghur, Mongolian and Chinese - could be written. The new script met with limited success and only scanty accounts of its creation exist in the biographies written by \'Phags pa\'s disciples.',
                    omnicode: 'phagspa',
                    wikicode: '%27Phags-pa_script',
                    font: {
                        'name': '',
                        'url': ''
                    },
                    language: ['Sanskrit & Pali', 'Pali'],
                    status: ['Extinct', 'Extinct: Medieval'],
                    invented: ['Derived: Brahmi'],
                    region: ['Central Asian']
                }, {
                    label: 'Punjabi (Gurmukhi)',
                    value: 'Gurmukhi',
                    sscode: 'Guru',
                    ssdesc: 'The Gurmukhi script is used primarily by followers of the Sikh religion in India to write the Punjabi language. Gurmukhi writing is historically derived from Brahmi, but its present form was developed in the 16th century by Guru Angad, successor to the founder of the Sikh religion, Guru Nanak. The word Gurmukhi means \'from the mouth of the guru\'. Muslims in the Pakistani Punjab write Punjabi in the Persian script; use of the Persian script for writing Punjabi is called Shahmukhi.',
                    omnicode: 'punjabi',
                    wikicode: 'Gurmukhi',
                    font: {
                        'name': '',
                        'url': ''
                    },
                    language: ['Only Pali', 'Pali'],
                    status: ['Living', 'Living: Major'],
                    invented: ['Derived: Brahmi'],
                    region: ['West Indic', 'Indic']
                }, {
                    label: 'Ranjana (Lantsa)',
                    value: 'Ranjana',
                    sscode: 'Qabb',
                    ssdesc: 'The Ranjana script is used for writing the Newari language of Nepal. This language is also called Nepal-Bhasha. The script was derived from Brahmi via the Old Nepal script, both of which are now extinct, around the 12th century AD. It has been used since that time in a gradually decreasing capacity, but is still used for producing Hindu and Buddhist religious texts and taught in Buddhist monasteries. It is also used as a decorative script in much the same way as calligraphy is used in the West.',
                    omnicode: 'ranjana',
                    wikicode: 'Ranjana_alphabet',
                    font: {
                        'name': 'Ranjana Unicode',
                        'url': 'https://github.com/virtualvinodh/aksharamukha/blob/master/aksharamukha-front/src/statics/RanjanaUNICODE1.0.TTF'
                    },
                    language: ['Sanskrit & Pali', 'Pali'],
                    status: ['Living', 'Living: Minor'],
                    invented: ['Derived: Brahmi'],
                    region: ['North Indic', 'Indic']
                }, {
                    label: 'Rejang',
                    value: 'Rejang',
                    sscode: 'Rjng',
                    ssdesc: 'The Rejang (also known as the Kaganga or Redjang) script is used to write the 5 Rejang dialects spoken collectively by about 200-250,000 people on the Indonesian island of Sumatra, and the Kerinci and Lampung languages of the same region. The script is thought to pre-date the introduction of Islam in the 12th century to the area, although the earliest attested document has been dated to the mid C18th. It is traditionally written on bamboo, buffalo horn, bark or copper plates',
                    omnicode: 'redjang',
                    wikicode: 'Rejang_script',
                    font: {
                        'name': 'Noto Sans Rejang',
                        'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansRejang/NotoSansRejang-Regular.otf'
                    },
                    language: ['Others'],
                    status: ['Living', 'Living: Minor'],
                    invented: ['Derived: Brahmi', 'Derived: Pallava'],
                    region: ['South East Asian: Insular', 'South East Asian']
                }, {
                    label: 'Rohingya (Hanifi)',
                    value: 'HanifiRohingya',
                    sscode: 'Rohg',
                    ssdesc: 'Hanifi Rohingya is one of four scripts used for writing the Rohingya language, spoken by about 1,500,000 people, mostly in Myanmar. There are also significant Rohingya-speaking refugee communities in Bangladesh and Thailand. The Rohingya language has been written in the  Arabic script for over 200 years, during which time it has also been written in  Myanmar and a modified Latin script known as Rohingyalish. Around 1960, Rohingya scholars began to see a need for a unique writing system which reflected their own language, and Molana Hanif created the Hanifi Rohingya script.',
                    omnicode: 'rohingya',
                    wikicode: 'Hanifi_Rohingya_script',
                    font: {
                        'name': 'Noto Sans HanifiRohingya',
                        'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansHanifiRohingya/NotoSansHanifiRohingya-Regular.otf'
                    },
                    language: ['Others'],
                    status: ['Living', 'Living: Minor'],
                    invented: ['Invented'],
                    region: ['South East Asian: Mainland', 'South East Asian']
                }, {
                    label: 'Santali (Ol Chiki)',
                    value: 'Santali',
                    sscode: 'Olck',
                    ssdesc: 'The Ol Chiki script (also called Ol Cemet, Ol, or Santali) was created by Pandit Raghunath Murmu in the 1920s for writing the Santali language, which is spoken by just under 6 million people in India, Bangladesh and Nepal. The Santali language is also written in the Devanagari, Bengali, Oriya and Roman scripts, and most people who are literate in Ol Chiki are also literate in at least one of the others. For this reason, not all Santali speakers are agreed as to the necessity of a unique script for their language, but despite competition from surrounding scripts, Ol Chiki is becoming more widely accepted.',
                    omnicode: 'santali',
                    wikicode: 'Ol_Chiki_script',
                    font: {
                        'name': 'Noto Sans Old Chiki',
                        'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansOlChiki/NotoSansOlChiki-Regular.otf'
                    },
                    language: ['Only Pali', 'Pali'],
                    status: ['Living', 'Living: Minor'],
                    invented: ['Invented'],
                    region: ['East Indic', 'Indic']
                }, {
                    label: 'Saurashtra',
                    value: 'Saurashtra',
                    sscode: 'Saur',
                    ssdesc: 'The Saurashtra language is spoken by approximately 130,000 people in Southern India. The Saurashtra script is of Brahmic origin, although its exact derivation is not known. Unlike most of the surrounding Dravidian languages, Saurashtra is Indo-European. The language has its own script of the same name, but is also written in the Tamil, Telugu, and Devanagari scripts. There is some debate amongst speakers of the Saurashtra language as to which script is best suited to the language.',
                    omnicode: 'saurashtra',
                    wikicode: 'Saurashtra_alphabet',
                    font: {
                        'name': 'Noto Sans Saurashtra',
                        'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansSaurashtra/NotoSansSaurashtra-Regular.otf'
                    },
                    language: ['Sanskrit & Pali', 'Pali'],
                    status: ['Living', 'Living: Minor'],
                    invented: ['Invented'],
                    region: ['South Indic', 'Indic']
                }, {
                    label: 'Siddham',
                    value: 'Siddham',
                    sscode: 'Sidd',
                    ssdesc: 'Siddham is an extinct Brahmic script which was used between 600-1200 AD for writing Sanskrit. The script travelled along the silk road to China, Japan and Korea in the form of Buddhist tantra texts. An adaptation of the script is still used in some esoteric Buddhist schools in Japan, where it is called Bonji.',
                    omnicode: 'siddham',
                    wikicode: 'Siddhaṃ_script',
                    font: {
                        'name': 'Noto Sans Siddham',
                        'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansSiddham/NotoSansSiddham-Regular.otf'
                    },
                    language: ['Sanskrit & Pali', 'Pali'],
                    status: ['Living', 'Living: Minor'],
                    invented: ['Derived: Brahmi'],
                    region: ['East Asian']
                }, {
                    label: 'Shan',
                    value: 'Shan',
                    sscode: '',
                    ssdesc: '',
                    omnicode: 'shan',
                    wikicode: 'Shan_language#Alphabet',
                    font: {
                        'name': '',
                        'url': ''
                    },
                    language: ['Sanskrit & Pali', 'Pali'],
                    status: ['Living', 'Living: Minor'],
                    invented: ['Derived: Brahmi', 'Derived: Pallava'],
                    region: ['South East Asian: Mainland', 'South East Asian'],
                    miscsrc: '(from Omniglot)',
                    miscdesc: 'Shan is a Tai language spoken by about 3.3 million people in the Shan States of Burma in the northeast of the country, and also in parts of northern Thailand and in the Xishuangbanna (Sipsongpanna) Dai Autonomous Prefecture of Yunnan province in southwestern China.The Shan script is used in Burma to write Shan, although few Shan speakers can read and write in the Shan script.'
                }, {
                    label: 'Sharada',
                    value: 'Sharada',
                    sscode: 'Shrd',
                    ssdesc: 'The Sharada script evolved from Gupta Brahmi in the 9th century AD. In its earlier forms it was widespread over the northwest parts of the Indian subcontinent and was the progenitor of the Gurmukhi script, but later it became restricted to Kashmir, where it was the principal means of writing until the 20th century. In the 1950s a Perso-Arabic script was made the official script of Kashmir. Sharada is now only used by Kashmiri Pandits - a Hindu, ethnically Aryan group who inhabited the Kashmiri valley until they were exiled in the 1990s - for religious and ceremonial purposes.',
                    omnicode: 'sharda',
                    wikicode: 'Sharada_script',
                    font: {
                        'name': 'Noto Sans Sharada',
                        'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansSharada/NotoSansSharada-Regular.otf'
                    },
                    language: ['Sanskrit & Pali', 'Pali'],
                    status: ['Living', 'Living: Minor'],
                    invented: ['Derived: Brahmi'],
                    region: ['North Indic', 'Indic']
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
                    },
                    language: ['Sanskrit & Pali', 'Pali'],
                    status: ['Living', 'Living: Major'],
                    invented: ['Derived: Brahmi', 'Derived: Pallava'],
                    region: ['South Indic', 'Indic']
                }, {
                    label: 'Sora Sompeng',
                    value: 'SoraSompeng',
                    sscode: 'Sora',
                    ssdesc: 'The Sora Sompeng script is used for writing the Sora language spoken by about 310,000 people in India, predominantly in the eastern state of Orissa. Sora is in the Munda language family. It is also sometmes called Saora or Savara, but is not to be confused with the Savara language in the Dravidian family.',
                    omnicode: 'sorangsompeng',
                    wikicode: 'Sorang_Sompeng_alphabet',
                    font: {
                        'name': 'Noto Sans SoraSompeng',
                        'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansSoraSompeng/NotoSansSoraSompeng-Regular.otf'
                    },
                    language: ['Others'],
                    status: ['Living', 'Living: Minor'],
                    invented: ['Invented'],
                    region: ['East Indic', 'Indic']
                }, {
                    label: 'Soyombo',
                    value: 'Soyombo',
                    sscode: 'Soyo',
                    ssdesc: 'The Soyombo script was developed by the Mongolian monk and scholar Bogdo Zanabazar in 1686 to write Mongolian. According to legend, Zanabazar based the script on letter-like signs he saw in the sky one night. Other theories suggest that the shapes of the letters may have been based on the Ranjana script of Nepal. Soyombo can also be used to write Tibetan and Sanskrit.',
                    omnicode: 'soyombo',
                    wikicode: 'Soyombo_script',
                    font: {
                        'name': 'Noto Sans Soyombo',
                        'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansSoyombo/NotoSansSoyombo-Regular.otf'
                    },
                    language: ['Sanskrit & Pali', 'Pali'],
                    status: ['Extinct', 'Extinct: Medieval'],
                    invented: ['Derived: Brahmi'],
                    region: ['Central Asian']
                }, {
                    label: 'Sundanese',
                    value: 'Sundanese',
                    sscode: 'Sund',
                    ssdesc: 'The Sundanese script is used to write the Sundanese language, spoken by about 27 million people on the Indonesian island of Java. Today, the language is generally written in either the Sundanese or the Latin script, but has historically also been written using other scripts. It is currently taught in schools and used for public signage.',
                    omnicode: 'sundanese',
                    wikicode: 'Sundanese_script',
                    font: {
                        'name': 'Noto Sans Sundanese',
                        'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/unhinted/NotoSansSundanese-Regular.ttf'
                    },
                    language: ['Others'],
                    status: ['Living', 'Living: Minor'],
                    invented: ['Derived: Brahmi', 'Derived: Pallava'],
                    region: ['South East Asian: Insular', 'South East Asian']
                }, {
                    label: 'Syloti Nagari',
                    value: 'SylotiNagri',
                    sscode: 'Sylo',
                    ssdesc: 'The Syloti Nagri script (also called Sylheti Nagri) is the original script for the Sylheti language, spoken in Bangladesh. The script has been almost entirely replaced by the Bengali and, to a lesser extent, Latin, scripts. At its peak however, it was used by all literate Sylheti speakers for personal correspondence, record-keeping, business purposes and religious texts in the language. The script appears to be derived from the Kaithi script used in Bihar.',
                    omnicode: 'syloti',
                    wikicode: 'Sylheti_Nagari',
                    font: {
                        'name': 'Noto Sans SylotiNagri',
                        'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansSylotiNagri/NotoSansSylotiNagri-Regular.otf'
                    },
                    language: ['Others'],
                    status: ['Living', 'Living: Minor'],
                    invented: ['Derived: Brahmi'],
                    region: ['East Indic', 'Indic']
                }, {
                    label: 'Tagbanwa',
                    value: 'Tagbanwa',
                    sscode: 'Tagb',
                    ssdesc: 'The Tagbanwa (also known as Apurahuano) script is one of the Brahmic scripts indigenous to the Philippines. It is used to write the Tagbanwa language, which is spoken by approximately 8,000 people living in scattered communities throughout the Palawan region; literacy in the script is low. Of the three living indigenous Philippine scripts - Hanunoo, Buhid and Tagbanwa - Tagbanwa is acknowledged to be the least widely used.',
                    omnicode: 'tagbanwa',
                    wikicode: 'Tagbanwa',
                    font: {
                        'name': 'Noto Sans Tagbanwa',
                        'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/unhinted/NotoSansTagbanwa-Regular.ttf'
                    },
                    language: ['Others'],
                    status: ['Living', 'Living: Minor'],
                    invented: ['Derived: Brahmi', 'Derived: Pallava'],
                    region: ['South East Asian: Insular', 'South East Asian']
                }, {
                    label: 'Tagalog',
                    value: 'Tagalog',
                    sscode: 'Tglg',
                    ssdesc: 'The Tagalog script, also known as Baybayin, is an extinct script indigenous to the Philippines. It was used to write the Tagalog language, which is still spoken by 21 million people throughout the Philippines, although it is now written in the Latin script. The Tagalog script was an abugida which descended from the Oldl Kawi, and ultimately the Brahmic, scripts.',
                    omnicode: 'tagalog',
                    wikicode: 'Baybayin',
                    font: {
                        'name': 'Noto Sans Tagalog',
                        'url': 'Noto Sans Tagalog'
                    },
                    language: ['Others'],
                    status: ['Living', 'Living: Minor', 'Derived: Pallava'],
                    invented: ['Derived: Brahmi'],
                    region: ['South East Asian: Insular', 'South East Asian']
                }, {
                    label: 'Tai Laing',
                    value: 'TaiLaing',
                    sscode: '',
                    ssdesc: '',
                    omnicode: '',
                    wikicode: '',
                    miscsrc: '(from <a href="https://unicode.org/L2/L2011/11130-mymr-extras.pdf">L2/11-130</a>)',
                    miscdesc: 'The Tai Laing are a language group of about 100,000 speakers living along the Irrawaddy River in Myanmar. The writing system is part of their history that has not completely died out and there is interest in reviving it. While the script is not taught formally in schools, it is taught during school breaks.',
                    font: {
                        'name': '',
                        'url': ''
                    },
                    language: ['Only Pali', 'Pali'],
                    status: ['Living', 'Living: Minor'],
                    invented: ['Derived: Brahmi', 'Derived: Pallava'],
                    region: ['South East Asian: Mainland', 'South East Asian']
                }, {
                    label: 'Tai Tham (Lanna)',
                    sublabel: 'Beta',
                    value: 'TaiTham',
                    sscode: 'Lana',
                    ssdesc: 'The Lanna script is also known as the Tai Tham, Dham, Yuan, or Northern Thai script. It has been used for writing the Northern Thai, Lü and Khün languages. Northern Thai is the biggest language group which uses the script, with 6 million speakers, but literacy is low. The script has religious significance and is used in Buddhist monasteries.',
                    omnicode: 'lanna',
                    wikicode: 'Tai_Tham_script',
                    font: {
                        'name': 'Pali Tilok',
                        'url': 'https://github.com/virtualvinodh/aksharamukha/blob/master/aksharamukha-front/src/statics/Pali_Tilok.ttf'
                    },
                    language: ['Sanskrit & Pali', 'Pali'],
                    status: ['Living', 'Living: Minor'],
                    invented: ['Derived: Brahmi', 'Derived: Pallava'],
                    region: ['South East Asian: Mainland', 'South East Asian']
                }, {
                    label: 'Takri',
                    value: 'Takri',
                    sscode: 'Takr',
                    ssdesc: 'The Takri script was used between the 16th and 19th centuries in what are now Jammu and Kashmir, Himachal Pradesh, the Punjab, and Uttarakhand. It was used for writing the Chambeali and Dogri languages, as well as a number of Pahari (Himalayan) languages including Jaunsari and Kulvi. The script is derived from Sharada, one of the Gupta scripts, and is related to the Gurmukhi and Lahnda scripts. It was widely used both in official and personal contexts.',
                    omnicode: 'takri',
                    wikicode: 'Takri_alphabet',
                    font: {
                        'name': 'Noto Sans Takri',
                        'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansTakri/NotoSansTakri-Regular.otf'
                    },
                    language: ['Only Pali', 'Pali'],
                    status: ['Extinct', 'Extinct: Pre-Modern'],
                    invented: ['Derived: Brahmi'],
                    region: ['West Indic', 'Indic']
                }, {
                    label: 'Tamil',
                    value: 'Tamil',
                    sscode: 'Taml',
                    ssdesc: 'The Tamil script is used for writing the Tamil language, a Dravidian language spoken by over 65,500,000 people in India, Sri Lanka, Singapore, Malaysia and Mauritius. Tamil is an official language in the south Indian state of Tamil Nadu as well as in Sri Lanka and Malaysia. The script is derived from Brahmi, so is related to many of the scripts used for writing Indian Indo-Aryan languages',
                    omnicode: 'tamil',
                    wikicode: 'Tamil_script',
                    font: {
                        'name': 'Noto Sans Tamil',
                        'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansTamil/NotoSansTamil-Regular.otf'
                    },
                    language: ['Sanskrit & Pali', 'Pali'],
                    status: ['Living', 'Living: Major'],
                    invented: ['Derived: Brahmi', 'Derived: Pallava'],
                    region: ['South Indic', 'Indic']
                }, {
                    label: 'Tamil (Extended)',
                    value: 'TamilGrantha',
                    sscode: '',
                    ssdesc: '',
                    miscsrc: '',
                    miscdesc: 'Tamil (Extended) represents the attempts to use the full complimentary set of Grantha letters to fill the gaps in the Tamil script (as compared to the pan-Indic system). Modern Tamil only adopts /ja/, /śa/, /ṣa/, /ha/ and the compound /śrī/ from Grantha into its character reportoire. This was probably done instead of using superscript numerals to increase the readability of the text (and the possible wide-spread familiarity with Grantha script few decades ago).',
                    omnicode: '',
                    wikicode: '',
                    font: {
                        'name': 'e-Grantamil',
                        'url': 'http://virtualvinodh.com/download/e-Grantamil.ttf'
                    },
                    language: ['Sanskrit & Pali', 'Pali'],
                    status: ['Living', 'Living: Minor'],
                    invented: ['Derived: Brahmi', 'Derived: Pallava'],
                    region: ['South Indic', 'Indic']
                }, {
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
                    },
                    language: ['Others'],
                    status: ['Extinct', 'Extinct: Ancient'],
                    invented: ['Derived: Brahmi'],
                    region: ['South Indic', 'Indic']
                }, {
                    label: 'Telugu',
                    value: 'Telugu',
                    sscode: 'Telu',
                    ssdesc: 'The Telugu script is used for writing the Telugu language, a Dravidian language spoken by almost 70,000,000 people in South India. The Telugu script is also used for writing a number of Living: Minor languages in Southern India, including Chenchu, Savara and Manna-Dora to which the Telugu language is related. The script is closely related to the Kannada script.',
                    omnicode: 'telugu',
                    wikicode: 'Telugu_script',
                    font: {
                        'name': 'Lohit Telugu',
                        'url': 'https://pagure.io/lohit/tree/master'
                    },
                    language: ['Sanskrit & Pali', 'Pali'],
                    status: ['Living', 'Living: Major'],
                    invented: ['Derived: Brahmi'],
                    region: ['South Indic', 'Indic']
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
                    },
                    language: ['Others'],
                    status: ['Living', 'Living: Major'],
                    invented: ['Derived: Perso-Arabic'],
                    region: ['South Asian: Other']
                }, {
                    label: 'Thai',
                    value: 'Thai',
                    sscode: 'Thai',
                    ssdesc: 'The Thai script is used primarily for writing the Thai language, as well as Northern Thai, Northeastern Thai, Southern Thai, and Thai Song, which are separate languages. It is also used to write a number of Living: Minor languages in Thailand, Laos and China, as well as Pali, which is widely used in Buddhist temples and monasteries. Both the Thai language and script are closely related to Laotian. The script is of Indic origin, derived from Old Khmer.',
                    omnicode: 'thai',
                    wikicode: 'Thai_alphabet',
                    font: {
                        'name': '',
                        'url': ''
                    },
                    language: ['Sanskrit & Pali', 'Pali'],
                    status: ['Living', 'Living: Major'],
                    invented: ['Derived: Brahmi', 'Derived: Pallava'],
                    region: ['South East Asian: Mainland', 'South East Asian']
                }, {
                    label: 'Tibetan',
                    value: 'Tibetan',
                    sscode: 'Tibt',
                    ssdesc: 'The Tibetan script is used for writing the Tibetan, Dzongkha, Ladakhi and Sikkimese languages, spoken in Tibet, Bhutan, Nepal and India. It is also used for transcribing religious Sanskrit texts. Tibetan Buddhism traditionally ascribes its creation to Minister Thon mi Sambhota in Northeast India. What is generally agreed upon is that it is ultimately derived from the Brahmi script.',
                    omnicode: 'tibetan',
                    wikicode: 'Tibetan_alphabet',
                    font: {
                        'name': '',
                        'url': ''
                    },
                    language: ['Sanskrit & Pali', 'Pali'],
                    status: ['Living', 'Living: Major'],
                    invented: ['Derived: Brahmi'],
                    region: ['Central Asian']
                }, {
                    label: 'Tirhuta (Maithili)',
                    value: 'Tirhuta',
                    sscode: 'Tirh',
                    ssdesc: 'The Tirhuta (also called Mithilakshar) script has historically been used for writing the Maithili language, an Indo-Aryan language spoken by almost 35 million people. Nowadays, the Maithili language is written almost exclusively in the Devanagari script, although Tirhuta is still sometimes used by religious pundits for writing ceremonial letters and documents, and efforts are underway to broaden the scope of its usage.',
                    omnicode: 'maithili',
                    wikicode: 'Tirhuta',
                    font: {
                        'name': 'Mithila Uni',
                        'url': 'http://vedicastrology.wikidot.com/local--files/mithilakshara-font/MithilaUni.ttf'
                    },
                    language: ['Sanskrit & Pali', 'Pali'],
                    status: ['Living', 'Living: Minor'],
                    invented: ['Derived: Brahmi'],
                    region: ['East Indic', 'Indic']
                }, {
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
                    },
                    language: ['Sanskrit & Pali', 'Pali'],
                    status: ['Living', 'Living: Major'],
                    invented: ['Derived: Perso-Arabic'],
                    region: ['North Indic', 'Indic']
                }, {
                    label: 'Vatteluttu',
                    value: 'Vatteluttu',
                    sscode: '',
                    ssdesc: '',
                    wikicode: 'Vatteluttu_alphabet',
                    font: {
                        'name': 'e-Vatteluttu',
                        'url': 'https://github.com/virtualvinodh/aksharamukha/blob/master/aksharamukha-front/src/statics/e-VatteluttuOT.ttf'
                    },
                    language: ['Others'],
                    status: ['Extinct', 'Extinct: Medieval'],
                    invented: ['Derived: Brahmi'],
                    region: ['South Indic', 'Indic'],
                    wikidesc: 'The Vaṭṭeḻuttu, also spelled Vattezhutthu (literally "Round Script") was an abugida writing system in southern India and Sri Lanka in the latter half of the 1st millennium AD. Vatteluttu was the common script for writing various forms of Tamil language in Pandya-Chera region till the 9th century and after that time it came to be replaced by the present-day Tamil script everywhere except in Kerala'
                }, {
                    label: 'Warang Citi',
                    value: 'WarangCiti',
                    sscode: 'Wara',
                    ssdesc: 'The Warang Citi script is used for writing the Ho language spoken largely in the state of Jharkhand in eastern India. The script displays a number of similarities with other scripts including Latin and Brahmi; scholars generally believe it is the result of borrowing into it. ',
                    omnicode: 'varangkshiti',
                    wikicode: 'Warang_Citi',
                    font: {
                        'name': 'Noto Sans WarangCiti',
                        'url': 'https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansWarangCiti/NotoSansWarangCiti-Regular.otf'
                    },
                    language: ['Others'],
                    status: ['Living', 'Living: Minor'],
                    invented: ['Invented'],
                    region: ['East Indic', 'Indic']
                }, {
                    label: 'Zanabazar Square',
                    value: 'ZanabazarSquare',
                    sscode: 'Zanb',
                    ssdesc: 'The Zanabazar Square script is also known as the Mongolian Square script. It is named after its creator, Zanabazar, the first spiritual leader of Tibetan Buddhism in Mongolia, who also developed the Soyombo script. It was used for writing the Mongolian, Sanskrit and Tibetan languages. The Zanabazar Square script was inspired by the Tibetan script and has graphical similarities to Phags-pa and its variant forms.',
                    wikicode: 'Horizontal_square_script',
                    omnicode: 'mhss',
                    font: {
                        'name': 'Noto Sans ZanabazarSquare',
                        'url': 'https://github.com/googlefonts/noto-fonts/tree/master/phaseIII_only/unhinted/otf/NotoSansZanabazarSquare'
                    },
                    language: ['Sanskrit & Pali', 'Pali'],
                    status: ['Extinct', 'Extinct: Medieval'],
                    invented: ['Derived: Brahmi'],
                    region: ['Central Asian']
                }
            ],
            scriptsLatin: [{
                label: 'Roman (Harvard-Kyoto)',
                value: 'HK'
            }, {
                label: 'Roman (Readable)',
                value: 'RomanReadable'
            }, {
                label: 'Roman (ITRANS)',
                value: 'Itrans'
            }, {
                label: 'Roman (IAST)',
                value: 'IAST'
            }, {
                label: 'Roman (IAST: Pāḷi)',
                value: 'IASTPali'
            }, {
                language: ['Others'],
                status: ['Living', 'Living: Minor'],
                invented: ['Derived: Latin'],
                region: ['Eurasia'],
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
            }, {
                label: 'Roman (ISO 15919)',
                value: 'ISO'
            }, {
                label: 'Roman (Titus)',
                value: 'Titus'
            }, {
                label: 'Roman (Velthuis)',
                value: 'Velthuis'
            }, {
                language: ['Others'],
                status: ['Living', 'Living: Major'],
                invented: ['Derived: Greek'],
                region: ['Eurasia'],
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
            }],
            scriptsRomanization: [{
                label: 'Harvard-Kyoto',
                value: 'HK'
            }, {
                label: 'ITRANS',
                value: 'Itrans'
            }, {
                label: 'Velthuis',
                value: 'Velthuis'
            }, {
                label: 'IAST',
                value: 'IAST'
            }, {
                label: 'IAST (Pāḷi)',
                value: 'IASTPali'
            }, {
                label: 'ISO',
                value: 'ISO'
            }, {
                label: 'Titus',
                value: 'Titus'
            }, {
                label: 'Roman (Readable)',
                value: 'RomanReadable'
            }],
            scriptsIME: [{
                label: 'Harvard-Kyoto',
                value: 'HK'
            }, {
                label: 'ITRANS',
                value: 'Itrans'
            }, {
                label: 'Velthuis',
                value: 'Velthuis'
            }, {
                label: 'Devanagari',
                value: 'Devanagari'
            }],
            Region: ['South Asia', 'East Asian', 'South East Asia'],
            RegionExpand: ['Iran', 'India', 'Sri Lanka', 'Burmese', 'Philippines', 'Indonesia', 'Japan'],
            Status: ['Living', 'Extinct'],
            StatusExpand: ['Extinct', 'Living: Major', 'Living: Minor'],
            indicSubset: ['Shan', 'Khmer', 'Burmese', 'Lao', 'Thai', 'Balinese', 'Javanese', 'Tibetan', 'LaoPali', 'TaiTham', 'Cham', 'Lepcha', 'Ahom', 'ZanabazarSquare']
        }
    },
    computed: {
        scriptsOutput: function() {
            return this.scripts.filter(function(el) {
                return el.value !== 'GranthaGrantamil'
            })
            // return this.scripts.slice(1)
        },
        scriptsInput: function() {
            return this.autodetect.slice().concat(this.scripts)
        },
        scripts: function() {
            var scriptAll = this.scriptsIndic.slice().concat(this.scriptsLatin.slice())
            scriptAll.sort(this.compareObjects)
            return scriptAll
        },
        compounds: function() {
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
        downloadHTML: function(content) {
            var warning = '<span class="printhide">Proper display of the some of the text below may depend on webfonts, which in turn require being connected to the internet<br/> </span> <br/>'
            var doc = '<html><head><meta charset="utf-8"/><link rel="stylesheet" type="text/css" href="http://www.virtualvinodh.com/aksharamkh/fonts.css"></head><body>' + warning + content + '</span></body></html>'
            var blob = ''
            const e = document.createEvent('MouseEvents')
            const a = document.createElement('a')
            a.download = 'text.html'
            blob = new Blob([doc], {
                type: 'plain/html'
            })
            a.dataset.downloadurl = ['text/html', a.download, a.href].join(':')
            console.log(blob)
            a.href = window.URL.createObjectURL(blob)
            e.initEvent('click', true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null)
            a.dispatchEvent(e)
        },
        getResultPost: function(url, data = {}) {
            return new Promise(resolve => {
                this.$axios.post(url, data).then(function(response) {
                    resolve(response)
                }).catch(function(error) {
                    console.log(error)
                })
            })
        },
        readFile: function(url) {
            return new Promise(resolve => {
                var reader = new FileReader()
                reader.onload = function() {
                    resolve(reader.result)
                }
                reader.readAsDataURL(url)
            })
        },
        compareObjects: function(a, b) {
            if (a.label < b.label) {
                return -1
            } else if (a.label > b.label) {
                return 1
            }
            return 0
        },
        getScriptObject: function(name) {
            for (const s of this.scripts) {
                if (s.value === name) {
                    return s
                }
            }
            if (name === 'autodetect') {
                return this.autodetect[0]
            }
            return {
                label: '',
                value: ''
            }
        },
        getScriptObjectLabel: function(label) {
            for (const s of this.scripts) {
                if (s.label === label) {
                    return s
                }
            }
            if (name === 'autodetect') {
                return this.autodetect[0]
            }
            return {
                label: '',
                value: ''
            }
        },
        getDescription: function(script, link = true) {
            var desc
            var omniext
            if (script.value === 'Sundanese' || script.value === 'Ariyaka') {
                omniext = '.php'
            } else {
                omniext = '.htm'
            }
            if (typeof script.miscdesc === 'string' && script.miscdesc !== '') {
                desc = script.miscdesc
                if (link) {
                    desc += script.miscsrc
                }
                if (typeof script.omnicode === 'string' && script.omnicode !== '' && link) {
                    desc += ' See: <a href="https://www.omniglot.com/writing/' + script.omnicode + omniext + '" target="_blank">Omniglot<a>'
                }
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
        getOutputClass: function(tgt, postOptions = []) {
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
            } else if (postOptions.includes('tibetandbumed') && tgt === 'Tibetan') {
                return 'tibetandbumed'
            } else if (postOptions.includes('TaiThamLao') && tgt === 'TaiTham') {
                return 'taithamlao'
            } else if (postOptions.includes('TaiKuen') && tgt === 'TaiTham') {
                return 'taikuen'
            } else {
                return tgt.toLowerCase()
            }
        },
        getInputClass: function(src, preOptions = []) {
            if (preOptions.includes('siddhammukta') && src === 'Siddham') {
                return 'siddhammukta'
            } else if (preOptions.includes('egrantamil') && src === 'Grantha') {
                return 'granthagrantamil'
            } else if (preOptions.includes('LimbuDevanagariConvention') && src === 'Devanagari') {
                return 'limbudeva'
            } else if (preOptions.includes('TaiThamLao') && src === 'TaiTham') {
                return 'taithamlao'
            } else if (preOptions.includes('TaiKuen') && src === 'TaiTham') {
                return 'taikuen'
            } else {
                return src.toLowerCase()
            }
        },
        replaceCommaJSON: function(script, array2) {
            if (script === 'Urdu' || script === 'Thaana') {
                if (typeof array2 !== 'object') {
                    array2 = JSON.parse(array2.replace(/،/g, ','))
                }
            }
            return array2
        },
        getRandomInt: function(min, max) {
            return Math.floor(Math.random() * (max - min + 1)) + min
        },
        scriptRandom: function() {
            return this.scriptsIndic[this.getRandomInt(0, this.scriptsIndic.length - 1)]
        },
        checkDiacritics: function(Strng) {
            var diac = false
            var diacritic = ['ˮ', 'ʼ', 'ˇ', 'ʽ', 'ˆ', '˘', '\u00B7', '\u00B9', '\u00B2', '\u00B3', '\u2074', '\u2081', '\u2082', '\u2083', '\u2084']
            diacritic.forEach(function(char) {
                if (Strng.includes(char)) {
                    diac = true
                }
            })
            return diac
        },
        convertAsync: function(src, tgt, txt, sourcePreserve, optionsPost, optionsPre) {
            return new Promise(resolve => {
                var data = {
                    source: src,
                    target: tgt,
                    text: txt,
                    nativize: !sourcePreserve,
                    postOptions: optionsPost,
                    preOptions: optionsPre
                }
                this.apiCall.post('/convert', data).then(function(response) {
                    resolve(response.data)
                }).catch(function(error) {
                    console.log(error)
                })
            })
        },
        convertLoopTgtAsync: function(src, tgts, txt, sourcePreserve, optionsPost, optionsPre) {
            return new Promise(resolve => {
                var data = {
                    source: src,
                    targets: tgts,
                    text: txt,
                    nativize: !sourcePreserve,
                    postOptions: optionsPost,
                    preOptions: optionsPre
                }
                this.apiCall.post('/convert_loop_tgt', data).then(function(response) {
                    resolve(response.data)
                }).catch(function(error) {
                    console.log(error)
                })
            })
        },
        convertLoopSrcAsync: function(srcs, tgt, txt, sourcePreserve, optionsPost, optionsPre) {
            return new Promise(resolve => {
                var data = {
                    sources: srcs,
                    target: tgt,
                    text: txt,
                    nativize: !sourcePreserve,
                    postOptions: optionsPost,
                    preOptions: optionsPre
                }
                this.apiCall.post('/convert_loop_src', data).then(function(response) {
                    resolve(response.data)
                }).catch(function(error) {
                    console.log(error)
                })
            })
        }
    }
}
// Author: Vinodh Rajan vinodh@virtualvinodh.com
// Website: http://www.virtualvinodh.com
// Plugin: Web plugin for http://www.aksharamukha.appspot.com
// Global Data
var apiURL = "https://aksharamukha.appspot.com/api/plugin"
var navbarOld = ''
var origText = [];
var nodesListAll = []
var counter = 0
var targetOld = ""
var target = ""
var postOptionsList = []
var preOptionsList = []
var postOptionsListOld = []
var preservePrevious = false
var optionsHide = true
var scripts = ScriptMixin.data().scriptsIndic;
var postOptions = ScriptMixin.data().postOptionsGroup;
var scriptsLTR = ['Urdu', 'Thaana', 'HanifiRohingya']
scriptList = []
ScriptMixin.data().scriptsIndic.forEach(function(e) {
    scriptList.push(e.value)
})
scriptList.push('ISO')
scriptList.push('IAST')
scriptList.push('IASTPali')
scriptList.push('RomanReadable')
scriptList.push('IPA')
scriptList.push('Original')
var myTags = document.getElementsByTagName("script");
var src = myTags[myTags.length - 1].src;
var sourceURL = 'autodetect'
if (src.includes('source')) {
    sourceURL = unescape(src).split("source=")[1].split("&")[0];
}
var classURL = 'aksharamukha-text'
if (src.includes('class')) {
    classURL = unescape(src).split("class=")[1].split("&")[0];
}
var preOptionsURL = ''
if (src.includes('preoptions')) {
    preOptionsURL = unescape(src).split("preoptions=")[1].split("&")[0].split(',');
}
async function translit(element, ind, source) {
    if (target != 'Original') {
        textsTran = await transliterateReq(source, target, preservePrevious, JSON.stringify(nodesListAll[ind]), postOptionsList, preOptionsList)
        var textsTranOrig = textsTran
        try {
            if (scriptsLTR.includes(target)) {
                textsTran = textsTran.replace(/،/g, ',')
            }
            textsTran = JSON.parse(textsTran)
        } catch (e) {
            console.log(e)
            console.log(textsTranOrig)
            // console.log(typeof textsTran)
            textsTran = textsTran
        }
    } else {
        textsTran = nodesListAll[ind]
    }
    var nodes = document.createTreeWalker(element, NodeFilter.SHOW_TEXT, null, null);
    var i = 0
    while (node = nodes.nextNode()) {
        if (node.nodeValue.trim() != '') {
            node.nodeValue = textsTran[i]
            i += 1
        }
    }
}

function transliterateReq(source, target, nativize, text, postOptions, preOptions) {
    var xhttp = new XMLHttpRequest();
    return new Promise(function(resolve, reject) {
        xhttp.open("POST", apiURL, true)
        xhttp.setRequestHeader("Content-type", "application/json")
        var data = JSON.stringify({
            "source": source,
            "target": target,
            "nativize": nativize,
            'postOptions': postOptions,
            'text': text,
            'preOptions': preOptions
        });
        xhttp.send(data);
        // Setup our listener to process compeleted requests
        xhttp.onreadystatechange = function() {
            // Only run if the request is complete
            if (xhttp.readyState !== 4) return;
            // Process the response
            if (xhttp.status >= 200 && xhttp.status < 300) {
                // If successful
                resolve(xhttp.responseText);
            } else {
                // If failed
                reject({
                    status: xhttp.status,
                    statusText: xhttp.statusText
                });
            }
        };
    });
}

function optionsOutput(outputScript) {
    if (typeof postOptions[outputScript] !== 'undefined') {
        var checkbox = ''
        if (optionsHide) {
            checkbox = '<br/><span id="options" class="aksharamukha-hidedown">';
        } else {
            checkbox = '<br/><span id="options" class="aksharamukha-showup">';
        }
        postOptions[outputScript].forEach(function(option) {
            checkbox += '<input type="checkbox" name="aksharamukha-optionpost" value="' + option.value + '">' + option.label + '<br>';
        })
        return checkbox + '</span>'
    } else {
        return ''
    }
}

function appendTool() {
    if (counter == 0) {
        var transContent2 = document.getElementsByClassName(classURL)
        if (transContent2.length == 0) {
            var div = document.createElement("span");
            div.className = "aksharamukha-text " + "inputscript-" + sourceURL + " preoptions-" + preOptionsURL;
            // Move the body's children into this wrapper
            while (document.body.firstChild) {
                div.appendChild(document.body.firstChild);
            }
            // Append the wrapper to the body
            document.body.appendChild(div);
        }
        origBody = document.body.innerHTML;
    }
    // Selection Items
    var selectInit = '<span class="aksharamukha-selection"><select name="scriptinput" id="aksharamukhaselect" placeholder="Select output script"/>'
    var selectEnd = '</select></span>' ///</datalist></span>'
    var selectMid = '' // '<datalist id="script-list">'
    selectMid += '<option value="Original"> Original script </option>'
    selectMid += '<option value="IAST">IAST</option>'
    selectMid += '<option value="IASTPali">IAST (Pali)</option>'
    selectMid += '<option value="ISO">ISO</option>'
    selectMid += '<option value="RomanReadable">Readable Roman</option>'
    selectMid += '<option value="IPA">IPA</option>'
    var preservebutton = '<input type="checkbox" name="preserve" id="aksharamukha-preserve"/> Preserve source </input>'
    scripts.forEach(function(script) {
        selectMid += '<option value="' + script.value + '">' + script.label + "</option>";
    });
    document.body.insertAdjacentHTML('afterbegin', `
      <div id="aksharamukha-navbar" class="sticky">
      <div class="aksharamukha-logosec">
      <div class="logo-aksharamukha"/>
        <a href="http://aksharamukha.appspot.com">
          <img src="https://raw.githubusercontent.com/virtualvinodh/aksharamukha/master/aksharamukha-front/src/statics/icons/favicon-32x32.png" width="20px" >
        </a> <span class="aksharamukha-name">Aksharamukha</span>
      </div>
      </div>
` + selectInit + selectMid + selectEnd + preservebutton + `
  `);
    var newStyle = document.createElement('style');
    newStyle.appendChild(document.createTextNode(`
    .logo-aksharamukha {
      padding-right:5px;
    }

    .aksharamukha-logosec {
      margin-bottom: 5px;
    }

    .aksharamukha-selection {
      margin-top: 5px;
    }

    .aksharamukha-name {
      font-style: italic;
    }

    #aksharamukha-more {
      margin-top:2px;
      margin-bottom: 5px;
    }

    .aksharamukha-hidedown {
      display: none;
    }

    .aksharamukha-showup {
      display: all;
    }

    #aksharamukhaselect {
      font-family: calibri;
      width:140px;
    }

    #aksharamukha-preserve {
      margin-top:10px;
      margin-bottom: 10px;
    }

    #aksharamukha-navbar {
      float: right;
      font-family: calibri;
      position: -webkit-sticky;
      position: sticky;
      top: 20px;
      // border: 1px solid black;
      width: 150px;
      padding: 5px 5px 5px 5px;
      background: #CDCDCD;
      z-index: 1000;
    }

    #aksharamukha-navbar a {
     text-decoration: none;
    }

    #akshmukha-text {

    }
  `));
    document.head.appendChild(newStyle);
    var link = document.createElement("link");
    link.type = "text/css";
    link.rel = "stylesheet";
    link.href = 'https://cdn.jsdelivr.net/gh/virtualvinodh/aksharamukha/aksharamukha-front/src/statics/fonts.css'
    document.head.appendChild(link)
    document.getElementById('aksharamukhaselect').addEventListener('input', transliterate)
    document.getElementById('aksharamukha-preserve').addEventListener('change', transliterate)
    // Storing original content
    var transContent = document.getElementsByClassName(classURL)
    var texts = []
    for (var i = 0; i < transContent.length; i++) {
        origText.push(transContent[i].innerHTML)
        var nodes = document.createTreeWalker(transContent[i], NodeFilter.SHOW_TEXT, null, null);
        texts = []
        while (node = nodes.nextNode()) {
            if (node.nodeValue.trim() != '') {
                texts.push(node.nodeValue)
            }
        }
        nodesListAll.push(texts)
    }
    counter += 1
    navbarOld = document.getElementById('aksharamukha-navbar').innerHTML
    // Restore values
    var sel = document.getElementById('aksharamukhaselect')
    if (window.localStorage.getItem('target')) {
        sel.value = window.localStorage.getItem('target')
    }
    if (window.localStorage.getItem('preservePrevious')) {
        document.getElementById('aksharamukha-preserve').checked = JSON.parse(window.localStorage.getItem('preservePrevious'))
    }
    if (window.localStorage.getItem('target')) {
        transliterate()
    }
}
async function transliterate() {
    var sel = document.getElementById('aksharamukhaselect')
    target = sel.value
    if (scriptList.includes(target)) {
        preservePrevious = document.getElementById('aksharamukha-preserve').checked
        var postOptionsChecked = []
        var postOptions = document.getElementsByName('aksharamukha-optionpost')
        postOptionsList = []
        // console.log(targetOld)
        // console.log(target)
        if (window.localStorage.getItem('postOptionsChecked' + sel.value)) {
            var storepostOptionsChecked = window.localStorage.getItem('postOptionsChecked' + sel.value).split(',').map(x => JSON.parse(x))
            var storepostOptionsList = window.localStorage.getItem('postOptionsList' + sel.value).split(',')
            if (window.localStorage.getItem('postOptionsList' + sel.value) != '') {
                postOptionsChecked = storepostOptionsChecked
                postOptionsList = storepostOptionsList
            }
        }
        if (targetOld == target) {
            postOptionsList = []
            postOptionsChecked = []
            postOptions.forEach(function(postOption) {
                postOptionsChecked.push(postOption.checked)
                if (postOption.checked) {
                    postOptionsList.push(postOption.value)
                }
            })
        }
        var navbar = document.getElementById('aksharamukha-navbar')
        var moreButton = ''
        if (optionsOutput(target) != '') {
            navbar.innerHTML = navbarOld
            if (optionsHide) {
                moreButton = '<br/><button id="aksharamukha-more">Show options</button>'
            } else {
                moreButton = '<br/><button id="aksharamukha-more">Hide options</button>'
            }
            navbar.innerHTML = navbarOld + moreButton + optionsOutput(target, '')
            document.getElementById('aksharamukha-more').addEventListener('click', optionsToggle)
            sel = document.getElementById('aksharamukhaselect')
            sel.value = target
        } else {
            navbar.innerHTML = navbarOld
        }
        document.getElementById('aksharamukha-preserve').checked = preservePrevious
        document.getElementById('aksharamukhaselect').addEventListener('input', transliterate)
        document.getElementById('aksharamukha-preserve').addEventListener('change', transliterate)
        postOptions.forEach(function(postOption, index) {
            postOption.checked = postOptionsChecked[index]
            postOption.addEventListener('change', transliterate)
        })
        window.localStorage.setItem('target', target)
        window.localStorage.setItem('preservePrevious', preservePrevious)
        window.localStorage.setItem('postOptionsChecked' + target, postOptionsChecked)
        window.localStorage.setItem('postOptionsList' + target, postOptionsList)
        var transContent = document.getElementsByClassName(classURL)
        document.getElementById('aksharamukhaselect').value = target
        for (var i = 0; i < transContent.length; i++) {
            var source = ''
            transContent[i].classList.forEach(function(clas) {
                if (clas.includes('inputscript')) {
                    source = clas.split('-')[1]
                }
                if (clas.includes('preoptions') && clas.split('-')[1] != '') {
                    preOptionsList = clas.split('-')[1].split(',')
                }
            })
            if (source == '') {
                source = 'autodetect'
            }
            if (sourceURL !== 'autodetect') {
                source = sourceURL
            }
            if (preOptionsURL !== '') {
                preOptionsList = preOptionsURL
            }
            if (targetOld != "") {
                // console.log('removing')
                // console.log(ScriptMixin.methods.getOutputClass(targetOld, postOptionsList))
                transContent[i].classList.remove(ScriptMixin.methods.getOutputClass(targetOld, postOptionsListOld))
            }
            transContent[i].classList.add(ScriptMixin.methods.getOutputClass(target, postOptionsList))
            await translit(transContent[i], i, source)
            //getResult(transContent[i], i, source, targetOld)
        }
        targetOld = target
        postOptionsListOld = postOptionsList
    }
}

function optionsToggle() {
    var el = document.getElementById('options')
    var button = document.getElementById('aksharamukha-more')
    optionsHide = !optionsHide
    if (button.innerHTML == 'Show options') {
        el.classList = ['aksharamukha-showup']
        button.innerHTML = 'Hide options'
    } else {
        el.classList = ['aksharamukha-hidedown']
        button.innerHTML = 'Show options'
    }
}
window.onload = appendTool
console.log('Aksharamukha plugin is loaded')
