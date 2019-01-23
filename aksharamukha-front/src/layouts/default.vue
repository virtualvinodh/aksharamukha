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
      class=""
      side="left"
      :width="230"
      :content-class="$q.theme === 'mat' ? 'bg-grey-2' : null"
    >
      <q-list
        no-border
        link
        inset-delimiter
      > <!-- link to other tools -->
        <!-- Options to create pseudo epigraphs -->
        <!-- Icon -->
        <q-item to="/converter">
          <q-item-side icon="translate" />
          <q-item-main label="Converter"/>
        </q-item>
        <q-item to="/website">
          <q-item-side icon="web" />
          <q-item-main label="Convert Websites"/>
        </q-item>
        <q-item to="/upload">
          <q-item-side icon="cloud upload" />
          <q-item-main label="Convert Files"/>
        </q-item>
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
        <q-collapsible icon="school" label="Learn" >
            <q-item to="/syllabary">
              <q-item-main label="Syllabary"/>
            </q-item>
            <q-item to="/conjuncts">
              <q-item-main label="Conjuncts"/>
            </q-item>
        </q-collapsible>
        <q-collapsible icon="how to reg" label="Play & Practice">
            <q-item to="/fill">
              <q-item-main label="Fill"/>
            </q-item>
            <q-item to="/match-letter">
              <q-item-main label="Match" />
            </q-item>
            <q-item to="/flipcards-shuffle">
              <q-item-main label="Flipcards" />
            </q-item>
            <q-item to="/memory-cards">
              <q-item-main label="Memorize"  />
            </q-item>
        </q-collapsible>
        <q-collapsible icon="build" label="Technical" >
          <q-item to="/api">
            <q-item-main label="API" />
          </q-item>
          <q-item to="/plugin">
            <q-item-main label="Website Plugin" />
          </q-item>
          </q-collapsible>
         <q-item to="/download">
          <q-item-side icon="cloud download" />
          <q-item-main label="Download" />
        </q-item>
        <q-item to="/help">
            <q-item-side icon="help" />
            <q-item-main label="Help" />
        </q-item>
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
                      quote="Try out this Indic Script Converter and convert between 64 scripts"
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
            Jinavani : ஜினவாணி <br/>
            http://tamiljinavani.appspot.com
          </div>
        </q-toolbar>
    </q-layout-footer>

  </q-layout>
</template>

<script>
import { openURL, QLayoutFooter, QTooltip, QWindowResizeObservable, QCollapsible } from 'quasar'
import Transliterate from '../components/Transliterate'
import SocialSharing from 'vue-social-sharing'
import {ScriptMixin} from '../mixins/ScriptMixin'

export default {
  name: 'LayoutDefault',
  mixins: [ScriptMixin],
  components: {
    QLayoutFooter,
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
  methods: {
    openURL,
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
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/unhinted/NotoSansAvestan-Regular.ttf')
}
@font-face {
  font-family: 'Noto Sans Buginese';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/unhinted/NotoSansBuginese-Regular.ttf')
}
@font-face {
  font-family: 'Noto Sans Tagalog';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/unhinted/NotoSansTagalog-Regular.ttf')
}
@font-face {
  font-family: 'Noto Sans Malayalam';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansMalayalam/NotoSansMalayalam-Regular.otf')
}
@font-face {
  font-family: 'Noto Sans Tagbanwa';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/unhinted/NotoSansTagbanwa-Regular.ttf')
}
@font-face {
  font-family: 'Noto Sans Sundanese';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/unhinted/NotoSansSundanese-Regular.ttf')
}
@font-face {
  font-family: 'Noto Sans Cham';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/unhinted/NotoSansCham-Regular.ttf')
}
@font-face {
  font-family: 'Noto Sans Chakma';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/unhinted/NotoSansChakma-Regular.ttf')
}
@font-face {
  font-family: 'Noto Sans Telugu';
  src: url('../statics/Lohit-Telugu.ttf')
}
@font-face {
  font-family: 'Noto Sans Batak';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/unhinted/NotoSansBatak-Regular.ttf')
}
@font-face {
  font-family: 'Noto Sans Lepcha';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/unhinted/NotoSansLepcha-Regular.ttf')
}
@font-face {
  font-family: 'Noto Sans Limbu';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/unhinted/NotoSansLimbu-Regular.ttf')
}
@font-face {
  font-family: 'Noto Sans Meetei Mayek';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/unhinted/NotoSansMeeteiMayek-Regular.ttf')
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
  src: url('../statics/BabelStoneZanabazar.woff')
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
  src: url('../statics/LaoPaliAlpha-Extralight.otf')
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
  font-family: 'Lamphun';
  src: url('../statics/lamphun.otf')
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
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansNewa/NotoSansNewa-Regular.otf')
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
  font-family: 'Noto Sans Brahmi';
  src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansBrahmi/NotoSansBrahmi-Regular.otf')
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
.tamil {
  font-family: "Noto Sans Tamil"
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
  font-family: "Noto Sans Tirhuta";
}
.oldpersian {
  font-family: "Noto Sans OldPersian";
}
.takri {
  font-family: "Noto Sans Takri";
}
.taitham {
  font-family: "Lamphun";
  font-size: 175%;
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
.siddham {
  font-size: 120%;
  font-family: Muktamsiddham
}
.siddhamunicode {
  font-family: MuktamsiddhamG
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
