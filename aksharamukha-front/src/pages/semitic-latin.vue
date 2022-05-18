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
        float-label="Guide Script"
        v-model="script2"
        @input="compoundsGen"
        class="q-ma-sm col-md-3"
        :options="scriptSemiticSorted"
      />
    </q-page-sticky>
      <h4> Semitic Romanization Schemes <q-spinner-comment color="dark" :size="30" v-show="loading"/> </h4>
      <div class="q-body-1">Roman (Semitic) is an internal scheme used by Aksharamukha to convert between Semitic and Indic scripts. As such, it has a one-to-one correspondance with the input. The letters with combining ^ directly map to the initial vowels in Indic scripts. Usually, the output is simplified with extraneous diacritics removed for the sake of readability. The extra diacritics can be retained using <i>Preserve Source</i>.</div> <br/>
      <div class="q-body-1">Roman (Semitic Typeable) is a typeable equivalent of Roman (Semitic) and allows users to use the scheme to output semitic characters without using diacritics. </div>
      <div v-if="letters.length > 0">
        <h5> Core Semitic</h5>
        <list-char-all-latin-semitic :chars="letters[0][i-1]" :script1="script1" :script2="script2"
        :chars2 = "guideChars[0][i-1]" :chars1="selectIndex(results,0,i-1)"
        v-for="i in letters[0].length" :key="'v1' + i" :charsrev="charsRev[0][i-1]">
        </list-char-all-latin-semitic>
      <h6> Additional Semitic </h6>
        <list-char-all-latin-semitic :chars="letters[1][i-1]" :script1="script1" :script2="script2"
        :chars2 = "guideChars[1][i-1]" :chars1="selectIndex(results,1,i-1)"
        v-for="i in letters[1].length" :key="'v2' + i" :charsrev="charsRev[1][i-1]">
        </list-char-all-latin-semitic>
      <h6> Diacritics 1</h6>
        <list-char-all-latin-semitic :chars="letters[2][i-1]" :script1="script1" :script2="script2"
        :chars2 = "guideChars[2][i-1]" :chars1="selectIndex(results,2,i-1)"
        v-for="i in letters[2].length" :key="'v3' + i" :charsrev="charsRev[2][i-1]">
        </list-char-all-latin-semitic>
      <h6> Diacritics 2</h6>
        <list-char-all-latin-semitic :chars="letters[3][i-1]" :script1="script1" :script2="script2"
        :chars2 = "guideChars[3][i-1]" :chars1="selectIndex(results,3,i-1)"
        v-for="i in letters[3].length" :key="'v4' + i" :charsrev="charsRev[3][i-1]">
        </list-char-all-latin-semitic>
    </div>
  </q-page>
</template>

<style>
</style>

<script>
import Learncard from '../components/Learncard'
import Transliterate from '../components/Transliterate'
import {ScriptMixin} from '../mixins/ScriptMixin'
import {QPageSticky, QSelect, QSpinnerComment} from 'quasar'
import ListCharAllLatinSemitic from '../components/ListCharAllLatinSemitic.vue'

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
    ListCharAllLatinSemitic
  },
  data () {
    return {
      options: {script: 'Arab', sourcePreserve: false},
      dash: _,
      text: '',
      chunkSize: this.$q.platform.is.mobile ? 3 : 8,
      chunkCons: this.$q.platform.is.mobile ? 3 : 5,
      script1: 'Kannada',
      script2: 'Arab',
      letters: [],
      loading: true,
      charlistCore: 'ʾ, b, g, d, h, w, z, ḥ, ṭ, y, k, l, m, n, s, ʿ, p, ṣ, q, r, š, t'.replace(' ', '').split(','),
      charAdditional: 'ḍ, ḏ, ḫ, ġ, ṯ, ẓ, v, f, č, j, ž, ɖ, ʈ, ʂ, ɭ, ɲ, ɳ, ɽ, p̣, kʰ, gʰ, čʰ, jʰ, ʈʰ, ɖʰ, tʰ, dʰ, pʰ, bʰ, ɽʰ, ʔ, ˀy, ˀw'.replace(' ', '').split(','),
      charInitVowels: 'â, ā̂, î, ī̂, û, ū̂, ê, ē̂, ô, ō̂, âŵ, âŷ, ˀâ, ˀî'.replace(' ', '').split(','),
      charlistVowels: 'la, lā, li, lī, lu, lū, le, lē, lo, lō, l꞉, l̽, lă, lĕ, lŏ, laŷ, laŵ, la̮, lā̮, laⁿ, luⁿ, liⁿ'.replace(' ', '').split(','),
      guideChars: {},
      charsRev: {},
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
      letters.push(this.dash.chunk(this.charlistCore, this.chunkSize))
      letters.push(this.dash.chunk(this.charAdditional, this.chunkSize))
      letters.push(this.dash.chunk(this.charInitVowels, this.chunkSize))
      letters.push(this.dash.chunk(this.charlistVowels, this.chunkSize))

      this.letters = letters

      var data = {
        chars: letters,
        scripts: this.semiticLatinList,
        guide: this.script2
      }
      var dhis = this
      this.apiCall.post('/latinsemiticmatrix', data)
        .then(function (response) {
          for (var key in response.data['results']) {
            console.log(key)
            console.log(response.data['results'][key])
            if (key === 'RomanReadable' || key === 'RomanColloquial') {
              console.log(response.data['results'][key].replace(/،/g, ',').replace(/""/g, '"\\"').replace(/"\\"/g, '""').replace(/\\g/g, 'g').replace(/\\̍/g, '̍').replace('\\\\̎', '̎').replace(/\\̱/g, '̱').replace('"a\\\\"', '"a"').replace('"a\\"', '"a"').replace('"a\\"', '"a","'))
              dhis.results[key] = JSON.parse(response.data['results'][key].replace(/،/g, ',').replace(/""/g, '"\\"').replace(/"\\"/g, '""').replace(/\\g/g, 'g').replace(/\\̍/g, '̍').replace('\\\\̎', '̎').replace('"a\\\\"', '"a"').replace('"a\\"', '"a"').replace('"a\\"', '"a"'))
            } else if (key !== 'Velthuis') {
              if (key !== 'Itrans' && key !== 'SLP1' && key !== 'WX') {
                dhis.results[key] = JSON.parse(response.data['results'][key].replace(/،/g, ',').replace(/""/g, '"\\"').replace(/"\\"/g, '""').replace(/\\g/g, 'g').replace(/\\̍/g, '̍').replace('\\\\̎', '̎').replace(/\\̱/g, '̱').replace(/\\̎/, '̎'))
              } else if (key === 'Itrans' || key === 'SLP1') {
                dhis.results[key] = JSON.parse(response.data['results'][key].replace(/،/g, ',').replace(/""/g, '"\\"').replace(/"\\"/g, '""').replace(/\\g/g, 'g').replace(/\\̍/g, '̍').replace('\\\\̎', '̎').replace(/\\̱/g, '̱').replace(/\\̎/, '̎').replace(/\\\\""/, '\\\\\\""').replace(/\\_/, '\\\\_').replace(/\\m/g, '\\\\m').replace(/a\\'/, 'a\\\\\''))
              } else if (key === 'WX') {
                dhis.results[key] = JSON.parse(response.data['results'][key].replace(/،/g, ',').replace(/""/g, '"\\"').replace(/"\\"/g, '""').replace(/\\g/g, 'g').replace(/\\̍/g, '̍').replace('\\\\̎', '̎').replace(/\\̱/g, '̱').replace(/\\̎/, '̎').replace(/\\\\""/, '\\\\\\""').replace(/\\_/, '\\\\_').replace(/\\m/g, '\\\\m').replace(/a\\'/, 'a\\\\\''))
              }
            } else {
              console.log('here333')
              dhis.results[key] = JSON.parse(response.data['results'][key].replace(/،/g, ',').replace(/""/g, '"\\"').replace(/"\\"/g, '""').replace(/\\g/g, 'g').replace(/\\̍/g, '̍').replace('\\\\̎', '̎').replace(/\\̱/g, '̱').replace(/""/g, '"\\"').replace(/\\"\\"/g, '\\""').replace(/\\_/, '\\\\_').replace(/\\m/g, '\\\\m').replace(/\\\\""/, '\\\\\\""'))
            }
          }
          dhis.guideChars = JSON.parse(response.data['guideChars'].replace(/\\/g, '').replaceAll('،', ','))
          dhis.charsRev = JSON.parse(response.data['resultsHK'].replace(/\\/g, '').replaceAll('،', ','))
          console.log(dhis.charsRev)
          dhis.loading = false
        })
        .catch(function (error) {
          console.log(error)
        })
    }
  }
}
</script>
