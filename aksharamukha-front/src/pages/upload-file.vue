<template>
  <q-page padding>
    <div class="print-hide">
      <controls-io v-model="optionsRet" :extra="false"> </controls-io>
    </div>
    <q-field
        icon="attachment"
        label="File"
        label-width="1"
        class="q-ma-md col-md-5"
      >
        <q-uploader url=""  hide-upload-button clearable extensions=".txt, .html, .htm, .xml"
           stack-label="You can add multiple files. Only .txt, .xml and .html extensions are allowed" auto-expand hide-upload-progress multiple ref="uploadF"/>
    </q-field>
    <q-btn class="q-ma-md" color="dark" @click="convertDownload"> Convert & Download </q-btn>
    <q-btn class="q-ma-md" color="dark" @click="convertView"> Convert & View </q-btn>
    <q-btn class="q-ma-md" color="dark" @click="clear"> Clear </q-btn> <br/>
    <i v-show="downloadWarning"> Your browser may try to block the downloads. In that case, please unblock and try again </i>
    <q-spinner-comment color="dark" :size="30" v-show="loading"/>
    <div v-for="(file, index) in files" :key="'file'+index" v-if="showContent">
      <b> {{file.name}} </b> <br/><br/>
      <transliterate :text="sanitize(file.content)" :src="options.inputScript" :tgt="options.outputScript" :preserveSource="options.sourcePreserve" :postOptions="options.postOptions" :preOptions="options.preOptions"> </transliterate>
      <br/><br/>
    </div>
  </q-page>
</template>

<style scoped>
.vinodh {
  font-family: Ariel;
}
</style>

<script>
import Transliterate from '../components/Transliterate'
import ControlsIo from '../components/ControlsIo'
import {QPageSticky, QUploader, QField, QSpinnerComment} from 'quasar'
import { ScriptMixin } from '../mixins/ScriptMixin'
import sanitizeHtml from 'sanitize-html'

export default {
  props: ['name'],
  mixins: [ScriptMixin],
  components: {
    ControlsIo,
    QPageSticky,
    Transliterate,
    QUploader,
    QSpinnerComment,
    QField
  },
  data () {
    return {
      options: {},
      optionsRet: {},
      files: [],
      showContent: false,
      loading: false,
      downloadWarning: false
    }
  },
  methods: {
    sanitize: function (html) {
      return sanitizeHtml(html)
    },
    convertView: async function () {
      this.readFiles()
      this.downloadWarning = false
      this.options = this.optionsRet
      this.showContent = true
    },
    readFiles: async function () {
      this.files = []
      for (var i = 0; i < this.$refs.uploadF.queue.length; i++) {
        var file = this.$refs.uploadF.queue[i]
        var text = await this.readFileText(file)
        this.files.push({name: file.name, content: text})
      }
    },
    readFileText: function (url) {
      return new Promise(resolve => {
        var reader = new FileReader()
        reader.onload = function () {
          resolve(reader.result)
        }
        reader.readAsText(url)
      })
    },
    convertDownload: async function () {
      this.loading = true
      this.downloadWarning = true
      this.showContent = false
      this.options = this.optionsRet
      console.log(this.options)
      await this.readFiles()
      console.log(this.files)
      for (var i = 0; i < this.files.length; i++) {
        var file = this.files[i]
        var data = {
          source: this.options.inputScript,
          target: this.options.outputScript,
          text: file.content,
          nativize: !this.options.sourcePreserve,
          postOptions: this.options.postOptions,
          preOptions: this.options.preOptions
        }
        console.log(data)
        var dhis = this
        this.apiCall.post('/convert', data)
          .then(function (response) {
            dhis.loading = false

            var content = response.data
            content = content.replace(new RegExp('<br/>', 'g'), '\n')
            // content = content.replace(new RegExp('e-Grantamil 7', 'g'), 'Noto Sans Tamil')
            // content = content.replace(new RegExp('e-Grantamil', 'g'), 'Noto Sans Tamil')

            var blob = ''
            const e = document.createEvent('MouseEvents')
            const a = document.createElement('a')
            a.download = dhis.options.inputScript + '_' + dhis.options.outputScript + '_' + file.name
            if (file.name.includes('.txt')) {
              blob = new Blob([content], {type: 'text/plain'})
              a.dataset.downloadurl = ['text/plain', a.download, a.href].join(':')
            } else if (file.name.includes('.xml')) {
              blob = new Blob([content], {type: 'text/xml'})
              a.dataset.downloadurl = ['text/plain', a.download, a.href].join(':')
            } else {
              blob = new Blob([content], {type: 'plain/html'})
              a.dataset.downloadurl = ['text/html', a.download, a.href].join(':')
            }
            a.href = window.URL.createObjectURL(blob)
            e.initEvent('click', true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null)
            a.dispatchEvent(e)
          })
          .catch(function (error) {
            console.log(error)
          })
      }
    },
    convert: function () {
    },
    clear: function () {
      this.files = []
    }
  }
}
</script>
