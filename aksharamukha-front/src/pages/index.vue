<template>
  <!-- Fix Urdu ai and au -->
  <q-page class="q-pa-md" id="scrollstart">
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
      ></q-input>
    <input-notice :inputScript="inputScript" :outputScript="outputScript" :preOptions="preOptions"
       :postOptions="postOptions"></input-notice>
    <input-options :inputScript="inputScript" :outputScript="outputScript" :preOptionsInput="preOptions"
      :postOptions="postOptions" v-model="preOptions" @input="convert"></input-options>
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
    <div
      v-html="sanitize(convertText)"
      ref="brahmiText"
      class="text-output col-xs-12 col-md-12 q-pa-md q-pr-lg bg-grey-1 "
      :class="getOutputClass(outputScript, postOptions)" :style="{'font-size': fontSize + '%'}"
      ></div>
    <output-notice :inputScript="inputScript" :outputScript="outputScript" :postOptions="postOptions"
     :convertText="convertText"></output-notice>
      <div class="q-mt-sm"><output-buttons @fontsizeinc="fontSize += 20" @fontsizedec="fontSize -= 20"
       @printdoc="printDocument" @screenshot="imageConvert" @copytext="copy" :convertText="convertText"></output-buttons></div>
      <span><q-toggle color="dark" v-model="sourcePreserve" label="Preserve source" class="q-ml-sm q-mb-sm q-mt-md print-hide" @input="convert" /><q-tooltip>Preserve the source as-is and don't change the text to improve readability</q-tooltip></span>
    <output-options :inputScript="inputScript" :outputScript="outputScript" :postOptionsInput="postOptions"
       :convertText="convertText"
        v-model="postOptions" @input="convert"></output-options>    </div>
    </div>
  <transition
    enter-active-class="animated fadeIn"
    leave-active-class="animated fadeOut"
    appear
  >
    <div class="q-ma-lg q-body-1 print-hide" id="scrollend">
      This is a new beta version of Aksharamukha. Please report any bugs found in <a href="https://github.com/virtualvinodh/aksharamukha/issues">Github</a>. <br/>The old version is still temporarily available <a href="http://www.virtualvinodh.com/aksharamkh/aksharamukha-old.php">here</a>.
    </div>
  </transition>
  <a :href="brahmiImg" ref="imgDownload" :style="{'display': 'none'}" download="text.png"><button>Download</button></a>
<q-page-sticky position="top-right" :offset="[18, 18]" v-show="scrollExists">
    <span><q-btn round color="dark" @click="scrolldown" icon="arrow_downward" v-show="!scrolled"/><q-tooltip>Scroll down</q-tooltip> </span>
    <span><q-btn round color="dark" @click="scrollup" icon="arrow_upward" v-show="scrolled"/>
    <q-tooltip>Scroll up</q-tooltip> </span>
  </q-page-sticky>
  </q-page>
</template>

<style>
</style>

<script>
import {QTooltip, QEditor, QRadio, QBtn, QField, QBtnToggle, QToggle, QInput, QSelect, QOptionGroup, QAlert, QSpinnerComment, QPageSticky} from 'quasar'
import sanitizeHtml from 'sanitize-html'
import html2canvas from 'html2canvas'
import Transliterate from '../components/Transliterate'
import Controls from '../components/Controls'
import InputOptions from '../components/InputOptions'
import OutputOptions from '../components/OutputOptions'
import InputNotice from '../components/InputNotice'
import OutputNotice from '../components/OutputNotice'
import OutputButtons from '../components/OutputButtons'
import scrollTo from 'vue-scrollto'
import { ScriptMixin } from '../mixins/ScriptMixin'

var _ = require('underscore')

export default {
  name: 'PageIndex',
  mixins: [ScriptMixin],
  components: {
    QAlert,
    QEditor,
    QRadio,
    QBtn,
    QField,
    QBtnToggle,
    QToggle,
    Controls,
    QInput,
    QSelect,
    QSpinnerComment,
    QOptionGroup,
    QTooltip,
    Transliterate,
    InputOptions,
    OutputOptions,
    InputNotice,
    OutputNotice,
    OutputButtons,
    QPageSticky
  },
  data () {
    return {
      textInput: '',
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
      scrollExists: false
    }
  },
  mounted () {
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

      if (this.inputScript === 'Urdu') {
        this.$set(this, 'preOptions', ['UrduShortNotShown'])
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
    convert: async function () {
      this.convertText += ' . . . '
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
    imageConvert: function () {
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

          image2.onload = function () {
            dhis.$refs.imgDownload.click()
          }
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
