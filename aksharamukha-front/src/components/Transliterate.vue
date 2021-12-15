<template>
  <span :class="getOutputClass(tgt, postOptions, convertText)" v-html="convertText">
  </span>
</template>

<script>
import {QInnerLoading, QSpinnerGears} from 'quasar'
import { ScriptMixin } from '../mixins/ScriptMixin'

export default {
  // name: 'ComponentName',
  mixins: [ScriptMixin],
  components: {
    QInnerLoading,
    QSpinnerGears
  },
  props: ['src', 'tgt', 'text', 'sourcePreserve', 'postOptions', 'preOptions'],
  mounted: function () {
    this.convert()
    // console.log(this.text)
  },
  data () {
    return {
      convertText: '. . .',
      loading: true
    }
  },
  watch: {
    src: function () {
      // this.convertText = '...'
      this.convert()
    },
    tgt: function () {
      // this.convertText = '...'
      this.convert()
    },
    text: function () {
      // this.convertText = '...'
      this.convert()
    },
    sourcePreserve: function () {
      // this.convertText = '...'
      this.convert()
    },
    preOptions: function () {
      // this.convertText = '...'
      this.convert()
    },
    postOptions: function () {
      // this.convertText = '...'
      this.convert()
    }
  },
  methods: {
    convert: function () {
      if (this.text === '' || this.text === '. . .') {
        this.convertText = this.text
        return
      }
      /* if (this.src === this.tgt && this.postOptions.length === 0 && this.preOptions.length === 0) {
        this.convertText = this.text.replace(/\n/g, '<br/>')
        return
      } */
      var text = this.text
      // var text = this.text.replaceAll('<br/>', '\uE001').replaceAll('<br>', '\uE009').replaceAll('<h5>', '\uE002').replaceAll('</h5>', '\uE003').replaceAll('<div>', '\uE004').replaceAll('</div>', '\uE005').replaceAll('<hr/>', '\uE008').replaceAll('<b>', '\uE00A').replaceAll('</b>', '\uE00B')
      var data = {
        source: this.src,
        target: this.tgt,
        text: text,
        nativize: !this.sourcePreserve,
        postOptions: typeof this['postOptions'] !== 'undefined' ? this.postOptions : [],
        preOptions: typeof this['preOptions'] !== 'undefined' ? this.preOptions : []
      }
      var dhis = this
      this.apiCall.post('/convert', data)
        .then(function (response) {
          // console.log(response.data)
          dhis.convertText = response.data
          // dhis.convertText = response.data.replaceAll('\uE001', '<br/>').replaceAll('\uE009', '<br>').replaceAll('\uE002', '<h5>').replaceAll('\uE003', '</h5>').replaceAll('\uE004', '<div>').replaceAll('\uE005', '</div>').replaceAll('\uE008', '<hr/>').replaceAll('\uE00A', '<b>').replaceAll('\uE00B', '</b>')
          dhis.loading = false
          if (typeof dhis.postOptions !== 'undefined' && dhis.postOptions.includes('siddhamap')) {
            dhis.tgt = 'siddhamap'
          }
        })
        .catch(function (error) {
          console.log(error)
        })
    }
  }
}
</script>

<style>
</style>
