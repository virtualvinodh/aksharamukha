<template>
  <q-page padding>
  <!-- Batak add vowel signs -->
      <q-page-sticky position="top-right">
      <q-select
        filter
        inset
        autofocus-filter
        filter-placeholder="search"
        placeholder="Input Script"
        v-model="script2"
        @input="compoundsGen"
        class="q-ma-sm col-md-3"
        :options="scriptsLatin"
      />
    </q-page-sticky>
      <h4> Script Matrix <q-spinner-comment color="dark" :size="30" v-show="loading"/> </h4>
      <div style="text-align: right">
      <span class="text-red-2"> X</span> : Approximate equivalent <br/>
      <span class="text-blue-4"> Y</span> : Equivalent with diacritic <br/>
      </div>
      <div>
      <q-toggle color="dark" v-model="filterProperty" label="Property filter" class="q-ma-md" @input="filterList = false; tagsActive = []"></q-toggle>
      <q-toggle color="dark" v-model="filterList" label="List filter" class="q-ma-md" @input="filterProperty = false;"></q-toggle>
      <div class="q-ml-md q-ma-sm q-mb-md"><i>Script count</i>: {{filterScripts.length}}</div>
      <q-collapsible label="<i>Script Properties</i>" icon="category" :opened="true" v-if="filterProperty">
        <filter-tags v-model="tagsActive" :key="key" @input="tagsActiveClicked = true"></filter-tags>
      </q-collapsible> <br/>
      <q-collapsible :label="'<i>Script List</i>'" icon="category" :opened="true" v-if="filterList">
        <q-btn class="q-ma-sm" @click="allScripts" dense>
        <small>Select All</small>
      </q-btn> <q-btn class="q-ma-sm" @click="noScripts" dense>
        <small>Select None</small>
      </q-btn><br/>
        <q-btn rounded flat dense v-for="script in scriptsIndic" :key="script.value + 'v'" @click="scriptTagClick(script.value)">
        <q-chip :color="filterScripts.includes(script.value) ? 'green-3' : 'red-3'" dense tag>
          <small> {{script.label}} </small>
        </q-chip>
      </q-btn>
      </q-collapsible>
      </div>
      <div class="q-ma-md q-body-1" v-if="$q.platform.is.mobile"><small>The page might take a few minutes to load completely in a mobile browser and could become unresponsive. Please have some patience. </small></div>
      <q-tabs color="tertiary" inverted two-lines position="top">
        <!-- Tabs - notice slot="title" -->
        <q-tab default slot="title" name="tab-1" label="Vow" class="print-hide"/>
        <q-tab slot="title" name="tab-2" label="Cons" class="print-hide"/>
        <q-tab slot="title" name="tab-3" label="Vow.Signs" class="print-hide"/>
        <q-tab slot="title" name="tab-4" label="Others" class="print-hide"/>

      <div v-if="letters.length > 0">
        <q-tab-pane name="tab-1" keep-alive>
          <q-tabs color="tertiary" inverted two-lines position="top">
          <!-- Tabs - notice slot="title" -->
          <q-tab default slot="title" name="tab-11" label="Core" class="print-hide"/>
          <q-tab slot="title" name="tab-12" label="Others" class="print-hide"/>
          <q-tab slot="title" name="tab-13" label="Comb.Signs" class="print-hide"/>

        <q-tab-pane default name="tab-11" keep-alive>

        <list-char-all :chars="letters[0][i-1]" :script1="script1" :script2="script2"
        :chars2 = "guideChars[0][i-1]" :chars1="selectIndex(results,0,i-1)" :charsIr="selectIndex(resultsHK,0,i-1)"
        v-for="i in letters[0].length" :key="'v1' + i" :filterscripts="filterScripts">
        </list-char-all>

        </q-tab-pane>

        <q-tab-pane name="tab-12" keep-alive>

        <list-char-all :chars="letters[1][i-1]" :script1="script1" :script2="script2"
        :chars2 = "guideChars[1][i-1]" :chars1="selectIndex(results,1,i-1)" :charsIr="selectIndex(resultsHK,1,i-1)"
        v-for="i in letters[1].length" :key="'v2' + i" :filterscripts="filterScripts">
        </list-char-all>

        </q-tab-pane>

        <q-tab-pane name="tab-13" keep-alive>

        <list-char-all :chars="letters[2][i-1]" :script1="script1" :script2="script2"
        :chars2 = "guideChars[2][i-1]" :chars1="selectIndex(results,2,i-1)" :charsIr="selectIndex(resultsHK,2,i-1)"
        v-for="i in letters[2].length" :key="'v3' + i" :filterscripts="filterScripts">
        </list-char-all>

      </q-tab-pane>

      </q-tabs>

        </q-tab-pane>

        <q-tab-pane name="tab-2" keep-alive>

          <q-tabs color="tertiary" inverted two-lines position="top">
          <!-- Tabs - notice slot="title" -->
          <q-tab default slot="title" name="tab-21" label="Core 1" class="print-hide"/>
          <q-tab slot="title" name="tab-22" label="Core 2" class="print-hide"/>
          <q-tab slot="title" name="tab-23" label="S.Ind" class="print-hide"/>
          <q-tab slot="title" name="tab-24" label="Nukt." class="print-hide"/>
          <q-tab slot="title" name="tab-25" label="Sinh." class="print-hide"/>

          <q-tab-pane default name="tab-21" keep-alive>
            <list-char-all :chars="letters[3][i-1]" :script1="script1" :script2="script2"
            :chars2 = "guideChars[3][i-1]" :chars1="selectIndex(results,3,i-1)" :charsIr="selectIndex(resultsHK,3,i-1)"
            v-for="i in letters[3].length" :key="'v4' + i" :filterscripts="filterScripts">
            </list-char-all>
          </q-tab-pane>

          <q-tab-pane name="tab-22" keep-alive>
            <list-char-all :chars="letters[4][i-1]" :script1="script1" :script2="script2"
            :chars2 = "guideChars[4][i-1]" :chars1="selectIndex(results,4,i-1)" :charsIr="selectIndex(resultsHK,4,i-1)"
            v-for="i in letters[4].length" :key="'v5' + i" :filterscripts="filterScripts">
            </list-char-all>
          </q-tab-pane>
          <q-tab-pane name="tab-23" keep-alive>
            <list-char-all :chars="letters[5][i-1]" :script1="script1" :script2="script2"
            :chars2 = "guideChars[5][i-1]" :chars1="selectIndex(results,5,i-1)" :charsIr="selectIndex(resultsHK,5,i-1)"
            v-for="i in letters[5].length" :key="'v6' + i" :filterscripts="filterScripts">
            </list-char-all>
          </q-tab-pane>
          <q-tab-pane name="tab-24" keep-alive>
            <list-char-all :chars="letters[6][i-1]" :script1="script1" :script2="script2"
            :chars2 = "guideChars[6][i-1]" :chars1="selectIndex(results,6,i-1)" :charsIr="selectIndex(resultsHK,6,i-1)"
            v-for="i in letters[6].length" :key="'v7' + i" :filterscripts="filterScripts">
            </list-char-all>
          </q-tab-pane>
          <q-tab-pane name="tab-25" keep-alive>
            <list-char-all :chars="letters[7][i-1]" :script1="script1" :script2="script2"
            :chars2 = "guideChars[7][i-1]" :chars1="selectIndex(results,7,i-1)" :charsIr="selectIndex(resultsHK,7,i-1)"
            v-for="i in letters[7].length" :key="'v8' + i" :filterscripts="filterScripts">
            </list-char-all>
          </q-tab-pane>
        </q-tabs>

        </q-tab-pane>

        <q-tab-pane name="tab-3" keep-alive>

          <q-tabs color="tertiary" inverted two-lines position="top">
          <!-- Tabs - notice slot="title" -->
          <q-tab default slot="title" name="tab-31" label="Core" class="print-hide"/>
          <q-tab slot="title" name="tab-32" label="South Indic" class="print-hide"/>
          <q-tab slot="title" name="tab-33" label="Comb.Signs" class="print-hide"/>

        <q-tab-pane name="tab-31" keep-alive>

        <list-char-all :chars="letters[8][i-1]" :script1="script1" :script2="script2"
        :chars2 = "guideChars[8][i-1]" :chars1="selectIndex(results,8,i-1)" :charsIr="selectIndex(resultsHK,8,i-1)"
        v-for="i in letters[8].length" :key="'v9' + i" :filterscripts="filterScripts">
        </list-char-all>

      </q-tab-pane>
        <q-tab-pane name="tab-32" keep-alive>

        <list-char-all :chars="letters[9][i-1]" :script1="script1" :script2="script2"
        :chars2 = "guideChars[9][i-1]" :chars1="selectIndex(results,9,i-1)" :charsIr="selectIndex(resultsHK,9,i-1)"
        v-for="i in letters[9].length" :key="'v10' + i" :filterscripts="filterScripts">
        </list-char-all>

      </q-tab-pane>

              <q-tab-pane name="tab-33" keep-alive>

        <list-char-all :chars="letters[10][i-1]" :script1="script1" :script2="script2"
        :chars2 = "guideChars[10][i-1]" :chars1="selectIndex(results,10,i-1)" :charsIr="selectIndex(resultsHK,10,i-1)"
        v-for="i in letters[10].length" :key="'v11' + i" :filterscripts="filterScripts">
        </list-char-all>

      </q-tab-pane>
    </q-tabs>
        </q-tab-pane>

        <q-tab-pane name="tab-4" keep-alive>
        <list-char-all :chars="letters[11][i-1]" :script1="script1" :script2="script2"
        :chars2 = "guideChars[11][i-1]" :chars1="selectIndex(results,11,i-1)" :charsIr="selectIndex(resultsHK,11,i-1)"
        v-for="i in letters[11].length" :key="'v12' + i" :filterscripts="filterScripts">
        </list-char-all>
        </q-tab-pane>
      </div>
      </q-tabs>
      <h5> Notes </h5>
      <div class="q-body-1">Look into script pages for specific notes. General comments regarding the mapping are listed here. <br/><br/>
      If a script is open-ended like Sharada, Kannada, Grantha, Balinese or many North Indic-scripts (with Nukta and/or other characters that allow natural extensions of the alphabet) to represent non-native characters, they have been utilized to extend the scripts appropriately and create one-to-one equivalent characters to fill in the holes as much as possible. <br/><br/>
      East-Asian scripts have been retrofitted into the Brahmi model of consonants/vowels on a purely etymological/historical basis (particularly if they don't have a tradition of writing Sanskrit/Pali). The modern phonology of characters in many modern East-Asian scripts have significantly deviated from their Brahmic prototypes and many of these scripts have extended or modified the role of some of the characters in unprecedented ways.<br/><br/>
      If a script doesn't have /l̤a/, /ṣa/ with Nukta has been used as the equivalent character for /ḻa/. <br/><br/>
      In Philippine/Indonesian scripts, /e/, /o/ have been mapped to short /e/ and short /o/ based on phonetics. Paleographically, they probably descended from the long /e/ and long /o/ of the Pallava alphabet. <br/><br/>
      In few scripts, the extended vowels /ĕ/, /ŏ/, /æ/, /ǣ/, /ô/ were mapped to the native non-Brahmic vowel extensions of the scripts just to create a one-to-one mapping. They may not be phonetically/etymologically related to those characters. On the same note, /qa/, /k͟ha/, /ġa/, /za/, /r̤a/, /r̤ha/, /fa/, /ẏa/ are also sometimes mapped to non-Brahmic consonants to create one-to-one mapping and may not be related per se. <br/><br/>
      For minority North Indic scripts, signs such as Avagraha are sometimes borrowed from Devanagari.
      </div>
  </q-page>
</template>

<style>
</style>

<script>
import Learncard from '../components/Learncard'
import ListCharAll from '../components/ListCharAll'
import Transliterate from '../components/Transliterate'
import FilterTags from '../components/FilterTags'
import {ScriptMixin} from '../mixins/ScriptMixin'
import {QPageSticky, QToggle, QSelect, QChip, QSpinnerComment, QTabs, QTab, QTabPane, QRouteTab, QCollapsible} from 'quasar'

var _ = require('underscore')

export default {
  name: 'PageIndex',
  mixins: [ScriptMixin],
  components: {
    QPageSticky,
    Transliterate,
    Learncard,
    QSelect,
    FilterTags,
    QSpinnerComment,
    ListCharAll,
    QCollapsible,
    QToggle,
    QTabs,
    QTab,
    QChip,
    QTabPane,
    QRouteTab
  },
  data () {
    return {
      options: {script: 'Devanagari', sourcePreserve: false},
      dash: _,
      loading: true,
      text: '',
      chunkSize: this.$q.platform.is.mobile ? 3 : 8,
      chunkCons: this.$q.platform.is.mobile ? 3 : 5,
      script1: 'Kannada',
      script2: 'IAST',
      vowelMain: ['a', 'A', 'i', 'I', 'u', 'U', 'R', 'RR', 'lR', 'lRR', 'e', 'ai', 'o', 'au'],
      othersV: ['E', 'O', 'aE', 'AE', 'aO'],
      othersAyo: ['aM', 'aH', 'a~'],
      consonants: ['ka', 'kha', 'ga', 'gha', 'Ga', 'ca', 'cha', 'ja', 'jha', 'Ja', 'Ta', 'Tha', 'Da', 'Dha', 'Na',
        'ta', 'tha', 'da', 'dha', 'na', 'pa', 'pha', 'ba', 'bha', 'ma', 'ya', 'ra', 'la', 'va', 'za', 'Sa', 'sa', 'ha'],
      othersC1: ['La', 'Za', 'r2a', 'n2a'],
      othersC2: ['qa', 'qha', 'g2a', 'z2a', 'r3a', 'r3ha', 'fa', 'Ya'],
      othersCS: ['n*ga', 'n*ja', 'n*Da', 'n*da', 'm*ba'],
      numerals: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      otherSymbols: ['\'', 'oM', '.', '..'],
      letters: [],
      results: {},
      resultsHK: {},
      guideChars: [],
      tagsActive: [],
      key: true,
      scriptsManual: [],
      tagsActiveClicked: false,
      filterProperty: false,
      filterList: false
    }
  },
  watch: {
    '$route' (to, from) {
      this.script1 = to.params.script
    },
    tagsActive () {
      this.tagsActiveClicked = true
    }

  },
  mounted: function () {
    this.tagsActiveClicked = true
    this.compoundsGen()
  },
  computed: {
    filterScripts: function () {
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

      tagsU = _.unique(tagsU.map(tag => this.scriptsIndic.filter(script => script.status.includes(tag)).map(x => x.value)).flat())
      tagsR = _.unique(tagsR.map(tag => this.scriptsIndic.filter(script => script.region.includes(tag)).map(x => x.value)).flat())
      tagsD = _.unique(tagsD.map(tag => this.scriptsIndic.filter(script => script.invented.includes(tag)).map(x => x.value)).flat())
      tagsL = _.unique(tagsL.map(tag => this.scriptsIndic.filter(script => script.language.includes(tag)).map(x => x.value)).flat())

      tagsU = tagsU.length === 0 ? this.scriptsIndic.map(x => x.value) : tagsU
      tagsR = tagsR.length === 0 ? this.scriptsIndic.map(x => x.value) : tagsR
      tagsD = tagsD.length === 0 ? this.scriptsIndic.map(x => x.value) : tagsD
      tagsL = tagsL.length === 0 ? this.scriptsIndic.map(x => x.value) : tagsL

      if (this.tagsActiveClicked) {
        return _.intersection(tagsU, tagsR, tagsD, tagsL)
      } else {
        return this.scriptsManual
      }
    }
  },
  methods: {
    allScripts: function () {
      this.scriptsManual = this.scriptsIndic.map(x => x.value)
      this.tagsActiveClicked = false
      this.filterProperty = false
    },
    noScripts: function () {
      this.key = !this.key
      this.scriptsManual = []
      this.tagsActiveClicked = false
      this.filterProperty = false
    },
    scriptTagClick: function (script) {
      this.scriptsManual = Array.from(this.filterScripts)
      this.key = !this.key
      this.tagsActiveClicked = false
      this.filterProperty = false

      if (!this.scriptsManual.includes(script)) {
        this.scriptsManual.push(script)
      } else {
        this.scriptsManual = this.scriptsManual.filter(function (value, index, arr) { return value !== script })
      }
    },
    selectIndex: function (dictio, index1, index2) {
      var dic = {}
      for (var key in dictio) {
        dic[key] = dictio[key][index1][index2]
      }
      return dic
    },
    compoundsGen: function () {
      var letters = []
      this.loading = true
      letters.push(this.dash.chunk(this.vowelMain, this.chunkSize))
      letters.push(this.dash.chunk(this.othersV, this.chunkSize))
      letters.push(this.dash.chunk(this.othersAyo, this.chunkSize))
      letters.push(this.dash.chunk(this.consonants.slice(0, 25), this.chunkCons))
      letters.push(this.dash.chunk(this.consonants.slice(25, 35), this.chunkSize))
      letters.push(this.dash.chunk(this.othersC1, this.chunkSize))
      letters.push(this.dash.chunk(this.othersC2, this.chunkSize))
      letters.push(this.dash.chunk(this.othersCS, this.chunkSize))
      letters.push(this.dash.chunk(this.vowelMain.map(x => 'k' + x), this.chunkSize))
      letters.push(this.dash.chunk(this.othersV.map(x => 'k' + x), this.chunkSize))
      var othersAyo2 = this.othersAyo
      othersAyo2.push('')
      letters.push(this.dash.chunk(othersAyo2.map(x => 'k' + x), this.chunkSize))
      letters.push(this.dash.chunk(this.otherSymbols, this.chunkSize))

      this.letters = letters

      // console.log(JSON.stringify(letters))
      // console.log(JSON.stringify(this.scriptsIndic.map(x => x.value)))

      /*
      var data = {
        chars: letters,
        scripts: this.scriptsIndic.map(x => x.value),
        guide: this.script2
      } */

      var data = {
        // Number of characters per row
        charnums: typeof this.$q.platform.is.mobile === 'undefined' ? '5' : '3',
        guide: this.script2
      }

      var dhis = this
      this.apiCall.post('/scriptmatrix', data)
        .then(function (response) {
          for (var key in response.data['results']) {
            dhis.results[key] = response.data['results'][key]
            dhis.resultsHK[key] = response.data['resultsHK'][key]
          }
          dhis.guideChars = response.data['guideChars']
          dhis.loading = false
        })
        .catch(function (error) {
          console.log(error)
        })
    }
  }
}
</script>
