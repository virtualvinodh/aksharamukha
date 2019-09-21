<template>
  <q-page padding>
    <div class="q-ma-sm">
    <i>Categorize:</i>
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
        Current use
      </q-btn>
      <q-btn class="q-ma-sm" @click="linguistic" :color="activeButton === 'linguistic' ? 'dark' : ''">
        Capability
      </q-btn>
      <q-btn class="q-ma-sm" @click="derivatic" :color="activeButton === 'derivatic' ? 'dark' : ''">
        Derivation
      </q-btn>
    </div>
    <div class="q-ma-sm">
    <i>Filters: </i>
    <q-btn rounded flat dense v-for="tag in tagsAll" :key="tag + 'v'" @click="tagClick(tag)">
    <q-chip :color="tagsActive.includes(tag) ? 'green-3' : 'red-3'" dense tag>
      {{tag}}
    </q-chip>
    </q-btn>
    </div>
      <div class="row">
      <div class="q-mt-xl q-mr-sm col-md-1"><i>Character:</i></div>
      <q-select
        filter
        inset
        autofocus-filter
        filter-placeholder="search"
        placeholder="Letter"
        v-model="charsC"
        float-label="Choose consonant"
        class="q-ma-sm col-md-3"
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
        float-label="Choose vowel"
        class="q-ma-sm col-md-3"
        :options="letteroptionsV"
        @input="getLetters"
      />
    </div>
  <transition-group
   enter-active-class="animated fadeIn"
   leave-active-class="animated fadeOut"
   mode="out-in"
    >
   <div v-for="category in Object.keys(scriptsCategorizedFilter)" :key="category"
     v-if="scriptsCategorizedFilter[category].length > 0">
    <h5> {{category}} ({{scriptsCategorizedFilter[category].length}} scripts) </h5>
      <explorecard :text1="chars1[script.value]" :script1="script.value" @click="clicked(script)"
       v-for="script in scriptsCategorizedFilter[category]" :key="category + script.value">
     </explorecard>
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
      label="More info"
    />

    <q-btn
      class="q-mr-sm"
      color="dark"
      @click="opened = false"
      label="Learn"
    />

    <q-btn
      class="q-mr-sm"
      color="dark"
      @click="opened = false"
      icon='close'
    />

  </div>
    <h5 class="q-mb-lg q-mt-sm">{{scriptcurrent.label}}</h5>
    <div class="q-ma-md"><big><transliterate :text="$q.platform.is.mobile ? 'नमो रत्नत्रयाय' : 'ॐ नमो बुद्धाय । नमः समन्तबुद्धानां ॥'"
      src="Devanagari" :tgt="scriptcurrent.value"> </transliterate></big></div>
    <q-chip class="q-ma-xs" color="dark" v-for="tag in tags"
      :key="tag" tag dense> {{tag}} </q-chip>
    <div class="q-body-1 q-mt-md q-mb-md" v-html="getDescription(scriptcurrent, false)"> </div>
  </q-modal>

  </q-page>
</template>

<script>
import {tree} from 'vued3tree'
import { QSelect, QChip, QBtn, QModal, CloseOverlay, QPageSticky, QField } from 'quasar'
import Explorecard from '../components/Explorecard'
import Transliterate from '../components/Transliterate'
import { ScriptMixin } from '../mixins/ScriptMixin'

export default {
  // name: 'PageName',
  mixins: [ScriptMixin],
  directives: {CloseOverlay},
  components: {
    tree,
    QBtn,
    QChip,
    Explorecard,
    QSelect,
    QModal,
    QPageSticky,
    Transliterate,
    QField
  },
  data () {
    return {
      opened: false,
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
      script2: 'HK',
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
    var vowels = ['a', 'A', 'i', 'I', 'u', 'U', 'R', 'RR', 'lR', 'lRR', 'e', 'ai', 'o', 'au', 'E', 'O', 'aE', 'AE', 'aO', 'aM', 'aH', 'a~', '']
    var vowelsIAST = ['a', 'ā', 'i', 'ī', 'u', 'ū', 'ṛ', 'ṝ', 'ḷ', 'ḹ', 'e', 'ai', 'o', 'au', 'ĕ', 'ŏ', 'æ', 'ǣ', 'ô', 'aṃ', 'aḥ', 'am̐', '']

    var cons = ['', 'ka', 'kha', 'ga', 'gha', 'Ga', 'ca', 'cha', 'ja', 'jha', 'Ja', 'Ta', 'Tha', 'Da', 'Dha', 'Na', 'ta', 'tha', 'da', 'dha', 'na', 'pa', 'pha', 'ba', 'bha', 'ma', 'ya', 'ra', 'la', 'va', 'za', 'Sa', 'sa', 'ha', 'La', 'Za', 'r2a', 'n2a', 'qa', 'qha', 'g2a', 'z2a', 'r3a', 'r3ha', 'fa', 'Ya'].map(x => x.replace('a', ''))

    var consIAST = ['', 'ka', 'kha', 'ga', 'gha', 'ṅa', 'ca', 'cha', 'ja', 'jha', 'ña', 'ṭa', 'ṭha', 'ḍa', 'ḍha', 'ṇa', 'ta', 'tha', 'da', 'dha', 'na', 'pa', 'pha', 'ba', 'bha', 'ma', 'ya', 'ra', 'la', 'va', 'śa', 'ṣa', 'sa', 'ha', 'l̤a', 'ḻa', 'ṟa', 'ṉa', 'qa', 'k͟ha', 'ġa', 'za', 'r̤a', 'r̤ha', 'fa', 'ẏa'].map(x => x.replace('a', ''))

    vowels.forEach(function (vowel, index) {
      this.letteroptionsV.push({label: vowelsIAST[index], value: vowel})
    }.bind(this))

    cons.forEach(function (con, index) {
      this.letteroptionsC.push({label: consIAST[index], value: con})
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
      return this.charsC + this.charsV
    },
    scriptsCategorizedFilter: function () {
      var scripts = {}
      var keys = Object.keys(this.scriptsCategorized)

      var dhis = this

      keys.forEach(function (key) {
        scripts[key] = []

        dhis.scriptsCategorized[key].forEach(function (script) {
          if (dhis.tagsActive.every(elem => dhis.tagsGet(script).indexOf(elem) > -1) &&
            dhis.charsIr[script.value] === dhis.chars) {
            scripts[key].push(script)
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
      if (this.chars.length === 0) {
        return
      }

      this.chars2 = await this.convertAsync(this.script2, 'HK', JSON.stringify(this.chars), true, [], [])
      var scriptsV = this.scriptsIndic.map(x => x.value)
      var chars1 = await this.convertLoopTgtAsync(this.script2, scriptsV, JSON.stringify(this.chars), this.sourcePreserve, [], [])
      for (var script in chars1) {
        if (script === 'Urdu' || script === 'Thaana') {
          chars1[script] = chars1[script].replace(/،/g, ',')
        }
        this.$set(this.chars1, script, JSON.parse(chars1[script]))
      }
      var charsIr = await this.convertLoopSrcAsync(scriptsV, 'HK', JSON.stringify(this.chars1), true, [], [])
      for (script in charsIr) {
        this.$set(this.charsIr, script, charsIr[script])
      }

      this.updatedList = !this.updatedList
    }
  }
}

</script>

<style scoped>
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
