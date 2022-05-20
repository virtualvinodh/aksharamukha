<template>
  <div>
  <div class="row">
    <q-select
        filter
        inline
        autofocus-filter
        filter-placeholder="search"
        @input="update"
        v-model="inputScript"
        placeholder="Input Script"
        class="col-xs-11 col-lg-3 q-ma-md"
        :options="inputindic ? scriptsIndic: scripts"
      />
    <q-select
        filter
        inline
        :multiple="multiple"
        @input="update"
        autofocus-filter
        filter-placeholder="search"
        v-model="outputScript"
        placeholder="Output Script"
        class="col-xs-11 col-lg-3 q-ma-md"
        :options="scriptsOutput"
      />

      <span class="col-lg-2 col-xs-5 q-ma-lg">
        <q-toggle v-model="sourcePreserve" @input="update" color="faded"
        label="Preserve source" left-label /><q-tooltip>Preserve the source as-is and don't change the text to improve readability</q-tooltip>
      </span>

    </div>
    <input-options :inputScript="inputScript" :outputScript="outputScript[0]" :preOptionsInput="preOptions[inputScript]"
    :hideSourcePreserve="true"
      v-model="preOptions[inputScript]" @input="update"></input-options>
      <span v-if="!(outputScript instanceof Array)">
    <output-options :inputScript="inputScript" :outputScript="outputScript" :postOptionsInput="postOptions[outputScript]"
        :hideSourcePreserve="true" @input="update"
        v-model="postOptions[outputScript]"></output-options>
      </span>
      <span v-else>
        <span v-for="script in outputScript" :key="script">
          <output-options :inputScript="inputScript" :outputScript="script" :postOptionsInput="postOptions[script]"
       :hideSourcePreserve="true" :showscriptName="true" @input="update"
        v-model="postOptions[script]"></output-options>
        </span>
      </span>
  </div>
</template>

<script>
import {QRadio, QField, QBtnToggle, QToggle, QSelect, QBtn, QOptionGroup, QTooltip, QCollapsible} from 'quasar'
import {ScriptMixin} from '../mixins/ScriptMixin'
import InputOptions from '../components/InputOptions'
import OutputOptions from '../components/OutputOptions'

export default {
  // name: 'ComponentName',
  mixins: [ScriptMixin],
  props: ['multiple', 'inputindic'],
  components: {
    QRadio,
    QField,
    QBtnToggle,
    QToggle,
    QSelect,
    QBtn,
    QOptionGroup,
    QTooltip,
    QCollapsible,
    InputOptions,
    OutputOptions
  },
  data () {
    return {
      outputScript: this.multiple ? [] : '',
      inputScript: '',
      postOptions: this.multiple ? {} : [],
      preOptions: [],
      sourcePreserve: false,
      advanced: false
    }
  },
  mounted: function () {
    this.update()
    for (var i = 0; i < this.scriptsOutput.length; i++) {
      this.$set(this.postOptions, this.scriptsOutput[i].value, [])
    }
    for (i = 0; i < this.scriptsOutput.length; i++) {
      this.$set(this.preOptions, this.scriptsOutput[i].value, [])
    }
  },
  methods: {
    update: function () {
      console.log('here updating the thigns')
      var options = {}

      if (!this.multiple) {
        options['inputScript'] = this.inputScript
        options['outputScript'] = this.outputScript
        options['sourcePreserve'] = this.sourcePreserve
        options['postOptions'] = this.postOptions[this.outputScript]
        options['preOptions'] = this.preOptions[this.inputScript]
      } else {
        options['inputScript'] = this.inputScript
        options['outputScript'] = this.outputScript
        options['sourcePreserve'] = this.sourcePreserve
        options['postOptions'] = this.postOptions
        options['preOptions'] = this.preOptions
      }

      console.log(options)

      this.$emit('input', options)
    }
  }
}
</script>

<style scoped>
.vinodh {
  font-family: calibri;
}
</style>
