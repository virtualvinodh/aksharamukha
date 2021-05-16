<template>
  <q-page padding>
    <h5> REST API </h5>
    <h5> How to Use </h5> <br/>
    <p class="q-body-1">In its simplest form, a (GET) request in the following form would work. </p>

    <a href="http://aksharamukha-plugin.appspot.com/api/public?source=HK&target=Telugu&text=buddhaH">http://aksharamukha-plugin.appspot.com/api/public?source=HK&target=Telugu&text=buddhaH</a> <br/><br/>

    <p class="q-body-1">At the minimum, the request needs two parameters: target and text. If the source script is not given, the system will try to auto-detect the script of the text.</p>

    <a href="http://aksharamukha-plugin.appspot.com/api/public?target=IAST&text=ꯃꯤꯇꯩ_ꯃꯌꯦꯛ">http://aksharamukha-plugin.appspot.com/api/public?target=IAST&text=ꯃꯤꯇꯩ_ꯃꯌꯦꯛ</a> <br/><br/>

   <p class="q-body-1">More elaborate transliterations can be performed by passing extra flags as pre-options and post-options</p>

      <a href="http://aksharamukha-plugin.appspot.com/api/public?source=HK&target=Tamil&text=maMgaLa&nativize=false">http://aksharamukha-plugin.appspot.com/api/public?source=HK&target=Tamil&text=maMgaLa&nativize=false</a> <br/><br/>

      <a href="http://aksharamukha-plugin.appspot.com/api/public?source=HK&target=Tamil&text=bRhaspati_gaMgA&nativize=false&postoptions=TamilSubScript,TamilRemoveApostrophe">http://aksharamukha-plugin.appspot.com/api/public?source=HK&target=Tamil&text=bRhaspati_gaMgA&nativize=false&postoptions=TamilSubScript,TamilRemoveApostrophe</a> <br/><br/>

      <a href="http://aksharamukha-plugin.appspot.com/api/public?source=Thai&target=Devanagari&text=พุทธัง%20สะระณัง%20คัจฉามิ&nativize=false&preoptions=ThaiOrthography">http://aksharamukha-plugin.appspot.com/api/public?source=Thai&target=Devanagari&text=พุทธัง%20สะระณัง%20คัจฉามิ&nativize=false&preoptions=ThaiOrthography</a> <br/><br/>

    <p class="q-body-1">Of course, the API supports both GET and POST requests.</p>

    <p class="q-body-1">Please note that all identifiers and parameters are case-sensitive. Hence, only <i>Telugu</i> would work and <i>telugu</i> wouldn't.</p>

    <h5>Parameters</h5>
    <br/>
    <table class="q-body-1">
      <tr>
        <td><b>Parameter</b></td>
        <td><b>Description</b></td>
      </tr>
    <tr>
        <td>source</td>
        <td>Script identifier of the source script</td>
    </tr>
    <tr>
        <td>target</td>
        <td>Script identifier of the target script</td>
    </tr>
    <tr>
        <td>text</td>
        <td>The text to be transliterated</td>
    </tr>
    <tr>
        <td>nativize</td>
        <td>The text is by default nativized in accordance to the conventions of the output script. Set the value to <i>false</i> to prevent this. </td>
    </tr>
    <tr>
        <td>preoptions</td>
        <td>Various options that are relevant to the input text. A comma separated list of strings, the strings being the various options. </td>
    </tr>
    <tr>
        <td>postoptions</td>
        <td>Various options that customize the transliteration output. A comma separated list of strings, the strings being the various options. </td>
    </tr>
    </table> <br/>

    <p class="q-body-1">All script identifiers and the various flags for Pre- and Post-Options are listed in detail <router-link to='/documentation'>here</router-link> along with their description.</p>

    <h5> High Volume Requests </h5> <br/>

    <p class="q-body-1">Please be considerate in your API requests. Please do not use the public API for high volume requests, as you will end up overloading the GAE instance(s) and, eventually, shut it down (as I have a spending limit). I'm not explicitly limiting anything, assuming that people are reasonable entities :) If you'd like to use it for high volume requests, feel free to deploy it in your own server (the code is open source after all) or contact me vinodh@virtualvinodh.com.</p>

  </q-page>
</template>

<script>
import { QTooltip, QPageSticky } from 'quasar'
import { ScriptMixin } from '../mixins/ScriptMixin'

export default {
  // name: 'PageName',
  mixins: [ScriptMixin],
  components: {
    QTooltip,
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
</style>
