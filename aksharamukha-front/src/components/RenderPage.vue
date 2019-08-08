<template>
  <div class="book-content">
    <div class="print-hide">
      <q-page-sticky position="top-right">
        <controls-plug v-model="options" :extra="false"> </controls-plug>
      </q-page-sticky>
    </div>
      <transliterate :text="text" src="Devanagari" :tgt="options.script" :sourcePreserve="options.sourcePreserve" :postOptions="options.postOptions">
      </transliterate>
  </div>
</template>

<style>
</style>

<script>
import Transliterate from '../components/Transliterate'
import ControlsPlug from '../components/ControlsPlug'
import {QPageSticky, QInnerLoading, QSpinnerGears} from 'quasar'

export default {
  props: ['name'],
  components: {
    ControlsPlug,
    QPageSticky,
    Transliterate,
    QInnerLoading,
    QSpinnerGears
  },
  data () {
    return {
      options: {script: 'IAST', sourcePreserve: false},
      text: '',
      loading: true
    }
  },
  created: function () {
    var dhis = this
    this['old'] = Date.now()
    this.$axios.get('../statics/' + this.name + '.html', {})
      .then(function (response) {
        dhis.text = response.data
        dhis.loading = false
      })
      .catch(function (error) {
        console.log(error)
      })
  },
  methods: {
  }
}
</script>
