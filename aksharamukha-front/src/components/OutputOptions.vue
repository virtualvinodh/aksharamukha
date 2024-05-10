<template>
     <q-collapsible :sublabel="label"
         icon="settings" dense class="q-mb-xs q-mt-xs print-hide" ref="collapse"
     >
    <div class="col-xs-12 col-md-12 print-hide">
      <q-option-group
        color="dark"
        type="checkbox"
        inline
        class="q-ml-sm q-mt-sm print-hide"
        v-model="postOptions"
        @input="convert"
        :options="postOptionList"
      />
      <span>
        <q-toggle color="dark" v-model="romanNumerals" label="Indo-Arabic numerals" class="q-ml-sm q-mb-sm q-mt-md print-hide" @input="convert" v-if='!romanNumeralScripts.includes(outputScript) &&!transliterationScripts.includes(outputScript)'/><q-tooltip></q-tooltip>
      </span>
      <span>
        <q-toggle color="dark" v-model="indicNumerals" label="Native numerals" class="q-ml-sm q-mb-sm q-mt-md print-hide" @input="convert" v-if='romanNumeralScripts.includes(outputScript)'/>
        <q-tooltip></q-tooltip>
      </span>
      <span>
        <q-toggle color="dark" v-model="indicDandas" label="Use dandas" class="q-ml-sm q-mb-sm q-mt-md print-hide" @input="convert" v-if='romanPunctscripts.includes(outputScript) || transliterationScripts.includes(outputScript) '/>
        <q-tooltip></q-tooltip>
      </span>
      <span>
        <q-toggle color="dark" v-model="romanFullStop" label="Use fullstop" class="q-ml-sm q-mb-sm q-mt-md print-hide" @input="convert" v-if='!romanPunctscripts.includes(outputScript) && !transliterationScripts.includes(outputScript)'/>
        <q-tooltip></q-tooltip>
      </span>
    </div>
      <span v-if="showSourcePreserve && !hideSourcePreserve">
        <span>
            <q-toggle color="dark" v-model="sourcePreserve" label="Preserve source" class="q-ml-sm q-mb-sm q-mt-md print-hide" @input="convert" /><q-tooltip>Preserve the source as-is and don't change the text to improve readability. May use archaic characters and/or diacritics. <br/><br/><div v-if="scriptSemiticList.includes(inputScript) || ['Urdu', 'Thaana', 'Hebrew', 'Shahmukhi', 'Sindhi'].includes(inputScript)">This also preserves the semitic consonants using the nukta (if present in the output script).</div></q-tooltip>
        </span>
        <small><div class="q-ml-xl print-hide" v-html="preserveSourceExampleOut[outputScript]"></div></small>
      </span>
     </q-collapsible>
</template>

<script>
import {QRadio, QTooltip, QField, QBtnToggle, QToggle, QSelect, QBtn, QOptionGroup, QSlideTransition, QCollapsible} from 'quasar'
import Transliterate from '../components/Transliterate'
import {ScriptMixin} from '../mixins/ScriptMixin'

export default {
  // name: 'ComponentName',
  mixins: [ScriptMixin],
  props: ['inputScript', 'outputScript', 'postOptionsInput', 'convertText', 'sourcePreserveInput', 'hideSourcePreserve', 'showscriptName'],
  components: {
    QRadio,
    QField,
    QBtnToggle,
    QToggle,
    QSelect,
    QBtn,
    QOptionGroup,
    QSlideTransition,
    Transliterate,
    QTooltip,
    QCollapsible
  },
  data () {
    return {
      postOptions: this.postOptionsInput,
      sourcePreserve: this.sourcePreserveInput,
      romanNumerals: this.postOptionsInput.includes('romanNumerals'),
      romanFullStop: this.postOptionsInput.includes('romanFullStop'),
      indicNumerals: this.postOptionsInput.includes('indicNumerals'),
      indicDandas: this.postOptionsInput.includes('indicDandas')
    }
  },
  mounted: function () {
  },
  updated: function () {
    this.romanNumerals = this.postOptionsInput.includes('romanNumerals')
    this.romanFullStop = this.postOptionsInput.includes('romanFullStop')
    this.indicNumerals = this.postOptionsInput.includes('indicNumerals')
    this.indicDandas = this.postOptionsInput.includes('indicDandas')
  },
  computed: {
    activeOptionsCount: function () {
      let count
      count = this.postOptions.length + this.sourcePreserve
      return count
    },
    label: function () {
      if (this.showscriptName) {
        return '<i>' + this.outputScript + ' output options (' + this.optionCount + ')</i> : ' + this.activeOptionsCount + ' active'
      } else {
        return '<i>Output options (' + this.optionCount + ')</i> : ' + this.activeOptionsCount + ' active'
      }
    },
    optionCount: function () {
      var optionCount
      if (!this.hideSourcePreserve) {
        optionCount = this.showSourcePreserve + this.postOptionList.length
      } else {
        optionCount = this.postOptionList.length
      }
      var numeralsDandas = (!this.romanNumeralScripts.includes(this.outputScript) && !this.transliterationScripts.includes(this.outputScript)) + this.romanNumeralScripts.includes(this.outputScript) + (this.romanPunctscripts.includes(this.outputScript) || this.transliterationScripts.includes(this.outputScript)) + (!this.romanPunctscripts.includes(this.outputScript) && !this.transliterationScripts.includes(this.outputScript))

      return optionCount + numeralsDandas
    },
    showSourcePreserve: function () {
      var sourcePreserveExists = typeof this.preserveSourceExampleOut[this.outputScript] !== 'undefined'
      var semiticToIndic = (this.scriptSemiticList.includes(this.inputScript) || ['Urdu', 'Thaana', 'Hebrew', 'Shahmukhi', 'Sindhi'].includes(this.inputScript)) && this.scriptIndicList.includes(this.outputScript)
      return sourcePreserveExists || semiticToIndic
    },
    postOptionList: function () {
      var postOptionList = []
      if (typeof this.postOptionsGroup[this.outputScript] !== 'undefined') {
        postOptionList = postOptionList.concat(this.postOptionsGroup[this.outputScript])
      }
      if (typeof this.postOptionsIndic[this.outputScript] !== 'undefined' && this.scriptIndicList.includes(this.inputScript)) {
        postOptionList = postOptionList.concat(this.postOptionsIndic[this.outputScript])
      }
      if (typeof this.postOptionsSemitic[this.outputScript] !== 'undefined' && this.scriptSemiticListAll.includes(this.inputScript)) {
        postOptionList = postOptionList.concat(this.postOptionsSemitic[this.outputScript])
      }
      if (typeof this.postOptionsGroupSpecific[this.outputScript + this.inputScript] !== 'undefined') {
        postOptionList = postOptionList.concat(this.postOptionsGroupSpecific[this.outputScript + this.inputScript])
      }

      return postOptionList
    }
  },
  watch: {
    optionCount (newV, oldV) {
      if (newV === 0) {
        if (typeof this.$refs.collapse !== 'undefined') {
          this.$refs.collapse.hide()
        }
      }
    },
    postOptionsInput: function () {
      this.postOptions = this.postOptionsInput
    },
    sourcePreserveInput: function () {
      this.sourcePreserve = this.sourcePreserveInput
    }
  },
  methods: {
    convert: function () {
      this.postOptions = this.filterRadio(this.postOptions, this.outputScript)

      if (this.romanNumerals && !this.postOptions.includes('romanNumerals')) {
        this.postOptions = this.postOptions.concat(['romanNumerals'])
      }
      if (!this.romanNumerals) {
        this.postOptions = this.postOptions.filter(item => item !== 'romanNumerals')
      }
      if (this.indicNumerals && !this.postOptions.includes('indicNumerals')) {
        this.postOptions = this.postOptions.concat(['indicNumerals'])
      }
      if (!this.indicNumerals) {
        this.postOptions = this.postOptions.filter(item => item !== 'indicNumerals')
      }
      if (this.indicDandas && !this.postOptions.includes('indicDandas')) {
        this.postOptions = this.postOptions.concat(['indicDandas'])
      }
      if (!this.indicDandas) {
        this.postOptions = this.postOptions.filter(item => item !== 'indicDandas')
      }
      if (this.romanFullStop && !this.postOptions.includes('romanFullStop')) {
        this.postOptions = this.postOptions.concat(['romanFullStop'])
      }
      if (!this.romanFullStop) {
        this.postOptions = this.postOptions.filter(item => item !== 'romanFullStop')
      }

      console.log(this.postOptions)
      if (!this.hideSourcePreserve) {
        this.$emit('input', [this.postOptions, this.sourcePreserve])
      } else {
        this.$emit('input', this.postOptions)
      }
    }
  }
}
</script>

<style scoped>
.notice {
  color: gray;
  font-size: 12px;
}
.float-div {
  display: inline-block;
  float: left;
}
</style>
