<template>
  <!-- Fix Urdu ai and au -->
  <q-page class="q-pa-md">
<q-tabs color="tertiary" no-pane-border animated swipeable inverted position="top">
  <!-- Tabs - notice slot="title" -->
  <q-tab default slot="title" name="tab-1" icon="translate" label="Type" class="print-hide"/>
  <q-tab slot="title" name="tab-2" icon="keyboard" label="Mapping" class="print-hide"/>
  <q-tab slot="title" name="tab-3" icon="settings" label="Settings" class="print-hide" v-if="typeof postOptionsGroup[outputScript] !== 'undefined' || typeof preserveSourceExampleOut[outputScript] !== 'undefined'"/>
  <q-tab slot="title" name="tab-4" icon="font_download" class="print-hide" label="Font" v-if="getScriptObject(outputScript).font.name !== ''"/>
  <q-tab slot="title" name="tab-5" icon="help" label="Help" class="print-hide"/>
    <h5 class="title print-hide"> {{getScriptObject(outputScript).label}} Text Composer : <span :class="getOutputClass(outputScript, postOptions)"> <transliterate text="akSaramukha" src="HK" :tgt="outputScript" sourcePreserve="false">
    </transliterate> </span> </h5>
  <!-- Targets -->
  <q-tab-pane name="tab-1">
    <div class="row">
    <div class="row col-xs-11 col-md-11 col-xl-11 q-ma-md float-div">
  <div class="q-ma-md print-hide" v-if="isIndicScript">
  <span class="q-ma-sm">Keyboard scheme: </span> <q-btn-toggle
  v-model="inputScript"
  @input="compoundsGen"
  toggle-color="dark"
  :options="inputOptions"
  :dense="$q.platform.is.mobile"
  />
</div>
<span class="q-ml-lg"> Use space to trigger conversion <q-toggle class="q-ma-md" v-model="spacetrigger" color="dark"></q-toggle > </span>
  <q-collapsible icon="functions" label="Insert special characters" :opened="false" class="print-hide" v-if="typeof letters[outputScript] !== 'undefined'">
    <div class="print-hide">
<q-btn v-for="letter in letters[outputScript]" :key="letter" class="q-ma-xs" @click.native="insertChar(letter)"> <span :class="getOutputClass(outputScript, postOptions, letter)"> {{letter}} </span> </q-btn>
    </div>
  </q-collapsible>
    <q-input
      autofocus
      v-model="textInput"
      ref="brahmiText"
      type="textarea"
      float-label="Input text"
      class="text-input col-xs-12 col-md-12 q-ma-sm"
      :class="getOutputClass(outputScript, postOptions, textInput)"
      :style="{'font-size': fontSize + '%'}"
      v-on="!spacetrigger ? {input: throttled} : {keyup: convertEnter}"
      clearable
      color="dark"
      rows="10"
      :max-height="1500"
      :loading="loading"
      ></q-input>
    <div class="col-xs-12 col-md-12 q-ma-sm print-hide">
    <output-notice :inputScript="inputScript" :outputScript="outputScript" :postOptions="postOptions"
     :convertText="convertText" :inputText="textInput"></output-notice>
      <q-btn class="q-ma-sm btn print-hide" :data-clipboard-text="convertText.replace(/<br\/>/g, '\n')" @click="copy"> <q-icon name="file copy" /><q-tooltip>Copy text</q-tooltip></q-btn>
      <q-btn class="q-ma-sm print-hide" @click="imageConvert">
        <q-icon name="photo camera" /><q-tooltip>Text screenshot</q-tooltip></q-btn>
      <q-btn class="q-ma-sm print-hide" @click="printDocument"><q-tooltip class="print-hide">Print text</q-tooltip><q-icon name="print" /></q-btn>
      <q-btn class="q-ma-sm print-hide" @click="fontSize += 20"> <q-icon name="zoom in" /><q-tooltip>Increase size</q-tooltip></q-btn>
      <q-btn class="q-ma-sm print-hide" @click="fontSize -= 20"> <q-icon name="zoom out" /><q-tooltip>Decrease size</q-tooltip></q-btn>
      <q-btn class="q-ma-sm print-hide" @click="downloadHTML2"><q-icon name="cloud download"></q-icon> &nbsp; HTML</q-btn>
    <br/> <br/>
    <div class="q-body-1">This is an experimental feature. Please report any feature requests/suggestions/bugs at <a href="https://github.com/virtualvinodh/aksharamukha">Github</a> or alternatively send a mail to vinodh@virtualvinodh.com</div>
    </div>
    </div>
    </div>
  </q-tab-pane>

  <q-tab-pane name="tab-2">
    <h5> Keyboard Mapping </h5>
      <div>
        <div class="row">
          <div v-for="(char, index) in vowels2" :key="char+index" class="col-xs-2 col-lg-1 q-mb-lg">
            <span :class="inputScript.toLowerCase()"> {{char}} </span> <br/>
              <span :class="outputScript.toLowerCase()">
                <span class="letter"> {{vowels1[index]}}
              </span>
            </span>
          </div>
        </div>
        <hr/> <br/>
        <div class="row">
          <div v-for="(char, index) in consonants2" :key="char+index" class="col-xs-2 col-lg-1 q-mb-lg">
            <span :class="inputScript.toLowerCase()"> {{char}} </span> <br/>
              <span :class="outputScript.toLowerCase()">
                <span class="letter"> {{consonants1[index]}}
              </span>
            </span>
          </div>
        </div>
        <hr/> <br/>
        <div class="row">
          <div v-for="(char, index) in compounds2.slice(0,vowels2.length)" :key="char+index" class="col-xs-2 col-lg-1 q-mb-lg">
            <span :class="inputScript.toLowerCase()"> {{char}} </span> <br/>
              <span :class="outputScript.toLowerCase()">
                <span class="letter"> {{compounds1[index]}}
              </span>
            </span>
          </div>
        </div>
        <hr/> <br/>
        <div class="row">
          <div v-for="(char, index) in symbolsI" :key="char+index" class="col-xs-2 col-lg-1 q-mb-lg">
            <span :class="inputScript.toLowerCase()"> {{char}} </span> <br/>
              <span :class="outputScript.toLowerCase()">
                <span class="letter"> {{symbolsO[index]}}
              </span>
            </span>
          </div>
        </div>
      </div>
  </q-tab-pane>

  <q-tab-pane name="tab-3">
    <h5> Settings </h5>
    <span v-if="typeof preserveSourceExampleOut[outputScript] !== 'undefined'">

    <q-toggle color="dark" v-model="sourcePreserve" label="Preserve source" class="q-ml-sm q-mb-sm q-mt-sm print-hide" @input="convert" />
    <small><div class="q-ml-xl" v-html="preserveSourceExampleOut[outputScript]"></div></small>

      <br/>

    </span>

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
  </q-tab-pane>
  <q-tab-pane name="tab-4">
    <div v-if="getScriptObject(outputScript).font.name !== ''">
    <h5> Font </h5>
      <div class="q-body-1">The font used is {{getScriptObject(outputScript).font.name}}, which can be downloaded from <a :href="getScriptObject(outputScript).font.url">here</a>.</div>
    <br/>
    </div>
  </q-tab-pane>
  <q-tab-pane name="tab-5" v-if="isIndicScript">
    <h5> Help </h5>
    <div class="q-body-1">See <router-link :to="'/describe/'+outputScript">here</router-link> for information about the script. The default <i>Aksharaa</i> romanization format is used below.<br/><br/></div>
    <div class="q-body-1"> {} is used to stop conjuncts formation. bud{}dha : <transliterate text="bud{}dha" src="Aksharaa" :tgt="outputScript"></transliterate> :: lak{}shha : <transliterate text="lak{}shha" src="Aksharaa" :tgt="outputScript"></transliterate></div> <br/>
    <div v-if="outputScript === 'Kannada'">
      <div class="q-body-1">Text composer allows you to form several type of variations of vottus. <br/> <ul> <li> kaar()ya : <span class="Kannada">ಕಾರ್‍ಯ</span> as opposed to kaarya : <span class="Kannada">ಕಾರ್ಯ</span></li> <li> kar()ma : <span class="Kannada">ಕರ್‍ಮ</span> as opposed to karma : <span class="Kannada">ಕರ್ಮ</span></li></ul> </div>
    </div>
    <div v-if="outputScript === 'Grantha'">
      <div class="q-body-1">Text composer allows you to form several type of variations of conjuncts. <br/> <ul> <li> san[]ti : <span class="grantha">𑌸𑌨‍𑍍𑌤𑌿</span> as opposed to santi : <span class="grantha">𑌸𑌨𑍍𑌤𑌿</span></li> <li> kar[]ma : <span class="grantha">𑌕𑌰‍𑍍𑌮</span> as opposed to karma : <span class="grantha">𑌕𑌰𑍍𑌮</span></li><li> tat{}param : <span class="grantha">𑌤𑌤𑍍‌𑌪𑌰𑌮𑍍</span> as opposed to tatparam <span class="grantha">𑌤𑌤𑍍𑌪𑌰𑌮𑍍</span></li><li>yyam; : <span class="grantha">𑌯𑍍𑌯𑌁</span></li></ul> </div>
    </div>
    <div v-if="outputScript === 'Devanagari'">
      <div class="q-body-1">Text composer allows you to form several type of variations of conjuncts seamlessly. <br/> <ul> <li> lakshh{}mii : <span class="Devanagari">लक्‌ष्मी</span></li> <li>lakshh()mii : <span class="Devanagari">लक्‍ष्मी</span></li> <li> n() : <span class="Devanagari">न्‍</span> </li> <li> kar()ma : <span class="Devanagari">कर्‍म</span></li> </ul> </div>
    </div>
    <div v-if="outputScript === 'Sinhala'">
      <div class="q-body-1">Text composer allows you to form several type of Sinhala conjuncts seamlessly. <br/> <ul> <li> Touching consonants are formed using []. bud[]dha : <span class="sinhala">බුද‍්ධ</span>.</li> <li> Combining consonats are formed using (). bud()dha : <span class="sinhala">බුද්‍ධ</span>.</li> <li> Conjuncts of /ra/ and /ya/ can be disabled using {}. sat{}ya : <span class="sinhala">සත්‌ය</span>.</li> <li> Repha is formed using r(). kar()ma : <span class="sinhala">කර්‍ම</span> </li> </ul> The above assumes that the 'enable all conjuncts' option is not selected. If it is selected, it will overrride the above options. </div>
    </div>
    <div v-if="outputScript === 'Newa'">
      <div class="q-body-1">Text composer allows you to switch between repha and eye-lash forms of /r/. <br/> <ul> <li> Repha is formed using r[]. kar[]ma : <span class="newa">𑐎𑐬‍𑑂𑐩</span>.</li> <li> The eye-lash form is formed as usual. karma : <span class="newa">𑐎𑐬𑑂𑐩</span>.</li> </ul> The above assumes that the 'Disable Repha' option is selected. If it is not selected, Repha will be formed in all cases overriding all of the above. It will also not work with the Devanagari-based Newa font.</div>
    </div>
    <div v-if="outputScript === 'Saurashtra' && inputScript === 'Tamil'">
      <div class="q-body-1">
      <span class="tamil">நீ: </span>  <span class="saurashtra">ꢥꢴꢷ</span> <br/>
      <span class="tamil">ஸௌராஷ்ட்ர </span>  <span class="saurashtra">ꢱꣃꢬꢵꢰ꣄ꢜ꣄ꢬ</span> <br/>
      <span class="tamil">பு3த்3த4 </span>  <span class="saurashtra">ꢨꢸꢣ꣄ꢤ</span>  </div>
    </div>
    <div v-if="outputScript === 'Saurashtra' && inputScript !== 'Tamil'">
      <div class="q-body-1">
        <b> Aspirated letters with Haaru </b><br/>
        <span class="">nha mha rha lha - </span>  <span class="saurashtra">ꢥꢴ ꢪꢴ ꢬꢴ ꢭꢴ</span> <br/>
      </div>
    </div>
    <br/>
  </q-tab-pane>
</q-tabs>
  <div  class="q-pa-lg" :class="getOutputClass(outputScript, postOptions, textInput)" ref="outputTextImg" v-show="screenshot" v-html="sanitize(textInputHTML)"></div>
  <a :href="brahmiImg" ref="imgDownload" :style="{'display': 'none'}" download="text.png" @click="screenshot=false"><button>Download</button></a>
  </q-page>
</template>

<style>
</style>

<script>
import {QTooltip, QEditor, QRadio, QBtn, QField, QBtnToggle, QToggle, QInput, QSelect, QOptionGroup, QAlert, QSpinnerComment, QTabs, QTab, QTabPane, QRouteTab, QCollapsible} from 'quasar'
import sanitizeHtml from 'sanitize-html'
import html2canvas from 'html2canvas'
import Transliterate from '../components/Transliterate'
import OutputNotice from '../components/OutputNotice'
import { ScriptMixin } from '../mixins/ScriptMixin'
import ScriptMap from '../mixins/script_mapping.json'
import ClipboardJS from 'clipboard'

var _ = require('underscore')

var clipboard = new ClipboardJS('.btn')
console.log(clipboard)

export default {
  name: 'PageIndex',
  mixins: [ScriptMixin],
  components: {
    QAlert,
    OutputNotice,
    Transliterate,
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
    QTabs,
    QTab,
    QTabPane,
    QRouteTab,
    QCollapsible
  },
  data () {
    return {
      textInput: '',
      spacetrigger: false,
      inputOptions: '',
      inputOptionsN: [
        {label: 'Aksharaa', value: 'Aksharaa'},
        {label: 'HK', value: 'HK'},
        {label: 'Itrans', value: 'Itrans'},
        {label: 'Velthuis', value: 'Velthuis'}
      ],
      inputOptionsD: [
        {label: 'Aksharaa', value: 'Aksharaa'},
        {label: 'HK', value: 'HK'},
        {label: 'Itrans', value: 'Itrans'},
        {label: 'Velthuis', value: 'Velthuis'},
        {label: 'Devanagari', value: 'Devanagari'}
      ],
      inputOptionsT: [
        {label: 'Aksharaa', value: 'Aksharaa'},
        {label: 'HK', value: 'HK'},
        {label: 'Itrans', value: 'Itrans'},
        {label: 'Velthuis', value: 'Velthuis'},
        {label: 'Tamil', value: 'Tamil'}
      ],
      screenshot: false,
      symbolsIndic: ['a\\\'', 'a\\"', 'a\\_', '\\m+', '\\m++', '\'', 'oM', '.', '..'],
      symbols: ['\'', 'oM', '.', '..'],
      symbolsI: [],
      symbolsO: [],
      indicSubset: ['TamilGrantha', 'Grantha', 'Assamese', 'Bengali', 'Devanagari', 'Gujarati', 'Gurmukhi', 'Kannada', 'Malayalam', 'Oriya', 'Tamil', 'Telugu'],
      letters: {
        Grantha: ['𑍝', '᳴', '॑', '᳚', 'ᳲ', 'ᳳ', '᳸', '᳹', '᳐', '᳒', '᳓', '⃰', '𑍞', '𑍟', '𑌀', '𑍦', '𑍧', '𑍨', '𑍩', '𑍪', '𑍫', '𑍬', '𑍰', '𑍱', '𑍲', '𑍳', '𑍴'],
        Newa: ['𑑈', '𑑊', '𑑍', '𑑎', '𑑏', '𑑛', '𑑝'],
        Tamil: ['௰', '௱', '௲', '௳', '௴', '௵', '௶', '௷', '௸', '௹', '௺'],
        Devanagari: '꣠꣡꣢꣣꣤꣥꣦꣧꣨꣩꣪꣫꣬꣭꣮꣯꣰꣱ꣲꣳꣴꣵꣶꣷ꣸꣹꣺ꣻ꣼ꣽ᳐᳑᳒᳓᳔᳕᳖᳗᳘᳙᳜᳝᳞᳟᳚᳛᳠᳡᳢᳣᳤᳥᳦᳧᳨ᳩᳪᳫᳬ᳭ᳮᳯᳰᳱᳲᳳ᳴ᳵᳶ᳷᳸᳹'.split(''),
        Sinhala: ['෦', '෧', '෨', '෩', '෪', '෫', '෬', '෭', '෮', '෯', '෴', '𑇡', '𑇢', '𑇣', '𑇤', '𑇥', '𑇦', '𑇧', '𑇨', '𑇩', '𑇪', '𑇫', '𑇬', '𑇭', '𑇮', '𑇯', '𑇰', '𑇱', '𑇲', '𑇳', '𑇴'],
        Siddham: '𑗘 𑗙 𑗚 𑗛 𑗜 𑗝 𑗁 𑗄 𑗅 𑗆 𑗇 𑗈 𑗉 𑗊 𑗋 𑗌 𑗍 𑗎 𑗏 𑗐 𑗑 𑗒 𑗓 𑗔 𑗕 𑗗'.split(' '),
        Tirhuta: '𑒀 𑓅 𑓆'.split(' '),
        Kannada: 'ಆ್ಯ ೱ ೲ ಀ'.split(' '),
        Sharada: '𑇂 𑇃 𑇇 𑇉 𑇍 𑇚 𑇛 𑇜 𑇝 𑇞 𑇟'.split(' '),
        Ahom: '𑜺 𑜻 𑜾 𑜿'.split(' ')
      },
      desc: {
        Grantha: '𑌗𑍍𑌰𑌨𑍍𑌥 𑌲𑌿𑌪𑌿'
      },
      beta: true,
      loading: false,
      model: [],
      inputScript: 'Aksharaa',
      outputScript: this.$route.params.script,
      postOptions: [],
      preOptions: [],
      postOptionsIME: {},
      sourcePreserve: true,
      options: {},
      convertText: '',
      brahmiImg: '',
      fontSize: 100,
      dash: _,
      inputPast: '',
      outputPast: '',
      lineHeight: {
        'Grantha': '2.3em'
      },
      throttled: _.debounce(this.convert, 1000),
      screenshotted: _.debounce(this.imageConvert2, 500),
      vowels1: '',
      vowels2: '',
      consonants1: '',
      consonants2: '',
      textInputOld: '',
      inputDone: false,
      selectionStart: 0
    }
  },
  computed: {
    textInputHTML: function () {
      return this.textInput.replace(/\n/g, '<br/>') + '<br/>'
    },
    isIndicScript: function () {
      return !this.scriptSemiticList.includes(this.outputScript) && this.outputScript !== 'Hebrew'
    }
  },
  mounted () {
    // Also change in Watch ::

    if (this.outputScript === 'Sharada') {
      window.location.replace('https://satisarsharada.appspot.com')
    }

    if (this.outputScript === 'Grantha') {
      window.location.replace('https://granthavarman.appspot.com')
    }

    if (['Grantha', 'Newa', 'Ranjana', 'Tirhuta', 'Siddham'].includes(this.outputScript)) {
      this.inputOptions = this.inputOptionsD
    } else if (['Saurashtra'].includes(this.outputScript)) {
      this.inputOptions = this.inputOptionsT
    } else {
      this.inputOptions = this.inputOptionsN
    }

    if (localStorage.postOptionsIMEIndex) {
      this.postOptionsIME = JSON.parse(localStorage.postOptionsIMEIndex)

      if (typeof this.postOptionsIME[this.outputScript] === 'undefined') {
        this.postOptionsIME[this.outputScript] = []
      }
      this.$set(this, 'postOptions', this.postOptionsIME[this.outputScript])
    }
    if (localStorage.sourcePreserveIME) {
      this.sourcePreserve = JSON.parse(localStorage.sourcePreserveIME)
    }
    if (localStorage.inputScriptIME) {
      this.inputScript = localStorage.inputScriptIME
    }
    if (localStorage.spacetrigger) {
      this.spacetrigger = JSON.parse(localStorage.spacetrigger)
    }

    if (!this.isIndicScript) {
      this.inputScript = 'Type'
    } else {
      this.inputScript = 'Aksharaa'
    }

    this.compoundsGen()
  },
  updated: function () {
    // console.log('The dom is updated ' + this.screenshot)
    if (this.screenshot) {
      this.screenshotted()
    }
    if (typeof this.lineHeight[this.outputScript] !== 'undefined') {
      this.$refs['brahmiText'].$refs.input.style.lineHeight = '2.3em'
    }
    if (this.inputDone) {
      this.$refs['brahmiText'].$refs.input.focus()
      this.$refs['brahmiText'].$refs.input.setSelectionRange(this.selectionStart, this.selectionStart)
      this.inputDone = false
    }
  },
  watch: {
    '$route' (to, from) {
      this.outputScript = to.params.script
      this.textInput = ''

      if (this.outputScript === 'Sharada') {
        window.location.replace('https://satisarsharada.appspot.com')
      }

      if (['Grantha', 'Newa', 'Ranjana', 'Tirhuta', 'Siddham'].includes(this.outputScript)) {
        this.inputOptions = this.inputOptionsD
      } else if (['Saurashtra'].includes(this.outputScript)) {
        this.inputOptions = this.inputOptionsT
      } else {
        this.inputOptions = this.inputOptionsN
      }
      // console.log(this.postOptionsIME)
      this.$set(this, 'postOptions', this.postOptionsIME[this.outputScript])
      // console.log(this.postOptions)

      this.compoundsGen()
    },
    sourcePreserve (newV, oldV) {
      localStorage.sourcePreserveIME = JSON.stringify(newV)
    },
    inputScript (newScript, oldScript) {
      localStorage.inputScriptIME = newScript
    },
    spacetrigger (newVal, oldVar) {
      localStorage.spacetrigger = newVal
    },
    postOptions (newOpt, oldOpt) {
      this.postOptionsIME[this.outputScript] = newOpt
      localStorage.postOptionsIMEIndex = JSON.stringify(this.postOptionsIME)

      if (typeof this.postOptionsIME[this.outputScript] === 'undefined') {
        this.postOptionsIME[this.outputScript] = []
      }

      this.$set(this, 'postOptions', this.postOptionsIME[this.outputScript])
    }
  },
  methods: {
    downloadHTML2: function () {
      this.downloadHTML('<div class="' + this.getOutputClass(this.outputScript, this.postOptions, this.textInput) + '">' + this.textInput.replace(/\n/g, '<br/>') + '</div>')
    },
    convertEnter: function (event) {
      if (event.key === ' ' || event.key === 'Enter') {
        this.convert()
      }
    },
    compoundsGen: async function () {
      this.loading = true
      var data = {
        script1: this.outputScript,
        script2: this.inputScript
      }
      var dhis = this
      if (this.isIndicScript) {
        this.apiCall.post('/syllabary', data)
          .then(function (response) {
            // console.log(response.data)
            dhis.vowels1 = response.data['vowelsScript1']
            dhis.vowels2 = response.data['vowelsScript2']
            dhis.consonants1 = response.data['consonantsScript1']
            dhis.consonants2 = response.data['consonantsScript2']
            dhis.compounds1 = response.data['compoundsScript1']
            dhis.compounds2 = response.data['compoundsScript2']
            dhis.loading = false
            // console.log(dhis.compounds1)
            // console.log(dhis.compounds2)
          })
          .catch(function (error) {
            console.log(error)
          })

        var symbols = this.indicSubset.includes(this.outputScript) ? this.symbolsIndic : this.symbols

        this.symbolsI = await this.convertAsync('HK', 'HK', JSON.stringify(symbols), true, [], [])

        this.symbolsO = await this.convertAsync('HK', this.outputScript, JSON.stringify(symbols), false, [], [])

        this.symbolsO = JSON.parse(this.symbolsO.replace(new RegExp('\\\\', 'g'), ''))
      } else {
        data = {
          script1: this.outputScript === 'Hebrew' ? 'Hebr' : this.outputScript,
          script2: 'Type'
        }
        this.apiCall.post('/describesemitic', data)
          .then(function (response) {
            console.log(response.data)
            dhis.vowels1 = response.data['script1']
            dhis.vowels2 = response.data['script2']
            dhis.consonants1 = []
            dhis.consonants2 = []
            dhis.compounds1 = []
            dhis.compounds2 = []
            dhis.loading = false
            // console.log(dhis.compounds1)
            // console.log(dhis.compounds2)
          })
          .catch(function (error) {
            console.log(error)
          })
      }
    },
    insertChar: function (char) {
      var position = this.$refs['brahmiText'].$refs.input.selectionStart
      this.textInput = [this.textInput.slice(0, position), char, this.textInput.slice(position)].join('')
      this['inputDone'] = true
      this['selectionStart'] = position + char.length
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
    convert: async function () {
      this.convertText += ' . . . '
      if (this.textInput === '' || this.inputScript === '' || this.outputScript === '' ||
        this.inputScript === 'undefined' || this.outputScript === 'undefined') {
        this.convertText = ''
        return
      }
      this.loading = true

      console.log(this.inputScript)
      console.log(this.outputScript)

      // var textDiff = this.textInput.replace(this.textInputOld, '')
      var textInputZ
      if (this.isIndicScript) {
        textInputZ = this.textInput.replace(new RegExp('\u200C', 'g'), '{}')
        var virama = ScriptMap[this.outputScript.toLowerCase()].vowelsigns.virama
        textInputZ = textInputZ.replace(new RegExp('\u200D' + virama, 'g'), virama + '[]')
        textInputZ = textInputZ.replace(new RegExp('\u200D', 'g'), '()')
      } else {
        textInputZ = this.textInput
      }

      var data0 = {
        source: this.outputScript,
        target: this.inputScript,
        text: textInputZ,
        nativize: false,
        postOptions: [],
        preOptions: []
      }

      var dhis = this
      // console.log('Calling with this options')
      // console.log(this.postOptions)
      this.apiCall.post('/convert', data0)
        .then(function (response) {
          dhis.convertText0 = response.data
          dhis.convertText0 = dhis.convertText0.replace(new RegExp('<br/>', 'g'), '\n')

          if (dhis.inputScript === 'Tamil') {
            dhis.preOptions = ['TamilNumeralSub', 'SaurastraHaaruColonTamil']
          } else {
            dhis.preOptions = []
          }

          var data = {
            source: dhis.inputScript,
            target: dhis.outputScript,
            text: dhis.convertText0,
            nativize: !dhis.sourcePreserve,
            postOptions: dhis.postOptions,
            preOptions: dhis.preOptions
          }

          dhis.apiCall.post('/convert', data)
            .then(function (response) {
              dhis.convertText = response.data
              dhis.convertText = dhis.convertText.replace(new RegExp('<br/>', 'g'), '\n')

              if (dhis.inputScript === 'Tamil') {
                dhis.preOptions = ['TamilNumeralSub', 'SaurastraHaaruColonTamil']
              }

              dhis.textInput = dhis.convertText
              dhis.loading = false
            })
            .catch(function (error) {
              console.log(error)
            })
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    imageConvert: function () {
      this.screenshot = true
    },
    imageConvert2: function () {
      var node = this.$refs.outputTextImg
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
            this.convert = false
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

      var cropTop = scanY(true) - 50
      var cropBottom = scanY(false) + 50
      var cropLeft = scanX(true) - 50
      var cropRight = scanX(false) + 50
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
h5.title {
  margin-bottom: -25px;
  margin-top: 10px;
}
</style>
