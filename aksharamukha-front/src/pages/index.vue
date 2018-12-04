<template>
  <!-- Fix Urdu ai and au -->
  <q-page class="q-pa-md">
    <div class="row">
      <div class="row col-xs-12 col-md-11 col-xl-5 q-ma-md float-div print-hide">
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
      <div class="notice q-ma-sm" v-show="indicSubset.includes(inputScript)">Currently, only the cognate 'Indic' subset of the script is supported for conversion</div>
      <q-option-group
        color="dark"
        type="checkbox"
        inline
        class="q-ml-sm q-mb-sm q-mt-sm"
        v-model="preOptions"
        @input="convert"
        :options="typeof preOptionsGroup[inputScript] !== 'undefined' ? preOptionsGroup[inputScript] : []"
        v-show="typeof preOptionsGroup[inputScript] !== 'undefined'"
      />
      <q-option-group
        color="dark"
        type="checkbox"
        inline
        class="q-ml-sm q-mb-sm q-mt-sm"
        v-model="preOptions"
        @input="convert"
        :options="typeof preOptionsGroupSpecific[inputScript+outputScript] !== 'undefined' ? preOptionsGroupSpecific[inputScript+outputScript] : []"
        v-show="typeof preOptionsGroupSpecific[inputScript+outputScript] !== 'undefined'"
      />
      <div class="notice q-ma-sm" v-show="inputScript === 'Urdu'">Urdu is an abjad. Please read the script <router-link to="/describe/Urdu">notes</router-link> to read about Urdu reading conventions.</div>
    </div>
    <div class="q-ma-md print-hide">
      <div class="col">
      <q-btn class="row"> <q-icon name="swap_horiz" @click.native="swap"/> </q-btn>
      <!-- q-spinner-comment color="dark" :size="30" v-show="loading" class="row"/> -->
      </div>
    </div>
    <div class="row col-xs-12 col-md-11 col-xl-5 q-ma-md float-div">
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
    <div
      v-html="sanitize(convertText)"
      ref="brahmiText"
      class="text-output col-xs-12 col-md-12 q-pa-md q-pr-lg bg-grey-1 "
      :class="getOutputClass(outputScript, postOptions)" :style="{'font-size': fontSize + '%'}"
      ></div>
    <div class="col-xs-12 col-md-12 q-ma-sm print-hide">
      <div class="notice q-ma-sm" v-show="String(convertText).includes('ஶ')">ஶ is pronounced like a 'soft' ஷ </div>
      <div class="notice q-ma-sm" v-show="String(convertText).includes('ఴ')">ఴ is a historic Telugu letter that is equivalent to Tamil ழ/Malayalam ഴ. Your font may not support this character.</div>
      <div class="notice q-ma-sm" v-show="String(convertText).includes('ഩ')">ഩ is a historic Malayalam letter that is equivalent to Tamil ன. Your font may not support this character.</div>
      <div class="notice q-ma-sm" v-show="String(convertText).includes('ఀ')">Your font may not support ఀ the Telugu Chandrabindu character.</div>
      <div class="notice q-ma-sm" v-show="String(convertText).includes('ഀ')">Your font may not support ഀ the Malayalam Anusvara above character. Try enabling traditional orthogrpahy to view the character properly.</div>
      <div class="notice q-ma-sm" v-show="outputScript === 'TamilGrantha'">This only works with e-Grantamil Font and uses a mixture of Tamil & Bengali codepoints to encode the characters. </div>
      <div class="notice q-ma-sm" v-show="outputScript === 'GranthaPandya'">This only works with e-Pandya font and uses Malayalam codepoints to encode Grantha (Pandya) characters.</div>
      <div class="notice q-ma-sm" v-show="outputScript === 'Vatteluttu'">This only works with e-Vatteluttu OT font and uses Tamil codepoints to encode Vatteluttu characters.</div>
      <div class="notice q-ma-sm" v-show="outputScript === 'Siddham' &&
        !postOptions.includes('siddhamUnicode')">This only works with MuktamSiddham font and uses Devanagari codepoints to encode Siddham characters.</div>
      <div class="notice q-ma-sm" v-show="outputScript === 'Siddham' &&
        postOptions.includes('siddhamUnicode')">Works only with a Graphite-supporting browser like Firefox.</div>
      <div class="notice q-ma-sm" v-show="outputScript === 'Tamil' &&
            String(convertText).includes('𑌃')    ">This only works with Google Noto Tamil fonts </div>

      <q-toggle color="dark" v-model="sourcePreserve" label="Preserve source" class="q-ml-sm q-mb-sm q-mt-sm print-hide" @input="convert" />
      <br/>
      <q-option-group
        color="dark"
        type="checkbox"
        inline
        class="q-ml-sm q-mb-sm q-mt-sm print-hide"
        v-model="postOptions"
        @input="convert"
        :options="typeof postOptionsGroup[outputScript] !== 'undefined' ? postOptionsGroup[outputScript] : []"
        v-show="typeof postOptionsGroup[outputScript] !== 'undefined'"
      />
      <q-option-group
        color="dark"
        type="checkbox"
        inline
        class="q-ml-sm q-mb-sm q-mt-sm print-hide"
        v-model="postOptions"
        @input="convert"
        :options="typeof postOptionsGroupSpecific[outputScript+inputScript] !== 'undefined' ? postOptionsGroupSpecific[outputScript+inputScript] : []"
        v-show="typeof postOptionsGroupSpecific[outputScript+inputScript] !== 'undefined'"
      />
      <q-btn class="q-ma-sm btn print-hide" :data-clipboard-text="convertText.replace(/<br\/>/g, '\n')" @click="copy"> <q-icon name="file copy" /></q-btn>
      <q-btn class="q-ma-sm print-hide" @click="imageConvert"> <q-icon name="photo camera" /></q-btn>
      <q-btn class="q-ma-sm print-hide" @click="printDocument"> <q-icon name="print" /></q-btn>
      <q-btn class="q-ma-sm print-hide" @click="fontSize += 20"> <q-icon name="zoom in" /></q-btn>
      <q-btn class="q-ma-sm print-hide" @click="fontSize -= 20"> <q-icon name="zoom out" /></q-btn>
    </div>
    </div>
    </div>
  <transition
    enter-active-class="animated fadeIn"
    leave-active-class="animated fadeOut"
    appear
  >
    <div class="q-ma-lg q-body-1">
      This is a new beta version of Aksharamukha. Please report any bugs found in <a href="https://github.com/virtualvinodh/aksharamukha/issues">Github</a>. <br/>The old version is still temporarily available <a href="http://www.virtualvinodh.com/aksharamkh/aksharamukha-old.php">here.</a>.
    </div>
  </transition>
  <a :href="brahmiImg" ref="imgDownload" :style="{'display': 'none'}" download="text.png"><button>Download</button></a>
  </q-page>
</template>

<style>
</style>

<script>
import {QEditor, QRadio, QBtn, QField, QBtnToggle, QToggle, QInput, QSelect, QOptionGroup, QAlert, QSpinnerComment} from 'quasar'
import sanitizeHtml from 'sanitize-html'
import html2canvas from 'html2canvas'
import Controls from '../components/Controls'
import { ScriptMixin } from '../mixins/ScriptMixin'
import ClipboardJS from 'clipboard'

var _ = require('underscore')

var clipboard = new ClipboardJS('.btn')
console.log(clipboard)

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
    QOptionGroup
  },
  data () {
    return {
      textInput: '',
      indicSubset: ['Khmer', 'Burmese', 'Lao', 'Thai', 'Balinese', 'Javanese', 'Tibetan', 'LaoPali', 'TaiTham', 'Cham', 'Lepcha', 'Ahom'],
      beta: true,
      model: [],
      inputScript: '',
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
      throttled: _.debounce(this.convert, 500)
    }
  },
  mounted () {
    if (localStorage.inputScript) {
      this.inputScript = localStorage.inputScript
    }
    if (localStorage.outputScript) {
      this.outputScript = localStorage.outputScript
    }
  },
  watch: {
    inputScript (newScript) {
      localStorage.inputScript = newScript
    },
    outputScript (newScript) {
      localStorage.outputScript = newScript
    }
  },
  methods: {
    updateInput: function () {
      this.$set(this, 'preOptions', [])
      if (this.inputScript === 'Urdu') {
        console.log('here333')
        this.$set(this, 'preOptions', ['UrduShortNotShown'])
      }
      this.convert()
    },
    updateOuput: function () {
      this.$set(this, 'postOptions', [])
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
    convert: function () {
      this.convertText += ' . . . '
      if (this.textInput === '' || this.inputScript === '' || this.outputScript === '') {
        this.convertText = ''
        return
      }
      this.loading = true

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
