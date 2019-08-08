<template>
  <q-page padding>
    <h5> Python package</h5>
    <h5> How to Use </h5> <br/>
    <p class="q-body-1">Install, Aksharamukha from pip </p>

    <span class="code">pip install aksharamukha</span><br/><br/>

    <span class="code">from aksharamukha import transliterate</span> <br/> <br/>

    <hr/>

    <span class="code">transliterate(src, tgt, txt, nativize = True, pre_options = [], post_options = [])</span><br/><br/>
    <table class="q-body-1">
      <tr>
        <td><b>Parameter</b></td>
        <td><b>Description</b></td>
      </tr>
    <tr>
        <td>src</td>
        <td>Script identifier of the source script</td>
    </tr>
    <tr>
        <td>tgt</td>
        <td>Script identifier of the target script</td>
    </tr>
    <tr>
        <td>txt</td>
        <td>The text to be transliterated</td>
    </tr>
    <tr>
        <td>nativize</td>
        <td>The text is by default nativized in accordance to the conventions of the output script. Set the value to <i>False</i> to prevent this. </td>
    </tr>
    <tr>
        <td>pre_options</td>
        <td>Various options that are relevant to the input text. An array of strings, the strings being the various options.</td>
    </tr>
    <tr>
        <td>post_options</td>
        <td>Various options that customize the transliteration output. An array of strings, the strings being the various options.</td>
    </tr>
    </table> <br/>

    <hr/> <br/>

    <span class="code">transliterate.process('HK', 'Telugu', 'buddhaH')</span> <br/> <br/>

    <p class="q-body-1">If the source script is not known, set it as <i>autodetect</i></p>

    <span class="code">transliterate.process('autodetect', 'IAST', 'ꯃꯤꯇꯩ_ꯃꯌꯦꯛ')</span><br/><br/>

    <span class="code">transliterate.process('autodetect', 'IAST', 'พุทธัง สะระณัง คัจฉามิ')</span><br/><br/>

    <p class="q-body-1">You can also just use auto_detect to find the script of a text.</p>

    <span class="code">transliterate.auto_detect('ꯃꯤꯇꯩ_ꯃꯌꯦꯛ')</span><br/><br/>

    <p class="q-body-1">More elaborate transliterations can be performed by passing extra flags as pre-options and post-options</p>

    <span class="code">transliterate.process('HK', 'Tamil', 'maMgaLa', False)</span> <br/><br/>

    <span class="code">transliterate.process('HK', 'Tamil', 'bRhaspati gaMgA', False, post_options = ['TamilSubScript','TamilRemoveApostrophe'])</span> <br/><br/>

    <span class="code">transliterate.process('Thai', 'Devanagari', 'พุทธัง สะระณัง คัจฉามิ', pre_options=['ThaiOrthography'])</span> <br/><br/>

    <span class="code">transliterate.process('Devanagari', 'IAST', 'धर्म भारत की श्रमण परम्परा से निकला धर्म और दर्शन है', pre_options=['RemoveSchwaHindi'])</span> <br/><br/>

    <p class="q-body-1">Please note that all identifiers and parameters are case-sensitive. Hence, only <i>Telugu</i> would work and <i>telugu</i> wouldn't.</p>

    <p class="q-body-1">All script identifiers and the various flags for Pre- and Post-Options are listed in detail <router-link to='/documentation'>here</router-link> along with their description.</p>
  </q-page>
</template>

<script>
import { QTooltip, QPageSticky } from 'quasar'
import { ScriptMixin } from '../mixins/ScriptMixin'
import Transliterate from '../components/Transliterate'

export default {
  // name: 'PageName',
  mixins: [ScriptMixin],
  components: {
    QTooltip,
    Transliterate,
    QPageSticky
  },
  data () {
    return {
    }
  }
}
</script>

<style scoped>
h6 {
  margin-bottom: -10px;
}
h5 {
  margin-bottom: -10px;
}
table, td {
  border: 0.5px solid;
  border-collapse: collapse;
}
td {
  padding: 10px;
}
.code {
  font-family: Courier New;
}
</style>
