<template>
  <q-page padding>
      <!-- <div style="text-align: right" class="q-ma-md">
        <span class="text-red-4"> X</span> : Approximate equivalent <br/>
      </div><br/> -->
<h5> Input (IME) </h5>
  <div class="q-body-1 q-mt-md"> Tap on a script to start typing in the script. </div><br/>
  <transition-group
   enter-active-class="animated fadeIn"
   leave-active-class="animated fadeOut"
   mode="out-in"
    >
   <div v-for="category in Object.keys(scriptsCategorizedFilter)" :key="category"
     v-if="scriptsCategorizedFilter[category].length > 0">
      <component :text1="chars1[script.value]" :script1="script.value" @click="openlink(getIMELink(script.value))"
       v-for="script in scriptsCategorizedFilter[category]" :key="category + script.value" :hidetitle="hidetitle"
       :approx="script.approx" :is="type" :text2="charsIr[script.value]" v-if="type == 'explorecard'">
     </component>
   </div>
    </transition-group>
  </q-page>
</template>

<script>
import {tree} from 'vued3tree'
import { QSelect, QTooltip, QChip, QBtnToggle, QBtn, QModal, CloseOverlay, QCollapsible, QPageSticky, QField, QToggle, QSpinnerComment, QInput } from 'quasar'
import Explorecard from '../components/Explorecard'
import Explorecardsent from '../components/Explorecardsent'
import Transliterate from '../components/Transliterate'
import FilterTags from '../components/FilterTags'
import { ScriptMixin } from '../mixins/ScriptMixin'

var _ = require('underscore')

export default {
  // name: 'PageName',
  mixins: [ScriptMixin],
  directives: {CloseOverlay},
  components: {
    tree,
    QBtn,
    FilterTags,
    QToggle,
    QTooltip,
    QBtnToggle,
    QCollapsible,
    QChip,
    QInput,
    Explorecard,
    Explorecardsent,
    QSpinnerComment,
    QSelect,
    QModal,
    QPageSticky,
    Transliterate,
    QField
  },
  data () {
    return {
      opened: false,
      loading: false,
      showapprox: false,
      highapprox: false,
      sourcePreserve: false,
      type: 'explorecard',
      typeCategory: 'Indic',
      typeoptions: [
        {label: 'Sample Letter', value: 'explorecard'},
        {label: 'Sample Phrase', value: 'explorecardsent'}
      ],
      typeoptionsCategory: [
        {label: 'Indic', value: 'Indic'},
        {label: 'Semitic', value: 'Semitic'}
      ],
      scriptsCategorized: {},
      trees: {
        name: 'father',
        children: [{
          name: 'son1',
          children: [{name: 'grandson'}, {name: 'grandson2'}]
        },
        {
          name: 'son2',
          children: [{name: 'grandson3'}, {name: 'grandson4'}]
        }]
      },
      charsC: '',
      charsV: 'a',
      hidetitle: false,
      mobiletext: 'oṃ namo ratnatrayāya .',
      maintext: 'ye dharmā hetuprabhavā hetuṃ teṣāṃ tathāgato hyavadat . \nteṣāṃ ca yo nirodha evaṃ vādī mahāśramaṇaḥ ..',
      maindisp: 'āryāvalokiteśvarabodhisattvo gambhīrāyāṃ prajñāpāramitāyāṃ caryāṃ caramāṇo vyavalokayati sma .',
      mobiledisp: 'iha śāriputra rūpaṃ śūnyatā, śūnyataiva rūpam.',
      hebrewTextLong: 'וַיֹּאמֶר אֱלֹהִים אֶל מֹשֶׁה אֶהְיֶה אֲשֶׁר אֶהְיֶה וַיֹּאמֶר כֹּה תֹאמַר לִבְנֵי יִשְׂרָאֵל אֶהְיֶה שְׁלָחַנִי אֲלֵיכֶם',
      hebrewTextShort: 'אֶהְיֶה אֲשֶׁר אֶהְיֶה',
      letteroptionsC: [],
      letteroptionsCSemitic: [],
      letteroptionsV: [],
      scriptcurrent: {
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
        language: ['Sanskrit', 'Pali', 'Others'],
        status: ['Living', 'Majority'],
        invented: ['Derived: Brahmi']
      },
      updatedList: true,
      script2: 'IAST',
      chars1: {},
      chars2: ['...'],
      charsIr: {},
      scriptDescription: {},
      alphabet: 'abcdefghijklmnopqrstuvwxyz'.toUpperCase().split(''),
      languages: ['Sanskrit & Pali', 'Only Pali', 'Others'],
      status: ['Living: Major', 'Living: Minor', 'Extinct'],
      derivation: ['Invented', 'Derived: Aramaic', 'Derived: Perso-Arabic', 'Derived: Cuneiform', 'Derived: Brahmi', 'Derived: Proto-Sinaitic', 'Derived: Phoenician', 'Derived: Greek', 'Derived: Latin'],
      regions: ['Pan-Indic', 'East Indic', 'West Indic', 'North Indic', 'South Indic', 'South East Asian: Mainland', 'South East Asian: Insular', 'Central Asian', 'East Asian', 'South Asian: Other', 'West Asian', 'Mediterranean', 'North African', 'Eurasia'],
      tagsActive: [],
      activeButton: 'all',
      consIAST: ['', 'ka', 'kha', 'ga', 'gha', 'ṅa', 'ca', 'cha', 'ja', 'jha', 'ña', 'ṭa', 'ṭha', 'ḍa', 'ḍha', 'ṇa', 'ta', 'tha', 'da', 'dha', 'na', 'pa', 'pha', 'ba', 'bha', 'ma', 'ya', 'ra', 'la', 'va', 'śa', 'ṣa', 'sa', 'ha', 'l̤a', 'ḻa', 'ṟa', 'ṉa', 'qa', 'k͟ha', 'ġa', 'za', 'r̤a', 'r̤ha', 'fa', 'ẏa'].map(x => x.replace('a', '')),
      consSemitic: ['ʾ', 'b', 'g', 'd', 'h', 'w', 'z', 'ḥ', 'ṭ', 'y', 'k', 'l', 'm', 'n', 's', 'ʿ', 'p', 'ṣ', 'q', 'r', 'š', 't'],
      cons: ['', 'ka', 'kha', 'ga', 'gha', 'Ga', 'ca', 'cha', 'ja', 'jha', 'Ja', 'Ta', 'Tha', 'Da', 'Dha', 'Na', 'ta', 'tha', 'da', 'dha', 'na', 'pa', 'pha', 'ba', 'bha', 'ma', 'ya', 'ra', 'la', 'va', 'za', 'Sa', 'sa', 'ha', 'La', 'Za', 'r2a', 'n2a', 'qa', 'qha', 'g2a', 'z2a', 'r3a', 'r3ha', 'fa', 'Ya'].map(x => x.replace('a', ''))

    }
  },
  mounted: function () {
    var vowels = ['', 'a', 'A', 'i', 'I', 'u', 'U', 'R', 'RR', 'lR', 'lRR', 'e', 'ai', 'o', 'au', 'E', 'O', 'aE', 'AE', 'aO', 'aM', 'aH', 'a~', 'oM']
    var vowelsIAST = ['', 'a', 'ā', 'i', 'ī', 'u', 'ū', 'ṛ', 'ṝ', 'ḷ', 'ḹ', 'e', 'ai', 'o', 'au', 'ĕ', 'ŏ', 'æ', 'ǣ', 'ô', 'aṃ', 'aḥ', 'am̐', 'oṃ']

    vowels.forEach(function (vowel, index) {
      this.letteroptionsV.push({label: vowelsIAST[index], value: vowelsIAST[index]})
    }.bind(this))

    this.cons.forEach(function (con, index) {
      this.letteroptionsC.push({label: this.consIAST[index], value: this.consIAST[index]})
    }.bind(this))

    this.consSemitic.forEach(function (con, index) {
      this.letteroptionsCSemitic.push({label: this.consSemitic[index], value: this.consSemitic[index]})
    }.bind(this))

    //  Update this with each script
    this.chars1 = {'Ahom': '𑜒', 'Ariyaka': 'a', 'Assamese': 'অ', 'Avestan': '𐬀', 'Balinese': 'ᬅ', 'BatakKaro': 'ᯀ', 'BatakManda': 'ᯀ', 'BatakPakpak': 'ᯀ', 'BatakSima': 'ᯁ', 'BatakToba': 'ᯀ', 'Bengali': 'অ', 'Bhaiksuki': '𑰀', 'Brahmi': '𑀅', 'Buginese': 'ᨕ', 'Buhid': 'ᝀ', 'Burmese': 'အ', 'Chakma': '𑄃𑄧', 'Cham': 'ꨀ', 'Devanagari': 'अ', 'Dogra': '𑠀', 'Grantha': '𑌅', 'GranthaPandya': 'അ', 'Gujarati': 'અ', 'GunjalaGondi': '𑵠', 'Gurmukhi': 'ਅ', 'HanifiRohingya': '𐴀𐴝', 'Hanunoo': 'ᜠ', 'Javanese': 'ꦄ', 'Kaithi': '𑂃', 'Kannada': 'ಅ', 'KhamtiShan': 'ဢ', 'Kharoshthi': '𐨀', 'Khmer': 'អ', 'Khojki': '𑈀', 'KhomThai': 'อ', 'Khudawadi': '𑊰', 'KhuenTham': 'ᩋ', 'Lao': 'ອະ', 'LaoPali': 'ອ', 'LaoTham': 'ᩋ', 'Lepcha': 'ᰣ', 'Limbu': 'ᤀ', 'LueTham': 'ᩋ', 'Mahajani': '𑅐', 'Malayalam': 'അ', 'Marchen': '𑲏', 'MasaramGondi': '𑴀', 'MeeteiMayek': 'ꯑ', 'Modi': '𑘀', 'Mon': 'အ', 'Mongolian': 'ᠠ᠋', 'Mro': '𖩒', 'Multani': '𑊀', 'Newa': '𑐀', 'OldPersian': '𐎠', 'Oriya': 'ଅ', 'PhagsPa': 'ꡝ', 'Ranjana': 'अ', 'Rejang': 'ꥆ', 'Santali': 'ᱚ', 'Saurashtra': 'ꢂ', 'Shan': 'ဢ', 'Sharada': '𑆃', 'Siddham': '𑖀', 'Sinhala': 'අ', 'SoraSompeng': '𑃦𑃨', 'Soyombo': '𑩐', 'Sundanese': 'ᮃ', 'SylotiNagri': 'ꠅ', 'Tagalog': 'ᜀ', 'Tagbanwa': 'ᝠ', 'TaiLaing': 'အ', 'TaiTham': 'ᩋ', 'Takri': '𑚀', 'Tamil': 'அ', 'TamilBrahmi': '𑀅', 'TamilExtended': 'അ', 'Telugu': 'అ', 'Thaana': 'އަ', 'Thai': 'อ', 'Tibetan': 'ཨ', 'Tirhuta': '𑒁', 'Urdu': 'اَ', 'Vatteluttu': 'அ', 'Wancho': '𞋁', 'WarangCiti': '𑣁', 'ZanabazarSquare': '𑨀', 'Hebrew': 'אַ', 'Hiragana': 'あ', 'Katakana': 'ア', 'Kawi': '𑼄', 'Pallava': 'ꦄ', 'Nandinagari': '𑦠', 'Makasar': '𑻱', 'Arab': 'أَ', 'Armi': '𐡀', 'Elym': '𐿠', 'Ethi': 'አ', 'Hatr': '𐣠', 'Mani': '𐫀', 'Narb': '𐪑', 'Nbat': '𐢁', 'Palm': '𐡠', 'Phli': '𐭠', 'Phlp': '𐮀', 'Phnx': '𐤀', 'Prti': '𐭀', 'Samr': 'ࠀ', 'Sarb': '𐩱', 'Shahmukhi': 'اَ', 'Sogd': '𐼰', 'Sogo': '𐼀', 'Syrc': 'ܐ', 'Ugar': '𐎀', 'Arab-Fa': 'اَ', 'Hebr-Ar': 'א', 'Syre': 'ܐ', 'Syrj': 'ܐܰ', 'Syrn': 'ܐܲ', 'IPA': 'ə', 'RussianCyrillic': 'а', 'DivesAkuru': '𑤀'}

    this.charsIr = {'Ahom': 'a', 'Ariyaka': 'a', 'Assamese': 'a', 'Avestan': 'a', 'Balinese': 'a', 'BatakKaro': 'a', 'BatakManda': 'a', 'BatakPakpak': 'a', 'BatakSima': 'a', 'BatakToba': 'a', 'Bengali': 'a', 'Bhaiksuki': 'a', 'Brahmi': 'a', 'Buginese': 'a', 'Buhid': 'a', 'Burmese': 'a', 'Chakma': 'a', 'Cham': 'a', 'Devanagari': 'a', 'Dogra': 'a', 'Grantha': 'a', 'GranthaPandya': 'a', 'Gujarati': 'a', 'GunjalaGondi': 'a', 'Gurmukhi': 'a', 'HanifiRohingya': 'a', 'Hanunoo': 'a', 'Javanese': 'a', 'Kaithi': 'a', 'Kannada': 'a', 'KhamtiShan': 'a', 'Kharoshthi': 'a', 'Khmer': 'a', 'Khojki': 'a', 'KhomThai': 'a', 'Khudawadi': 'a', 'KhuenTham': 'a', 'Lao': 'a', 'LaoPali': 'a', 'LaoTham': 'a', 'Lepcha': 'a', 'Limbu': 'a', 'LueTham': 'a', 'Mahajani': 'a', 'Malayalam': 'a', 'Marchen': 'a', 'MasaramGondi': 'a', 'MeeteiMayek': 'a', 'Modi': 'a', 'Mon': 'a', 'Mongolian': 'a', 'Mro': 'a', 'Multani': 'a', 'Newa': 'a', 'OldPersian': 'a', 'Oriya': 'a', 'PhagsPa': 'a', 'Ranjana': 'a', 'Rejang': 'a', 'Santali': 'a', 'Saurashtra': 'a', 'Shan': 'a', 'Sharada': 'a', 'Siddham': 'a', 'Sinhala': 'a', 'SoraSompeng': 'a', 'Soyombo': 'a', 'Sundanese': 'a', 'SylotiNagri': 'a', 'Tagalog': 'a', 'Tagbanwa': 'a', 'TaiLaing': 'a', 'TaiTham': 'a', 'Takri': 'a', 'Tamil': 'a', 'TamilBrahmi': 'a', 'TamilExtended': 'a', 'Telugu': 'a', 'Thaana': 'a', 'Thai': 'a', 'Tibetan': 'a', 'Tirhuta': 'a', 'Urdu': 'a', 'Vatteluttu': 'a', 'Wancho': 'a', 'WarangCiti': 'a', 'ZanabazarSquare': 'a', 'Hebrew': 'a', 'Hiragana': 'a', 'Katakana': 'a', 'Kawi': 'a', 'Pallava': 'a', 'Nandinagari': 'a', 'Makasar': 'a', 'Arab': 'a', 'Armi': 'a', 'Elym': 'a', 'Ethi': 'a', 'Hatr': 'a', 'Mani': 'a', 'Narb': 'a', 'Nbat': 'a', 'Palm': 'a', 'Phli': 'a', 'Phlp': 'a', 'Phnx': 'a', 'Prti': 'a', 'Samr': 'a', 'Sarb': 'a', 'Shahmukhi': 'a', 'Sogd': 'a', 'Sogo': 'a', 'Syrc': 'a', 'Ugar': 'a', 'Arab-Fa': 'a', 'Hebr-Ar': 'a', 'Syre': 'a', 'Syrj': 'a', 'Syrn': 'a', 'IPA': 'a', 'RussianCyrillic': 'a', 'DivesAkuru': 'a'}
    // console.log(this.letteroptionsC)
    // console.log(this.letteroptionsV)

    this.scriptsCategorized = {'All': this.scriptsIndic}
    this.displayAll()
  },
  updated: function () {
  },
  watch: {
    tagsActive: function () {
      if (this.activeButton === 'all') {
        this.displayAll()
      } else if (this.activeButton === 'alphabetic') {
        this.alphabetic()
      } else if (this.activeButton === 'derivatic') {
        this.derivatic()
      } else if (this.activeButton === 'linguistic') {
        this.linguistic()
      } else if (this.activeButton === 'current') {
        this.current()
      } else if (this.activeButton === 'geographical') {
        this.geographical()
      }
    },
    typeCategory: function (newV, oldV) {
      // console.log(!this.consSemitic.includes(this.charsC))
      if (newV === 'Semitic' && (this.charsC === '' || !this.consSemitic.includes(this.charsC))) {
        this.charsC = 'ʾ'
      }
      // console.log(this.charsC)
      if (newV === 'Indic' && (this.charsC === '' || !this.cons.includes(this.charsC))) {
        this.charsC = ''
      }
      this.getLetters()
    }
  },
  computed: {
    chars: function () {
      if (this.type === 'explorecard') {
        if (this.typeCategory === 'Indic') {
          return this.charsC + this.charsV
        } else {
          return this.charsC
        }
      } else {
        if (this.$q.platform.is.mobile) {
          return this.mobiledisp
        } else {
          return this.maindisp
        }
      }
    },
    scriptsCategorizedFilter: function () {
      var scripts = {}
      var keys = Object.keys(this.scriptsCategorized)

      var dhis = this

      keys.forEach(function (key) {
        scripts[key] = []

        var scriptsListCategory = dhis.filterScripts(dhis.scriptsCategorized[key], key)

        scriptsListCategory.forEach(function (script) {
          if (dhis.charsIr[script.value].trim() === dhis.chars) {
            script['approx'] = false
            scripts[key].push(script)
          } else {
            if (dhis.showapprox) {
              script['approx'] = true
              scripts[key].push(script)
            } else {
              if (dhis.type === 'explorecardsent') {
                script['approx'] = true
                scripts[key].push(script)
              }
            }
          }
        })
      })

      return scripts
    }
  },
  methods: {
    getIMELink: function (scriptValue) {
      if (scriptValue === 'Hebrew') {
        scriptValue = 'Hebr'
      }
      return '/input/' + scriptValue
    },
    filterScripts: function (scriptsList, key) {
      var dhis = this
      var tagsU = []
      var tagsR = []
      var tagsD = []
      var tagsL = []

      this.tagsActive.forEach(function (tag) {
        if (dhis.tagsUsage.includes(tag)) {
          tagsU.push(tag)
        } else if (dhis.tagsRegion.includes(tag)) {
          tagsR.push(tag)
        } else if (dhis.tagsDerivation.includes(tag)) {
          tagsD.push(tag)
        } else if (dhis.tagsLanguage.includes(tag)) {
          tagsL.push(tag)
        }
      })

      tagsU = _.unique(tagsU.map(tag => scriptsList.filter(script => script.status.includes(tag))).flat())
      tagsR = _.unique(tagsR.map(tag => scriptsList.filter(script => script.region.includes(tag))).flat())
      tagsD = _.unique(tagsD.map(tag => scriptsList.filter(script => script.invented.includes(tag))).flat())
      tagsL = _.unique(tagsL.map(tag => scriptsList.filter(script => script.language.includes(tag))).flat())

      tagsU = tagsU.length === 0 ? scriptsList : tagsU
      tagsR = tagsR.length === 0 ? scriptsList : tagsR
      tagsD = tagsD.length === 0 ? scriptsList : tagsD
      tagsL = tagsL.length === 0 ? scriptsList : tagsL

      var sortedArray = _.intersection(tagsU, tagsR, tagsD, tagsL).sort(function (a, b) {
        if (a.label > b.label) {
          return 1
        }
        if (a.label < b.label) {
          return -1
        }
        return 0
      })

      return sortedArray
    },
    displayAll: function () {
      this.scriptsCategorized = {'All': this.scriptAboutList} // this.scriptsIndic.concat(this.scriptsSemitic)}
      // console.log(this.scriptsCategorized)
      this.activeButton = 'all'
    },
    openlink: function (link) {
      let routeData = this.$router.resolve({path: link})
      window.open(routeData.href, '_self')
    },
    getLetters: async function () {
      this.loading = true

      if (this.chars.length === 0) {
        return
      }

      var preserveSource
      var script2

      if (this.type === 'explorecard') {
        preserveSource = true
        if (this.typeCategory === 'Indic') {
          script2 = 'IAST'
        } else {
          script2 = 'Latn'
        }
      } else {
        preserveSource = this.sourcePreserve
        script2 = this.script2
      }

      // console.log(script2)

      // this.chars2 = await this.convertAsync(this.script2, 'HK', JSON.stringify(this.chars), false, [], [])
      var scriptsV = this.scriptAboutList.map(x => x.value) // this.scriptsIndic.concat(this.scriptsSemitic).map(x => x.value)

      var chars1 = await this.convertLoopTgtAsync(script2, scriptsV, JSON.stringify(this.chars), preserveSource, ['RemoveDiacritics'], [])
      for (var script in chars1) {
        if (script === 'Urdu' || script === 'Thaana') {
          chars1[script] = chars1[script].replace(/،/g, ',')
        }
        this.$set(this.chars1, script, JSON.parse(chars1[script]))
      }
      var charsIr = await this.convertLoopSrcAsync(scriptsV, script2, JSON.stringify(this.chars1), true, [], [])
      for (script in charsIr) {
        this.$set(this.charsIr, script, charsIr[script])
      }

      // console.log(JSON.stringify(this.chars1))
      // console.log(JSON.stringify(this.charsIr))

      this.updatedList = !this.updatedList

      this.loading = false
    }
  }
}

</script>

<style scoped>
.quotetext {
  font-size:75%;
}
.q-body-1 {
  line-height: 1.75em;
  font-color: red;
}
h5 {
  margin-bottom: 10px;
}
.flip-list-move {
  transition: transform 1s;
}
</style>
