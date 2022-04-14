<template>
  <div>
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
        class="q-ml-sm q-mb-sm q-mt-sm print-hide"
        v-model="preOptions"
        @input="convert"
        :options="typeof preOptionsIndic[inputScript] !== 'undefined' ? preOptionsIndic[inputScript] : []"
        v-show="typeof preOptionsIndic[inputScript] !== 'undefined' && scriptIndicList.includes(outputScript)"
      />
      <q-option-group
        color="dark"
        type="checkbox"
        inline
        class="q-ml-sm q-mb-sm q-mt-sm print-hide"
        v-model="preOptions"
        @input="convert"
        :options="typeof preOptionsSemitic[inputScript] !== 'undefined' ? preOptionsSemitic[inputScript] : []"
        v-show="typeof preOptionsSemitic[inputScript] !== 'undefined' && scriptSemiticListAll.includes(outputScript)"
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
  </div>
</template>

<script>
import {QRadio, QField, QBtnToggle, QToggle, QSelect, QBtn, QOptionGroup, QSlideTransition} from 'quasar'
import Transliterate from '../components/Transliterate'

import {ScriptMixin} from '../mixins/ScriptMixin'

export default {
  // name: 'ComponentName',
  mixins: [ScriptMixin],
  props: ['inputScript', 'outputScript', 'preOptionsInput', 'postOptions'],
  components: {
    QRadio,
    QField,
    QBtnToggle,
    QToggle,
    QSelect,
    QBtn,
    QOptionGroup,
    QSlideTransition,
    Transliterate
  },
  data () {
    return {
      preOptions: []
    }
  },
  mounted: function () {
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
