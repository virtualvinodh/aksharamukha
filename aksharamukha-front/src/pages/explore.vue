<template>
  <q-page padding>
    <div class="q-ma-sm">
      <q-btn class="q-ma-sm" @click="displayAll" :color="activeButton === 'all' ? 'dark' : ''">
        All
      </q-btn>
      <q-btn class="q-ma-sm" @click="alphabetic" :color="activeButton === 'alphabetic' ? 'dark' : ''">
        Alphabetic
      </q-btn>
      <q-btn class="q-ma-sm" @click="geographical" :color="activeButton === 'geographical' ? 'dark' : ''">
        Region
      </q-btn>
      <q-btn class="q-ma-sm" @click="current" :color="activeButton === 'current' ? 'dark' : ''">
        Usage
      </q-btn>
      <q-btn class="q-ma-sm" @click="linguistic" :color="activeButton === 'linguistic' ? 'dark' : ''">
        Language Capability
      </q-btn>
      <q-btn class="q-ma-sm" @click="derivatic" :color="activeButton === 'derivatic' ? 'dark' : ''">
        Derivation
      </q-btn>
    </div>
    <div class="q-ma-sm">
    <q-collapsible label="<i>Further filters</i>" icon="category" :opened="!$q.platform.is.mobile">
      <q-btn rounded flat dense v-for="tag in tagsAll" :key="tag + 'v'" @click="tagClick(tag)">
        <q-chip :color="tagsActive.includes(tag) ? 'green-3' : 'red-3'" dense tag>
          {{tag}}
        </q-chip>
      </q-btn>
    </q-collapsible>
    </div>
      <div class="row" v-if="type === 'explorecard'">
      <q-select
        filter
        inset
        autofocus-filter
        filter-placeholder="search"
        placeholder="Letter"
        v-model="charsC"
        float-label="Consonant"
        class="q-ma-sm col-md-2"
        :options="letteroptionsC"
        @input="getLetters"
      />
      <q-select
        filter
        inset
        autofocus-filter
        filter-placeholder="search"
        placeholder="Letter"
        v-model="charsV"
        float-label="Vowel"
        class="q-ma-sm col-md-2"
        :options="letteroptionsV"
        @input="getLetters"
      />
    </div>
      <div class="row" v-if="type === 'explorecardsent'">
      <q-select
        filter
        inset
        autofocus-filter
        filter-placeholder="search"
        placeholder="Input Script"
        v-model="script2"
        class="q-ma-sm col-md-2"
        :options="scriptsOutput"
      />
      <q-input
        autofocus-filter
        placeholder="Text"
        v-model="mobiledisp"
        float-label="Text"
        class="q-ma-sm col-md-8"
        v-if="$q.platform.is.mobile"
      />
      <q-input
        autofocus-filter
        placeholder="Text"
        v-model="maindisp"
        float-label="Text"
        class="q-ma-sm col-md-8"
        v-if="!$q.platform.is.mobile"
      />
      <q-btn class="q-ma-md" color="dark" @click="getLetters"> Convert </q-btn>
    </div>
    <q-btn-toggle v-model="type" :options="typeoptions"  toggle-color="dark" class="col-md-2 q-ma-md"
       @input="getLetters"></q-btn-toggle>
    <q-toggle class="q-ma-md col-md-2" v-model="showapprox" label="Show approx. equivalents" v-if="type == 'explorecard'"> </q-toggle>
    <q-toggle class="q-ma-md col-md-2" v-model="highapprox" label="Highlight approx. equivalents" v-if="type == 'explorecardsent'"> </q-toggle>
    <span v-if="type == 'explorecardsent'"><q-toggle color="dark" v-model="sourcePreserve" label="Preserve source" class="q-ml-sm q-mb-sm q-mt-sm" @input="getLetters"/><q-tooltip>Preserve the source as-is and don't change the text to improve readability. May use archaic characters and/or diacritics.</q-tooltip></span>

    <div v-show="loading" class="q-ma-xs"><q-spinner-comment color="dark" :size="30" v-show="loading"/> </div>
      <!-- <div style="text-align: right" class="q-ma-md">
        <span class="text-red-4"> X</span> : Approximate equivalent <br/>
      </div><br/> -->
  <div class="q-body-1 q-mb-md" v-if="$q.platform.is.mobile"> Tap on the text to view more information about the script. </div><br/><br/>
  <transition-group
   enter-active-class="animated fadeIn"
   leave-active-class="animated fadeOut"
   mode="out-in"
    >
   <div v-for="category in Object.keys(scriptsCategorizedFilter)" :key="category"
     v-if="scriptsCategorizedFilter[category].length > 0">
    <q-collapsible opened
    :label="scriptsCategorizedFilter[category].length == 1 ? category + ' (' + scriptsCategorizedFilter[category].length +  ' script)' : category + ' (' + scriptsCategorizedFilter[category].length +  ' scripts)'"
      :header-style="{'font-size': '125%'}" class="q-mb-md">
      <component :text1="chars1[script.value]" :script1="script.value" @click="clicked(script)"
       v-for="script in scriptsCategorizedFilter[category]" :key="category + script.value" :hidetitle="hidetitle"
       :approx="script.approx" :is="type" :text2="charsIr[script.value]" v-if="type == 'explorecard'">
     </component>
      <component :text1="chars1[script.value]" :script1="script.value" @click="clicked(script)"
       v-for="script in scriptsCategorizedFilter[category]" :key="category + script.value" :hidetitle="hidetitle"
       :approx="script.approx" :is="type" :text2="charsIr[script.value]" v-if="type == 'explorecardsent'" :highapprox="highapprox">
     </component>
    </q-collapsible>
   </div>
    </transition-group>

  <q-modal v-model="opened"
     :content-css="!$q.platform.is.mobile ? {maxWidth: '60vw', maxHeight: '50vh', padding: '20px'} : {minWidth: '90vw', minHeight: '90vh', padding: '20px'}">
    <div class="q-mb-md">

    <q-btn
      class="q-mr-sm"
      color="dark"
      @click="openlink('describe/' + scriptcurrent.value)"
      icon='info'
      label="More"
    />

    <!-- <q-btn
      class="q-mr-sm"
      color="dark"
      @click="opened = false"
      label="Learn"
    /> -->

    <q-btn
      class="q-mr-sm"
      color="dark"
      @click="opened = false"
      icon='close'
    />

  </div>
    <h5 class="q-mb-lg q-mt-sm">{{scriptcurrent.label}}</h5>
    <div class="q-ma-md"><span class="quotetext"><big><transliterate :text="$q.platform.is.mobile ? mobiletext : maintext"
      :src="script2" :tgt="scriptcurrent.value"> </transliterate></big></span></div>
    <q-chip class="q-ma-xs" color="dark" v-for="tag in tags"
      :key="tag" tag dense> {{tag}} </q-chip>
    <div class="q-body-1 q-mt-md q-mb-md" v-html="getDescription(scriptcurrent, false)"> </div>
  </q-modal>

  </q-page>
</template>

<script>
import {tree} from 'vued3tree'
import { QSelect, QTooltip, QChip, QBtnToggle, QBtn, QModal, CloseOverlay, QCollapsible, QPageSticky, QField, QToggle, QSpinnerComment, QInput } from 'quasar'
import Explorecard from '../components/Explorecard'
import Explorecardsent from '../components/Explorecardsent'
import Transliterate from '../components/Transliterate'
import { ScriptMixin } from '../mixins/ScriptMixin'

export default {
  // name: 'PageName',
  mixins: [ScriptMixin],
  directives: {CloseOverlay},
  components: {
    tree,
    QBtn,
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
      typeoptions: [
        {label: 'Letter', value: 'explorecard'},
        {label: 'Text', value: 'explorecardsent'}
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
      letteroptionsC: [],
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
        language: ['Sanskrit & Pali'],
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
      status: ['Extinct', 'Minority', 'Majority'],
      derivation: ['Invented', 'Derived: Aramaic', 'Derived: Perso-Arabic', 'Derived: Cuneiform', 'Derived: Brahmi'],
      regions: ['Pan-Indic', 'East Indic', 'West Indic', 'North Indic', 'South Indic', 'South East Asian: Mainland', 'South East Asian: Insular', 'Central Asian', 'East Asian', 'South Asian: Other', 'West Asian'],
      tagsActive: [],
      activeButton: 'all'
    }
  },
  mounted: function () {
    var vowels = ['a', 'A', 'i', 'I', 'u', 'U', 'R', 'RR', 'lR', 'lRR', 'e', 'ai', 'o', 'au', 'E', 'O', 'aE', 'AE', 'aO', 'aM', 'aH', 'a~', 'oM', '']
    var vowelsIAST = ['a', 'ā', 'i', 'ī', 'u', 'ū', 'ṛ', 'ṝ', 'ḷ', 'ḹ', 'e', 'ai', 'o', 'au', 'ĕ', 'ŏ', 'æ', 'ǣ', 'ô', 'aṃ', 'aḥ', 'am̐', 'oṃ', '']

    var cons = ['', 'ka', 'kha', 'ga', 'gha', 'Ga', 'ca', 'cha', 'ja', 'jha', 'Ja', 'Ta', 'Tha', 'Da', 'Dha', 'Na', 'ta', 'tha', 'da', 'dha', 'na', 'pa', 'pha', 'ba', 'bha', 'ma', 'ya', 'ra', 'la', 'va', 'za', 'Sa', 'sa', 'ha', 'La', 'Za', 'r2a', 'n2a', 'qa', 'qha', 'g2a', 'z2a', 'r3a', 'r3ha', 'fa', 'Ya'].map(x => x.replace('a', ''))

    var consIAST = ['', 'ka', 'kha', 'ga', 'gha', 'ṅa', 'ca', 'cha', 'ja', 'jha', 'ña', 'ṭa', 'ṭha', 'ḍa', 'ḍha', 'ṇa', 'ta', 'tha', 'da', 'dha', 'na', 'pa', 'pha', 'ba', 'bha', 'ma', 'ya', 'ra', 'la', 'va', 'śa', 'ṣa', 'sa', 'ha', 'l̤a', 'ḻa', 'ṟa', 'ṉa', 'qa', 'k͟ha', 'ġa', 'za', 'r̤a', 'r̤ha', 'fa', 'ẏa'].map(x => x.replace('a', ''))

    vowels.forEach(function (vowel, index) {
      this.letteroptionsV.push({label: vowelsIAST[index], value: vowelsIAST[index]})
    }.bind(this))

    cons.forEach(function (con, index) {
      this.letteroptionsC.push({label: consIAST[index], value: consIAST[index]})
    }.bind(this))

    this.getLetters()

    console.log(this.letteroptionsC)
    console.log(this.letteroptionsV)

    this.scriptsCategorized = {'All': this.scriptsIndic}
  },
  updated: function () {
  },
  computed: {
    chars: function () {
      if (this.type === 'explorecard') {
        return this.charsC + this.charsV
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

        dhis.scriptsCategorized[key].forEach(function (script) {
          if (dhis.tagsActive.every(elem => dhis.tagsGet(script).indexOf(elem) > -1)) {
            if (dhis.charsIr[script.value] === dhis.chars) {
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
          }
        })
      })

      return scripts
    },
    tagsAll: function () {
      let arr = []
      return arr.concat(this.languages, ['Pali'], this.status, this.derivation, ['Derived: Pallava'], this.regions, ['Indic', 'South East Asian'])
    },
    tags: function () {
      if (this.scriptcurrent !== '') {
        return this.scriptcurrent.language.concat(this.scriptcurrent.invented, this.scriptcurrent.status, this.scriptcurrent.region)
      } else {
        return []
      }
    },
    regionalScripts: function () {
      var scriptsCategorized = {}

      var dhis = this
      this.regions.forEach(function (region) {
        scriptsCategorized[region] = []
        dhis.scriptsIndic.forEach(function (script) {
          if (script.region.includes(region)) {
            scriptsCategorized[region].push(script)
          }
        })
      })

      return scriptsCategorized
    },
    linguisticScripts: function () {
      var scriptsCategorized = {}

      var dhis = this
      this.languages.forEach(function (language) {
        scriptsCategorized[language] = []
        dhis.scriptsIndic.forEach(function (script) {
          if (script.language.includes(language)) {
            scriptsCategorized[language].push(script)
          }
        })
      })

      return scriptsCategorized
    },
    alphabeticScripts: function () {
      var scriptsCategorized = {}

      var dhis = this
      this.alphabet.forEach(function (letter) {
        scriptsCategorized[letter] = []
        dhis.scriptsIndic.forEach(function (script) {
          if (script.label[0] === letter) {
            scriptsCategorized[letter].push(script)
          }
        })
      })
      return scriptsCategorized
    },
    statusScripts: function () {
      var scriptsCategorized = {}

      var dhis = this
      this.status.forEach(function (state) {
        scriptsCategorized[state] = []
        dhis.scriptsIndic.forEach(function (script) {
          if (script.status.includes(state)) {
            scriptsCategorized[state].push(script)
          }
        })
      })
      return scriptsCategorized
    },
    derivedScripts: function () {
      var scriptsCategorized = {}

      var dhis = this
      this.derivation.forEach(function (state) {
        scriptsCategorized[state] = []
        dhis.scriptsIndic.forEach(function (script) {
          if (script.invented.includes(state)) {
            scriptsCategorized[state].push(script)
          }
        })
      })
      return scriptsCategorized
    }
  },
  methods: {
    alphabetic: function () {
      this.scriptsCategorized = this.alphabeticScripts
      this.activeButton = 'alphabetic'
    },
    derivatic: function () {
      this.scriptsCategorized = this.derivedScripts
      this.activeButton = 'derivatic'
    },
    linguistic: function () {
      this.scriptsCategorized = this.linguisticScripts
      this.activeButton = 'linguistic'
    },
    current: function () {
      this.scriptsCategorized = this.statusScripts
      this.activeButton = 'current'
    },
    geographical: function () {
      this.scriptsCategorized = this.regionalScripts
      this.activeButton = 'geographical'
    },
    displayAll: function () {
      this.scriptsCategorized = {'All': this.scriptsIndic}
      this.activeButton = 'all'
    },
    tagsGet: function (script) {
      if (script !== '') {
        return script.language.concat(script.invented, script.status, script.region)
      } else {
        return []
      }
    },
    tagClick: function (tag) {
      if (!this.tagsActive.includes(tag)) {
        this.tagsActive.push(tag)
      } else {
        this.tagsActive = this.tagsActive.filter(function (value, index, arr) { return value !== tag })
      }

      console.log(this.tagsActive)
    },
    openlink: function (link) {
      let routeData = this.$router.resolve({path: link})
      window.open(routeData.href, '_blank')
    },
    clicked: function (script) {
      this.opened = true
      this.scriptcurrent = script
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
        script2 = 'IAST'
      } else {
        preserveSource = this.sourcePreserve
        script2 = this.script2
      }

      // this.chars2 = await this.convertAsync(this.script2, 'HK', JSON.stringify(this.chars), false, [], [])
      var scriptsV = this.scriptsIndic.map(x => x.value)

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
