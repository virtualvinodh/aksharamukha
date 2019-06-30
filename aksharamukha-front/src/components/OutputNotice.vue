<template>
  <span>
      <div class="notice q-ma-sm" v-show="String(convertText).includes('ஶ')">ஶ is pronounced like a 'soft' ஷ </div>
      <div class="notice q-ma-sm" v-show="String(convertText).includes('ఴ')">ఴ is a historic Telugu letter that is equivalent to Tamil ழ/Malayalam ഴ. Your font may not support this character.</div>
      <div class="notice q-ma-sm" v-show="String(convertText).includes('ഩ')">ഩ is a historic Malayalam letter that is equivalent to Tamil ன. Your font may not support this character.</div>
      <div class="notice q-ma-sm" v-show="String(convertText).includes('ఀ')">Your font may not support ఀ the Telugu Chandrabindu character.</div>
      <div class="notice q-ma-sm" v-show="String(convertText).includes('ഀ')">Your font may not support ഀ the Malayalam Anusvara above character. Try enabling traditional orthogrpahy to view the character properly.</div>
      <div class="notice q-ma-sm" v-show="outputScript === 'TamilGrantha'">This only works with <a href="http://virtualvinodh.com/download/e-Grantamil.ttf">e-Grantamil Font</a> and uses a mixture of Tamil & Bengali codepoints to encode the characters. </div>
      <div class="notice q-ma-sm" v-show="outputScript === 'GranthaPandya'">This only works with e-Pandya font and uses Malayalam codepoints to encode Grantha (Pandya) characters.</div>
      <div class="notice q-ma-sm" v-show="outputScript === 'Grantha' &&
        !postOptions.includes('egrantamil')">This uses a Unicode Grantha font. It can be downloaded from <a href="https://github.com/googlei18n/noto-fonts/tree/master/phaseIII_only/unhinted/otf/NotoSansGrantha">here.</a></div>
      <div class="notice q-ma-sm" v-show="outputScript === 'Grantha' &&
        postOptions.includes('egrantamil')">This does not use the proper Unicode encoding. Please consider disabling the e-Grantamil option and use Grantha Unicode.</div>
      <div class="notice q-ma-sm" v-show="outputScript === 'Vatteluttu'">This only works with e-Vatteluttu OT font and uses Tamil codepoints to encode Vatteluttu characters.</div>
      <div class="notice q-ma-sm" v-show="outputScript === 'Siddham' &&
        postOptions.includes('siddhammukta')">This only works with MuktamSiddham font and uses Devanagari codepoints to encode Siddham characters.</div>
      <div class="notice q-ma-sm" v-show="outputScript === 'Siddham' &&
        postOptions.includes('siddhamap')">This only works with ApDevSiddham  font and uses Devanagari codepoints to encode Siddham characters.</div>
      <div class="notice q-ma-sm" v-show="outputScript === 'Newa' &&
        postOptions.includes('nepaldevafont')">This uses Devanagari codepoints to encode the characters. Without the specific font, the characters will just appear as Devanagari. Please consider using an Unicode font that uses the appropriate Newa (Nepal Lipi) codepoints.</div>
      <div class="notice q-ma-sm" v-show="outputScript === 'Ranjana' &&
        !postOptions.includes('ranjanalantsa') &&
        !postOptions.includes('ranjanawartu')">This uses Devanagari codepoints to encode the characters. Without the specific font, the characters will just appear as Devanagari.</div>
     <div class="notice q-ma-sm" v-show="outputScript === 'Ranjana' &&
        postOptions.includes('ranjanalantsa')">This uses Tibetan codepoints to encode the characters. Without the specific font, the characters will just appear as Tibetan.</div>
     <div class="notice q-ma-sm" v-show="outputScript === 'Ranjana' &&
        postOptions.includes('ranjanawartu')">This uses Tibetan codepoints to encode the characters. Without the specific font, the characters will just appear as Tibetan.</div>
      <div class="notice q-ma-sm" v-show="outputScript === 'Tamil' &&
            String(convertText).includes('𑌃')    ">This only works with Google Noto Tamil fonts </div>
      <div class="notice q-ma-sm" v-show="inputScript === 'Tamil' && outputScript === 'IPA'">The results displayed have been obtained from <a href="http://anunaadam.appspot.com" target="_blank">Anunaadam</a>. Use the tool for further options.</div>
  </span>
</template>

<script>
import {ScriptMixin} from '../mixins/ScriptMixin'

export default {
  // name: 'ComponentName',
  mixins: [ScriptMixin],
  props: ['inputScript', 'outputScript', 'postOptions', 'convertText'],
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
