<template>
  <div>
    <div class="col-xs-12 col-md-12 print-hide">
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
        class="q-ml-sm q-mb-sm print-hide"
        v-model="postOptions"
        @input="convert"
        :options="typeof postOptionsGroupSpecific[outputScript+inputScript] !== 'undefined' ? postOptionsGroupSpecific[outputScript+inputScript] : []"
        v-show="typeof postOptionsGroupSpecific[outputScript+inputScript] !== 'undefined'"
      />
    </div>
  </div>
</template>

<script>
import {QRadio, QTooltip, QField, QBtnToggle, QToggle, QSelect, QBtn, QOptionGroup, QSlideTransition} from 'quasar'
import Transliterate from '../components/Transliterate'
import {ScriptMixin} from '../mixins/ScriptMixin'

export default {
  // name: 'ComponentName',
  mixins: [ScriptMixin],
  props: ['inputScript', 'outputScript', 'postOptionsInput', 'convertText'],
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
    QTooltip
  },
  data () {
    return {
      postOptions: this.postOptionsInput
    }
  },
  mounted: function () {
  },
  watch: {
    postOptionsInput: function () {
      this.postOptions = this.postOptionsInput
    }
  },
  methods: {
    convert: function () {
      this.postOptions = this.filterRadio(this.postOptions, this.outputScript)

      // console.log(this.postOptions)
      this.$emit('input', this.postOptions)
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
