<template>
  <div>
  <div class="row">
    <q-select
        filter
        inline
        autofocus-filter
        filter-placeholder="search"
        @input="update2"
        v-model="inputScript"
        placeholder="Input Script"
        class="col-xs-12 col-lg-3 q-ma-md"
        :options="scripts"
      />
    <q-select
        filter
        inline
        @input="update2"
        autofocus-filter
        filter-placeholder="search"
        v-model="outputScript"
        placeholder="Output Script"
        class="col-xs-12 col-lg-3 q-ma-md"
        :options="scriptsOutput"
      />
    <q-toggle v-model="sourcePreserve" @input="update" color="faded"
      label="Preserve source" left-label class="col-lg-2 col-xs-5 q-ma-sm"/>
    </div>
    <div class="row">
      <q-option-group
        color="dark"
        type="checkbox"
        class="col-xs-12 col-lg-3 q-ml-md q-mr-md"
        v-model="preOptions"
        @input="update"
        :options="typeof preOptionsGroup[inputScript] !== 'undefined' ? preOptionsGroup[inputScript] : []"
      />
      <q-option-group
        color="dark"
        type="checkbox"
        class="col-xs-12 col-lg-3 q-ml-md q-mr-md"
        v-model="postOptions"
        @input="update"
        :options="typeof postOptionsGroup[outputScript] !== 'undefined' ? postOptionsGroup[outputScript] : []"
      />
    </div>
    <div class="row">
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
    </div>
  </div>
</template>

<script>
import {QRadio, QField, QBtnToggle, QToggle, QSelect, QBtn, QOptionGroup} from 'quasar'
import {ScriptMixin} from '../mixins/ScriptMixin'

export default {
  // name: 'ComponentName',
  mixins: [ScriptMixin],
  components: {
    QRadio,
    QField,
    QBtnToggle,
    QToggle,
    QSelect,
    QBtn,
    QOptionGroup
  },
  data () {
    return {
      outputScript: '',
      inputScript: '',
      postOptions: [],
      preOptions: [],
      sourcePreserve: false,
      advanced: false
    }
  },
  mounted: function () {
    this.update()
  },
  methods: {
    update2: function () {
      this.$set(this, 'postOptions', [])
      this.$set(this, 'preOptions', [])

      var options = {}

      options['inputScript'] = this.inputScript
      options['outputScript'] = this.outputScript
      options['sourcePreserve'] = this.sourcePreserve
      options['postOptions'] = this.postOptions
      options['preOptions'] = this.preOptions

      this.$emit('input', options)
    },
    update: function () {
      var options = {}

      console.log('here')

      options['inputScript'] = this.inputScript
      options['outputScript'] = this.outputScript
      options['sourcePreserve'] = this.sourcePreserve
      options['postOptions'] = this.postOptions
      options['preOptions'] = this.preOptions

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
