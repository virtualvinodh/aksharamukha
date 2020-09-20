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
        v-model="inputScriptComposer"
        float-label="Input Script"
        class="col-xs-6 col-md-6 q-ma-sm"
        :options="scriptsOutput"
      />
      </div>
    <span class="q-body-1"></span>
    <q-input
      v-model.trim="textInput"
      type="textarea"
      float-label="Input text"
      class="text-input col-xs-12 col-md-12 q-ma-sm"
      :class="getInputClass(inputScriptComposer, preOptions)"
      autofocus
      @input="throttled"
      clearable
      color="dark"
      rows="10"
      :max-height="1500"
      ></q-input>
    <input-options :inputScript="inputScriptComposer" :outputScript="outputScript[0]" :preOptionsInput="preOptions"
      :postOptions="postOptions" v-model="preOptions" @input="convert"></input-options>
    <q-input v-model="split" maxlength="5" float-label="Split input text using" v-if="outputScript1.length > 1 && !ignore1"></q-input>
    <div class="notice q-ma-sm">
    <div class="q-body-1"># toggles between primary and secondary scripts. <pre>primary text #secondary text#</pre></div>

    <div class="q-body-1 q-mt-md">Manually specify the [input] and/or (output) <router-link :to="'/documentation/'">script(s)</router-link> (to override the default value) of the secondary. Add @PS to enable <i>Preserve Source</i>
      <pre>#nija# #kila#(Telugu) #neLa#(Lao, Thai)
#niśa#[IAST] #niśa#[IAST](Lao)
#mana#(Tamil@PS) #here#(Ignore) </pre>
   <div class="q-body-1 q-mt-md">Outputs are separated by a new line for multiple output scripts. <br/><br/>
In case of multiple outputs for the primary, the text is split into lines by default using a single new line character  (this can be changed) and then processed line by line.</div>
  </div>
    </div>
  </div>
    <div class="row col-xs-12 col-md-11 col-xl-5 q-ma-md float-div">
      <div class="row">
       <q-select
        filter
        autofocus-filter
        @input="updateOuput"
        multiple
        chips
        filter-placeholder="search"
        v-model="outputScript1"
        placeholder="Primary script"
        chips-bg-color="dark"
        float-label="Primary"
        :disable="ignore1"
        class="col-xs-6 col-md-6 q-ma-sm print-hide"
        :options="scriptsOutput"
      />
      <span><q-toggle color="dark" v-model="ignore1" label="Don't convert" class="q-ml-sm q-mb-sm q-mt-lg print-hide" @input="convert" /><q-tooltip>Ignore primary text</q-tooltip></span>
      </div>
      <div class="row">
       <q-select
        filter
        autofocus-filter
        @input="updateOuput"
        filter-placeholder="search"
        v-model="outputScript2"
        placeholder="Secondary"
        :disable="ignore2"
        multiple
        chips
        chips-bg-color="dark"
        float-label="#Secondary# output"
        class="col-xs-6 col-md-6 q-ma-sm print-hide"
        :options="scriptsOutput"
      />
      <span><q-toggle color="dark" v-model="ignore2" label="Don't convert" class="q-ml-sm q-mb-sm q-mt-lg print-hide" @input="convert" /><q-tooltip>Ignore secondary text</q-tooltip></span>
      </div>
    <div class="notice q-ma-sm" v-show="outputScript1.length > 1 && textInput.includes('#')">Multiple primary output scripts detected. Secondary text will be ignored.</div>
    <div ref="brahmiText"
      class="text-output col-xs-12 col-md-12 q-pa-md q-pr-lg bg-grey-1 "
      ><span
      :style="{'font-size': fontSize + '%'}">
        <span  v-if="outputScript1.length > 1 && !ignore1">
        <span v-for="(line, index) in textInput.split(this.processSplit(this.split))" :key="'line'+index">

          <span v-if="line != ''">
            <span v-for="(scriptO, index) in outputScript1" :key="'out1' + index">
              <transliterate :text="line" :src="inputScriptComposer" :tgt="!ignore1 ? scriptO : ''" :sourcePreserve="sourcePreserveComposer" :postOptions="postOptionsScriptComposer[scriptO]" :preOptions="preOptions">
              </transliterate> <br/><br/>
            </span>
          <span v-if="line === ''">
            <br/>
          </span>
          <br/>
        </span>

        </span>
        </span>

      <span v-if="outputScript1.length <= 1 || this.ignore1">
      <span v-for="(token, index) in tokensNew" :key="index" v-if="token.type !== 'param' || token.type !== 'paramin'">
        <span v-if="typeof outputScript1[0] !== 'undefined'">
        <transliterate :text="token.value" :src="chooseInput(token)" :tgt="!ignore1 ? outputScript1[0] : ''" :sourcePreserve="choosePS(token)" :postOptions="postOptionsScriptComposer[outputScript1[0]]" v-if="token.type=='primary'"  :preOptions="preOptions">
        </transliterate>
        </span>
        <span v-else>
          <span v-if="token.type == 'primary'" v-html="newLineBreak(token.value)"> </span>
        </span>

        <span v-for="(scriptO, index) in chooseTgt(token)" :key="'out' + index" v-if="chooseTgt(token).length > 1 && !ignore2">
          <span v-if="token.type=='secondary'">
            <transliterate :text="token.value" :src="chooseInput(token)" :tgt="scriptO" :sourcePreserve="choosePS(token)" :postOptions="postOptionsScriptComposer[scriptO]" :preOptions="preOptions">
            </transliterate>
            <span v-if="index !== chooseTgt(token).length-1"><br/><br/></span>
          </span>

        </span>

        <span v-else>
          <transliterate :text="token.value" :src="chooseInput(token)" :tgt="chooseTgt(token)[0]" :sourcePreserve="choosePS(token)" :postOptions="postOptionsScriptComposer[chooseTgt(token)[0]]" v-if="token.type=='secondary'"  :preOptions="preOptions">
          </transliterate>

        </span>

      </span>
      </span>
      </span>
      </div>

      <div class="q-mt-sm"><output-buttons @fontsizeinc="fontSize += 20" @fontsizedec="fontSize -= 20"
       @printdoc="printDocument" @screenshot="imageConvert(downloadImage.bind(this))" @copytext="copy" :convertText="convertText" :content="downHTML"></output-buttons></div>
      <q-btn icon="share" label="text" class="q-ma-sm" @click="shareCordovaText" v-if="$q.platform.is.cordova"/> <q-btn icon="share" label="image" class="q-ma-sm" @click="imageConvert(shareCordovaImage.bind(this))" v-if="$q.platform.is.cordova" /> <br/>
      <span><q-toggle color="dark" v-model="sourcePreserveComposer" label="Preserve source" class="q-ml-sm q-mb-sm q-mt-md print-hide" @input="convert" /><q-tooltip>Preserve the source as-is and don't change the text to improve readability</q-tooltip></span> <br/> <br/>

    <br/><br/>
    <span v-for="scriptO in outputScript1" :key="'o'+scriptO" class="print-hide" v-if="typeof postOptionsGroup[scriptO] !== 'undefined'">
          {{scriptO}} Options <br/>

    <output-options :inputScript="inputScriptComposer" :outputScript="scriptO" :postOptionsInput="postOptionsScriptComposer[scriptO]"
       :convertText="convertText"
        v-model="postOptionsScriptComposer[scriptO]" @input="convert"></output-options>

    </span>

        <span v-for="scriptO in outputScript2" :key="scriptO" class="print-hide" v-if="typeof postOptionsGroup[scriptO] !== 'undefined'">
          {{scriptO}} Options <br/>
              <output-options :inputScriptComposer="inputScriptComposer" :outputScript="scriptO" :postOptionsInput="postOptionsScriptComposer[scriptO]"
       :convertText="convertText"
        v-model="postOptionsScriptComposer[scriptO]" @input="convert"></output-options>
        </span>
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
    <span><q-btn round color="dark" @click="scrollup" icon="arrow_upward" v-show="scrolled"/>
    <q-tooltip>Scroll up</q-tooltip> </span>
  </q-page-sticky>
</q-page>
</template>

<style>
</style>

<script>
import {QTabs, QTab, QTabPane, QRouteTab, QTooltip, QEditor, QRadio, QBtn, QField, QBtnToggle, QToggle, QInput, QSelect, QOptionGroup, QAlert, QSpinnerComment, QPageSticky, QUploader} from 'quasar'
import sanitizeHtml from 'sanitize-html'
import html2canvas from 'html2canvas'
import Transliterate from '../components/Transliterate'
import InputOptions from '../components/InputOptions'
import OutputOptions from '../components/OutputOptions'
import InputNotice from '../components/InputNotice'
import OutputNotice from '../components/OutputNotice'
import OutputButtons from '../components/OutputButtons'
import scrollTo from 'vue-scrollto'
import { ScriptMixin } from '../mixins/ScriptMixin'

const moo = require('moo')

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
    QPageSticky,
    QUploader,
    QTabs,
    QTab,
    QTabPane,
    QRouteTab
  },
  data () {
    return {
      textInput: '',
      ignore1: false,
      ignore2: false,
      split: '\\n',
      beta: true,
      model: [],
      scrolled: false,
      inputScriptComposer: '',
      outputScript: [],
      outputScript1: [],
      postOptions: [],
      preOptions: [],
      sourcePreserveComposer: false,
      options: {},
      convertText: '',
      brahmiImg: '',
      fontSize: 100,
      dash: _,
      loading: false,
      inputPast: '',
      outputPast: '',
      throttled: _.debounce(this.convert, 300),
      postOptionsScriptComposer: {},
      preOptionsScriptComposer: {},
      scrollExists: false,
      tokensNew: [],
      outputScript2: []
    }
  },
  mounted () {
    for (var i = 0; i < this.scriptsOutput.length; i++) {
      this.$set(this.postOptionsScriptComposer, this.scriptsOutput[i].value, [])
    }

    if (localStorage.postOptionsScriptComposer) {
      this.postOptionsScriptComposer = JSON.parse(localStorage.postOptionsScriptComposer)
    }

    if (localStorage.ignore1) {
      this.ignore1 = JSON.parse(localStorage.ignore1)
    }

    if (localStorage.ignore2) {
      this.ignore2 = JSON.parse(localStorage.ignore2)
    }

    if (localStorage.sourcePreserveComposer) {
      this.sourcePreserveComposer = JSON.parse(localStorage.sourcePreserveComposer)
    }
    if (localStorage.inputScriptComposer) {
      this.inputScriptComposer = localStorage.inputScriptComposer
    }
    if (localStorage.outputScript1) {
      this.outputScript1 = JSON.parse(localStorage.outputScript1)
    }
    if (localStorage.outputScript2) {
      this.outputScript2 = JSON.parse(localStorage.outputScript2)
    }
    if (localStorage.outputPast) {
      this.outputPast = localStorage.outputPast
    }
    /* if (localStorage.postOptionsScriptComposerIndex) {
      this.postOptionsScriptComposer = JSON.parse(localStorage.postOptionsScriptComposerIndex)

      if (typeof this.postOptionsScriptComposer[this.outputScript] === 'undefined') {
        this.postOptionsScriptComposer[this.outputScript] = []
      }
      this.$set(this, 'postOptions', this.postOptionsScriptComposer[this.outputScript])
    }
    */
    if (localStorage.preOptionsScriptComposerIndex) {
      this.preOptionsScriptComposer = JSON.parse(localStorage.preOptionsScriptComposerIndex)

      if (typeof this.preOptionsScriptComposer[this.inputScriptComposer] === 'undefined') {
        this.preOptionsScriptComposer[this.inputScriptComposer] = []
      }
      this.$set(this, 'preOptions', this.preOptionsScriptComposer[this.inputScriptComposer])
    }
  },
  updated: function () {
    if (window.innerWidth > document.body.clientWidth) {
      this.scrollExists = true
    } else {
      this.scrollExists = false
    }
    this.convertText = this.$refs.brahmiText.innerText
  },
  watch: {
    outputScript1 (newV, oldV) {
      localStorage.outputScript1 = JSON.stringify(newV)
    },
    sourcePreserveComposer (newV, oldV) {
      localStorage.sourcePreserveComposer = JSON.stringify(newV)
    },
    ignore1 (newV, oldV) {
      localStorage.ignore1 = JSON.stringify(newV)
    },
    ignore2 (newV, oldV) {
      localStorage.ignore2 = JSON.stringify(newV)
    },
    inputScriptComposer (newScript, oldScript) {
      this.inputPast = oldScript
      localStorage.inputScriptComposer = newScript
    },
    outputScript2 (newScript, oldScript) {
      localStorage.outputScript2 = JSON.stringify(newScript)
    },
    preOptions (newOpt, oldOpt) {
      this.preOptionsScriptComposer[this.inputScriptComposer] = newOpt
      localStorage.preOptionsScriptComposerIndex = JSON.stringify(this.preOptionsScriptComposer)

      if (typeof this.preOptionsScriptComposer[this.inputScriptComposer] === 'undefined') {
        this.preOptionsScriptComposer[this.inputScriptComposer] = []
      }

      this.$set(this, 'preOptions', this.preOptionsScriptComposer[this.inputScriptComposer])
    }
  },
  methods: {
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
    downHTML: function (strng) {
      this.downloadHTML(this.$refs.brahmiText.innerHTML)
    },
    newLineBreak: function (strng) {
      strng = strng.replace(/\n/g, '<br/>')

      return strng
    },
    processSplit: function (strng) {
      strng = strng.replace(/\\n+/g, '\n')

      return strng
    },
    choosePS: function (token) {
      if (typeof token['preserveSource'] !== 'undefined') {
        return true
      } else {
        return this.sourcePreserveComposer
      }
    },
    chooseInput: function (token) {
      if (typeof token['inputScript'] !== 'undefined') {
        return token['inputScript'][0]
      } else {
        return this.inputScriptComposer
      }
    },
    chooseTgt: function (token) {
      if (this.ignore2) {
        return ['']
      } else {
        if (typeof token['outputScript'] !== 'undefined') {
          return token.outputScript
        } else {
          if (this.outputScript2.length === 0) {
            return [this.inputScriptComposer]
          } else {
            return this.outputScript2
          }
        }
      }
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
      this.inputScriptComposer = this.inputPast
      this.updateInput()
    },
    updateInput: function () {
      if (typeof this.preOptionsScriptComposer[this.inputScriptComposer] === 'undefined') {
        this.preOptionsScriptComposer[this.inputScriptComposer] = []
      }
      this.$set(this, 'preOptions', this.preOptionsScriptComposer[this.inputScriptComposer])

      if (this.inputScriptComposer === 'Urdu') {
        this.$set(this, 'preOptions', ['UrduShortNotShown'])
      }

      this.convert()
    },
    updateHistOut: function () {
      this.outputScript = this.outputPast
      this.updateOuput()
    },
    updateOuput: function () {
      if (typeof this.postOptionsScriptComposer[this.outputScript] === 'undefined') {
        this.postOptionsScriptComposer[this.outputScript] = []
      }
      this.$set(this, 'postOptions', this.postOptionsScriptComposer[this.outputScript])
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
    sanitize: function (html) {
      return sanitizeHtml(html)
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
      localStorage.postOptionsScriptComposer = JSON.stringify(this.postOptionsScriptComposer)

      console.log('here')

      if (this.outputScript1.length > 1 && !this.ignore1) {
        console.log('returning')
        return
      }

      let lexer = moo.compile({
        secondary: {match: /#[\s\S]+?#/, lineBreaks: true, value: x => x.replace('#', '').replace('#', '')},
        param: {match: /\(.+?\)/, value: x => x},
        paramin: {match: /\[.+?\]/, value: x => x},
        primary: {match: /[\s\S]+?/, lineBreaks: true}
      })

      lexer.reset(this.textInput)

      var tokens = Array.from(lexer)

      this.tokensNew = []

      var text = ''

      for (let i = 0; i < tokens.length; i++) {
        var token = tokens[i]
        if (token.type === 'primary') {
          text += token.value
        } else {
          if (text !== '') {
            this.tokensNew.push({type: 'primary', value: text})
          }
          this.tokensNew.push(token)
          text = ''
        }
      }

      if (text !== '') {
        this.tokensNew.push({type: 'primary', value: text})
      }

      console.log(JSON.stringify(this.tokensNew))

      for (let i = 0; i < this.tokensNew.length; i++) {
        try {
          if (this.tokensNew[i].type === 'param') {
            if (this.tokensNew[i - 1].type === 'secondary') {
              this.tokensNew[i - 1]['outputScript'] = this.tokensNew[i].value.replace('(', '').replace(')', '').split(',').map(x => x.trim())

              if (this.tokensNew[i - 1]['outputScript'] === 'Ignore') {
                this.tokensNew[i - 1]['outputScript'] = ''
              }
              for (let j = 0; j < this.tokensNew[i - 1]['outputScript'].length; j++) {
                console.log(this.tokensNew[i - 1]['outputScript'][j].includes('@PS'))
                if (this.tokensNew[i - 1]['outputScript'][j].includes('@PS')) {
                  this.tokensNew[i - 1]['outputScript'][j] = this.tokensNew[i - 1]['outputScript'][j].replace('@PS', '')
                  this.tokensNew[i - 1]['preserveSource'] = true
                }
              }
            } else if (this.tokensNew[i - 1].type === 'paramin' && this.tokensNew[i - 2].type === 'secondary') {
              console.log('here trying this')

              this.tokensNew[i - 2]['outputScript'] = this.tokensNew[i].value.replace('(', '').replace(')', '').split(',').map(x => x.trim())

              if (this.tokensNew[i - 2]['outputScript'] === 'Ignore') {
                this.tokensNew[i - 2]['outputScript'] = ''
              }

              for (let j = 0; j < this.tokensNew[i - 2]['outputScript'].length; j++) {
                if (this.tokensNew[i - 2]['outputScript'][j].includes('@PS')) {
                  this.tokensNew[i - 2]['outputScript'][j] = this.tokensNew[i - 2]['outputScript'][j].replace('@PS', '')
                  this.tokensNew[i - 2]['preserveSource'] = true
                }
              }
            } else {
              this.tokensNew[i].type = 'primary'
            }
          }
        } catch (e) {
          this.tokensNew[i].type = 'primary'
        }

        try {
          if (this.tokensNew[i].type === 'paramin') {
            if (this.tokensNew[i - 1].type === 'secondary') {
              this.tokensNew[i - 1]['inputScript'] = this.tokensNew[i].value.replace('[', '').replace(']', '').split(',').map(x => x.trim())
            } else {
              this.tokensNew[i].type = 'primary'
            }
          }
        } catch (e) {
          this.tokensNew[i].type = 'primary'
        }
      }

      console.log(JSON.stringify(this.tokensNew))
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
