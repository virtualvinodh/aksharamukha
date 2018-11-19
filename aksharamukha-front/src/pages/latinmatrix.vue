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
        class="q-ma-sm col-md-3"
        :options="scriptsIndic"
      />
    </q-page-sticky>
      <h4> Romanization Schemes </h4>
      <h5> Vowels</h5>
      <list-char-all-latin :chars="vowel" :script1="script1" :script2="script2" v-for="(vowel, index) in dash.chunk(vowelMain, chunkSize)" :key="'v22'+index">
      </list-char-all-latin>
      <list-char-all-latin :chars="vowel" :script1="script1" :script2="script2" v-for="(vowel, index) in dash.chunk(othersV, chunkSize)" :key="'v23'+index">
      </list-char-all-latin>
      <list-char-all-latin :chars="vowel" :script1="script1" :script2="script2" v-for="(vowel, index) in dash.chunk(othersAyo, chunkSize)" :key="'v33'+index">
      </list-char-all-latin>
      <h5> Consonants </h5>
      <list-char-all-latin :chars="vowel" :script1="script1" :script2="script2" v-for="(vowel, index) in dash.chunk(consonants.slice(0,25), chunkCons)" :key="'v44'+index">
      </list-char-all-latin>
      <list-char-all-latin :chars="vowel" :script1="script1" :script2="script2" v-for="(vowel, index) in dash.chunk(consonants.slice(25,35), chunkSize)" :key="'v45'+index">
      </list-char-all-latin>
      <list-char-all-latin :chars="vowel" :script1="script1" :script2="script2" v-for="(vowel, index) in dash.chunk(othersC1, chunkSize)" :key="'v56'+index">
      </list-char-all-latin>
      <list-char-all-latin :chars="vowel" :script1="script1" :script2="script2" v-for="(vowel, index) in dash.chunk(othersC2, chunkSize)" :key="'v68'+index">
      </list-char-all-latin>
      <list-char-all-latin :chars="vowel" :script1="script1" :script2="script2" v-for="(vowel, index) in dash.chunk(othersCS, chunkSize)" :key="'v7'+index">
      </list-char-all-latin>
      <h5> Others </h5>
      <list-char-all-latin :chars="vowel" :script1="script1" :script2="script2" v-for="(vowel, index) in dash.chunk(otherSymbols, chunkSize)" :key="'v78'+index"> </list-char-all-latin>
    <h5> Notes </h5>
      <div class="q-body-1">
      <transliterate text="अइ" src="Devanagari" :tgt="script2"></transliterate> and  <transliterate text="अउ" src="HK" :tgt="script2"></transliterate> are converted to a_i and a_u respectively, to avoid confusion with /ai/ and /au/. Similarly, for <transliterate text="कइ" src="Devanagari" :tgt="script2"></transliterate> and  <transliterate text="कउ" src="HK" :tgt="script2"></transliterate>, which become /ka_i/ and /ka_u/.

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
import {QPageSticky, QSelect} from 'quasar'

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
      vowelMain: ['a', 'A', 'i', 'I', 'u', 'U', 'R', 'RR', 'lR', 'lRR', 'e', 'ai', 'o', 'au'],
      othersV: ['E', 'O', 'aE', 'AE', 'aO'],
      othersAyo: ['aM', 'aH', 'a~'],
      consonants: ['ka', 'kha', 'ga', 'gha', 'Ga', 'ca', 'cha', 'ja', 'jha', 'Ja', 'Ta', 'Tha', 'Da', 'Dha', 'Na',
        'ta', 'tha', 'da', 'dha', 'na', 'pa', 'pha', 'ba', 'bha', 'ma', 'ya', 'ra', 'la', 'va', 'za', 'Sa', 'sa', 'ha'].map(x => x.replace('a', '')),
      othersC1: ['La', 'Za', 'r2a', 'n2a'].map(x => x.replace('a', '')),
      othersC2: ['qa', 'qha', 'g2a', 'z2a', 'r3a', 'r3ha', 'fa', 'Ya'].map(x => x.replace('a', '')),
      othersCS: ['n*ga', 'n*ja', 'n*Da', 'n*da', 'm*ba'].map(x => x.replace('a', '')),
      numerals: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      otherSymbols: ['\'', 'oM', 'K', '.', '..']
    }
  },
  watch: {
    '$route' (to, from) {
      this.script1 = to.params.script
    }
  },
  mounted: function () {
  },
  methods: {
  }
}
</script>
