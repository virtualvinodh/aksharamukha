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

.title-ka {
  font-family: "Kharoshthi Ka";
  font-size: 30px;
  margin-top: 25px;
  margin-left: 5px;
}

@import url('../statics/fonts.css');

</style>
