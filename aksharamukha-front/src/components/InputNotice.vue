<template>
  <span>
      <div class="notice q-ma-sm" v-show="indicSubset.includes(inputScript)">Currently, only the cognate 'Indic' subset of the script is supported for conversion</div>
      <div class="notice q-ma-sm" v-show="inputScript === 'Urdu'">Urdu is an abjad. Please read the script <router-link to="/describe/Urdu">notes</router-link> to read about Urdu reading conventions.</div>
      <div class="notice q-ma-sm" v-show="inputScript === 'Grantha' &&
        preOptions.includes('egrantamil')">This does not use the proper Unicode encoding. Please consider converting the text into Grantha Unicode.</div>
      <div class="notice q-ma-sm" v-show="(outputScript === 'IAST' || outputScript === 'ISO') &&
        postOptions.includes('capitalizeSentence')">To capitalize a specific word, add @ to the beginning of word. e.g. @<transliterate text="buddha" src="HK" :tgt="inputScript"></transliterate></div>
  </span>
</template>

<script>
import {ScriptMixin} from '../mixins/ScriptMixin'
import Transliterate from '../components/Transliterate'

export default {
  // name: 'ComponentName',
  mixins: [ScriptMixin],
  components: {
    Transliterate
  },
  props: ['inputScript', 'outputScript', 'preOptions', 'postOptions'],
  data () {
    return {}
  }
}
</script>

<style scoped>
.notice {
  color: gray;
  font-size: 12px;
}
</style>
