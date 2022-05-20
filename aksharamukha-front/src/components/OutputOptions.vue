<template>
     <q-collapsible :sublabel="label"
         icon="settings" dense class="q-mb-xs q-mt-xs"
        :style="{'visibility': optionCount === 0 ? 'none' : '', 'display': hideSourcePreserve  && optionCount === 0 ? 'none' : ''}" ref="collapse"
     >
    <div class="col-xs-12 col-md-12 print-hide">
      <q-option-group
        color="dark"
        type="checkbox"
        inline
        class="q-ml-sm q-mb-sm q-mt-sm print-hide"
        v-model="postOptions"
        @input="convert"
        :options="postOptionList"
      />
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
      sourcePreserve: this.sourcePreserveInput
    }
  },
  mounted: function () {
  },
  computed: {
    label: function () {
      if (this.showscriptName) {
        return '<i>' + this.outputScript + ' output options (' + this.optionCount + ')</i>'
      } else {
        return '<i>Output options (' + this.optionCount + ')</i>'
      }
    },
    optionCount: function () {
      var optionCount
      if (!this.hideSourcePreserve) {
        optionCount = this.showSourcePreserve + this.postOptionList.length
      } else {
        optionCount = this.postOptionList.length
      }
      return optionCount
    },
    showSourcePreserve: function () {
      var sourcePreserveExists = typeof this.preserveSourceExampleOut[this.outputScript] !== 'undefined'
      var semiticToIndic = (this.scriptSemiticList.includes(this.inputScript) || ['Urdu', 'Thaana', 'Hebrew', 'Shahmukhi', 'Sindhi'].includes(this.inputScript)) && this.scriptIndicList.include(this.outputScript)
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

      // console.log(this.postOptions)
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
