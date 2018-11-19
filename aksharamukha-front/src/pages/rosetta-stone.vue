<template>
  <q-page padding>
  <!-- Batak add vowel signs -->
      <h4> Rosetta Stone <q-spinner-comment color="dark" :size="30" v-show="loading"/> </h4>
      <div style="text-align: right">
        <span class="text-red-4"> X</span> : Approximate equivalent <br/>
        <span class="text-blue-4"> Y</span> : Equivalent with diacritic <br/>
      </div>
      Enter a word or a phrase that you want to see in all the other {{scriptsIndic.length}} scripts <br/><br/>
      <div class="row">
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
      <q-field
          label="Text"
          label-width="1"
          class="q-ma-sm col-md-8"
        >
          <q-input v-model="textTemp" />
        </q-field>
        <q-btn class="q-ma-md" color="dark" @click="convert"> Convert </q-btn>
    </div>
    <q-toggle color="dark" v-model="sourcePreserve" label="Preserve source" class="q-ml-sm q-mb-sm q-mt-sm"/>
    <br/>
      <list-text :chars="text" :script2="script2" :script1="'Devanagari'" :sourcePreserve="sourcePreserve" @loaded="loading = false"> </list-text>
  </q-page>
</template>

<style>
</style>

<script>
import Controls from '../components/Controls'
import Learncard from '../components/Learncard'
import ListText from '../components/ListText'
import Transliterate from '../components/Transliterate'
import {ScriptMixin} from '../mixins/ScriptMixin'
import {QPageSticky, QSelect, QField, QInput, QToggle, QSpinnerComment} from 'quasar'

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
    ListText,
    QField,
    QInput,
    QToggle,
    QSpinnerComment
  },
  data () {
    return {
      options: {script: 'Devanagari', sourcePreserve: false},
      dash: _,
      script2: 'HK',
      text: [],
      textTemp: '',
      sourcePreserve: false,
      loading: false
    }
  },
  mounted: function () {
  },
  methods: {
    convert: function () {
      this.loading = true
      this.text = [this.textTemp]
    }
  }
}
</script>
