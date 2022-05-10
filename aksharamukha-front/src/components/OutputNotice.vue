<template>
  <span class="print-hide">
      <div class="notice q-ma-sm" v-show="String(convertText).includes('ஶ')">ஶ is pronounced like a 'soft' ஷ </div>
      <div class="notice q-ma-sm" v-show="String(convertText).includes('ఴ') && !postOptions.includes('TeluguTamilZha')">ఴ is a historic Telugu letter that is equivalent to Tamil ழ/Malayalam ഴ. Your font may not support this character.</div>
      <div class="notice q-ma-sm" v-show="postOptions.includes('TeluguTamilZha') || postOptions.includes('TeluguTamilRra')">You need to use <a href="https://cdn.jsdelivr.net/gh/virtualvinodh/aazhvaar-telugu/AazhvaarTelugu.otf">Aazvhvaar Telugu</a> font to display the Tamil-style letters properly. Without the font, the letters will appear as <span class="telugu">ఴ</span> & <span class="telugu">ౘ</span>.</div>
      <div class="notice q-ma-sm" v-show="postOptions.includes('ThaiNativeConsonants')">You need to use <a href="https://cdn.jsdelivr.net/gh/virtualvinodh/aksharamukha/aksharamukha-front/src/statics/KaccayanaThai.otf">Kaccayana Thai</a> font to display <span class="thainative">ก̥</span> & <span class="thainative">จ̥</span> properly. Without the font, the letters will appear as <span class="thai">ก̥</span> & <span class="thai">จ̥</span>.</div>
      <div class="notice q-ma-sm" v-show="outputScript === 'Kawi'">This only works with Tantular Kawi font and uses Javanese to encode the characters. In the absense of this font, the characters will appear as Javanese.</div>
      <div class="notice q-ma-sm" v-show="outputScript === 'Pallava' && !postOptions.includes('sundapura') && !postOptions.includes('kawitan')">This only works with Purnawarman font and uses Javanese to encode the characters. In the absense of this font, the characters will appear as Javanese.</div>
      <div class="notice q-ma-sm" v-show="outputScript === 'Pallava' && postOptions.includes('sundapura')">This only works with Sundapura font and uses Javanese to encode the characters. In the absense of this font, the characters will appear as Javanese.</div>
      <div class="notice q-ma-sm" v-show="outputScript === 'Pallava' && postOptions.includes('kawitan')">This only works with Kawitan font and uses Javanese to encode the characters. In the absense of this font, the characters will appear as Javanese.</div>
      <div class="notice q-ma-sm" v-show="String(convertText).includes('ഩ') && outputScript === 'Malayalam'">ഩ is a historic Malayalam letter that is equivalent to Tamil ன. Your font may not support this character.</div>
      <div class="notice q-ma-sm" v-show="String(convertText).includes('ఀ')">Your font may not support ఀ the Telugu Chandrabindu character.</div>
      <div class="notice q-ma-sm" v-show="String(convertText).includes('ഀ')">Your font may not support ഀ the Malayalam Anusvara above character. Try enabling traditional orthogrpahy to view the character properly.</div>
      <div class="notice q-ma-sm" v-show="outputScript === 'TamilExtended'">This only works with <a href="https://github.com/virtualvinodh/agastya-tamil-extended/blob/main/agastya_sans.otf?raw=true">Agastya Sans Extended Tamil font</a> and uses Malayalam to encode the characters. In the absense of this font, the characters will appear as Malayalam</div>
      <div class="notice q-ma-sm" v-show="outputScript === 'GranthaPandya'">This only works with e-Pandya font and uses Malayalam codepoints to encode Grantha (Pandya) characters.</div>
      <div class="notice q-ma-sm" v-show="outputScript === 'Grantha' &&
        !postOptions.includes('egrantamil')">This uses a Unicode Grantha font. It can be downloaded from <a href="https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansGrantha/NotoSansGrantha-Regular.ttf?raw=true">here.</a></div>
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
        !postOptions.includes('ranjanawartu')">This uses Devanagari codepoints to encode the characters. Without the specific font, the characters will just appear as Devanagari. Some ligatures/conjuncts used in the font may not be correct.</div>
     <div class="notice q-ma-sm" v-show="outputScript === 'Ranjana' &&
        postOptions.includes('ranjanalantsa')">This uses Tibetan codepoints to encode the characters. Without the specific font, the characters will just appear as Tibetan. Some ligatures/conjuncts used in the font may not be correct.</div>
     <div class="notice q-ma-sm" v-show="outputScript === 'Ranjana' &&
        postOptions.includes('ranjanawartu')">This uses Tibetan codepoints to encode the characters. Without the specific font, the characters will just appear as Tibetan. Some ligatures/conjuncts used in the font may not be correct.</div>
     <div class="notice q-ma-sm" v-show="outputScript === 'KhomThai'">This uses Thai codepoints to encode the characters. Without the specific font, the characters will just appear as Thai.</div>
     <div class="notice q-ma-sm" v-show="(outputScript === 'TaiTham' || outputScript === 'LaoTham' || outputScript === 'LueTham' || outputScript === 'KhuenTham') && postOptions.includes('ThamShiftMaiKangLai')">The font might place Mai Kang Lai on top of the vowel sign instead of the consonant. As in: <span :class="outputScript.toLowerCase()"> ᩈᨥᩘ </span> but <span :class="outputScript.toLowerCase()">ᩈᩉᩮᩣᩘ</span>. This appears to be a font issue. The font should ideally skip the vowel sign and place it directly on top of the consonant</div>
     <div class="notice q-ma-sm" v-show="inputScript === 'Telugu' && inputText.includes('ఁ')">The Arasunna (ఁ) in the input text is being transliterated as Chandrabindu in the output text.</div>
     <div class="notice q-ma-sm" v-show="outputScript === 'Telugu' && postOptions.includes('TeluguReph')">The Reph sign is only currently supported in <a href="https://github.com/googlefonts/noto-fonts/blob/main/hinted/ttf/NotoSansTelugu/NotoSansTelugu-Regular.ttf?raw=true">Noto Sans Telugu</a></div>
     <div class="notice q-ma-sm" v-show="outputScript === 'Mongolian'">The Mongolian mapping for Ali Gali is not yet verified. If you have any feedback on the mapping and the forms of the letters used, please send it to vinodh@virtualvinodh.com</div>
      <div class="notice q-ma-sm" v-show="outputScript === 'Tamil' &&
            String(convertText).includes('𑌃')    ">Grantha Visarga only works with Google's Noto Tamil fonts </div>
      <div class="notice q-ma-sm" v-show="outputScript === 'Tamil' &&
            postOptions.includes('oldtamilortho') ">You can use the <a href="https://www.fontsc.com/font/lohit-tamil-classical">Lohit Tamil Classical</a> font to represent the old orthography for Tamil</div>
      <div class="notice q-ma-sm" v-show="(String(convertText).includes('॒') || String(convertText).includes('᳚') ||
            String(convertText).includes('॑')) && vedicScripts.includes(outputScript)">This text uses Vedic notational marks. Without an appropriate font, the text would not be rendered properly. Look into the individual <router-link :to="'/describe/' + outputScript">script</router-link> page for a working font.</div>

      <div class="notice q-ma-sm" v-show="(String(convertText).includes('𑇌') || String(convertText).includes('𑇋'))">This text uses custom notations to display Kashmiri vowels. The text is best displayed using the Satisar Sharada font.</div>

      <div class="notice q-ma-sm" v-show="(String(inputText).includes('॒') || String(inputText).includes('᳚') ||
            String(inputText).includes('॑')) && !vedicScripts.includes(outputScript)">The input text contains combining Vedic accent marks. These have been replaced with a readable notation.</div>
      <div class="notice q-ma-sm" v-show="inputScript === 'Tamil' && outputScript === 'IPA'">The results displayed have been obtained from <a href="http://anunaadam.appspot.com" target="_blank">Anunaadam</a>. Use the tool for further options.</div>
      <!-- Semitic notices -->
      <div class="notice q-ma-sm" v-show="scriptSemiticList.includes(inputScript) && scriptLatinList.includes(outputScript) &&
      outputScript !== 'Latn'">You're converting from a consonantal Abjad to an Indic romanization scheme. This may result in inclusion of 'a' with every consonant. Please choose Roman (Semitic) to view the appropiate romanization.</div>
      <div class="notice q-ma-sm" v-show="['Urdu', 'Hebrew', 'Punjabi', 'Hebrew'].includes(inputScript) && scriptLatinList.includes(outputScript) &&
      outputScript !== 'Latn'">You're converting from a consonantal Abjad to an Indic romanization scheme. This may result in inclusion of 'a' with every consonant. Please choose Roman (Semitic) to view the appropiate romanization.</div>
      <div class="notice q-ma-sm" v-show="scriptIndicList.includes(inputScript) && scriptSemiticList.includes(outputScript) && !this.localized(outputScript)">You're converting from a vocalized script to a consonantal Abjad. Short vowels will be removed and long vowels will be shown as <i>Mater Lectionis</i>.</div>
      <div class="notice q-ma-sm" v-show="scriptSemiticList.includes(inputScript) && scriptIndicList.includes(outputScript)">You're converting from a consonantal Abjad to a vocalized script. The consonantal skeleton will be padded with an inherent 'a' to aid readability, if no vowels diacritics are present.</div>
      <div class="notice q-ma-sm" v-show="outputScript === 'Latn' && String(convertText).includes('꞉')">꞉ indicates gemination of the preceding consonant. rak꞉a → rakka</div>

  </span>
</template>

<script>
import {ScriptMixin} from '../mixins/ScriptMixin'

export default {
  // name: 'ComponentName',
  mixins: [ScriptMixin],
  props: ['inputScript', 'outputScript', 'postOptions', 'convertText', 'inputText'],
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
