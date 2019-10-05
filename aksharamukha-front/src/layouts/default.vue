<template>
  <q-layout view="hHr Lpr fFf">
    <q-window-resize-observable @resize="onResize" />

    <q-layout-header class="print-hide">
      <q-toolbar
        color="dark"
      >
        <q-btn
          flat
          dense
          round
          aria-label="Menu"
          @click.native="leftDrawerOpen = !leftDrawerOpen"
        >
          <q-icon name="menu" />

        </q-btn>

        <q-btn
          round
          size="xl"
          text-color="white"
          color="#5D8D89"
          to ="/converter"
        >
         <!-- <span class="khraoshthi-title">𐨐  </span> -->
         <span class="title-ka">A</span>
       </q-btn>
        <q-toolbar-title>
          Aksharamukha : Script Converter <br/>
          <span><transliterate text="akSaramukha" src="HK" :tgt="randomScript.value" sourcePreserve="false">
            </transliterate>             <q-tooltip>{{randomScript.label}}</q-tooltip> </span>
        </q-toolbar-title>

      </q-toolbar>
    </q-layout-header>

    <q-layout-drawer
      ref="drawer"
      v-model="leftDrawerOpen"
      side="left"
      :width="230"
      :content-class="$q.theme === 'mat' ? 'bg-grey-2' : null"
      class=""
    >
      <q-list
        no-border
        link
        inset-delimiter
      > <!-- link to other tools -->
        <!-- Options to create pseudo epigraphs -->
        <!-- Icon -->
        <q-item to="/converter">
          <q-item-side icon="translate"/>
          <q-item-main label="Converter"/>
        </q-item>
        <q-item to="/composer">
          <q-item-side icon="language" />
          <q-item-main label="Composer (Multiple scripts)"/>
        </q-item>
        <q-item to="/website/">
          <q-item-side icon="web" />
          <q-item-main label="Convert Websites"/>
        </q-item>
        <q-item to="/upload/">
          <q-item-side icon="cloud upload" />
          <q-item-main label="Convert Files (Batch)"/>
        </q-item>
        <q-collapsible icon="keyboard" label="Input (Beta)" >
            <q-item :to="'/input/Devanagari'">
              <q-item-main label="Devanagari"/>
            </q-item>
             <q-item :to="'/input/Grantha'">
              <q-item-main label="Grantha"/>
            </q-item>
            <q-item :to="'/input/Kannada'">
              <q-item-main label="Kannada"/>
            </q-item>
            <q-item :to="'/input/Ranjana'">
              <q-item-main label="Ranjana"/>
            </q-item>
            <q-item :to="'/input/Siddham'">
              <q-item-main label="Siddham"/>
            </q-item>
            <q-item :to="'/input/Sinhala'">
              <q-item-main label="Sinhala"/>
            </q-item>
            <q-item :to="'/input/Tamil'">
              <q-item-main label="Tamil"/>
            </q-item>
            <q-item :to="'/input/TamilGrantha'">
              <q-item-main label="Tamil (with full Grantha"/>
            </q-item>
             <q-item :to="'/input/Tirhuta'">
              <q-item-main label="Tirhuta (Maithili)"/>
            </q-item>
             <q-item :to="'/input/Newa'">
              <q-item-main :label="'Newa (Nepal Bhasa)'"/>
            </q-item>
        </q-collapsible>
        <hr/>
        <q-collapsible icon="book" label="Sample Texts"  >
            <q-item :to="'/texts/' + text.path" v-for="text in texts" :key="text.path">
              <q-item-main :label="text.name"/>
            </q-item>
        </q-collapsible>
        <q-collapsible icon="edit" label="Scripts" >
            <q-item to="/roman">
              <q-item-main label="Roman Transliteration Schemes"/>
            </q-item>
            <q-item :to="'/describe/' + script.value" v-for="script in scriptsIndic" :key="script.value">
              <q-item-main :label="script.label"/>
            </q-item>
            <q-item :to="'/describe/RussianCyrillic'">
              <q-item-main :label="'Cyrillic (Russian)'"/>
            </q-item>
            <q-item :to="'/describe/IPA'">
              <q-item-main :label="'IPA'"/>
            </q-item>
        </q-collapsible>
        <q-item to="/script-matrix">
          <q-item-side icon="table chart" />
            <q-item-main label="Script Matrix"/>
          </q-item>
        <q-item to="/rosetta-stone">
          <q-item-side icon="view column" />
            <q-item-main label="Rosetta Stone"/>
          </q-item>
        <hr/>
        <q-collapsible icon="build" label="Technical" >
          <q-item to="/web-api">
            <q-item-main label="Web API" />
          </q-item>
          <q-item to="/python">
            <q-item-main label="Python package" />
          </q-item>
          <q-item to="/documentation">
            <q-item-main label="Documentation" />
          </q-item>
          <q-item to="/plugin">
            <q-item-main label="Website Plugin" />
          </q-item>
        <q-item to="/help">
            <q-item-main label="Help" />
        </q-item>
          </q-collapsible>
         <q-item to="/about">
          <q-item-side icon="info" />
          <q-item-main label="About"/>
        </q-item>
        <q-collapsible icon="developer board" label="Other Tools">
            <q-item @click.native="openURL('http://tamiljinavani.appspot.com')" link>
              <q-item-main label="Jinavani" />
            </q-item>
            <q-item @click.native="openURL('http://www.avalokitam.com')" link>
              <q-item-main label="Avalokitam" />
            </q-item>
            <q-item @click.native="openURL('http://www.anunaadam.appspot.com')" link>
              <q-item-main label="Anunaadam" />
            </q-item>
        </q-collapsible>
      </q-list>
      <br/>
<social-sharing url="http://aksharamukha.appspot.com"
                      title="Aksharamukha"
                      description="Indic Script Converter"
                      quote="Try out this Indic Script Converter and convert between 75 scripts"
                      hashtags="scripts, indic, orthography, brahmic, writing system, unicode"
                      inline-template>
  <div class="social">
      <network network="facebook" class="q-ma-md cursor-pointer">
        <img src="../statics/facebook.svg" width="20px">
      </network>
      <network network="whatsapp" class="q-ma-md mobile-only">
        <img src="../statics/whatsapp.svg" width="20px">
      </network>
      <network network="twitter" class="q-ma-md cursor-pointer">
        <img src="../statics/twitter.svg" width="20px">
      </network>
  </div>
</social-sharing>
    </q-layout-drawer>
    <q-page-container class="page">
      <br/>
      <div :class="$q.platform.is.mobile ? 'alert2': 'alert'" v-if="visibleAlert">
      <q-alert
          color="grey-7"
          icon="favorite"
          appear
          :actions="[{ label: 'Dismiss', handler: hideAlert }]"
          class="q-mb-sm"
        > Like Aksharamukha? Consider <a href="https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=LRY7AE7SXDHTN&source=url">supporting</a> it! </q-alert>
      </div>
      <router-view/>
    </q-page-container>
    <q-layout-footer v-show="showFooter" class="print-hide">
        <q-toolbar color="tertiary" class="footer-quote">
          © 2018 <a href="http://www.virtualvinodh.com">Vinodh Rajan</a>&nbsp;&nbsp;&nbsp;vinodh@virtualvinodh.com. This software is released under GNU AGPL 3.0 license.
          <q-btn
          round
          size="md"
          text-color="white"
          color="dark"
          class="print-only q-ml-sm q-mr-sm"
        >
          <!-- <vatteluttu text="ஶ்ரீ" class="demo1"> </vatteluttu> -->
          </q-btn>
          <div class="print-only">
            Aksharamukha <br/>
            http://aksharamukha.appspot.com
          </div>
        </q-toolbar>
    </q-layout-footer>

  </q-layout>
</template>

<script>
import { openURL, QLayoutFooter, QTooltip, QWindowResizeObservable, QCollapsible, QAlert } from 'quasar'
import Transliterate from '../components/Transliterate'
import SocialSharing from 'vue-social-sharing'
import {ScriptMixin} from '../mixins/ScriptMixin'

export default {
  name: 'LayoutDefault',
  mixins: [ScriptMixin],
  components: {
    QLayoutFooter,
    QAlert,
    QTooltip,
    Transliterate,
    QWindowResizeObservable,
    QCollapsible,
    SocialSharing
  },
  data () {
    return {
      leftDrawerOpen: true,
      showFooter: true,
      randomScript: '',
      visibleAlert: true,
      texts: [
        {
          name: 'Triratnanusmriti Sutra',
          path: 'triratnanusmriti'
        },
        {
          name: 'Khuddaka Patha',
          path: 'khuddakapatha'
        },
        {
          name: 'Dhammachakkappavattana Sutra',
          path: 'dhammachakka'
        },
        {
          name: 'Lalitavistara Sutra',
          path: 'lalitavistara'
        },
        {
          name: 'Panchavimsatisahasrika Prajnaparamita Sutra',
          path: 'panchavimsati'
        },
        {
          name: 'Heart Sutra',
          path: 'heart'
        },
        {
          name: 'Lotus Sutra',
          path: 'lotus'
        },
        {
          name: 'Nilakantha Dharani',
          path: 'nilakantha'
        },
        {
          name: 'Karanda Mudra Dharani',
          path: 'karanda'
        },
        {
          name: 'Ushnisha Vijaya Dharani',
          path: 'ushnisha'
        }
      ]
    }
  },
  created: function () {
    this.randomScript = this.scriptRandom()
  },
  mounted: function () {
    if (localStorage.visibleAlert) {
      this.visibleAlert = JSON.parse(localStorage.visibleAlert)
    }
  },
  methods: {
    openURL,
    hideAlert: function () {
      this.visibleAlert = false
      localStorage.visibleAlert = JSON.stringify(this.visibleAlert)
    },
    onResize: function (size) {
      if (size.width < 992) {
        this.showFooter = false
      } else {
        this.showFooter = true
      }
    }
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Mukta+Malar&subset=latin-ext,tamil');
@import url('https://fonts.googleapis.com/css?family=Padauk&display=swap');

.alert {
  width: 460px;
}

.alert a:link {
  color:white;
}

.alert a:visited {
  color:white;
}

.alert2 a:link {
  color:white;
}

.alert2 a:visited {
  color:white;
}

.donate {
  display: inline-block;
}

.footer-img {
  height: 20px;
}
.footer-quote {
  font-size: 12px;
}
.page {
  margin-left: 10px;
}
.footer-quote {
  text-align: right;
  float:center;
}
.quotef {
  float: center;
}
.demo1 {
    color: white;
    background-color: #424242;
    text-shadow: 0px 1px 0px rgba(0,0,0,.5);
}
.social {
  text-align: center;
}
.q-body-1 {
  line-height: 1.75em;
}
@font-face {
  font-family: 'Noto Sans Tamil';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansTamil/NotoSansTamil-Regular.otf')
}
@font-face {
  font-family: 'Noto Sans Saurashtra';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansSaurashtra/NotoSansSaurashtra-Regular.otf')
}
@font-face {
  font-family: 'Noto Serif Bali';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSerifBalinese/NotoSerifBalinese-Regular.otf')
}
@font-face {
  font-family: 'e-Grantamil';
  src: url('../statics/e-Grantamil.ttf')
}
@font-face {
  font-family: 'Noto Sans Javanese';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansJavanese/NotoSansJavanese-Regular.otf')
}
@font-face {
  font-family: 'Noto Sans Khojki';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansKhojki/NotoSansKhojki-Regular.otf')
}
@font-face {
  font-family: 'Noto Sans Avestan';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansAvestan/NotoSansAvestan-Regular.otf')
}
@font-face {
  font-family: 'Noto Sans Buginese';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansBuginese/NotoSansBuginese-Regular.otf')
}
@font-face {
  font-family: 'Noto Sans Tagalog';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansTagalog/NotoSansTagalog-Regular.otf')
}
@font-face {
  font-family: 'Noto Sans Malayalam';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansMalayalam/NotoSansMalayalam-Regular.otf')
}
@font-face {
  font-family: 'Noto Sans Tagbanwa';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansTagbanwa/NotoSansTagbanwa-Regular.otf')
}
@font-face {
  font-family: 'Noto Sans Sundanese';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansSundanese/NotoSansSundanese-Regular.otf')
}
@font-face {
  font-family: 'Noto Sans Cham';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansCham/NotoSansCham-Regular.otf')
}
@font-face {
  font-family: 'Noto Sans Chakma';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansChakma/NotoSansChakma-Regular.otf')
}
@font-face {
  font-family: 'Noto Sans Telugu';
  src: url('../statics/Lohit-Telugu.ttf')
}
@font-face {
  font-family: 'Noto Sans Batak';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansBatak/NotoSansBatak-Regular.otf')
}
@font-face {
  font-family: 'Noto Sans Lepcha';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansLepcha/NotoSansLepcha-Regular.otf')
}
@font-face {
  font-family: 'Noto Sans Limbu';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansLimbu/NotoSansLimbu-Regular.otf')
}
@font-face {
  font-family: 'Noto Sans Meetei Mayek';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansMeeteiMayek/NotoSansMeeteiMayek-Regular.otf')
}
@font-face {
  font-family: 'Noto Sans Nastaliq Urdu';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoNastaliqUrdu/NotoNastaliqUrdu-Regular.otf')
}
@font-face {
  font-family: 'Noto Serif Gujarati';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSerifGujarati/NotoSerifGujarati-Regular.otf')
}
@font-face {
  font-family: 'Noto Sans Khmer';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSerifKhmer/NotoSerifKhmer-Regular.otf')
}
@font-face {
  font-family: 'Noto Sans OldPersian';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansOldPersian/NotoSansOldPersian-Regular.otf')
}
@font-face {
  font-family: 'Noto Sans Sinhala';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansSinhala/NotoSansSinhala-Regular.otf')
}
@font-face {
  font-family: 'Noto Sans Kannada';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansKannada/NotoSansKannada-Regular.otf')
}
@font-face {
  font-family: 'Noto Sans Tai Tham';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/unhinted/NotoSansTaiTham-Regular.ttf')
}
@font-face {
  font-family: 'Noto Sans Grantha2';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansGrantha/NotoSansGrantha-Regular.otf')
}
@font-face {
  font-family: 'Muktamsiddham';
  src: url('../statics/Muktamsiddham.otf')
}
@font-face {
  font-family: 'MuktamsiddhamG';
  src: url('../statics/MuktamsiddhamG.ttf')
}
@font-face {
  font-family: 'ApDevaSiddham';
  src: url('../statics/ApDevaSiddham.ttf')
}
@font-face {
  font-family: 'Nepal2';
  src: url('../statics/Nepal-lipi2.woff')
}
@font-face {
  font-family: 'BabelStoneZanabazar';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansZanabazarSquare/NotoSansZanabazarSquare-Regular.otf')
}
@font-face {
  font-family: 'Adinatha Tamil Brahmi';
  src: url('../statics/AdinathaTamilBrahmi2.otf')
}
@font-face {
  font-family: 'Kharoshthi Ka';
  src: url('../statics/ka-khar.otf')
}
@font-face {
  font-family: 'Meera';
  src: url('../statics/Meera-Regular.ttf')
}
@font-face {
  font-family: 'Lao Pali';
  src: url('../statics/Lanexang_Mon4.otf')
}
@font-face {
  font-family: 'MithilaUni';
  src: url('../statics/MithilaUni.ttf')
}
@font-face {
  font-family: 'e-Vatteluttu';
  src: url('../statics/e-VatteluttuOT.ttf')
}
@font-face {
  font-family: 'e-Pandya';
  src: url('../statics/e-Pandya.ttf')
}
@font-face {
  font-family: 'JMYZK--LZT Lantsa';
  src: url('../statics/JMYZK--LZT.ttf')
}
@font-face {
  font-family: 'JMYZK--WDT Wartu';
  src: url('../statics/JMYZK--WDT.ttf')
}
@font-face {
  font-family: 'PaliTilok';
  src: url('../statics/Pali_Tilok.ttf')
}
@font-face {
  font-family: 'Lamphun';
  src: url('../statics/Pali_Khottabun.ttf')
}
@font-face {
  font-family: 'Tibetan Dbu Med';
  src: url('../statics/Qomolangma-Betsu.ttf')
}
@font-face {
  font-family: 'Patimokkha';
  src: url('../statics/Patimokkha.ttf')
}
@font-face {
  font-family: 'Ariyaka';
  src: url('../statics/ariyaka.ttf')
}
@font-face {
  font-family: 'AnnaPurna';
  src: url('../statics/AnnapurnaSIL-TT-Regular.ttf')
}
@font-face {
  font-family: 'Noto Sans Modi';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansModi/NotoSansModi-Regular.otf')
}
@font-face {
  font-family: 'Noto Sans Multani';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansMultani/NotoSansMultani-Regular.otf')
}
@font-face {
  font-family: 'Noto Sans SoraSompeng';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansSoraSompeng/NotoSansSoraSompeng-Regular.otf')
}
@font-face {
  font-family: 'Noto Sans Mahajani';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansMahajani/NotoSansMahajani-Regular.otf')
}
@font-face {
  font-family: 'Noto Sans Kaithi';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansKaithi/NotoSansKaithi-Regular.otf')
}
@font-face {
  font-family: 'Noto Sans Tirhuta';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansTirhuta/NotoSansTirhuta-Regular.otf')
}
@font-face {
  font-family: 'Noto Sans Takri';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansTakri/NotoSansTakri-Regular.otf')
}
@font-face {
  font-family: 'Noto Sans SylotiNagri';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansSylotiNagri/NotoSansSylotiNagri-Regular.otf')
}
@font-face {
  font-family: 'Noto Sans Newa';
  src: url('https://cdn.jsdelivr.net/gh/googlefonts/noto-fonts/phaseIII_only/unhinted/otf/NotoSansNewa/NotoSansNewa-Regular.otf');
}
@font-face {
  font-family: 'Noto Sans Sharada';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansSharada/NotoSansSharada-Regular.otf')
}
@font-face {
  font-family: 'Noto Sans Bhaiksuki';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansBhaiksuki/NotoSansBhaiksuki-Regular.otf')
}
@font-face {
  font-family: 'Noto Sans Khudawadi';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansKhudawadi/NotoSansKhudawadi-Regular.otf')
}
@font-face {
  font-family: 'Noto Serif Ahom';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSerifAhom/NotoSerifAhom-Regular.otf')
}
@font-face {
  font-family: 'Noto Sans Siddham';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansSiddham/NotoSansSiddham-Regular.otf')
}
@font-face {
  font-family: 'Noto Sans Brahmi';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansBrahmi/NotoSansBrahmi-Regular.otf')
}
@font-face {
  font-family: 'Noto Sans Ol Chiki';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansOlChiki/NotoSansOlChiki-Regular.otf')
}
@font-face {
  font-family: 'Noto Sans Rejang';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansRejang/NotoSansRejang-Regular.otf')
}
@font-face {
  font-family: 'Noto Sans Buhid';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansBuhid/NotoSansBuhid-Regular.otf')
}
@font-face {
  font-family: 'Noto Sans Hanunoo';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansHanunoo/NotoSansHanunoo-Regular.otf')
}
@font-face {
  font-family: 'Noto Sans WarangCiti';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansWarangCiti/NotoSansWarangCiti-Regular.otf')
}
@font-face {
  font-family: 'Noto Sans PhagsPa';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansPhagsPa/NotoSansPhagsPa-Regular.otf')
}
@font-face {
  font-family: 'Noto Sans Kharoshthi';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansKharoshthi/NotoSansKharoshthi-Regular.otf')
}
@font-face {
  font-family: 'Noto Sans Regular';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/hinted/ttf/NotoSans/NotoSans-Regular.ttf')
}

@font-face {
  font-family: 'RanjanaUnicode';
  src: url('../statics/RanjanaUNICODE1.0.ttf')

}
@font-face {
  font-family: 'Noto Sans Brahmi';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansBrahmi/NotoSansBrahmi-Regular.otf')
}
.title-ka {
  font-family: "Kharoshthi Ka";
  font-size: 30px;
  margin-top: 25px;
  margin-left: 5px;
}

.russiancyrillic {
  font-family: 'Noto Sans Regular';
}

.ariyaka {
  font-family: 'Ariyaka';
  line-height: 1.5em;
}

.tamilold {
  font-family: "Mukta Malar Regular";
  font-feature-settings: "ss04", "kern";
}
.tamil {
  font-family: "Noto Sans Tamil"
}
.tibetandbumed {
  font-family: "Tibetan Dbu Med";
  line-height: 2.3em;
}
.buhid {
  font-family: "Noto Sans Buhid"
}
.rejang {
  font-family: "Noto Sans Rejang"
}
.hanunoo {
  font-family: "Noto Sans Hanunoo"
}
.saurashtra {
  font-family: "Noto Sans Saurashtra"
}
.sorasompeng {
  font-family: "Noto Sans SoraSompeng"
}
.warangciti {
  font-family: "Noto Sans WarangCiti"
}
.balinese {
  font-family: "Noto Serif Bali"
}
.kannada {
  font-family: "Noto Sans Kannada"
}
.javanese {
  font-family: "Noto Sans Javanese", "Javanese Text";
}
.avestan {
  font-family: "Noto Sans Avestan";
  direction: rtl;
}
.buginese {
  font-family: "Noto Sans Buginese"
}
.sinhala {
  font-family: "Noto Sans Sinhala"
}
.tagalog {
  font-family: "Noto Sans Tagalog"
}
.tagbanwa {
  font-family: "Noto Sans Tagbanwa";
  writing-mode: bt-lr;

}
.sundanese {
  font-family: "Noto Sans Sundanese"
}
.cham {
  font-family: "Noto Sans Cham"
}
.malayalam {
  font-family: "Noto Sans Malayalam"
}
.malayalamold {
  font-family: "Meera";
  font-size:130%;
  line-height:125%;

}
.chakma {
  font-family: "Noto Sans Chakma"
}
.lepcha {
  font-family: "Noto Sans Lepcha"
}
.limbu {
  font-family: "Noto Sans Limbu"
}
.batakkaro {
  font-family: "Noto Sans Batak"
}
.batakmanda {
  font-family: "Noto Sans Batak"
}
.batakpakpak {
  font-family: "Noto Sans Batak"
}
.bataksima {
  font-family: "Noto Sans Batak"
}
.bataktoba {
  font-family: "Noto Sans Batak"
}
.telugu {
  font-family: "Noto Sans Telugu"
}
.khmer {
  font-family: "Noto Sans Khmer"
}
.meeteimayek {
  font-family: "Noto Sans Meetei Mayek"
}
.tolongsiki {
  font-family: "kellytolong"
}
.tamilbrahmi {
  font-family: "Adinatha Tamil Brahmi"
}
.phagspa {
  font-family: "Microsoft PhagsPa", "Noto Sans PhagsPa";
  writing-mode: vertical-lr;
  line-height: 1.8em;
}
.urdu {
  font-family: "Noto Sans Nastaliq Urdu";
  direction: rtl;
}
.kaithi {
  font-family: "Noto Sans Kaithi";
}
.gujarati {
  font-family: "Noto Serif Gujarati";
}
.modi {
  font-family: "Noto Sans Modi";
}
.multani {
  font-family: "Noto Sans Multani";
}
.ahom {
  font-family: "Noto Serif Ahom";
}
.tirhuta {
  font-family: "MithilaUni";
}
.oldpersian {
  font-family: "Noto Sans OldPersian";
}
.takri {
  font-family: "Noto Sans Takri";
}
.taitham {
  font-family: "PaliTilok";
  font-size: 150%;
}
.khomthai {
  font-family: "Patimokkha";
  font-size: 130%;
}
.taithamlao {
  font-family: "Lamphun";
  font-size: 150%;
}
.sylotinagri {
  font-family: "Noto Sans SylotiNagri"
}
.granthagrantamil {
  font-family: "e-Grantamil";
  font-size: 110%;
  line-height: 1.5em;
}
.tamilgrantha {
  font-family: "e-Grantamil";
  font-size: 110%;
  line-height: 1.5em;
}
.siddhammukta {
  font-size: 120%;
  font-family: Muktamsiddham
}
.siddham {
  font-size: 100%;
  font-family: "Noto Sans Siddham"
}
.grantha {
  font-family: "Noto Sans Grantha2";
  line-height: 2em;
}
.kharoshthi {
   font-family: "Segoe UI Historic", "Noto Sans Kharoshthi";
  direction: rtl;
}
.thaana {
  direction: rtl;
}
.tibetan {
  font-size:150%;
}
.zanabazarsquare {
  font-family: "BabelStoneZanabazar";
  line-height: 3em;
}
.newa {
  font-family: "Noto Sans Newa"
}
.sharada {
  font-family: "Noto Sans Sharada"
}
.mahajani {
  font-family: "Noto Sans Mahajani"
}
.multani {
  font-family: "Noto Sans Multani"
}
.bhaiksuki {
  font-family: "Noto Sans Bhaiksuki"
}
.khojki {
  font-family: "Noto Sans Khojki"
}
.khudawadi {
  font-family: "Noto Sans Khudawadi"
}
.granthapandya {
  font-family: "e-Pandya"
}
.vatteluttu {
  font-family: "e-Vatteluttu"
}
.brahmi {
  font-family: "Segoe UI Historic", "Noto Sans Brahmi"
}
.siddhamap {
  font-family: "ApDevaSiddham"
}
.limbudeva {
  font-family: "AnnaPurna"
}
.laopali {
  font-family: "Lao Pali"
}
.nepaldevafont {
  font-family: "Nepal2"
}
.santali {
  font-family: "Noto Sans Ol Chiki"
}
.ranjana {
  font-family: "RanjanaUnicode"
}
.ranjanalantsa {
  font-family: "JMYZK--LZT Lantsa"
}
.ranjanawartu {
  font-family: "JMYZK--WDT Wartu"
}
</style>
