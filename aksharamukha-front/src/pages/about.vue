<template>
    <q-page padding>
      <q-page-sticky position="top-right">
        <controls v-model="options" :extra="false" :minimizeO="false"> </controls>
      </q-page-sticky>
        <div class="quote q-color-tertiary">
        <div class="q-mb-md">
          <transliterate text='viśvāmitramācāryamevamāha - katamāṃ me bho upādhyāya lipiṃ śikṣāpayasi? brāhmīkharoṣṭīpuṣkarasāriṃ aṅgalipiṃ vaṅgalipiṃ magadhalipiṃ [.. ityādi ..] āsāṃ bho upādhyāya catuṣṣaṣṭīlipīnāṃ katamāṃ tvaṃ śiṣyāpayiṣyasi?' src="IAST" :tgt="options.script" :sourcePreserve="options.sourcePreserve" :postOptions="options.postOptions"> </transliterate>
        </div>
        <div class="q-mb-md">
                [He then] addressed the master Vishvamitra. Which script, O master, will you be teaching me? The Brahmi script, the Kharoshthi script, the Pushkarasari script, the Anga script, the Vanga script, the Magadha script [.. et cetera ..] Master, which of those 64 scripts will you teach me?
        </div>
              <div class=""> — The young Buddha to his teacher (Lalitavistara Sutra) </div>
        </div>
        <div class="q-body-1">Aksharamukha aims to provide script conversion between various scripts within the Indic cultural sphere. These include historic scripts, contemporary Brahmi-derived/inspired scripts, scripts invented for minority Indian languages, scripts that have co-existed with Indic scripts (like Avestan) or linguistically related scripts like Old Persian. It also specifically provides lossless transliteration between the main Indian scripts (along with Sinhala).</div> <br/>

        <div class="q-body-1">Apart from the simple mapping of characters, Askharamukha also attempts to implement various script/language-specific orthographic conventions (where known) such as vowel lengths, gemination and nasalization. It also provides several customization options to fine-tune and get the desired orthography.</div> <br/>

        <div class="q-body-1"><i>Aksharamukha as of now supports <router-link to="/script-matrix">{{scriptsIndic.length + 2}} scripts</router-link> and <router-link to="/roman">{{scriptsLatin.length - 2}} romanization</router-link> methods.</i></div> <br/>

        <div class="q-body-1">The scripts supported are:</div> <br/>

        <div class="q-body-1"><span v-for="script in scriptsIndic.concat([{label: 'Cyrillic (Russian)', value: 'RussianCyrillic'}, {label: 'IPA', value: 'IPA'}])" :key="script.value"> <router-link :to="'/describe/' + script.value">{{script.label}}</router-link>, </span></div> <br/>

        <div class="q-body-1">The Romanization Formats supported are:</div> <br/>

        <div class="q-body-1"><span v-for="script in scriptsRomanization" :key="script.value">{{script.label}}, </span></div> <br/>

        <div class="q-body-1">The source code is released under GNU AGPL and can be found in <a href="https://github.com/virtualvinodh/aksharamukha">Github</a>. Please report any bugs or suggestions over there.</div>

        <div class="q-display-1 q-mt-lg q-mb-md">Donate</div>
        <div class="q-body-1">If you'd like to donate to support and/or appreciate the work, you can send a donation through Paypal.</div>
          <form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top">
          <input type="hidden" name="cmd" value="_s-xclick">
          <input type="hidden" name="hosted_button_id" value="Z4UVDAFR396KC">
          <input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif" border="0" name="submit" alt="PayPal - The safer, easier way to pay online!">
          <img alt="" border="0" src="https://www.paypalobjects.com/en_US/i/scr/pixel.gif" width="1" height="1">
          </form>
        <div class="q-display-1 q-mt-lg q-mb-md">Feedback</div>
        <div class="q-body-1">Please send your feedback/comments to vinodh@virtualvinodh.com</div>

  </q-page>
</template>

<script>
import { QTooltip, QPageSticky } from 'quasar'
import { ScriptMixin } from '../mixins/ScriptMixin'
import Controls from '../components/Controls'
import Transliterate from '../components/Transliterate'

export default {
  // name: 'PageName',
  mixins: [ScriptMixin],
  components: {
    QTooltip,
    Controls,
    Transliterate,
    QPageSticky
  },
  data () {
    return {
      options: {script: 'IAST', sourcePreserve: false}
    }
  }
}
</script>

<style scoped>
.invoc {
  display:inline;
}
.invoc-img {
  margin-top: -30px;
  display:inline-block;
}
@font-face {
  font-family: Adinatha Tamil Brahmi;
  src: url('../statics/AdinathaTamilBrahmi2.otf');
}
@font-face {
  font-family: e-Brahmi T;
  src: url('../statics/e-Brahmi-T.ttf');
}
@font-face {
  font-family: e-Velvi;
  src: url('../statics/e-Velvi.ttf');
}
.quote {
  text-align: left;
  margin-right: 0px;
  --q-color-primary: #777;
  font-style:italic;
  font-size:14px;
  line-height:20px;
}
.scriptlist li {
  float : left;
  margin-right: 40px;
}
</style>
