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
        :options="scriptsIndic"
      />
    </q-page-sticky>
      <h4> Romanization Schemes <q-spinner-comment color="dark" :size="30" v-show="loading"/> </h4>
      <div v-if="letters.length > 0">
        <h5> Vowels</h5>
        <list-char-all-latin :chars="letters[0][i-1]" :script1="script1" :script2="script2"
        :chars2 = "guideChars[0][i-1]" :chars1="selectIndex(results,0,i-1)"
        v-for="i in letters[0].length" :key="'v1' + i">
        </list-char-all-latin>
        <list-char-all-latin :chars="letters[1][i-1]" :script1="script1" :script2="script2"
        :chars2 = "guideChars[1][i-1]" :chars1="selectIndex(results,1,i-1)"
        v-for="i in letters[1].length" :key="'v2' + i">
        </list-char-all-latin>
        <list-char-all-latin :chars="letters[2][i-1]" :script1="script1" :script2="script2"
        :chars2 = "guideChars[2][i-1]" :chars1="selectIndex(results,2,i-1)"
        v-for="i in letters[2].length" :key="'v3' + i">
        </list-char-all-latin>
        <h5> Consonants </h5>
        <list-char-all-latin :chars="letters[3][i-1]" :script1="script1" :script2="script2"
        :chars2 = "guideChars[3][i-1]" :chars1="selectIndex(results,3,i-1)"
        v-for="i in letters[3].length" :key="'v4' + i">
        </list-char-all-latin>
        <list-char-all-latin :chars="letters[4][i-1]" :script1="script1" :script2="script2"
        :chars2 = "guideChars[4][i-1]" :chars1="selectIndex(results,4,i-1)"
        v-for="i in letters[4].length" :key="'v5' + i">
        </list-char-all-latin>
        <list-char-all-latin :chars="letters[5][i-1]" :script1="script1" :script2="script2"
        :chars2 = "guideChars[5][i-1]" :chars1="selectIndex(results,5,i-1)"
        v-for="i in letters[5].length" :key="'v6' + i">
        </list-char-all-latin>
        <list-char-all-latin :chars="letters[6][i-1]" :script1="script1" :script2="script2"
        :chars2 = "guideChars[6][i-1]" :chars1="selectIndex(results,6,i-1)"
        v-for="i in letters[6].length" :key="'v7' + i">
        </list-char-all-latin>
        <list-char-all-latin :chars="letters[7][i-1]" :script1="script1" :script2="script2"
        :chars2 = "guideChars[7][i-1]" :chars1="selectIndex(results,7,i-1)"
        v-for="i in letters[7].length" :key="'v8' + i">
        </list-char-all-latin>
      <h5> Others </h5>
        <list-char-all-latin :chars="letters[8][i-1]" :script1="script1" :script2="script2"
        :chars2 = "guideChars[8][i-1]" :chars1="selectIndex(results,8,i-1)"
        v-for="i in letters[8].length" :key="'v9' + i">
        </list-char-all-latin>
    </div>
    <h5> Notes </h5>
      <div class="q-body-1">
      <transliterate text="अइ" src="Devanagari" :tgt="script2"></transliterate> and <transliterate text="अउ" src="Devanagari" :tgt="script2"></transliterate> are converted to a_i and a_u respectively, to avoid confusion with /ai/ and /au/. Similarly, for <transliterate text="कइ" src="Devanagari" :tgt="script2"></transliterate> and  <transliterate text="कउ" src="Devanagari" :tgt="script2"></transliterate>, which become /ka_i/ and /ka_u/.

      </div>
  </q-page>
</template>

<style>
</style>

<script>
import Controls from '../components/Controls'
import Learncard from '../components/Learncard'
import ListCharAllLatin from '../components/ListCharAllLatin'
import Transliterate from '../components/Transliterate'
import {ScriptMixin} from '../mixins/ScriptMixin'
import {QPageSticky, QSelect, QSpinnerComment} from 'quasar'

var _ = require('underscore')

export default {
  name: 'PageIndex',
  mixins: [ScriptMixin],
  components: {
    Controls,
    QPageSticky,
    Transliterate,
    Learncard,
    QSelect,
    QSpinnerComment,
    ListCharAllLatin
  },
  data () {
    return {
      options: {script: 'Devanagari', sourcePreserve: false},
      dash: _,
      text: '',
      chunkSize: this.$q.platform.is.mobile ? 3 : 8,
      chunkCons: this.$q.platform.is.mobile ? 3 : 5,
      script1: 'Kannada',
      script2: 'Devanagari',
      letters: [],
      loading: true,
      vowelMain: ['a', 'A', 'i', 'I', 'u', 'U', 'R', 'RR', 'lR', 'lRR', 'e', 'ai', 'o', 'au'],
      othersV: ['E', 'O', 'aE', 'AE', 'aO'],
      othersAyo: ['aM', 'aH', 'a~'],
      consonants: ['ka', 'kha', 'ga', 'gha', 'Ga', 'ca', 'cha', 'ja', 'jha', 'Ja', 'Ta', 'Tha', 'Da', 'Dha', 'Na',
        'ta', 'tha', 'da', 'dha', 'na', 'pa', 'pha', 'ba', 'bha', 'ma', 'ya', 'ra', 'la', 'va', 'za', 'Sa', 'sa', 'ha'].map(x => x.replace('a', '')),
      othersC1: ['La', 'Za', 'r2a', 'n2a'].map(x => x.replace('a', '')),
      othersC2: ['qa', 'qha', 'g2a', 'z2a', 'r3a', 'r3ha', 'fa', 'Ya'].map(x => x.replace('a', '')),
      othersCS: ['n*ga', 'n*ja', 'n*Da', 'n*da', 'm*ba'].map(x => x.replace('a', '')),
      numerals: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      otherSymbols: ['\'', 'oM', 'K', '.', '..'],
      guideChars: {},
      results: {}
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
      letters.push(this.dash.chunk(this.otherSymbols, this.chunkSize))

      this.letters = letters

      var data = {
        chars: letters,
        scripts: this.scriptsRomanization.map(x => x.value),
        guide: this.script2
      }
      var dhis = this
      this.apiCall.post('/scriptmatrix', data)
        .then(function (response) {
          for (var key in response.data['results']) {
            dhis.results[key] = JSON.parse(response.data['results'][key].replace(/،/g, ',').replace(/""/g, '"\\"'))
          }
          dhis.guideChars = JSON.parse(response.data['guideChars'])
          dhis.loading = false
          console.log(dhis.results)
        })
        .catch(function (error) {
          console.log(error)
        })
    }
  }
}
</script>
