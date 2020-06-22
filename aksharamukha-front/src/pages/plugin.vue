<template>
  <q-page padding>
    <h5> Web Plugin </h5>
    <div class="q-body-1">Akshramukha is also available as a web plugin. You can see a live demo  at <a href="https://sanskritdocuments.org/doc_ganesha/gajAnanastotram.html">Sanskrit Documents</a> and <a href="http://www.lalitaalaalitah.com/%e0%a4%a6%e0%a5%8d%e0%a4%b5%e0%a4%bf%e0%a4%a4%e0%a5%80%e0%a4%af%e0%a4%be%e0%a4%ad%e0%a4%be%e0%a4%b5%e0%a4%83/">here</a>. It basically attaches itself to the top right corner of a website.</div>

    <div class="q-body-1">It can be added to any site by adding the corresponding javascript file within the HTML document head tag.</div>

    <pre>&lt;script src="https://cdn.jsdelivr.net/gh/virtualvinodh/aksharamukha/aksharamukha-web-plugin/aksharamukha-v3.js"&gt;&lt;/script&gt;</pre>

    <div class="q-body-1">Additionally, the plugin will also load the necessary font files for minority scripts. Hence, any script of your choice should be rendered properly.</div>

    <h5> Additional Instructions </h5>
    <div class="q-body-1">In its simplistic form, you just need to place the script tag as shown above in the head section of your HTML. It will then autodetect the input script and proceed to convert the entire site. However, with mixed content (as it oftens occurs in websites), the autodetection can sometimes fail to detect the source script appropriately. It is suggested you provide the source script along with script file. </div>

    <pre>&lt;script src="http://www.virtualvinodh.com/aksharamkh/aksharamukha-v3.js?source=scriptidentifier"&gt;&lt;/script&gt;</pre>

    <div class="q-body-1">If you'd like to restrict the scripts appearing in the drop-down menu, you need to pass the <i>scriptlist</i> parameter. </div>

    <pre>&lt;script src="http://www.virtualvinodh.com/aksharamkh/aksharamukha-v3.js?scriptlist=Grantha,Kannada"&gt;&lt;/script&gt;</pre>

    <div class="q-body-1">You can also choose one of the pre-filtered options using the parameter <i>prelist</i>.</div>

    <div class="q-body-1">
    <ul>
    <li><i>majorindic:</i> Major Indic Scripts</li>
    <li><i>majorall:</i> All Major Scripts</li>
    <li><i>sansktradall:</i> Scripts traditionally used to write Sanskrit</li>
    <li><i>sanskall:</i> All Scripts capable of writing Sanskrit</li>
    </ul>
    </div>

    <pre>&lt;script src="http://www.virtualvinodh.com/aksharamkh/aksharamukha-v3.js?prelist=sansktradall"&gt;&lt;/script&gt;</pre>

    <div class="q-body-1">You can provide additional preoptions in case, the input needs to be processed differently. For instance, </div>
    <pre>&lt;script src="http://www.virtualvinodh.com/aksharamkh/aksharamukha-v3.js?source=Tamil&preoptions=TamilTranscribe"&gt;&lt;/script&gt;</pre>

    <div class="q-body-1">If you want to restrict the conversion to only some content, you can pass the class name that needs to be converted. </div>

    <pre>&lt;script src="http://www.virtualvinodh.com/aksharamkh/aksharamukha-v3.js?class=classname"&gt;&lt;/script&gt;</pre>

    <div class="q-body-1">You can also have different source scripts in your content. You just need to mark the text appropriately with the classname in the form <i>inputscript-scriptidentifier</i>. You also need to give it a classname marking it for conversion. For instance, </div> <br/>

    <pre>
      &lt;div class="verse inputscript-Telugu">మహాశ్రమణ&lt;/div&gt;
      &lt;div class="verse inputscript-Malayalam">കുസുമിതോ ലക്ഷണൈഃ&lt;/div&gt;
      &lt;div class="verse inputscript-Tamil preoptions-TamilTranscribe">ஆதீஸ்வர் ஸ்ரீவிருஷபநாதர் &lt;/div&gt;
    </pre>

    <div class="q-body-1">The corresponding script would be:</div>
    <pre>&lt;script src="http://www.virtualvinodh.com/aksharamkh/aksharamukha-v3.js?class=verse"&gt;&lt;/script&gt;</pre>

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
      <pre>&lt;script src="http://www.virtualvinodh.com/aksharamkh/aksharamukha-v3.js?class=site-content"&gt; &lt;/script&gt;</pre>
      If you already know the input script, say, Devanagari:<br/>
      <pre>&lt;script src="http://www.virtualvinodh.com/aksharamkh/aksharamukha-v3.js?class=site-content&source=Devanagari"&gt; &lt;/script&gt;</pre> (If your site's wrapper class is not named <i>site-content</i>, replace it with the relevant class name or remove the <i>class</i> parameter altogether)
      The script name needs to be capitalized.
      <li><i>Save Settings</i> at the bottom </li>
    </ol>
    <div class="q-body-1">If you refresh your site, you should be able to see the plugin already activated and working</div>
    </div>
    <h5> CSS Styling </h5>
    <div class="q-body-1">The plugin has minimal stylying to help integrating it to any site. The plugin has been wrapped inside a div with the id <i>aksharamukha-navbar</i>. Any necessary modification to the appearance, should be made to this div id in the CSS.</div>

    <h5>Note</h5>
    <div class="q-body-1">The conversion might be slow as it uses a publicly hosted Google App Engine instance to serve the API requests. Depending upon the volume of requests at a given point, the latency may widely vary. If you would want minimal latency and seamlessly quicker conversion, a better solution would be host a backend server yourself and serve the requests. </div> <br/>

    <div class="q-body-1">If you do need help integrating the plugin to your site, contact me at vinodh@virtualvinodh.com</div>
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
