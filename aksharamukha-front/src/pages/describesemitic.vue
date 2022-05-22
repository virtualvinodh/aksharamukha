<template>
  <q-page padding>
      <q-page-sticky position="top-right">
      <q-select
        filter
        inset
        autofocus-filter
        filter-placeholder="search"
        placeholder="Input Script"
        float-label="Guide Script"
        v-model="script2"
        class="q-ma-sm col-md-3"
        :options="scriptsOutput"
      />
    </q-page-sticky>
<h4> {{getScriptObject(script1).label}} <q-spinner-comment color="dark" :size="30" v-show="loading"/> </h4>
      <div class="q-body-1" v-html="getDescription(getScriptObject(script1))">
      </div> <br/> <q-chip class="q-ma-xs" color="dark" v-for="tag in tags"
      :key="tag" small tag> {{tag}} </q-chip><br/> <br/>
<q-tabs color="tertiary" no-pane-border inverted position="top">
  <!-- Tabs - notice slot="title" -->
  <q-tab default slot="title" name="tab-1" icon="info" label="Overview" class="print-hide"/> <br/>

  <q-tab-pane name="tab-1" keep-alive>
      <div style="text-align: right">
      <span class="text-red-2"> X</span> : Approximate equivalent <br/>
      <span class="text-blue-4"> Y</span> : Equivalent with diacritic <br/>
      </div>
      <div v-if="getScriptObject(script1).value === 'Hebr'">
        Click here to view the <a href="/describe/Hebrew">Indic mapping</a>.
      </div>
      <div v-if="getScriptObject(script1).value === 'Thaa'">
        Click here to view the <a href="/describe/Thaana">Indic mapping</a>.
      </div>
      <div v-if="getScriptObject(script1).value === 'Arab-Ur'">
        Click here to view the <a href="/describe/Urdu">Indic mapping</a>.
      </div>
      <div v-if="getScriptObject(script1).value === 'Arab-Pa'">
        Click here to view the <a href="/describe/Shahmukhi">Indic mapping</a>.
      </div>
<br/><br/>
  <div class="row">
    <div v-for="(char, index) in script1Chars" :key="char+index" class="col-xs-2 col-lg-1 q-mb-lg letter">
      <span :class="script1.toLowerCase()">
        <span :class="script2Chars[index] !== script1RChars[index] ? 'text-red-2' : 'text-grey-7'">
        <span :class="checkDiacriticsSemitic(char) ? 'text-blue-4' : ''">{{char}}</span> </span>
      </span> <br/><br/>
      <span>
        <span :class="script2.toLowerCase()">
          <span class="letter iast" :class="script1Chars[index] !== script2RChars[index] ? 'text-red-2' : 'text-grey-7'"> {{script2Chars[index]}} <br/><br/>
          </span>
        </span>
      </span>
      <span>
        <!-- <span class="iast text-grey-7">
          <span class="letter"> {{scriptLatnChars[index]}}
          </span>
        </span> -->
      </span>
    </div>
    </div>
    <div v-show="typeof textNative[script1] !== 'undefined'">
        <h5> {{getScriptObject(script1).label}} Text </h5>
    <div v-html="textNative[script1]" :class="script1.toLowerCase()"></div><br/>
        <transliterate :text="textNative[script1]" :src="script1" :tgt="script2" :sourcePreserve="false" :postOptions="[]"
        :preOptions="script1 === 'Urdu' || script1 == 'Shahmukhi'? ['UrduShortNotShown'] : []">
        </transliterate>
      </div>
      <h5> Sample Text </h5>
      <!--<h5> Phoenician Text </h5>
      <transliterate :text="quotePho" src="Phnx" tgt="Latn" :sourcePreserve="false" :postOptions="[]">
      </transliterate><br/><br/>
      <div :class="script2.toLowerCase()"><transliterate :text="quotePho" src="Phnx" :tgt="script2" :sourcePreserve="false" :postOptions="[]">
      </transliterate><br/><br/></div>
      <div :class="script1.toLowerCase()"><transliterate :text="quotePho" src="Phnx" :tgt="script1" :sourcePreserve="false" :postOptions="[]">
      </transliterate></div> -->
      <h5> Aramaic Text </h5>
      <transliterate :text="quoteHe" src="Hebr" :tgt="script2" :sourcePreserve="true" :preOptions="['novowelshebrewSemitic']">
      </transliterate><br/><br/>
      <!-- <div :class="script2.toLowerCase()"><transliterate :text="quoteHe" src="Hebr" :tgt="script2" :sourcePreserve="false" :postOptions="[]">
      </transliterate></div><br/> -->
      <div :class="script1.toLowerCase()"><transliterate :text="quoteHe" src="Hebr" :tgt="script1" :sourcePreserve="false" :preOptions="['novowelshebrewSemitic']">
      </transliterate></div><br/><br/>
      <h5> Sanskrit Text </h5>
      <div :class="script2.toLowerCase()"><transliterate :text="quoteSa" src="HK" :tgt="'IAST'" :sourcePreserve="true" :postOptions="[]">
      </transliterate> </div><br/>
       <div :class="script1.toLowerCase()"><transliterate :text="quoteSa" src="HK" :tgt="script1" :sourcePreserve="false" :postOptions="[]">
      </transliterate></div>

      <div v-if="getScriptObject(script1).font.name !== ''">
      <h5> Font </h5>
      <div class="q-body-1">The font used is {{getScriptObject(script1).font.name}}, which can be downloaded from <a :href="getScriptObject(script1).font.url">here</a>.</div>
      </div>
      <h5> Notes </h5>
      <div class="q-body-1"> The script is an Abjad and does not usually mark vowels. However, long vowels can be represented by a system known as <i>Mater Lectionis</i>. In this system, some consonants can also contextually stand for long owels. In most Abjads, /y/ can stand of /e/ & long /ī/. Similarly, /w/ can stand for /o/ and /ū/. The Aleph may stand for /ā/ following a consonant or to mark initial vowels. This is the system used by Aksharamukha when converting from a vocalized script to an Abjad.</div> <br/>
      <div class="q-body-1">For general character mapping notes, please refer to <router-link to="/semitic-matrix">Semitic Matrix </router-link>.</div><br/>
      <div class="q-body-1" v-html="notes[script1]"> </div>
      <h5 v-if="links[script1]"> Related Links </h5>
      <ol v-if="links[script1]" class="q-body-1">
      <li v-for="link in links[script1]" :key="link"> <a :href="link"> {{link}} </a> </li>
      </ol>
  </q-tab-pane>
</q-tabs>
  </q-page>
</template>

<style scoped>
h4 {
  margin-top: -20px;
}
.letter {
  font-size: 25px;
}
</style>

<script>
import Learncard from '../components/Learncard'
import ListChar from '../components/ListChar'
import Transliterate from '../components/Transliterate'
import Syllabary from '../components/Syllabary'
import Conjuncts from '../components/Conjuncts'

import {ScriptMixin} from '../mixins/ScriptMixin'
import {QPageSticky, QSelect, QSpinnerComment, QTabs, QTab, QTabPane, QRouteTab, QChip} from 'quasar'

var _ = require('underscore')

export default {
  name: 'PageIndex',
  mixins: [ScriptMixin],
  components: {
    QPageSticky,
    QChip,
    Syllabary,
    QSpinnerComment,
    Transliterate,
    Learncard,
    QSelect,
    ListChar,
    QTabs,
    QTab,
    QTabPane,
    QRouteTab,
    Conjuncts
  },
  computed: {
    tags: function () {
      let script = this.getScriptObject(this.script1)
      return script.language.concat(script.invented, script.status, script.region)
    }
  },
  data () {
    return {
      options: {script: 'Latn', sourcePreserve: false},
      dash: _,
      loading: true,
      text: '',
      script1: this.$route.params.script,
      script2: 'Latn',
      quoteSa: 'anirodham anutpAdam anucchedam azAzvatam .\nanekArtham anAnArtham anAgamam anirgamam ..\nyaH pratItyasamutpAdaM prapaJcopazamaM zivam .\ndezayAmAsa saMbuddhastaM vande vadatAM varam ..\n',
      quotePa: 'ye dhammA hetuppabhavA tesaM hetuM tathAgato Aha .\ntesaJca yo nirodho evaM vAdI mahAsamaNo ..\n',
      quotePho: '𐤀𐤍𐤊 𐤕𐤁𐤍𐤕 𐤊𐤄𐤍 𐤏𐤔𐤕𐤓𐤕 𐤌𐤋𐤊 𐤑𐤃𐤍𐤌 𐤁𐤍 𐤀𐤔𐤌𐤍𐤏𐤆𐤓 𐤊𐤄𐤍 𐤏𐤔𐤕𐤓𐤕 𐤌𐤋𐤊 𐤑𐤃𐤍𐤌 𐤔𐤊𐤁 𐤁𐤀𐤓𐤍 𐤆 𐤌𐤉 𐤀𐤕 𐤊𐤋 𐤀𐤃𐤌 𐤀𐤔 𐤕𐤐𐤒 𐤀𐤉𐤕 𐤄𐤀𐤓𐤍 𐤆 𐤀𐤋 𐤀𐤋 𐤕𐤐𐤕𐤇 𐤏𐤋𐤕𐤉 𐤅𐤀𐤋 𐤕𐤓𐤂𐤆𐤍 𐤊 𐤀𐤉 𐤀𐤓𐤋𐤍 𐤊𐤎𐤐 𐤀𐤉 𐤀𐤓 𐤋𐤍 𐤇𐤓𐤑 𐤅𐤊𐤋 𐤌𐤍𐤌 𐤌𐤔𐤃 𐤁𐤋𐤕 𐤀𐤍𐤊 𐤔𐤊𐤁 𐤁𐤀𐤓𐤍 𐤆 𐤀𐤋 𐤀𐤋 𐤕𐤐𐤕𐤇 𐤏𐤋𐤕𐤉 𐤅𐤀𐤋 𐤕𐤓𐤂𐤆𐤍 𐤊 𐤕𐤏𐤁𐤕 𐤏𐤔𐤕𐤓𐤕 𐤄𐤃𐤁𐤓 𐤄𐤀 𐤅𐤀𐤌 𐤐𐤕𐤇 𐤕𐤐𐤕𐤇 𐤏𐤋𐤕𐤉 𐤅𐤓𐤂𐤆 𐤕𐤓𐤂𐤆𐤍 𐤀𐤋 𐤉𐤊𐤍 𐤋𐤊 𐤆𐤓𐤏 𐤁𐤇𐤉𐤌 𐤕𐤇𐤕 𐤔𐤌𐤔 𐤅𐤌𐤔𐤊𐤁 𐤀𐤕 𐤓𐤐𐤀𐤌',
      quoteHe: `שנן י פתיתו עביד זי מראן פרידארש מלכא קשיטא מהקשט   מן אדין זעיר מרעא לכלהם אנשן וכלהם אדושיא הובד  ובכל ארקא ראם שתי ואף זי זנה כמאכלא למראן מלכא זעיר  קטלן זנה למחזה כלהם אנשן אתהחסינן אזי נוניא אחדן  אלך אנשן פתיזבת כנם זי פרבסת הוין אלך אתהחסינן מן  פרבסתי והופתיסתי לאמוהי ולאבוהי ולמזישתיא אנסן  איך אסרהי חלקותא ולא איתי דינא לכלהם אנשיא חסין  זנה הותיר לכלהם אנשן ואוסף יהותר`,
      script1Chars: [],
      script1RChars: [],
      script2Chars: [],
      script2RChars: [],
      scriptLatnChars: [],
      links: {
        'Buginese': ['https://r12a.github.io/scripts/buginese/']
      },
      textNative: {
        'Arab': `بوذا (بالسنسكريتي सिद्धार्थ गौतम) هو مؤسس ديانة أو فلسفة (1) البوذية (وهي أقرب إلى فلسفة الحياة منها إلى الدِّين حيث لا تؤمن بإله، وتقوم على التَّجرُّد والزُّهد تخلُّصًا من الشهوات والألم وطريقًا إلى الفناء التَّام، وتقول بالتَّناسخ ومبدأ السببيَّة، وتنكر البعث والحساب، وهي من أكثر الديانات انتشارًا في الهند والشرق الأقصى)،  ويلفظ اسمه أيضا (بودا (2) أي الساهر أو اليقظ، واسمه بالعربية البد، وفي الفارسية بددة) وبوذا ليس اسم علم على شخص بعينه، وإنما هو لقب ديني عظيم، معناه الحكيم، أو المستنير، أو ذو البصيرة النفاذة، وهو الذي يعلن طريقة خلاص البشر من دائرة الولادة المتكررة (سمسارا) ولكن أتباعه حولوا تعاليمه إلى مبادئ دينية وألهوه، وتذكر الروايات أنه ولد سنة 568 ق م، فيما تذكر أخرى أنه ولد سنة 563 ق. م، في بلدة لومبيني التي تقع حالياً جنوب جمهورية نيبال على الحدود الهندية وكان من أسرة نبيلة، وكان أبوه ملكا صغيرا في تلك البلاد، وقد تربى بوذا في وضع من الرفاهية، وكان يعيش كما يعيش أبناء السادة والملوك في نعيم عظيم. توفيت أمه مايا وهو في السابعة من عمره، فربته عمته وتزوج صغيراً ولما بلغ السادسة والعشرين هجر زوجته إلى الزهد والتقشف والتأمل في الكون وانتهج نهجا خاصاً في الكون ليتخلص الإنسان به من آلامه ودعا إلى ذلك كثيراً من الناس.`,
        'Arab-Fa': `آیین بودا[۱] یا آیین بودایی،[۲] بوداگرایی یا بودیسم (به انگلیسی: Buddhism) یکی از دین‌های هندی با ۵۰۰ میلیون پیرو در سراسر جهان است. این دین برپایه فلسفه‌ای مبتنی بر آموزه‌های سیدارتا گوتاما[۳] که در حدود ۵۶۶ (پیش از میلاد) تا ۴۸۶ (پیش از میلاد) می‌زیسته، بنیان‌گذاری شده است.

آیین بودا به تدریج از هندوستان به سراسر آسیا، آسیای میانه، تبت، سریلانکا، یمن، آسیای جنوب شرقی و نیز کشورهای خاور دور مانند چین، مغولستان، کره و ژاپن راه یافت. آیین بودایی به عنوان دین پاکان[۴] در نظر گرفته می‌شود و با ۵۰۰ میلیون پیرو یکی از ادیان اصلی جهان به‌شمار می‌آید. آیین بودا بیشتر بر کردار نیک، پرهیز از کردار بد و ورزیدگی ذهنی تأکید دارد.

آماج این ورزیدگی‌ها پایان دادن به چرخه تولد مجدد یا سمساره است که از طریق بیداری یا درک واقعیت راستین، رسیدن به رهایی یا نیروانا صورت می‌گیرد. اخلاقیات بودا گرایانه بر دو اصل بی‌گزندی و رواداری برپا شده‌است. آثار نوشتاری بوداگرایی بسیارند و بخش ارزنده‌ای از ادبیات دینی جهان به‌شمار می‌روند.
`,
        'Phnx': '𐤀𐤍𐤊 𐤕𐤁𐤍𐤕 𐤊𐤄𐤍 𐤏𐤔𐤕𐤓𐤕 𐤌𐤋𐤊 𐤑𐤃𐤍𐤌 𐤁𐤍 𐤀𐤔𐤌𐤍𐤏𐤆𐤓 𐤊𐤄𐤍 𐤏𐤔𐤕𐤓𐤕 𐤌𐤋𐤊 𐤑𐤃𐤍𐤌 𐤔𐤊𐤁 𐤁𐤀𐤓𐤍 𐤆 𐤌𐤉 𐤀𐤕 𐤊𐤋 𐤀𐤃𐤌 𐤀𐤔 𐤕𐤐𐤒 𐤀𐤉𐤕 𐤄𐤀𐤓𐤍 𐤆 𐤀𐤋 𐤀𐤋 𐤕𐤐𐤕𐤇 𐤏𐤋𐤕𐤉 𐤅𐤀𐤋 𐤕𐤓𐤂𐤆𐤍 𐤊 𐤀𐤉 𐤀𐤓𐤋𐤍 𐤊𐤎𐤐 𐤀𐤉 𐤀𐤓 𐤋𐤍 𐤇𐤓𐤑 𐤅𐤊𐤋 𐤌𐤍𐤌 𐤌𐤔𐤃 𐤁𐤋𐤕 𐤀𐤍𐤊 𐤔𐤊𐤁 𐤁𐤀𐤓𐤍 𐤆 𐤀𐤋 𐤀𐤋 𐤕𐤐𐤕𐤇 𐤏𐤋𐤕𐤉 𐤅𐤀𐤋 𐤕𐤓𐤂𐤆𐤍 𐤊 𐤕𐤏𐤁𐤕 𐤏𐤔𐤕𐤓𐤕 𐤄𐤃𐤁𐤓 𐤄𐤀 𐤅𐤀𐤌 𐤐𐤕𐤇 𐤕𐤐𐤕𐤇 𐤏𐤋𐤕𐤉 𐤅𐤓𐤂𐤆 𐤕𐤓𐤂𐤆𐤍 𐤀𐤋 𐤉𐤊𐤍 𐤆𐤓𐤏 𐤁𐤇𐤉𐤌 𐤕𐤇𐤕 𐤔𐤌𐤔 𐤅𐤌𐤔𐤊𐤁 𐤀𐤕 𐤓𐤐𐤀𐤌',
        'Hebr': 'וּמֹשֶׁה הָיָה רֹעֶה אֶת צֹאן יִתְרוֹ חֹתְנוֹ כֹּהֵן מִדְיָן וַיִּנְהַג אֶת הַצֹּאן אַחַר הַמִּדְבָּר וַיָּבֹא אֶל הַר הָאֱלֹהִים חֹרֵבָה. וַיֵּרָא מַלְאַךְ יְהֹוָה אֵלָיו בְּלַבַּת אֵשׁ מִתּוֹךְ הַסְּנֶה וַיַּרְא וְהִנֵּה הַסְּנֶה בֹּעֵר בָּאֵשׁ וְהַסְּנֶה אֵינֶנּוּ אֻכָּל. וַיֹּאמֶר אָנֹכִי אֱלֹהֵי אָבִיךָ אֱלֹהֵי אַבְרָהָם אֱלֹהֵי יִצְחָק וֵאלֹהֵי יַעֲקֹב וַיַּסְתֵּר מֹשֶׁה פָּנָיו כִּי יָרֵא מֵהַבִּיט אֶל הָאֱלֹהִים. י וְעַתָּה לְכָה וְאֶשְׁלָחֲךָ אֶל פַּרְעֹה וְהוֹצֵא אֶת עַמִּי בְנֵי יִשְׂרָאֵל מִמִּצְרָיִם. יא וַיֹּאמֶר מֹשֶׁה אֶל הָאֱלֹהִים מִי אָנֹכִי כִּי אֵלֵךְ אֶל פַּרְעֹה וְכִי אוֹצִיא אֶת בְּנֵי יִשְׂרָאֵל מִמִּצְרָיִם. יד וַיֹּאמֶר אֱלֹהִים אֶל מֹשֶׁה אֶהְיֶה אֲשֶׁר אֶהְיֶה וַיֹּאמֶר כֹּה תֹאמַר לִבְנֵי יִשְׂרָאֵל אֶהְיֶה שְׁלָחַנִי אֲלֵיכֶם. טו וַיֹּאמֶר עוֹד אֱלֹהִים אֶל מֹשֶׁה כֹּה תֹאמַר אֶל בְּנֵי יִשְׂרָאֵל יְהוָה אֱלֹהֵי אֲבֹתֵיכֶם אֱלֹהֵי אַבְרָהָם אֱלֹהֵי יִצְחָק וֵאלֹהֵי יַעֲקֹב שְׁלָחַנִי אֲלֵיכֶם זֶה שְּׁמִי לְעֹלָם וְזֶה זִכְרִי לְדֹר דֹּר.',
        'Hebr-Ar': 'יא אבאנא אלדי פי אלסמואת, יתׄקדס אסמך, תׄאתׄי מלכותׄך, תׄכון משיתך כסא פי אלסמא ועלי אלארץ, חבזנא אלדי ללעד אעטנא אליום, ואעפר לנא מא עלינו כמא נעפר נחן לםן לנא עליה, ולא תׄדחלנא אלתׄגארב, לכן נגנא מן אלשריר, לאן לך למלך ואלקות ואלמגד אלי אלאבד.'
      },
      notes: {
        'Arab': 'Though the script is usually an Abjad as noted earlier. It has vocalic diacritical marks that is sometimes used.<br/><br/> Some Arabic dialects also  use the additional letters /ڨ ڤ پ/ to denote the foreign consonants /g v p/ in proper names such places or brands. These letters can be enabled by selecting the <i>Preserve Source</i> option. Else, an etymological approximation to /j f f/ is performed for a Semitic source script and a phonetic approximation to /ġ f b/ for an Indic source script. However, an explicit option can be enabled to use the phonetic mapping instead when converting from a Semitic script.'
      }
    }
  },
  watch: {
    '$route' (to, from) {
      this.script1 = to.params.script
    },
    script1: async function () {
      this.compoundsGen()
    },
    script2: async function () {
      this.compoundsGen()
    }
  },
  mounted: function () {
    this.compoundsGen()
  },
  methods: {
    compoundsGen: async function () {
      this.loading = true
      var data = {
        script1: this.script1,
        script2: this.script2
      }
      var dhis = this
      this.apiCall.post('/describesemitic', data)
        .then(function (response) {
          console.log(response)
          dhis.loading = false
          dhis.$set(dhis, 'script1Chars', response.data['script1'])
          dhis.$set(dhis, 'script1RChars', response.data['script1R'])
          dhis.$set(dhis, 'script2Chars', response.data['script2'])
          dhis.$set(dhis, 'script2RChars', response.data['script2R'])
          dhis.$set(dhis, 'scriptLatnChars', response.data['scriptLatn'])
        })
        .catch(function (error) {
          console.log(error)
        })
    }
  }
}
</script>
