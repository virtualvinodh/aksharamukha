<template>
  <span>
      <div class="notice q-ma-sm" v-show="indicSubset.includes(inputScript)">Currently, only the cognate 'Indic' subset of the script is supported for conversion</div>
      <div class="notice q-ma-sm" v-show="inputScript === 'Urdu'">Urdu is an abjad. Please read the script <router-link to="/describe/Urdu">notes</router-link> to read about Urdu reading conventions.</div>
      <div class="notice q-ma-sm" v-show="inputScript === 'Arab' || inputScript === 'Arab-Fa' || inputScript === 'Hebr-Ar'">Please note that only the core characters and main vowel diacritics are supported as of now.</div>
      <div class="notice q-ma-sm" v-show="inputScript === 'Syrc'">Please note that only the core characters and the main vowel diacritics are supported as of now.</div>
      <div class="notice q-ma-sm" v-show="inputScript === 'Hebrew' && scriptSemiticList.includes(outputScript)">Please note that only the core characters and the main vowel diacritics are supported as of now.</div>
      <div class="notice q-ma-sm" v-show="inputScript === 'RussianCyrillic'">Only the subset of characters used to transliterate Indic scripts is supported for conversion</div>
      <div class="notice q-ma-sm" v-show="outputScript === 'Tamil' || outputScript === 'TamilExtended'">You can force the use of <span class="tamil">ந</span> in the output by preprending {}. e.g. padma{}netra.</div>
      <div class="notice q-ma-sm" v-show="inputScript === 'Grantha' &&
        preOptions.includes('egrantamil')">This does not use the proper Unicode encoding. Please consider converting the text into Grantha Unicode.</div>
      <div class="notice q-ma-sm" v-show="(outputScript === 'IAST' || outputScript === 'ISO' || outputScript === 'WarangCiti' || outputScript === 'RussianCyrillic' || outputScript === 'RomanReadable'|| outputScript === 'IASTLOC') &&
        postOptions.includes('capitalizeSentence')">To capitalize a specific word, add @ to the beginning of word. e.g. @<transliterate text="buddha" src="HK" :tgt="inputScript"></transliterate></div>
      <div class="notice q-ma-sm" v-show="OCRPerformed">The text has been automatically recognized from the uploaded file. Please proof-read the text for errors,</div>
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
  props: ['inputScript', 'outputScript', 'preOptions', 'postOptions', 'OCRPerformed'],
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
