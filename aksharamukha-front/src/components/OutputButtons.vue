<template>
  <span>
      <q-btn class="q-ma-sm btn print-hide" @click="$emit('copytext')" :data-clipboard-text="convertText.replace(/<br\/>/g, '\n')"> <q-icon name="file copy" /><q-tooltip>Copy converted text</q-tooltip></q-btn>
      <q-btn class="q-ma-sm print-hide" @click="$emit('screenshot')">
        <q-icon name="photo camera" /><q-tooltip>Text screenshot</q-tooltip></q-btn>
      <q-btn class="q-ma-sm print-hide" @click="$emit('printdoc')" v-if="!$q.platform.is.cordova"><q-tooltip class="print-hide">Print text</q-tooltip><q-icon name="print" /></q-btn>
      <q-btn class="q-ma-sm print-hide" @click="$emit('fontsizeinc')"> <q-icon name="zoom in" /><q-tooltip>Increase size</q-tooltip></q-btn>
      <q-btn class="q-ma-sm print-hide" @click="$emit('fontsizedec')"> <q-icon name="zoom out" /><q-tooltip>Decrease size</q-tooltip></q-btn>
      <q-btn class="q-ma-sm print-hide" @click="content" v-if="!$q.platform.is.cordova"><q-icon name="cloud download"></q-icon> &nbsp; HTML</q-btn>
  </span>
</template>

<script>
import ClipboardJS from 'clipboard'
import {QBtn, QTooltip} from 'quasar'

var clipboard = new ClipboardJS('.btn')
console.log(clipboard)

export default {
  // name: 'ComponentName',
  props: ['convertText', 'content'],
  components: {
    QBtn,
    QTooltip
  },
  data () {
    return {}
  }
}
</script>

<style>
</style>
