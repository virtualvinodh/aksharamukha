<template>
  <q-page padding>
      <h4>Library of Congress Romanization <q-spinner-comment color="dark" :size="30" v-show="loading"/> </h4>
      <div class="q-body-1">The romanization of the supported scripts (as shown below) follow the guidelines of the Library of Congress as much as possible (unless they involve subjective reading of certain sequences and/or require lexical context). </div> <br/>

      <div class="q-body-1">Please not that many LoC romanization schemes are not reversible. Transliterating the source script from an LoC scheme, depending upon the script, may not always give the exact original source text back. </div> <br/>

      <div class="q-body-1">If the LoC romanization of a script is not yet supported, the output text will be rendered using ISO 233 if it's a Semitic script or ISO 15919 if it's an Indic script.</div> <br/>
      <q-table
    :data="scriptsLoC"
    :columns="columns"
    :pagination.sync="pagination"
    row-key="script"
  >

  <q-td slot="body-cell-script" slot-scope="props" :props="props">
    <a :href='"/describeSemitic/" + props.value.desc' v-if='scriptSemiticList.includes(props.value.desc)'>{{ props.value.label }}</a>
    <a href="/describeSemitic/Hebr" v-if='props.value.desc === "Hebrew"'>{{ props.value.label }}</a>
    <a :href='"/describe/" + props.value.desc' v-if='!scriptSemiticList.includes(props.value.desc)'>{{ props.value.label }}</a>
  </q-td>
  <q-td slot="body-cell-locURL" slot-scope="props" :props="props">
    <a :href='props.value'>{{ props.value }}</a>
  </q-td>
  </q-table>
  </q-page>
</template>

<style>
</style>

<script>
import {ScriptMixin} from '../mixins/ScriptMixin'
import {QPageSticky, QSelect, QSpinnerComment, QTable, QTh, QTr, QTd, QTableColumns} from 'quasar'

var _ = require('underscore')

export default {
  name: 'PageIndex',
  mixins: [ScriptMixin],
  components: {
    QPageSticky,
    QSelect,
    QSpinnerComment,
    QTable,
    QTh,
    QTr,
    QTd,
    QTableColumns
  },
  data () {
    return {
      dash: _,
      pagination: {
        sortBy: null, // String, column "name" property value
        descending: false,
        page: 1,
        rowsPerPage: 100 // current rows per page being displayed
      },
      columns: [
        {
          name: 'script',
          required: true,
          label: 'Script',
          align: 'left',
          field: 'script',
          sortable: true
        },
        {
          name: 'supported',
          required: true,
          label: 'Supported',
          align: 'left',
          field: 'supported',
          sortable: true
        },
        {
          name: 'locURL',
          required: true,
          label: 'URL',
          align: 'left',
          field: 'locURL',
          sortable: true
        }
      ],
      scriptsLoC: [
        {
          script: { label: 'Arabic', desc: 'Arab' },
          locURL: 'https://www.loc.gov/catdir/cpso/romanization/arabic.pdf',
          supported: '❌'
        },
        {
          script: { label: 'Assamese', desc: 'Assamese' },
          locURL: 'https://www.loc.gov/catdir/cpso/romanization/assamese.pdf',
          supported: '✔️'
        },
        {
          script: { label: 'Balinese', desc: 'Balinese' },
          locURL: 'https://www.loc.gov/catdir/cpso/romanization/balinese.pdf',
          supported: '✔️'
        },
        {
          script: { label: 'Batak', desc: 'Batak' },
          locURL: 'https://www.loc.gov/catdir/cpso/romanization/batak.pdf',
          supported: '❌'
        },
        {
          script: { label: 'Bengali', desc: 'Bengali' },
          locURL: 'https://www.loc.gov/catdir/cpso/romanization/bengali.pdf',
          supported: '✔️'
        },
        {
          script: { label: 'Burmese', desc: 'Burmese' },
          locURL: 'https://www.loc.gov/catdir/cpso/romanization/burmese.pdf',
          supported: '✔️'
        },
        {
          script: { label: 'Cham', desc: 'Cham' },
          locURL: 'https://www.loc.gov/catdir/cpso/romanization/cham.pdf',
          supported: '❌'
        },
        {
          script: { label: 'Dhivehi', desc: 'Thaana' },
          locURL: 'https://www.loc.gov/catdir/cpso/romanization/divehi.pdf',
          supported: '❌'
        },
        {
          script: { label: 'Gujarati', desc: 'Gujarati' },
          locURL: 'https://www.loc.gov/catdir/cpso/romanization/gujarati.pdf',
          supported: '✔️'
        },
        {
          script: { label: 'Hebrew', desc: 'Hebr' },
          locURL: 'https://www.loc.gov/catdir/cpso/romanization/hebrew.pdf',
          supported: '❌'
        },
        {
          script: { label: 'Hindi', desc: 'Devanagari' },
          locURL: 'https://www.loc.gov/catdir/cpso/romanization/hindi.pdf',
          supported: '✔️'
        },
        {
          script: { label: 'Japanese (Hiragana)', desc: 'Hiragana' },
          locURL: 'https://www.loc.gov/catdir/cpso/romanization/japanese.pdf',
          supported: '❌'
        },
        {
          script: { label: 'Japanese (Katakana)', desc: 'Katakana' },
          locURL: 'https://www.loc.gov/catdir/cpso/romanization/japanese.pdf',
          supported: '❌'
        },
        {
          script: { label: 'Javanese', desc: 'Javanese' },
          locURL: 'https://www.loc.gov/catdir/cpso/romanization/javanese.pdf',
          supported: '✔️'
        },
        {
          script: { label: 'Judeo-Arabic', desc: 'Hebr-Ar' },
          locURL: 'https://www.loc.gov/catdir/cpso/romanization/judeo-arabic.pdf',
          supported: '❌'
        },
        {
          script: { label: 'Kannada', desc: 'Kannada' },
          locURL: 'https://www.loc.gov/catdir/cpso/romanization/kannada.pdf',
          supported: '✔️'
        },
        {
          script: { label: 'Kashmiri', desc: 'Sharada' },
          locURL: 'https://www.loc.gov/catdir/cpso/romanization/kashmiri.pdf',
          supported: '❌'
        },
        {
          script: { label: 'Khmer', desc: 'Khmer' },
          locURL: 'https://www.loc.gov/catdir/cpso/romanization/khmer.pdf',
          supported: '✔️'
        },
        {
          script: { label: 'Lao', desc: 'Lao' },
          locURL: 'https://www.loc.gov/catdir/cpso/romanization/lao.pdf',
          supported: '❌'
        },
        {
          script: { label: 'Lepcha', desc: 'Lepcha' },
          locURL: 'https://www.loc.gov/catdir/cpso/romanization/lepcha.pdf',
          supported: '❌'
        },
        {
          script: { label: 'Limbu', desc: 'Limbu' },
          locURL: 'https://www.loc.gov/catdir/cpso/romanization/limbu.pdf',
          supported: '✔️'
        },
        {
          script: { label: 'Malayalam', desc: 'Malayalam' },
          locURL: 'https://www.loc.gov/catdir/cpso/romanization/malayalam.pdf',
          supported: '✔️'
        },
        {
          script: { label: 'Manipuri (Meitei)', desc: 'MeteiMayek' },
          locURL: 'https://www.loc.gov/catdir/cpso/romanization/manipuri.pdf',
          supported: '❌'
        },
        {
          script: { label: 'Marathi', desc: 'Devanagari' },
          locURL: 'https://www.loc.gov/catdir/cpso/romanization/marathi.pdf',
          supported: '✔️'
        },
        {
          script: { label: 'Mongolian', desc: 'Mongolian' },
          locURL: 'https://www.loc.gov/catdir/cpso/romanization/mongolia.pdf',
          supported: '❌'
        },
        {
          script: { label: 'Oriya', desc: 'Oriya' },
          locURL: 'https://www.loc.gov/catdir/cpso/romanization/oriya.pdf',
          supported: '✔️'
        },
        {
          script: { label: 'Pali', desc: 'Devanagari' },
          locURL: 'https://www.loc.gov/catdir/cpso/romanization/pali.pdf',
          supported: '✔️'
        },
        {
          script: { label: 'Punjabi', desc: 'Gurmukhi' },
          locURL: 'https://www.loc.gov/catdir/cpso/romanization/panjabi.pdf',
          supported: '✔️'
        },
        {
          script: { label: 'Persian', desc: 'Arab-Fa' },
          locURL: 'https://www.loc.gov/catdir/cpso/romanization/persian.pdf',
          supported: '❌'
        },
        {
          script: { label: 'Sanskrit/Prakrit', desc: 'Devanagari' },
          locURL: 'https://www.loc.gov/catdir/cpso/romanization/sanskrit.pdf',
          supported: '✔️'
        },
        {
          script: { label: 'Santali', desc: 'Santali' },
          locURL: 'https://www.loc.gov/catdir/cpso/romanization/santali.pdf',
          supported: '❌'
        },
        {
          script: { label: 'Shan', desc: 'Shan' },
          locURL: 'https://www.loc.gov/catdir/cpso/romanization/shan.pdf',
          supported: '✔️'
        },
        {
          script: { label: 'Sinhalese', desc: 'Sinhala' },
          locURL: 'https://www.loc.gov/catdir/cpso/romanization/sinhales.pdf',
          supported: '✔️'
        },
        {
          script: { label: 'Syriac (Estrengela)', desc: 'Syre' },
          locURL: 'https://www.loc.gov/catdir/cpso/romanization/syriac.pdf',
          supported: '❌'
        },
        {
          script: { label: 'Syriac (Eastern)', desc: 'Syrn' },
          locURL: 'https://www.loc.gov/catdir/cpso/romanization/syriac.pdf',
          supported: '❌'
        },
        {
          script: { label: 'Syriac (Western)', desc: 'Syrj' },
          locURL: 'https://www.loc.gov/catdir/cpso/romanization/syriac.pdf',
          supported: '❌'
        },
        {
          script: { label: 'Tamil', desc: 'Tamil' },
          locURL: 'https://www.loc.gov/catdir/cpso/romanization/tamil.pdf',
          supported: '✔️'
        },
        {
          script: { label: 'Telugu', desc: 'Telugu' },
          locURL: 'https://www.loc.gov/catdir/cpso/romanization/telugu.pdf',
          supported: '✔️'
        },
        {
          script: { label: 'Thai', desc: 'Thai' },
          locURL: 'https://www.loc.gov/catdir/cpso/romanization/thai.pdf',
          supported: '❌'
        },
        {
          script: { label: 'Tibetan', desc: 'Tibetan' },
          locURL: 'https://www.loc.gov/catdir/cpso/romanization/tibetan.pdf',
          supported: '✔️'
        },
        {
          script: { label: 'Urdu', desc: 'Urdu' },
          locURL: 'https://www.loc.gov/catdir/cpso/romanization/urdu.pdf',
          supported: '❌'
        }
      ]
    }
  },
  mounted: function () {
  },
  methods: {
  }
}
</script>
