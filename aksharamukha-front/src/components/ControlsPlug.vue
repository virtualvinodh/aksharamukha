<template>
  <div class="bg-grey-2 q-pr-md">
    <q-slide-transition>
    <div v-show="minimize">
    <q-select
        filter
        autofocus-filter
        @input="updateScript"
        filter-placeholder="search"
        v-model="outputScript"
        float-label="Guide Script"
        placeholder="Output Script"
        class="col-xs-6 col-md-6 q-ma-sm"
        :options="scriptsOutput"
      />
    <span v-if="typeof preserveSourceExampleOut[outputScript] !== 'undefined'">
      <q-toggle v-model="sourcePreserve" color="faded"
      @input="update"
      label="Preserve source" left-label class="q-ml-sm q-mb-sm q-mt-sm"/>
      <small><div class="q-ml-sm" v-html="preserveSourceExampleOut[outputScript]"></div></small>
    </span>
      <q-option-group
        color="dark"
        type="checkbox"
        class="q-ml-sm q-mb-sm"
        v-model="postOptions"
        @input="update"
        :options="typeof postOptionsGroup[outputScript] !== 'undefined' ? postOptionsGroup[outputScript] : []"
        v-show="typeof postOptionsGroup[outputScript] !== 'undefined'"
      />
    </div>
    </q-slide-transition>
    <q-btn flat :icon="minimize ? 'call made' : 'call received' " @click="minimize = !minimize" color="dark"/>
    <span class = "demo"></span>

  </div>
</template>

<script>
import {QRadio, QField, QBtnToggle, QToggle, QSelect, QBtn, QOptionGroup, QSlideTransition} from 'quasar'
import {ScriptMixin} from '../mixins/ScriptMixin'

export default {
  // name: 'ComponentName',
  mixins: [ScriptMixin],
  props: ['minimizeO', 'value'],
  components: {
    QRadio,
    QField,
    QBtnToggle,
    QToggle,
    QSelect,
    QBtn,
    QOptionGroup,
    QSlideTransition
  },
  data () {
    return {
      postOptions: [],
      minimize: this.minimizeO,
      advanced: 'false',
      outputScript: '',
      sourcePreserve: false
    }
  },
  mounted: function () {
    console.log(this.value)
    this.outputScript = this.value.script
    this.update()
  },
  methods: {
    updateScript: function () {
      this.postOptions = []
      this.update()
    },
    update: function () {
      var options = {}

      this.postOptions = this.filterRadio(this.postOptions, this.outputScript)

      options['script'] = this.outputScript
      options['sourcePreserve'] = this.sourcePreserve
      options['postOptions'] = this.postOptions

      this.$emit('input', options)
    }
  }
}
</script>

<style scoped>
.demo {
  font-family: Arial;
}
</style>
