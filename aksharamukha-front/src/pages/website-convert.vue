<template>
  <q-page>
      <q-alert
          color="grey-7"
          icon="extension"
          appear
          class="q-ma-md"
        > Consider using the following browser extensions for a better experience: <a href="https://chrome.google.com/webstore/detail/aksharamukha-script-conve/nahdihjmpjlifenlocchbokbnpoifpho">Chrome</a> / <a href="https://addons.mozilla.org/en-US/firefox/addon/aksharamukha-script-converter/">Firefox</a></q-alert>
    <q-slide-transition>
      <div class="print-hide" v-show="minimize">
        <controls-io v-model="options" :multiple="false"> </controls-io>
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
        <div class="q-body-1 q-ma-sm">The conversion might affect the formatting of the website</div>
      </div>
    </q-slide-transition>
    <q-btn flat :icon="minimize ? 'call made' : 'call received' " @click="minimize = !minimize" color="dark"/>
    <span v-show="!loading && urlT !== ''">The website is loading. Please wait. If the website doesn't load, click <a :href="urlT">here</a></span>
    <iframe width="99%" class="window-height" style="border:none;" ref="frame" :src="urlT" @load="load" v-if="urlT !== ''"> </iframe>
  </q-page>
</template>

<style scoped>
.url-bar {
}
.rajan {
  font-family: Arial;
}
</style>

<script>
import Transliterate from '../components/Transliterate'
import ControlsIo from '../components/ControlsIo'
import {QPageSticky, QUploader, QField, QInput, QSlideTransition, QAlert} from 'quasar'
import {ScriptMixin} from '../mixins/ScriptMixin'

export default {
  props: ['name'],
  mixins: [ScriptMixin],
  components: {
    ControlsIo,
    QPageSticky,
    Transliterate,
    QUploader,
    QField,
    QAlert,
    QInput,
    QSlideTransition
  },
  data () {
    return {
      options: {},
      url: '',
      urlT: '',
      text: '',
      minimize: true,
      loading: false
    }
  },
  mounted: function () {
    if (typeof this.$route.query.website !== 'undefined' && this.$route.query.src !== 'undefined' && this.$route.query.tgt !== 'undefined') {
      this.url = this.$route.query.website
      var src = this.$route.query.src
      this.options['inputScript'] = src.charAt(0).toUpperCase() + src.slice(1)
      var tgt = this.$route.query.tgt
      this.options['outputScript'] = tgt.charAt(0).toUpperCase() + tgt.slice(1)
      this.options['postOptions'] = []
      this.options['preOptions'] = []
      console.log(this.options)
      this.convertWeb()
    }
  },
  methods: {
    load: function () {
      this.loading = true
      console.log('The webpage is loaded')
    },
    convertWeb: async function () {
      this.urlT = ''
      this.loading = false
      // assigning content
      if (typeof this.options.inputScript === 'undefined' || typeof this.options.outputScript === 'undefined' || this.options.inputScript === '' || this.options.outputScript === '') {
        this.$q.notify({
          message: 'Please select input/ouput scripts before proceeding to conversion',
          position: 'center',
          timeout: 1000
        })
      } else {
        if (this.url.substring(0, 4) !== 'http') {
          this.url = 'http://' + this.url
        }
        this.minimize = false
        this.urlT = 'http://aksharamukha.appspot.com/api/website?url=' + this.url + '&source=' + this.options.inputScript +
          '&target=' + this.options.outputScript + '&preOptions=' + JSON.stringify(this.options.preOptions) +
          '&postOptions=' + JSON.stringify(this.options.postOptions) + '&nativize=' + JSON.stringify(!this.options.sourcePreserve)
        console.log(this.urlT)
        // this.$refs.frame.contentWindow.document.body.innerHTML = await this.getSiteContent(this.url)
      }
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
