<template>
  <q-page padding>
    <h5> Web Plugin </h5>
    <div class="q-body-1">Akshramukha is also available as a web plugin. You can see a live demo <a href="http://www.virtualvinodh.com/wp/category/blog-tamil/">here</a> (Wordpress) and <a href="http://www.virtualvinodh.com/aksharamkh/demo.html">here</a> (Simple HTML). It basically attaches itself to the right hand corner of the menu.</div>

    <div class="q-body-1">It can be added to any site by adding the corresponding javascript file to the document head</div>
    <pre>&lt;script src="http://www.virtualvinodh.com/aksharamkh/aksharamukha.js"&gt;&lt;/script&gt;</pre>

    <div class="q-body-1">If you'd like to use HTTPS, load it over a CDN from Github directly. All calls within the plugin are already only in HTTPS.</div>
    <pre>&lt;script src="https://cdn.jsdelivr.net/gh/virtualvinodh/aksharamukha/aksharamukha-web-plugin/aksharamukha.js"&gt;&lt;/script&gt;</pre>

    <div class="q-body-1">Additionally, the plugin will also load the necessary font files for minority scripts. Hence, any script of your choice should be rendered propertly</div>

    <h5> Additional Instructions </h5>
    <div class="q-body-1">In its simplistic form, you just need to attach the file as shown above. It will then autodetect the input script and proceed to convert the entire site. However, with mixed content (as it oftens occurs in websites), the autodetection can sometimes fail to detect the source script appropriately. It is suggested you provide the source script along with script file. </div>

    <pre>&lt;script src="http://www.virtualvinodh.com/aksharamkh/aksharamukha.js?source=scriptidentifier"&gt;&lt;/script&gt;</pre>

    <div class="q-body-1">If you'd like to restrict the scripts appearing in the drop-down menu, you need to pass the <i>scriptlist</i> parameter. </div>

    <pre>&lt;script src="http://www.virtualvinodh.com/aksharamkh/aksharamukha.js?scriptlist=Grantha,Kannada"&gt;&lt;/script&gt;</pre>

    <div class="q-body-1">You can provide additional preoptions in case, the input needs to be processed differently. For instance, </div>
    <pre>&lt;script src="http://www.virtualvinodh.com/aksharamkh/aksharamukha.js?source=Tamil&preoptions=TamilTranscribe"&gt;&lt;/script&gt;</pre>

    <div class="q-body-1">If you want to restrict the conversion to only some content, you can pass the class name that needs to be converted. </div>

    <pre>&lt;script src="http://www.virtualvinodh.com/aksharamkh/aksharamukha.js?class=classname"&gt;&lt;/script&gt;</pre>

    <div class="q-body-1">You can also have different source scripts in your content. You just need to mark the text appropriately with the classname in the form <i>inputscript-scriptidentifier</i>. You also need to give it a classname marking it for conversion. For instance, </div> <br/>

    <pre>
      &lt;div class="verse inputscript-Telugu">మహాశ్రమణ&lt;/div&gt;
      &lt;div class="verse inputscript-Malayalam">കുസുമിതോ ലക്ഷണൈഃ&lt;/div&gt;
      &lt;div class="verse inputscript-Tamil preoptions-TamilTranscribe">ஆதீஸ்வர் ஸ்ரீவிருஷபநாதர் &lt;/div&gt;
    </pre>

    <div class="q-body-1">The corresponding script would be:</div>
    <pre>&lt;script src="http://www.virtualvinodh.com/aksharamkh/aksharamukha.js?class=verse"&gt;&lt;/script&gt;</pre>

    <br/><br/>

    <p class="q-body-1">All script identifiers and the various flags for Pre- and Post-Options are listed in detail <router-link to='/documentation'>here</router-link> along with their description.</p>
    <h5>For Wordpress: </h5>
    <div class="q-body-1">To install it in a wordpress site, please follow the following instructions:</div>
    <div class="q-body-1">
    <ol>
      <li><i>Install plugin:</i> Header and Footer Scripts</li>
      <li><i>Activate plugin:</i> if it not yet activated</li>
      <li><i>Go to Settings -></i> Header and Footer Scripts</li>
      <li><i>Enter the following</i> within Scripts in header</li>

      If you want Aksharamukha to autodetect scripts:<br/>
      <pre>&lt;script src="http://www.virtualvinodh.com/aksharamkh/aksharamukha.js?class=site-content"&gt; &lt;/script&gt;</pre>
      If you already know the input script, say, Devanagari:<br/>
      <pre>&lt;script src="http://www.virtualvinodh.com/aksharamkh/aksharamukha.js?class=site-content&source=Devanagari"&gt; &lt;/script&gt;</pre>
      The script name needs to be capitalized.
      <li><i>Save Settings</i> at the bottom </li>
    </ol>
    <div class="q-body-1">If you refresh your site, you should be able to see the plugin already acivated and working</div>
    </div>
    <h5> CSS Styling </h5>
    <div class="q-body-1">The plugin has minimal stylying to help integrating it to any site. The plugin has been wrapped inside a div with the id <i>aksharamukha-navbar</i>. Any necessary modification to the appearance, should be made to this div id in the CSS.</div>

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
  margin-right: 140px;
  --q-color-primary: #777;
}
</style>
