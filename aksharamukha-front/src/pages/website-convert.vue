<template>
  <q-page>
    <q-slide-transition>
      <div class="print-hide" v-show="minimize">
        <controls2 v-model="options" :extra="false"> </controls2>
        <div class="row">
          <q-field
            icon="web asset"
            label="URL"
            label-width="1"
            class="q-ma-sm col-md-8"
          >
            <q-input v-model="url" />
          </q-field>
          <q-btn class="q-ma-md" color="dark" @click="convertWeb"> Convert URL </q-btn>
        </div>
      </div>
    </q-slide-transition>
    <q-btn flat :icon="minimize ? 'call made' : 'call received' " @click="minimize = !minimize" color="dark"/>
    <iframe width="99%" class="window-height" style="border:none;" ref="frame" :src="urlT"> </iframe>
  </q-page>
</template>

<style>
.url-bar {
}
</style>

<script>
import Transliterate from '../components/Transliterate'
import Controls2 from '../components/Controls2'
import {QPageSticky, QUploader, QField, QInput, QSlideTransition} from 'quasar'
import {ScriptMixin} from '../mixins/ScriptMixin'

export default {
  props: ['name'],
  mixins: [ScriptMixin],
  components: {
    Controls2,
    QPageSticky,
    Transliterate,
    QUploader,
    QField,
    QInput,
    QSlideTransition
  },
  data () {
    return {
      options: {},
      url: '',
      urlT: '',
      text: '',
      minimize: true
    }
  },
  methods: {
    convertWeb: async function () {
      // assigning content
      this.minimize = false
      this.urlT = 'http://aksharamukha.appspot.com/api/website?url=' + this.url + '&source=' + this.options.inputScript +
        '&target=' + this.options.outputScript + '&preOptions=' + JSON.stringify(this.options.preOptions) +
        '&postOptions=' + JSON.stringify(this.options.postOptions) + '&nativize=' + JSON.stringify(!this.options.sourcePreserve)
      // this.$refs.frame.contentWindow.document.body.innerHTML = await this.getSiteContent(this.url)
    },
    getSiteContent: function (url, options) {
      return new Promise(resolve => {
        var data = {
          url: this.url,
          source: this.options.inputScript,
          target: this.options.outputScript,
          nativize: !this.options.sourcePreserve,
          postOptions: this.options.postOptions,
          preOptions: this.options.preOptions
        }
        console.log(data)
        this.apiCall.get('/website', data)
          .then(function (response) {
            resolve(response.data)
          })
          .catch(function (error) {
            console.log(error)
          })
      })
    }
  }
}
</script>
