<template>
  <!-- Fix Urdu ai and au -->
  <q-page class="q-pa-md" id="scrollstart">
          <q-alert
          color="red-4"
          icon="signal_cellular_alt"
          appear
          :actions="[{ label: 'Retry', handler: retryPage }]"
          class="q-mb-sm q-mr-xl"
          v-if="!checkifOnline && $q.platform.is.cordova"
        > You're not currently connected. Please activate your mobile data or Wi-Fi to use the app.  </q-alert>
    <converter-menu highlight="texts"></converter-menu>
  <div class="row">
      <div class="row col-xs-12 col-md-11 col-xl-5 q-ma-md float-div print-hide">
       <div class="row">
       <q-select
        filter
        inset
        autofocus-filter
        filter-placeholder="search"
        @input="updateInput"
        placeholder="Input Script"
        v-model="inputScript"
        class="col-xs-6 col-md-6 q-ma-sm"
        :options="scriptsInput"
      />
      <q-btn class="col-xs-3 col-md-3 q-ma-sm" v-show="inputPast !== ''"
       @click="updateHist" dense> <small>{{getScriptObject(inputPast).label}}</small> </q-btn>
      <q-icon name="history" size="25px" v-show="inputPast !== ''" class="print-hide"/>
      </div>
      <q-btn class="q-ma-sm btn2 print-hide col-xs-1 col-md-1" @click="copySource" :data-clipboard-text="textInput.replace(/<br\/>/g, '\n')"> <q-icon name="file_copy" /><q-tooltip>Copy source text</q-tooltip></q-btn>
      <q-collapsible sublabel="<i>Input Options</i>" icon="settings" dense class="q-mb-sm q-mt-sm">
    <input-options :inputScript="inputScript" :outputScript="outputScript" :preOptionsInput="preOptions"
      :postOptions="postOptions" v-model="preOptions" @input="convert"></input-options>
      </q-collapsible>
    <q-input
      v-model.trim="textInput"
      type="textarea"
      float-label="Input text"
      class="text-input col-xs-12 col-md-12 q-ma-sm"
      :class="getInputClass(inputScript, preOptions)"
      autofocus
      @input="throttled"
      clearable
      color="dark"
      rows="10"
      :max-height="1500"
      @clear="OCRPerformed = false"
      ></q-input>
    <input-notice :inputScript="inputScript" :outputScript="outputScript" :preOptions="preOptions"
       :postOptions="postOptions" :OCRPerformed="OCRPerformed"></input-notice>
    <div class="">
      <q-btn class="q-ma-sm print-hide col-xs-3 col-md-3" @click="uploadImage" label="Image/PDF" v-show="displayImageButton" v-if="!$q.platform.is.cordova" icon="add photo alternate"> <q-tooltip>Upload image/PDF</q-tooltip></q-btn>
      <span v-show="showFileUpload" class="q-ma-sm">
            <q-uploader url="" clearable extensions=".jpg, .jpeg, .png, .bmp, .ico, .pdf" @add="showConvertImage" @remove:cancel="hideConvertButton"
               auto-expand hide-upload-button ref="uploadF" :style="{width:'200px'}"/>
      <q-select
        filter
        autofocus-filter
        float-label="Document Language"
        filter-placeholder="search"
        v-model="ocrLang"
        placeholder="Language"
        class="col-xs-3 col-md-3 q-ma-sm print-hide"
        :options="ocrLangOptions"
      />
            <q-btn class="q-mt-sm" v-show="displayButton" @click="performOCR"> <small> Detect Text & Convert </small> </q-btn>
            <!-- <q-spinner-comment color="dark" :size="30" v-show="loadingOCR" class="q-ma-sm"/> -->
          <span v-show="loadingOCR">
          <q-progress
            :percentage="ocrProgress"
            color="tertiary"
            animate
            height="25px"
            class="q-mt-md q-ma-sm"
          />   <span class="q-ma-sm"> {{pdfProgress}} : {{ocrStatus}}: {{Math.round(ocrProgress)}} %</span>
          </span>
      </span>
    </div>
    </div>
    <div class="q-ma-md print-hide">
      <div class="col">
      <q-btn class="row"> <q-icon name="swap_horiz" @click.native="swap"/> <q-tooltip>Swap Source & Target</q-tooltip> </q-btn>
      <!-- q-spinner-comment color="dark" :size="30" v-show="loading" class="row"/> -->
      </div>
    </div>
    <div class="row col-xs-12 col-md-11 col-xl-5 q-ma-md float-div">
      <div class="row">
       <q-select
        filter
        autofocus-filter
        @input="updateOuput"
        filter-placeholder="search"
        v-model="outputScript"
        placeholder="Output Script"
        class="col-xs-6 col-md-6 q-ma-sm print-hide"
        :options="scriptsOutput"
      />
      <q-btn class="col-xs-3 col-md-3 q-ma-sm print-hide" v-show="outputPast !== ''"
       @click="updateHistOut" dense> <small>{{getScriptObject(outputPast).label}}</small> </q-btn>
      <q-icon name="history" size="25px" v-show="outputPast !== ''" class="print-hide"/>
      </div>
 <div class="q-mt-sm"><output-buttons @fontsizeinc="fontSize += 20" @fontsizedec="fontSize -= 20"
       @printdoc="printDocument" @screenshot="imageConvert(downloadImage.bind(this))" @copytext="copy" :convertText="convertText" :content="downHTML"></output-buttons></div>
      <q-btn icon="share" label="text" class="q-ma-sm" @click="shareCordovaText" v-if="$q.platform.is.cordova"/> <q-btn icon="share" label="image" class="q-ma-sm" @click="imageConvert(shareCordovaImage.bind(this))" v-if="$q.platform.is.cordova" />
     <q-collapsible sublabel="<i>Output Options</i>" icon="settings" dense class="q-mb-sm q-mt-sm">
    <output-options :inputScript="inputScript" :outputScript="outputScript" :postOptionsInput="postOptions"
       :convertText="convertText"
        v-model="postOptions" @input="convert" ></output-options>
          <span v-if="typeof preserveSourceExampleOut[outputScript] !== 'undefined' || scriptSemiticList.includes(inputScript) || ['Urdu', 'Thaana', 'Hebrew', 'Shahmukhi', 'Sindhi'].includes(inputScript)">
        <span><q-toggle color="dark" v-model="sourcePreserve" label="Preserve source" class="q-ml-sm q-mb-sm q-mt-md print-hide" @input="convert" /><q-tooltip>Preserve the source as-is and don't change the text to improve readability. May use archaic characters and/or diacritics. <br/><br/><div v-if="scriptSemiticList.includes(inputScript) || ['Urdu', 'Thaana', 'Hebrew', 'Shahmukhi', 'Sindhi'].includes(inputScript)">This also preserves the semitic consonants using the nukta (if present in the output script).</div></q-tooltip>
        </span>
        <small><div class="q-ml-xl print-hide" v-html="preserveSourceExampleOut[outputScript]"></div></small>
      </span>
     </q-collapsible>
    <div
      ref="brahmiText"
      class="text-output col-xs-12 col-md-12 q-pa-md q-pr-lg bg-grey-1 "
      >
       <div :class="getOutputClass(outputScript, postOptions, convertText)" :style="{'font-size': fontSize + '%'}"
        v-html="sanitize(convertText)"></div>
      </div>
    <output-notice :inputScript="inputScript" :outputScript="outputScript" :postOptions="postOptions"
     :convertText="convertText" :inputText="textInput"></output-notice>
    </div>
    </div>
  <transition
    enter-active-class="animated fadeIn"
    leave-active-class="animated fadeOut"
    appear
  >
    <div class="q-ma-lg q-body-1 print-hide" id="scrollend">
      Please report any bugs found in <a href="https://github.com/virtualvinodh/aksharamukha/issues">Github</a>.
    </div>
  </transition>
  <a :href="brahmiImg" ref="imgDownload" :style="{'display': 'none'}" download="text.png"><button>Download</button></a>
<q-page-sticky position="top-right" :offset="[18, 18]" v-show="scrollExists">
    <span><q-btn round color="dark" @click="scrolldown" icon="arrow_downward" v-show="!scrolled"/><q-tooltip>Scroll down</q-tooltip> </span>
  </q-page-sticky>
  <q-page-sticky position="bottom-right" :offset="[18, 18]" v-back-to-top>
    <span><q-btn round color="dark" @click="scrollup" icon="arrow_upward"/><q-tooltip>Scroll Up</q-tooltip> </span>
  </q-page-sticky>
  </q-page>
</template>

<style>
</style>

<script>
import {QProgress, QTab, QTabs, QTooltip, QEditor, QRadio, QBtn, QField, QBtnToggle, QToggle, QInput, QSelect, QOptionGroup, QAlert, QSpinnerComment, QPageSticky, QUploader, QCollapsible} from 'quasar'
import sanitizeHtml from 'sanitize-html'
import html2canvas from 'html2canvas'
import Transliterate from '../components/Transliterate'
import InputOptions from '../components/InputOptions'
import OutputOptions from '../components/OutputOptions'
import InputNotice from '../components/InputNotice'
import OutputNotice from '../components/OutputNotice'
import OutputButtons from '../components/OutputButtons'
import ConverterMenu from '../components/ConverterMenu'

import scrollTo from 'vue-scrollto'
import { ScriptMixin } from '../mixins/ScriptMixin'
import { createWorker } from 'tesseract.js'

var pdfjs = require('pdfjs-dist')

import ClipboardJS from 'clipboard'

var clipboard = new ClipboardJS('.btn2')
console.log(clipboard)

var _ = require('underscore')
const isOnline = require('is-online')

export default {
  name: 'PageIndex',
  mixins: [ScriptMixin],
  meta: {
    // meta tags
    meta: {
      description: { name: 'description', content: 'Aksharamukha aims to provide script conversion or transliteration between various scripts within the Indic cultural sphere. These include historic scripts, contemporary Brahmi-derived/inspired scripts, scripts invented for minority Indian languages, scripts that have co-existed with Indic scripts (like Avestan) or linguistically related scripts like Old Persian.' },
      keywords: { name: 'keywords', content: 'scripts, writing systems, transliteration, unicode, conversion, indic' }
    },

    // <noscript> tags
    noscript: {
      default: 'Aksharamukha aims to provide script conversion between various scripts within the Indic cultural sphere. These include historic scripts, contemporary Brahmi-derived/inspired scripts, scripts invented for minority Indian languages, scripts that have co-existed with Indic scripts (like Avestan) or linguistically related scripts like Old Persian. It also specifically provides lossless transliteration between the main Indian scripts (along with Sinhala). Apart from the simple mapping of characters, Askharamukha also attempts to implement various script/language-specific orthographic conventions (where known) such as vowel lengths, gemination and nasalization. It also provides several customization options to fine-tune and get the desired orthography. Aksharamukha as of now supports 78 scripts and 7 romanization methods. The scripts supported are: Ahom, Ariyaka, Assamese, Avestan, Balinese, Batak Karo, Batak Mandailing, Batak Pakpak, Batak Toba, Batak Simalungun, Bengali, Brahmi, Bhaiksuki, Buginese (Lontara), Buhid, Burmese (Myanmar), Chakma, Cham, Devanagari, Dogra, Grantha, Grantha (Pandya), Gujarati, Hanunoo, Javanese, Kaithi, Kannada, Khamti Shan, Kharoshthi, Khmer (Cambodian), Khojki, Khom Thai, Khudawadi, Lao, Lao (Pali), Lepcha, Limbu, Malayalam, Mahajani, Meetei Mayek (Manipuri), Modi, Mon, Multani, Newa (Nepal Bhasa), Old Persian, Oriya, PhagsPa, Punjabi (Gurmukhi), Ranjana (Lantsa), Rejang, Santali (Ol Chiki), Saurashtra, Siddham, Shan, Sharada, Sinhala, Sora Sompeng, Sundanese, Syloti Nagari, Tagbanwa, Tagalog, Tai Laing, Tai Tham (Lanna), Takri, Tamil, Tamil (Extended), Tamil Brahmi, Telugu, Thaana (Dhivehi), Thai, Tibetan, Tirhuta (Maithili), Urdu, Vatteluttu, Warang Citi, Zanabazar Square, Cyrillic (Russian), IPA, The Romanization Formats supported are: Harvard-Kyoto, ITRANS, Velthuis, IAST, ISO, Titus, Roman (Readable)'
    }
  },
  components: {
    QTab,
    QProgress,
    QTabs,
    QAlert,
    QEditor,
    QRadio,
    QBtn,
    QField,
    QBtnToggle,
    QToggle,
    QInput,
    QSelect,
    QCollapsible,
    QSpinnerComment,
    QOptionGroup,
    QTooltip,
    Transliterate,
    InputOptions,
    OutputOptions,
    InputNotice,
    OutputNotice,
    OutputButtons,
    QPageSticky,
    QUploader,
    ConverterMenu
  },
  data () {
    return {
      textInput: '',
      checkifOnline: true,
      OCRPerformed: false,
      showFileUpload: false,
      imageFile: '',
      loadingOCR: false,
      displayButton: false,
      displayImageButton: true,
      beta: true,
      model: [],
      scrolled: false,
      inputScript: 'autodetect',
      outputScript: '',
      postOptions: [],
      preOptions: [],
      sourcePreserve: false,
      options: {},
      convertText: '',
      brahmiImg: '',
      fontSize: 100,
      dash: _,
      loading: false,
      inputPast: '',
      outputPast: '',
      throttled: _.debounce(this.convert, 300),
      postOptionsScript: {},
      preOptionsScript: {},
      scrollExists: false,
      worker: '',
      ocrProgress: 0,
      pdfProgress: '',
      ocrStatus: '',
      ocrLang: 'osd'
    }
  },
  mounted () {
    this.checkOnline()

    // this.runCode()

    this.worker = createWorker({
      logger: function (m) {
        this.ocrProgress = m.progress * 100
        this.ocrStatus = m.status
        console.log(m)
      }.bind(this)
    })

    if (localStorage.sourcePreserve) {
      this.sourcePreserve = JSON.parse(localStorage.sourcePreserve)
    }
    if (localStorage.inputScript) {
      this.inputPast = localStorage.inputScript
    }
    if (localStorage.outputScript) {
      this.outputScript = localStorage.outputScript
    }
    if (localStorage.outputPast) {
      this.outputPast = localStorage.outputPast
    }
    if (localStorage.postOptionsScriptIndex) {
      this.postOptionsScript = JSON.parse(localStorage.postOptionsScriptIndex)

      if (typeof this.postOptionsScript[this.outputScript] === 'undefined') {
        this.postOptionsScript[this.outputScript] = []
      }
      this.$set(this, 'postOptions', this.postOptionsScript[this.outputScript])
    }
    if (localStorage.preOptionsScriptIndex) {
      this.preOptionsScript = JSON.parse(localStorage.preOptionsScriptIndex)

      if (typeof this.preOptionsScript[this.inputScript] === 'undefined') {
        this.preOptionsScript[this.inputScript] = []
      }
      this.$set(this, 'preOptions', this.preOptionsScript[this.inputScript])
    }

    if (typeof this.$route.query.target !== 'undefined') {
      this.outputScript = this.$route.query.target
    }

    if (typeof this.$route.query.text !== 'undefined') {
      this.textInput = this.$route.query.text
      this.convert()
    }

    if (window.innerWidth > document.body.clientWidth) {
      this.scrollExists = true
    } else {
      this.scrollExists = false
    }
  },
  updated: function () {
    if (window.innerWidth > document.body.clientWidth) {
      this.scrollExists = true
    } else {
      this.scrollExists = false
    }
  },
  watch: {
    sourcePreserve (newV, oldV) {
      localStorage.sourcePreserve = JSON.stringify(newV)
    },
    inputScript (newScript, oldScript) {
      this.inputPast = oldScript
      localStorage.inputScript = newScript
    },
    outputScript (newScript, oldScript) {
      if (oldScript !== '') {
        this.outputPast = oldScript
        localStorage.outputPast = oldScript
      }
      localStorage.outputScript = newScript
    },
    postOptions (newOpt, oldOpt) {
      this.postOptionsScript[this.outputScript] = newOpt
      localStorage.postOptionsScriptIndex = JSON.stringify(this.postOptionsScript)

      if (typeof this.postOptionsScript[this.outputScript] === 'undefined') {
        this.postOptionsScript[this.outputScript] = []
      }

      this.$set(this, 'postOptions', this.postOptionsScript[this.outputScript])
    },
    preOptions (newOpt, oldOpt) {
      this.preOptionsScript[this.inputScript] = newOpt
      localStorage.preOptionsScriptIndex = JSON.stringify(this.preOptionsScript)

      if (typeof this.preOptionsScript[this.inputScript] === 'undefined') {
        this.preOptionsScript[this.inputScript] = []
      }

      this.$set(this, 'preOptions', this.preOptionsScript[this.inputScript])
    }
  },
  methods: {
    /* runCode: function () {
      console.log('getting called')
      window.languagePluginLoader.then(async () => {
        console.log('inside')
        window.pyodide.loadPackage('micropip').then(async () => {
          console.log('inside2')
          this.textInput = 'vinod'
          this.result = await window.pyodide.runPythonAsync(`
  def do_work(*args):
      from aksharamukha import transliterate
      import js
      print('vinod')
      return transliterate.process('` + this.inputScript + `','` + this.outputScript + `','` + this.textInput + `')

  import micropip
  micropip.install('aksharamukha').then(do_work)
            `)
          console.log(this.result)
        })
      })
    }, */
    downHTML: function () {
      this.downloadHTML(this.$refs.brahmiText.innerHTML)
    },
    retryPage: function () {
      this.checkOnline()

      if (this.checkifOnline) {
        document.location.reload(true)
        this.convert()
      }
    },
    checkOnline: async function () {
      this.checkifOnline = await isOnline()
    },
    performOCR: async function () {
      if (this.ocrLang === '') {
        this.$q.notify({
          type: 'info',
          message: 'Please select the language of the document',
          position: 'center',
          timeout: 1000
        })
        return
      }

      this.$q.notify({
        type: 'info',
        message: 'This may take a while. Please have some patience.',
        position: 'center',
        timeout: 1000
      })

      this.loadingOCR = true

      var base64 = await this.readFile(this.imageFile)
      var data = {
        'requests': [
          {
            'image': {
              'content': base64.split(',')[1]
            },
            'features': [
              {
                'type': 'DOCUMENT_TEXT_DETECTION'
              }
            ]
          }
        ]
      }
      console.log(data)

      await this.worker.load()
      await this.worker.loadLanguage(this.ocrLang)
      await this.worker.initialize(this.ocrLang)

      // console.log('Sending Results')
      // var result = await this.getResultPost('https://vision.googleapis.com/v1/images:annotate?key=' + keys.api_key, data)
      // console.log('Got the results back')
      pdfjs.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.6.347/pdf.worker.min.js'

      if (this.imageFile.type === 'application/pdf') {
        var pdf = await pdfjs.getDocument(await this.readFilePDF(this.imageFile)).promise
        var textOCR = ''

        for (var i = 1; i <= pdf.numPages; i++) {
          var page = await pdf.getPage(i)
          console.log('Scaning page ' + i)

          var viewport = page.getViewport({scale: 6})

          var canvas = document.createElement('canvas')
          var context = canvas.getContext('2d')
          canvas.height = viewport.height
          canvas.width = viewport.width

          await page.render({canvasContext: context, viewport: viewport}).promise

          base64 = canvas.toDataURL()

          this.pdfProgress = 'Page ' + i + '/' + pdf.numPages

          if (i === 1 && this.ocrLang === 'osd') {
            try {
              var detectionpdf = await this.worker.detect(base64)
            } catch (e) {
              console.log(e)
              this.$q.notify({
                type: 'info',
                message: 'Cannot detect script. Please select document language manually',
                position: 'center',
                timeout: 1500
              })
            }
            if (detectionpdf.data.script === 'Devanagari') {
              this.ocrLang = 'san'
            } else {
              this.ocrLang = this.getOCRScriptId(detectionpdf.data.script)
            }
            await this.worker.loadLanguage(this.ocrLang)
            await this.worker.initialize(this.ocrLang)
          }

          const { data: { text } } = await this.worker.recognize(base64)
          textOCR = textOCR + text + '\n\n'
        }
      } else {
        if (this.ocrLang === 'osd') {
          try {
            var detection = await this.worker.detect(base64)
          } catch (e) {
            console.log(e)
            this.$q.notify({
              type: 'info',
              message: 'Cannot detect script. Please select document language manually',
              position: 'center',
              timeout: 1500
            })
          }
          if (detection.data.script === 'Devanagari') {
            this.ocrLang = 'san'
          } else {
            this.ocrLang = this.getOCRScriptId(detection.data.script)
          }
          await this.worker.loadLanguage(this.ocrLang)
          await this.worker.initialize(this.ocrLang)
        }
        const { data: { text } } = await this.worker.recognize(base64)
        textOCR = text
      }
      // await this.worker.terminate()
      this.textInput = textOCR
      this.$q.notify({
        type: 'info',
        message: 'Text recognition is complete. Please proof-read the recognized text in the input area for possible errors.',
        position: 'center',
        timeout: 1500
      })
      this.convert()
      this.ocrStatus = ''
      this.ocrProgress = 0
      this.$refs.uploadF.reset()

      this.displayButton = false
      this.loadingOCR = false
      this.showFileUpload = false
      this.displayImageButton = true

      this.OCRPerformed = true
    },
    uploadImage: function () {
      this.showFileUpload = true
      document.getElementsByClassName('q-uploader-input')[0].click()
      this.displayImageButton = false
    },
    showConvertImage: function (files) {
      this.imageFile = files[0]
      this.displayButton = true
    },
    hideConvertButton: function (file) {
      this.displayButton = false
    },
    scrolldown: function () {
      scrollTo.scrollTo('#scrollend', 1000)
      this.scrolled = true
    },
    scrollup: function () {
      scrollTo.scrollTo('.q-toolbar-title', 1000)
      this.scrolled = false
    },
    updateHist: function () {
      this.inputScript = this.inputPast
      this.updateInput()
    },
    updateInput: function () {
      if (typeof this.preOptionsScript[this.inputScript] === 'undefined') {
        this.preOptionsScript[this.inputScript] = []
      }
      this.$set(this, 'preOptions', this.preOptionsScript[this.inputScript])

      if (this.inputScript === 'Urdu' || this.inputScript === 'Shahmukhi') {
        this.$set(this, 'preOptions', ['UrduShortNotShown'])
      }

      if (this.inputScript === 'Oriya' && this.outputScript === 'Bengali') {
        this.$set(this, 'postOptions', ['khandatabatova'])
      }

      var nikkuds = ['\u05B7', '\u05B8', '\u05B4', '\u05B4י', '\u05BB', '\u05C2', '\u05C1', '\u05B6', '\u05B5', '\u05B9', 'וֹ', '\u05B1', '\u05B2', '\u05B3', '\u05BC', '\u05B0', '\u05C7']

      console.log(nikkuds.some(nikkud => this.textInput.includes(nikkud)))

      if (this.inputScript === 'Hebrew' && this.scriptSemiticListAll.includes(this.outputScript) && !nikkuds.some(nikkud => this.textInput.includes(nikkud))) {
        this.$set(this, 'preOptions', ['novowelshebrewSemitic'])
      } else {
        this.$set(this, 'preOptions', [])
      }

      if (this.inputScript === 'Hebrew' && this.scriptIndicList.includes(this.outputScript) && !nikkuds.some(nikkud => this.textInput.includes(nikkud))) {
        this.$set(this, 'preOptions', ['novowelshebrewIndic'])
      } else {
        this.$set(this, 'preOptions', [])
      }

      this.convert()
    },
    updateHistOut: function () {
      this.outputScript = this.outputPast
      this.updateOuput()
    },
    updateOuput: function () {
      if (typeof this.postOptionsScript[this.outputScript] === 'undefined') {
        this.postOptionsScript[this.outputScript] = []
      }
      this.$set(this, 'postOptions', this.postOptionsScript[this.outputScript])

      if (this.inputScript === 'Oriya' && this.outputScript === 'Bengali') {
        this.$set(this, 'postOptions', ['khandatabatova'])
      }

      this.convert()
    },
    copy: function () {
      this.$q.notify({
        type: 'info',
        message: 'Copied',
        position: 'center',
        timeout: 200
      })
    },
    copySource: function () {
      this.$q.notify({
        type: 'info',
        message: 'Copied',
        position: 'center',
        timeout: 200
      })
    },
    audodetect: function (Strng) {
    },
    demo: function () {
      console.log('called')
    },
    sanitize: function (html) {
      return sanitizeHtml(html)
    },
    swap: function () {
      this.textInput = this.convertText.replace(new RegExp('<br/>', 'g'), '\n')
      let temp = this.inputScript
      this.inputScript = this.outputScript
      this.outputScript = temp
      this.convert()
      this.postOptions = []
      this.preOptions = []
    },
    printDocument: function () {
      // manually hide the side menu while printing and bring it back when printing is complete
      window.print()
    },
    getScript: async function (text) {
      var data = {
        'text': text
      }
      return new Promise(resolve => {
        this.apiCall.post('/autodetect', data)
          .then(function (response) {
            resolve(response.data)
          })
          .catch(function (error) {
            console.log(error)
          })
      })
    },
    getPre: async function (text, source) {
      var data = {
        'text': text,
        'source': source
      }
      return new Promise(resolve => {
        this.apiCall.post('/detectpre', data)
          .then(function (response) {
            resolve(response.data)
          })
          .catch(function (error) {
            console.log(error)
          })
      })
    },
    downloadImage: function () {
      var dhis = this
      if (dhis.$q.platform.is.cordova) {
        var params = {data: dhis.brahmiImg, prefix: 'aksharamukha_', format: 'PNG', quality: 100, mediaScanner: true}
        window.imageSaver.saveBase64Image(params,
          function (filePath) {
            console.log('File saved on ' + filePath)
            dhis.$q.notify({
              type: 'info',
              message: 'The image has been saved in your gallery. Please check there.',
              position: 'center',
              timeout: 5000
            })
          },
          function (msg) {
            console.error(msg)
          }
        )
      } else {
        dhis.$refs.imgDownload.click()
      }
    },
    shareCordovaImage: function () {
      var dhis = this

      var params = {data: dhis.brahmiImg, prefix: 'aksharamukha_', format: 'PNG', quality: 100, mediaScanner: true}
      window.imageSaver.saveBase64Image(params,
        function (filePath) {
          var options = {
            message: '',
            subject: '', // fi. for email
            files: [filePath], // an array of filenames either locally or remotely
            chooserTitle: 'Pick an app' // Android only, you can override the default share sheet title
          }

          var onSuccess = function (result) {
            console.log('Share completed? ' + result.completed)
            console.log('Shared to app: ' + result.app)
          }

          var onError = function (msg) {
            console.log('Sharing failed with message: ' + msg)
          }

          window.plugins.socialsharing.shareWithOptions(options, onSuccess, onError)
        },
        function (msg) {
          console.error(msg)
        }
      )
    },
    shareCordovaText: function () {
      var options = {
        message: this.convertText,
        subject: this.convertText, // fi. for email
        chooserTitle: 'Pick an app' // Android only, you can override the default share sheet title
      }

      var onSuccess = function (result) {
        console.log('Share completed? ' + result.completed)
        console.log('Shared to app: ' + result.app)
      }

      var onError = function (msg) {
        console.log('Sharing failed with message: ' + msg)
      }

      window.plugins.socialsharing.shareWithOptions(options, onSuccess, onError)
    },
    convert: async function () {
      this.convertText += ' . . . '

      // this.runCode()

      if (this.$q.platform.is.cordova) {
        this.checkOnline()
      }

      if (this.textInput === '' || this.inputScript === '' || this.outputScript === '' ||
        this.inputScript === 'undefined' || this.outputScript === 'undefined') {
        this.convertText = ''
        return
      }
      this.loading = true

      if (this.inputScript === 'autodetect') {
        this.inputScript = await this.getScript(this.textInput)

        if (typeof this.preOptionsScript[this.inputScript] !== 'undefined') {
          this.$set(this, 'preOptions', this.preOptionsScript[this.inputScript])
        }

        // Check with the list of scripts in transliterate.detect_preoptions()
        // scripts available tehre must be added here
        if (['Thai', 'Lao', 'LaoPali', 'Urdu'].includes(this.inputScript)) {
          var preOptionsTemp = await this.getPre(this.textInput, this.inputScript)
          this.preOptions = preOptionsTemp
        }
      }

      if (this.inputScript !== 'Urdu' && this.inputScript !== 'Shahmukhi') {
        this.postOptions = this.postOptions.filter(x => x !== 'urduRemoveInherent')
      }

      var data = {
        source: this.inputScript,
        target: this.outputScript,
        text: this.textInput,
        nativize: !this.sourcePreserve,
        postOptions: this.postOptions,
        preOptions: this.preOptions
      }
      var dhis = this
      // console.log('Calling with this options')
      // console.log(this.postOptions)
      this.apiCall.post('/convert', data)
        .then(function (response) {
          dhis.convertText = response.data
          dhis.loading = false
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    imageConvert: function (func) {
      var node = this.$refs.brahmiText
      console.log(node)
      var dhis = this
      this.$q.notify({
        type: 'info',
        message: 'Snapshot being generated',
        position: 'center',
        timeout: 200
      })

      html2canvas(node).then(function (canvas) {
        var image = new Image()
        image.src = canvas.toDataURL('image/png', 1)
        dhis.brahmiImg = image.src
        image.onload = function () {
          dhis.brahmiImg = image.src

          var image2 = new Image()
          var cropped = dhis.removeWhite(image)
          image2.src = cropped
          dhis.brahmiImg = cropped

          image2.onload = func
        }
      })
    },
    removeWhite: function (imageObject) {
      var imgWidth = imageObject.width
      var imgHeight = imageObject.height
      var canvas = document.createElement('canvas')
      canvas.setAttribute('width', imgWidth)
      canvas.setAttribute('height', imgHeight)
      var context = canvas.getContext('2d')
      context.drawImage(imageObject, 0, 0)

      var imageData = context.getImageData(0, 0, imgWidth, imgHeight)
      var data = imageData.data
      var getRBG = function (x, y) {
        var offset = imgWidth * y + x
        return {
          red: data[offset * 4],
          green: data[offset * 4 + 1],
          blue: data[offset * 4 + 2],
          opacity: data[offset * 4 + 3]
        }
      }
      var isWhite = function (rgb) {
        // many images contain noise, as the white is not a pure #fff white
        return rgb.red > 200 && rgb.green > 200 && rgb.blue > 200
      }
      var scanY = function (fromTop) {
        var offset = fromTop ? 1 : -1

        // loop through each row
        for (var y = fromTop ? 0 : imgHeight - 1; fromTop ? (y < imgHeight) : (y > -1); y += offset) {
        // loop through each column
          for (var x = 0; x < imgWidth; x++) {
            var rgb = getRBG(x, y)
            if (!isWhite(rgb)) {
              if (fromTop) {
                return y
              } else {
                return Math.min(y + 1, imgHeight - 1)
              }
            }
          }
        }
        return null // all image is white
      }
      var scanX = function (fromLeft) {
        var offset = fromLeft ? 1 : -1
        // loop through each column
        for (var x = fromLeft ? 0 : imgWidth - 1; fromLeft ? (x < imgWidth) : (x > -1); x += offset) {
          // loop through each row
          for (var y = 0; y < imgHeight; y++) {
            var rgb = getRBG(x, y)
            if (!isWhite(rgb)) {
              if (fromLeft) {
                return x
              } else {
                return Math.min(x + 1, imgWidth - 1)
              }
            }
          }
        }
        return null // all image is white
      }

      var cropTop = scanY(true) - 20
      var cropBottom = scanY(false) + 20
      var cropLeft = scanX(true) - 20
      var cropRight = scanX(false) + 20
      var cropWidth = cropRight - cropLeft
      var cropHeight = cropBottom - cropTop

      canvas.setAttribute('width', cropWidth)
      canvas.setAttribute('height', cropHeight)
      // finally crop the guy
      canvas.getContext('2d').drawImage(imageObject,
        cropLeft, cropTop, cropWidth, cropHeight,
        0, 0, cropWidth, cropHeight)

      return canvas.toDataURL()
    }
  }
}
</script>

<style scoped>
.float-div {
  display: inline-block;
  float: left;
}
.notice {
  color: gray;
  font-size: 12px;
}
.text-output {
  min-height: 230px;
}
</style>
