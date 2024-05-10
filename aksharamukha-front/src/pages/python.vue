<template>
  <q-page padding>
    <h5> Python package</h5>
    <h5> How to Use </h5> <br/>
    <p class="q-body-1">Install, Aksharamukha from pip </p>

    <span class="code">pip install aksharamukha</span><br/><br/>

    <span class="code">from aksharamukha import transliterate</span> <br/> <br/>

    <hr/>

    <span class="code">transliterate.process(src, tgt, txt, nativize = True, pre_options = [], post_options = [])</span><br/><br/>
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

    <p class="q-body-1">Instead of using Aksharamukha's identifiers, you can also the respective ISO codes (<a href="https://en.wikipedia.org/wiki/ISO_15924">ISO 15924</a> for scripts and <a href="https://en.wikipedia.org/wiki/ISO_639-1">ISO 639-1</a> or <a href="https://en.wikipedia.org/wiki/ISO_639-2">ISO 639-1</a> for languages). </p>

    <span class="code"> transliterate.process('deva', 'taml', 'धर्म भारत की ', param="script_code") </span><br/><br/>
    <span class="code"> transliterate.process('te', 'ur', 'ధర్మ భారత', param="lang_code")</span> <br/><br/>
    <span class="code"> transliterate.process('odia', 'ho', 'ଧର୍ମ ଭାରତ', param="lang_name")</span> <br/><br/>

    <p class="q-body-1"> You would need to use the format <i>lang_code-script_code</i> to use scripts that have multiple orthographies (e.g. Arabic script for Urdu and Punjabi) or languages that can be written in multiple scripts (e.g. Punjabi written in Gurmukhi and Shahmukhi). For romanization, you can use the language code <i>la-romanization_format</i> or the script code <i>latn-romanization_format</i> as input. </p>

    <span class="code">transliterate.process('autodetect', 'latn-iast', 'धर्म भारत की ', param="script_code")</span> <br/><br/>
    <span class="code">transliterate.process('autodetect', 'pa-arab', 'धर्म भारत की ', param="script_code")</span> <br/><br/>
    <span class="code">transliterate.process('la-HK', 'pa-guru', 'namo buddhAya', param="lang_code")</span> <br/><br/>

    <p class="q-body-1">All script identifiers and the various flags for Pre- and Post-Options are listed in detail <router-link to='/documentation'>here</router-link> along with their description.</p>

    <p class="q-body-1">You can also convert files (.docx, .html & .txt) as shown below.</p>
    <span class="code"> from aksharamukha import transliterate_file</span> <br/><br/>
    <span class="code"> transliterate_file.process(tgt, src, file_path, nativize=True, pre_options=[], post_options=[])</span> <br/><br/>

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
