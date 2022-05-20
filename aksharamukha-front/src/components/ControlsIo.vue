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
    <q-collapsible sublabel="<i>Options</i>" icon="settings" dense class="q-mb-sm q-mt-sm">
          <div class="q-ma-sm" v-if="typeof preOptionsGroup[inputScript] !== 'undefined'"><i>{{inputScript}} options</i></div>
      <q-option-group
        color="dark"
        type="checkbox"
        inline
        v-model="preOptions[inputScript]"
        @input="update"
        :options="typeof preOptionsGroup[inputScript] !== 'undefined' ? preOptionsGroup[inputScript] : []"
      />
      <span v-if="!(outputScript instanceof Array)">
          <div class="q-ma-sm"><i>{{outputScript}} options</i></div>
        <q-option-group
          color="dark"
          type="checkbox"
          inline
          class="col-xs-12 col-lg-3 q-ml-md q-mr-md"
          v-model="postOptions[outputScript]"
          @input="update"
          :options="typeof postOptionsGroup[outputScript] !== 'undefined' ? postOptionsGroup[outputScript] : []"
        />
      </span>
      <span v-else>
        <span v-for="script in outputScript" :key="script" class="col-xs-12 col-lg-3 q-ml-md q-mr-md" v-if="typeof postOptionsGroup[script] !== 'undefined'">
          <div class="q-ma-sm"><i>{{script}} options</i></div>
        <q-option-group
          color="dark"
          type="checkbox"
          inline
          class="col-xs-12 col-lg-3 q-ml-md q-mr-md"
          v-model="postOptions[script]"
          @input="update"
          :options="typeof postOptionsGroup[script] !== 'undefined' ? postOptionsGroup[script] : []"
        />
        </span>
      </span>
      <q-option-group
        color="dark"
        type="checkbox"
        inline
        class="col-xs-12 col-lg-3 q-ml-md q-mr-md"
        v-model="preOptions"
        @input="update"
        :options="typeof preOptionsGroupSpecific[inputScript+outputScript] !== 'undefined' ? preOptionsGroupSpecific[inputScript+outputScript] : []"
      />
      <q-option-group
        color="dark"
        type="checkbox"
        inline
        class="col-xs-12 col-lg-3 q-ml-md q-mr-md"
        v-model="postOptions"
        @input="update"
        :options="typeof postOptionsGroupSpecific[outputScript+inputScript] !== 'undefined' ? postOptionsGroupSpecific[outputScript+inputScript] : []"
      />
    </q-collapsible>
  </div>
</template>

<script>
import {QRadio, QField, QBtnToggle, QToggle, QSelect, QBtn, QOptionGroup, QTooltip, QCollapsible} from 'quasar'
import {ScriptMixin} from '../mixins/ScriptMixin'

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
    QCollapsible
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
