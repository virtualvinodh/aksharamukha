<template>
  <q-page class="q-pa-md" >
    <converter-menu highlight="files"></converter-menu>
    <div class="print-hide">
      <controls-io v-model="optionsRet" :extra="false" :multiple="true"> </controls-io>
    </div>
    <q-field
        icon="attachment"
        label="File"
        label-width="1"
        class="q-ma-md col-md-5"
      >
        <q-uploader url=""  hide-upload-button clearable extensions=".txt, .html, .htm, .xml, .json, .itx, .docx, .brh"
           stack-label="+ icon to add. You can add multiple files. <br/> .txt, .xml, .html, .itx, .docx, .json, .brh" auto-expand hide-upload-progress multiple ref="uploadF" :style="{width:'272px'}"/>
    </q-field>
    <q-btn class="q-ma-md" color="dark" @click="convertDownload"> Convert & Download </q-btn>
    <q-btn class="q-ma-md" color="dark" @click="convertView"> Convert & View </q-btn>
    <q-btn class="q-ma-md" color="dark" @click="clear"> Clear Files </q-btn> <br/>
    <div class="q-body-1" v-show="downloadWarning"> <i>Your browser may try to block the downloads. In that case, please unblock and try again. </i></div>
    <div class="q-body-1" v-show="docxWarning"> <br/><i>You are converting MS Word files. You may have to set the font of the converted text to match the target script manually in MS Word. </i></div>
    <div v-show="loading">Converting the file(s). Large files might take some time to convert.<q-spinner-comment color="dark" :size="30" /> </div>
    <div v-for="(file, index) in files" :key="'file'+index" v-if="showContent">
      <b> {{file.name}} </b> <br/><br/>
      <div v-for="script in options.outputScript" :key="script">
        <div class="q-ma-md">{{getScriptObject(script).label}}</div>
      <transliterate :text="sanitize(file.content)" :src="options.inputScript" :tgt="script" :sourcePreserve="options.sourcePreserve" :postOptions="options.postOptions[script]" :preOptions="options.preOptions"> </transliterate>
      <br/><br/>
      </div>
    </div>
  </q-page>
</template>

<style scoped>
.vinodh {
  font-family: Arial;
}
</style>

<script>
import Transliterate from '../components/Transliterate'
import ControlsIo from '../components/ControlsIo'
import ConverterMenu from '../components/ConverterMenu'

import {QPageSticky, QUploader, QField, QSpinnerComment} from 'quasar'
import { ScriptMixin } from '../mixins/ScriptMixin'
import sanitizeHtml from 'sanitize-html'
import { saveAs } from 'file-saver'

// var JSZip = require('jszip')

export default {
  props: ['name'],
  mixins: [ScriptMixin],
  components: {
    ControlsIo,
    QPageSticky,
    Transliterate,
    QUploader,
    QSpinnerComment,
    QField,
    ConverterMenu
  },
  data () {
    return {
      options: {},
      optionsRet: {},
      files: [],
      showContent: false,
      loading: false,
      downloadWarning: false,
      docxWarning: false,
      htmlWarning: false
    }
  },
  methods: {
    sanitize: function (html) {
      return sanitizeHtml(html)
    },
    convertView: async function () {
      console.log(this.optionsRet.inputScript)

      if (typeof this.optionsRet.inputScript === 'undefined' || typeof this.optionsRet.outputScript === 'undefined' || this.optionsRet.inputScript === '' || this.optionsRet.outputScript === '') {
        this.$q.notify({
          message: 'Please select input/ouput scripts before proceeding to conversion',
          position: 'center',
          timeout: 1000
        })
      } else {
        this.readFiles()
        console.log(this.htmlWarning)
        if (this.docxWarning || this.htmlWarning) {
          this.$q.notify({
            message: 'You cannot view DocX or HTML files. Please download them instead',
            position: 'center',
            timeout: 2000
          })
        } else {
          this.downloadWarning = false
          this.options = this.optionsRet
          this.showContent = true
        }
      }
    },
    readFiles: async function () {
      this.files = []
      for (var i = 0; i < this.$refs.uploadF.queue.length; i++) {
        var file = this.$refs.uploadF.queue[i]
        var ext = file.name.split('.')[1]
        var text = ''
        if (ext === 'docx') {
          this.docxWarning = true
          var contentZ = await this.readFileBinary(file)
        } else {
          if (ext.includes('htm')) {
            this.htmlWarning = true
          }
          text = await this.readFileText(file)
        }
        if (ext === 'docx') {
          this.files.push({name: file.name, content: contentZ})
        } else {
          this.files.push({name: file.name, content: text})
        }
      }
    },
    readFileBinary: function (url) {
      return new Promise(resolve => {
        var reader = new FileReader()
        reader.onload = function () {
          resolve(reader.result)
        }
        reader.readAsDataURL(url) // read as Base64
      })
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
      console.log(this.optionsRet.inputScript)
      if (typeof this.optionsRet.inputScript === 'undefined' || typeof this.optionsRet.outputScript === 'undefined' || this.optionsRet.inputScript === '' || this.optionsRet.outputScript === '') {
        this.$q.notify({
          message: 'Please select input/ouput scripts before proceeding to conversion',
          position: 'center',
          timeout: 1000
        })
      } else {
        this.loading = true
        this.downloadWarning = true
        this.showContent = false
        this.options = this.optionsRet
        await this.readFiles()

        var checkCondition = false
        if (checkCondition) {
          this.$q.notify({
            message: 'You cannot convert from Roman scripts with DocX files',
            position: 'center',
            timeout: 2000
          })
        } else {
          for (var j = 0; j < this.options.outputScript.length; j++) {
            var outputScript = this.options.outputScript[j]
            for (var i = 0; i < this.files.length; i++) {
              var file = this.files[i]

              if (file.name.includes('.txt') || file.name.includes('.brh')) {
                var content = await this.convertAsync(this.options.inputScript, outputScript, file.content, this.options.sourcePreserve, this.options.postOptions[outputScript], this.options.preOptions)

                content = content.replace(new RegExp('<br/>', 'g'), '\n')
              } else {
                content = ''
              }
              // content = content.replace(new RegExp('e-Grantamil 7', 'g'), 'Noto Sans Tamil')
              // content = content.replace(new RegExp('e-Grantamil', 'g'), 'Noto Sans Tamil')

              var blob = ''
              var downloadName = ''
              if (file.name.includes('.brh')) {
                downloadName = this.options.inputScript + '_' + outputScript + '_' + file.name + '.txt'
              } else {
                downloadName = this.options.inputScript + '_' + outputScript + '_' + file.name
              }
              if (file.name.includes('.txt') || file.name.includes('.brh')) {
                blob = new Blob([content], {type: 'text/plain;charset=utf-8'})
                saveAs(blob, downloadName)
              } else if (file.name.includes('.xml')) {
                content = await this.convertXMLAsync(this.options.inputScript, outputScript, file.content, this.options.sourcePreserve, this.options.postOptions[outputScript], this.options.preOptions)

                blob = new Blob([content], {type: 'text/xml;charset=utf-8'})
                saveAs(blob, downloadName)
              } else if (file.name.includes('.docx')) {
                content = await this.convertDocXAsync(this.options.inputScript, outputScript, file.content, this.options.sourcePreserve, this.options.postOptions[outputScript], this.options.preOptions)

                blob = await (await fetch(content)).blob()
                saveAs(blob, downloadName)
              } else if (file.name.includes('.htm')) {
                content = await this.convertHTMLAsync(this.options.inputScript, outputScript, file.content, this.options.sourcePreserve, this.options.postOptions[outputScript], this.options.preOptions)

                blob = new Blob([content], {type: 'plain/html;charset=utf-8'})
                saveAs(blob, downloadName)
              }
            }
          }
        }
        this.loading = false
      }
    },
    convert: function () {
    },
    clear: function () {
      this.$refs.uploadF.reset()
      this.downloadWarning = false
      this.docxWarning = false
    }
  }
}
</script>
