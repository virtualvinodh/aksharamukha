<template>
    <span v-if="$q.platform.is.desktop" class="print-hide">
     <q-btn-group>
        <q-btn color="grey-8" :flat="!(highlight == 'texts')" icon="notes" label="Text" to="/converter"/>
        <q-btn color="grey-8" :flat="!(highlight == 'composer')" icon="language" label="Multi-Script" to="/composer" />
        <q-btn color="grey-8" :flat="!(highlight == 'files')" icon="cloud upload" label="Files" to="/upload/"/>
        <q-btn color="grey-8" :flat="!(highlight == 'websites')" icon="web" label="Websites" to="/website/" />
      </q-btn-group>
      </span>
      <span v-else>
        <q-btn color="grey-8" :flat="!(highlight == 'texts')"  icon="notes" to="/converter"/>
        <q-btn color="grey-8" :flat="!(highlight == 'composer')" icon="language" to="/composer"/>
        <q-btn color="grey-8" :flat="!(highlight == 'files')" icon="cloud upload" to="/upload"/>
        <q-btn color="grey-8" :flat="!(highlight == 'websites')" icon="web" to="/website"/>
      </span>
</template>

<script>
import {QBtn, QBtnGroup} from 'quasar'

export default {
  // name: 'ComponentName',
  props: ['highlight'],
  components: {
    QBtn,
    QBtnGroup
  },
  data () {
    return {}
  }
}
</script>

<style>
</style>
