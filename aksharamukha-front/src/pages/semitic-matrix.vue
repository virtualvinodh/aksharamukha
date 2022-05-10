<template>
  <q-page padding>
      <q-page-sticky position="top-right">
      <q-select
        filter
        inset
        autofocus-filter
        filter-placeholder="search"
        placeholder="Input Script"
        float-label="Guide Script"
        v-model="script2"
        class="q-ma-sm col-md-3"
        :options="scriptsOutput"
      />
    </q-page-sticky>
<h4> Semitic Matrix <q-spinner-comment color="dark" :size="30" v-show="loading"/></h4>
      <div style="text-align: right">
      <span class="text-red-2"> X</span> : Approximate equivalent <br/>
      <span class="text-blue-4"> Y</span> : Equivalent with diacritic <br/>
      </div>
<div class="q-mt-lg q-mb-xl">
        <div class="q-ml-md q-ma-sm q-mb-md"><i>Script count</i>: {{scriptsManual.length}}</div>

 <q-btn class="q-ma-sm" @click="allScripts" dense>
        <small>Select All</small>
      </q-btn> <q-btn class="q-ma-sm" @click="noScripts" dense>
        <small>Select None</small>
      </q-btn><br/><br/>
        <q-btn rounded flat dense v-for="script in scriptSemiticSortedHebr" :key="script.value + 'v'" @click="scriptTagClick(script.value)">
        <q-chip :color="scriptsManual.includes(script.value) ? 'green-3' : 'red-3'" dense tag>
          <small> {{script.label}} </small>
        </q-chip>
      </q-btn>
</div>
  <q-tabs color="tertiary" inverted two-lines position="top">
    <!-- Tabs - notice slot="title" -->

      <q-tab default slot="title" name="tab-1" label="Core" class="print-hide"/>
      <q-tab slot="title" name="tab-2" label="Additional" class="print-hide"/>
      <q-tab slot="title" name="tab-3" label="Init. Vowels" class="print-hide"/>
      <q-tab slot="title" name="tab-4" label="Vowel Signs" class="print-hide"/>
  <q-tab-pane name="tab-1" keep-alive>
            <list-char-all-semitic :chars="results['core']['Latn']" :script1="script2" script2="Roman (Semitic)"
            :chars2 = "results['core']['Latn']" :chars1="results['core']" :charsIr="results['core']"
            :from="(i-1)*chunkSize"
            :to="i == parseInt(results['core']['Latn'].length/chunkSize) + 1 ? results['core']['Latn'].length : i*chunkSize - 1"
            :filterscripts="scriptsManual"
            v-for="i in parseInt(results['core']['Latn'].length/chunkSize)+1" :key="i"
            >
            </list-char-all-semitic>
  </q-tab-pane>
  <q-tab-pane name="tab-2" keep-alive>
            <list-char-all-semitic :chars="results['adds']['Latn']" :script1="script2" script2="Roman (Semitic)"
            :chars2 = "results['adds']['Latn']" :chars1="results['adds']" :charsIr="results['adds']"
            :from="(i-1)*chunkSize"
            :to="i == parseInt(results['adds']['Latn'].length/chunkSize) + 1 ? results['adds']['Latn'].length : i*chunkSize - 1"
            :filterscripts="scriptsManual"
            v-for="i in parseInt(results['adds']['Latn'].length/chunkSize)+1" :key="i"
            :hidegen="true"
            >
            </list-char-all-semitic>
  </q-tab-pane>
 <q-tab-pane name="tab-3" keep-alive>
            <list-char-all-semitic :chars="results['initvows']['Latn']" :script1="script2" script2="Roman (Semitic)"
            :chars2 = "results['initvows']['Latn']" :chars1="results['initvows']" :charsIr="results['initvows']"
            :from="(i-1)*chunkSize"
            :to="i == parseInt(results['initvows']['Latn'].length/chunkSize) + 1 ? results['initvows']['Latn'].length : i*chunkSize - 1"
            :filterscripts="scriptsManual"
            v-for="i in parseInt(results['initvows']['Latn'].length/chunkSize)+1" :key="i"
            :hidegen="true"
            >
            </list-char-all-semitic>
  </q-tab-pane>
   <q-tab-pane name="tab-4" keep-alive>
            <list-char-all-semitic :chars="results['vows']['Latn']" :script1="script2" script2="Roman (Semitic)"
            :chars2 = "results['vows']['Latn']" :chars1="results['vows']" :charsIr="results['vows']"
            :from="(i-1)*chunkSize"
            :to="i == parseInt(results['vows']['Latn'].length/chunkSize) + 1 ? results['vows']['Latn'].length : i*chunkSize - 1"
            :filterscripts="scriptsManual"
            v-for="i in parseInt(results['vows']['Latn'].length/chunkSize)+1" :key="i"
            :hidegen="true"
            >
            </list-char-all-semitic>
  </q-tab-pane>
  </q-tabs>
<div class="q-body-1">Look into script pages for specific notes. General comments regarding the mapping are listed here. <br/><br/>
The mapping has been done on a purely etymological/historical basis. Though most Semitic scripts have retained the core 22 consonants of the original Phoenician alphabet, the actual pronunciation of the letters have diverged over time (or have been adapted to suit the phonetics of the adapted langauge). For instance, the Arabic equivalent of Phoenician Gimel is ج. However, the instead of the original /g/, it now represents /j/ in many Arabic dialects. Similarly, the Phoenician Ṣādē corresponds to the Hebrew Tzade /צ/ representing /ts/ in Modern Hebrew. This must be kept in mind during transliteraion. When a letter is absent from a particular script, the closest letter is used instead.
      <br/><br/>
If an Indic script includes a Nukta in its reportoire, this has been employed to create the equivalent of the Semitic letters missing from the script.
</div>
  </q-page>
</template>

<style scoped>
h4 {
  margin-top: -20px;
}
</style>

<script>
import Learncard from '../components/Learncard'
import ListCharAllSemitic from '../components/ListCharAllSemitic'
import Transliterate from '../components/Transliterate'
import Syllabary from '../components/Syllabary'
import Conjuncts from '../components/Conjuncts'

import {ScriptMixin} from '../mixins/ScriptMixin'
import {QPageSticky, QSelect, QSpinnerComment, QTabs, QTab, QTabPane, QRouteTab, QChip} from 'quasar'

var _ = require('underscore')

export default {
  name: 'PageIndex',
  mixins: [ScriptMixin],
  components: {
    QPageSticky,
    QChip,
    Syllabary,
    QSpinnerComment,
    Transliterate,
    Learncard,
    QSelect,
    ListCharAllSemitic,
    QTabs,
    QTab,
    QTabPane,
    QRouteTab,
    Conjuncts
  },
  computed: {
    tags: function () {
      let script = this.getScriptObject(this.script1)
      return script.language.concat(script.invented, script.status, script.region)
    }
  },
  data () {
    return {
      options: {script: 'Devanagari', sourcePreserve: false},
      dash: _,
      loading: true,
      chunkSize: this.$q.platform.is.mobile ? 3 : 8,
      chunkCons: this.$q.platform.is.mobile ? 3 : 5,
      script2: 'Devanagari',
      results: {'core': ''},
      scriptsManual: ''
    }
  },
  watch: {
    script1: async function () {
      this.compoundsGen()
    },
    script2: async function () {
      this.compoundsGen()
    }
  },
  mounted: function () {
    this.compoundsGen()
    this.scriptsManual = this.scriptSemiticSortedHebr.map(x => x.value)
  },
  methods: {
    compoundsGen: async function () {
      this.loading = true
      var data = {
        script2: this.script2
      }
      var dhis = this
      this.apiCall.post('/semiticmatrix', data)
        .then(function (response) {
          console.log(response.data)
          dhis.loading = false
          dhis.$set(dhis, 'results', response.data)
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    allScripts: function () {
      this.scriptsManual = this.scriptSemiticSortedHebr.map(x => x.value)
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
      this.key = !this.key
      this.tagsActiveClicked = false
      this.filterProperty = false

      if (!this.scriptsManual.includes(script)) {
        this.scriptsManual.push(script)
      } else {
        this.scriptsManual = this.scriptsManual.filter(function (value, index, arr) { return value !== script })
      }
    }
  }
}
</script>
