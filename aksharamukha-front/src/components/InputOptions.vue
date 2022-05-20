<template>
      <q-collapsible :sublabel="'<i>Input options (' + preOptionList.length + ')</i>'" icon="settings" dense class="q-mb-xs q-mt-xs"
      :style="{'visibility': preOptionList.length === 0 ? 'hidden' : '', 'display': hideSourcePreserve  && preOptionList.length === 0 ? 'none' : '' }" ref="collapse2"
      >
      <q-option-group
        color="dark"
        type="checkbox"
        inline
        class="q-ml-sm q-mb-sm q-mt-sm"
        v-model="preOptions"
        @input="convert"
        :options="preOptionList"
        v-show="preOptionList.length > 0"
      />
      </q-collapsible>
</template>

<script>
import {QRadio, QField, QBtnToggle, QToggle, QSelect, QBtn, QOptionGroup, QSlideTransition, QCollapsible} from 'quasar'
import Transliterate from '../components/Transliterate'

import {ScriptMixin} from '../mixins/ScriptMixin'

export default {
  // name: 'ComponentName',
  mixins: [ScriptMixin],
  props: ['inputScript', 'outputScript', 'preOptionsInput', 'postOptions', 'hideSourcePreserve'],
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
    QCollapsible
  },
  data () {
    return {
      preOptions: []
    }
  },
  mounted: function () {
  },
  computed: {
    preOptionList: function () {
      var preOptionList = []
      if (typeof this.preOptionsGroup[this.inputScript] !== 'undefined') {
        preOptionList = preOptionList.concat(this.preOptionsGroup[this.inputScript])
      }
      if (typeof this.preOptionsIndic[this.inputScript] !== 'undefined' && this.scriptIndicList.includes(this.outputScript)) {
        preOptionList = preOptionList.concat(this.preOptionsIndic[this.inputScript])
      }
      if (typeof this.preOptionsSemitic[this.inputScript] !== 'undefined' && this.scriptSemiticListAll.includes(this.outputScript)) {
        preOptionList = preOptionList.concat(this.preOptionsSemitic[this.inputScript])
      }
      if (typeof this.preOptionsGroupSpecific[this.inputScript + this.outputScript] !== 'undefined') {
        preOptionList = preOptionList.concat(this.preOptionsGroupSpecific[this.inputScript + this.outputScript])
      }

      if (preOptionList.length === 0) {
        if (typeof this.$refs.collapse !== 'undefined') {
          this.$refs.collapse.hide()
        }
      }

      return preOptionList
    }
  },
  watch: {
    preOptionsInput: function () {
      this.preOptions = this.preOptionsInput
    }
  },
  methods: {
    convert: function () {
      this.$emit('input', this.preOptions)
    }
  }
}
</script>

<style scoped>
.notice {
  color: gray;
  font-size: 12px;
}
</style>
