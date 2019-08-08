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
      <div class="q-ma-md q-body-1" v-if="$q.platform.is.mobile">The page might take several minutes to load completely in a mobile browser and could be unresponsive while doing so. Please have some patience. Alternatively, you can also view the page in a desktop browser.</div>
      <div v-if="letters.length > 0">
        <h5> Vowels</h5>
        <list-char-all :chars="letters[0][i-1]" :script1="script1" :script2="script2"
        :chars2 = "guideChars[0][i-1]" :chars1="selectIndex(results,0,i-1)" :charsIr="selectIndex(resultsHK,0,i-1)"
        v-for="i in letters[0].length" :key="'v1' + i">
        </list-char-all>
        <list-char-all :chars="letters[1][i-1]" :script1="script1" :script2="script2"
        :chars2 = "guideChars[1][i-1]" :chars1="selectIndex(results,1,i-1)" :charsIr="selectIndex(resultsHK,1,i-1)"
        v-for="i in letters[1].length" :key="'v2' + i">
        </list-char-all>
        <list-char-all :chars="letters[2][i-1]" :script1="script1" :script2="script2"
        :chars2 = "guideChars[2][i-1]" :chars1="selectIndex(results,2,i-1)" :charsIr="selectIndex(resultsHK,2,i-1)"
        v-for="i in letters[2].length" :key="'v3' + i">
        </list-char-all>
        <h5> Consonants </h5>
        <list-char-all :chars="letters[3][i-1]" :script1="script1" :script2="script2"
        :chars2 = "guideChars[3][i-1]" :chars1="selectIndex(results,3,i-1)" :charsIr="selectIndex(resultsHK,3,i-1)"
        v-for="i in letters[3].length" :key="'v4' + i">
        </list-char-all>
        <list-char-all :chars="letters[4][i-1]" :script1="script1" :script2="script2"
        :chars2 = "guideChars[4][i-1]" :chars1="selectIndex(results,4,i-1)" :charsIr="selectIndex(resultsHK,4,i-1)"
        v-for="i in letters[4].length" :key="'v5' + i">
        </list-char-all>
        <list-char-all :chars="letters[5][i-1]" :script1="script1" :script2="script2"
        :chars2 = "guideChars[5][i-1]" :chars1="selectIndex(results,5,i-1)" :charsIr="selectIndex(resultsHK,5,i-1)"
        v-for="i in letters[5].length" :key="'v6' + i">
        </list-char-all>
        <list-char-all :chars="letters[6][i-1]" :script1="script1" :script2="script2"
        :chars2 = "guideChars[6][i-1]" :chars1="selectIndex(results,6,i-1)" :charsIr="selectIndex(resultsHK,6,i-1)"
        v-for="i in letters[6].length" :key="'v7' + i">
        </list-char-all>
        <list-char-all :chars="letters[7][i-1]" :script1="script1" :script2="script2"
        :chars2 = "guideChars[7][i-1]" :chars1="selectIndex(results,7,i-1)" :charsIr="selectIndex(resultsHK,7,i-1)"
        v-for="i in letters[7].length" :key="'v8' + i">
        </list-char-all>
        <h5> CV Syllables with KA</h5>
        <list-char-all :chars="letters[8][i-1]" :script1="script1" :script2="script2"
        :chars2 = "guideChars[8][i-1]" :chars1="selectIndex(results,8,i-1)" :charsIr="selectIndex(resultsHK,8,i-1)"
        v-for="i in letters[8].length" :key="'v9' + i">
        </list-char-all>
        <list-char-all :chars="letters[9][i-1]" :script1="script1" :script2="script2"
        :chars2 = "guideChars[9][i-1]" :chars1="selectIndex(results,9,i-1)" :charsIr="selectIndex(resultsHK,9,i-1)"
        v-for="i in letters[9].length" :key="'v10' + i">
        </list-char-all>
        <list-char-all :chars="letters[10][i-1]" :script1="script1" :script2="script2"
        :chars2 = "guideChars[10][i-1]" :chars1="selectIndex(results,10,i-1)" :charsIr="selectIndex(resultsHK,10,i-1)"
        v-for="i in letters[10].length" :key="'v11' + i">
        </list-char-all>
        <h5> Others </h5>
        <list-char-all :chars="letters[11][i-1]" :script1="script1" :script2="script2"
        :chars2 = "guideChars[11][i-1]" :chars1="selectIndex(results,11,i-1)" :charsIr="selectIndex(resultsHK,11,i-1)"
        v-for="i in letters[11].length" :key="'v12' + i">
        </list-char-all>
      </div>
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
import {ScriptMixin} from '../mixins/ScriptMixin'
import {QPageSticky, QSelect, QSpinnerComment} from 'quasar'

var _ = require('underscore')

export default {
  name: 'PageIndex',
  mixins: [ScriptMixin],
  components: {
    QPageSticky,
    Transliterate,
    Learncard,
    QSelect,
    QSpinnerComment,
    ListCharAll
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
      guideChars: []
    }
  },
  watch: {
    '$route' (to, from) {
      this.script1 = to.params.script
    }
  },
  mounted: function () {
    this.compoundsGen()
  },
  methods: {
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
