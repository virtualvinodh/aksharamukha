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
          size="lg"
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
      >

        <q-item to="/converter">
          <q-item-side icon="translate"/>
          <q-item-main label="Converter"/>
        </q-item>
        <q-item @click.native="openURL('https://uchcharaka.aksharamukha.com')" link>
          <q-item-side icon="mic"/>
          <q-item-main label="Transcriber"/>
        </q-item>
        <!-- <q-item to="/composer">
          <q-item-side icon="language" />
          <q-item-main label="Composer (Multiple scripts)"/>
        </q-item>
        <q-item to="/website/">
          <q-item-side icon="web" />
          <q-item-main label="Convert Websites"/>
        </q-item>
        <q-item to="/upload/" v-if="!$q.platform.is.cordova">
          <q-item-side icon="cloud upload" />
          <q-item-main label="Convert Files (Batch)"/>
        </q-item> -->
            <q-item to="/keyboards">
              <q-item-side icon="keyboard" />
              <q-item-main label="Input (IME)"/>
            </q-item>
        <hr/>
        <q-item to="/explore">
          <q-item-side icon="navigation" />
            <q-item-main label="Scripts Info"/>
          </q-item>
      <q-collapsible icon="table chart" label="Script Matrix"  >
          <q-item to="/script-matrix">
            <q-item-side icon="table chart" />
              <q-item-main label="Indic Matrix"/>
            </q-item>
          <q-item to="/semitic-matrix">
            <q-item-side icon="table chart" />
              <q-item-main label="Semitic Matrix"/>
            </q-item>
          </q-collapsible>
          <q-collapsible icon="spellcheck" label="Romanization"  >
            <q-item to="/roman">
              <q-item-main label="Indic Scripts"/>
            </q-item>
            <q-item to="/roman-semitic">
              <q-item-main label="Semitic Scripts"/>
            </q-item>
            <q-item to="/loc">
              <q-item-main label="Library of Congress"/>
            </q-item>
          </q-collapsible>
 <!--            <q-item :to="!scriptSemiticList.includes(script.value) ? '/describe/' + script.value : '/describesemitic/' + script.value"
            v-for="script in scriptAboutList" :key="script.value">
              <q-item-main :label="script.label"/>
            </q-item>
        </q-collapsible> -->
        <q-collapsible icon="book" label="Sample Texts"  >
            <q-item :to="'/texts/' + text.path" v-for="text in texts" :key="text.path">
              <q-item-main :label="text.name"/>
            </q-item>
        </q-collapsible>
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
         <q-item to="/download" v-if="!$q.platform.is.cordova">
          <q-item-side icon="cloud_download" />
          <q-item-main label="Download"/>
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
<!--
<social-sharing url="http://aksharamukha.appspot.com"
                      title="Aksharamukha"
                      description="Indic Script Converter"
                      quote="Try out this Indic Script Converter and convert between 75 scripts"
                      hashtags="scripts, indic, orthography, brahmic, writing system, unicode"
                      inline-template v-if="!$q.platform.is.cordova">
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
</social-sharing> -->
    </q-layout-drawer>
    <q-page-container class="page">
      <span v-if="!$q.platform.is.cordova">
      <div :class="$q.platform.is.mobile ? 'alert2': 'alert'" v-if="false && visibleAlert && !$q.platform.is.mobile">
      <br/>
      <q-alert
          color="grey-7"
          icon="favorite"
          appear
          :actions="[{ label: 'Dismiss', handler: hideAlert }]"
          class="q-mb-sm"
        > Like Aksharamukha? Consider <a href="https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=LRY7AE7SXDHTN&source=url">supporting</a> it! </q-alert>
      </div>
      <div :class="$q.platform.is.mobile ? 'alert2': 'alert'" v-if="visibleAlertTransc && !$q.platform.is.mobile">
      <br/>
      <q-alert
          color="grey-7"
          icon="mic"
          appear
          :actions="[{ label: 'Dismiss', handler: hideAlertTransc }]"
          class="q-mb-sm"
        > Transcribe languages now! Try: <a href="https://uchcharaka.aksharamukha.com">Aksharamukha: Uchcharaka</a></q-alert>
      </div>
      <div :class="$q.platform.is.mobile ? 'alert2': 'alert'" v-if="$q.platform.is.mobile && !hideAndroid">
      <br/>
      <q-alert
          color="grey-7"
          icon="android"
          appear
          :actions="[{ label: 'Dismiss', handler: hideAndroidHand }]"
          class="q-mb-sm"
        > Aksharamukha now available as an <a href="https://play.google.com/store/apps/details?id=org.cordova.quasar.aksharamukha">Android app</a>!</q-alert>
      </div>
    </span>
      <router-view/>
    </q-page-container>
    <q-layout-footer v-show="showFooter" class="print-hide">
        <q-toolbar color="tertiary" class="footer-quote">
          © 2018 <a href="http://www.virtualvinodh.com">Vinodh Rajan</a>&nbsp;&nbsp;&nbsp;vinodh@virtualvinodh.com. This software is released under GNU GPL 3.0 license.
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
import { openURL, QLayoutFooter, QTooltip, QWindowResizeObservable, QCollapsible, QAlert, QTab, QTabs } from 'quasar'
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
    SocialSharing,
    QTab,
    QTabs
  },
  data () {
    return {
      leftDrawerOpen: true,
      hideAndroid: false,
      showFooter: true,
      randomScript: '',
      visibleAlert: true,
      visibleAlertTransc: true,
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
        },
        {
          name: 'UDHR (Neo-Aramaic)',
          path: 'udhr'
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
    if (localStorage.visibleAlertTransc) {
      this.visibleAlertTransc = JSON.parse(localStorage.visibleAlertTransc)
    }
    if (localStorage.hideAndroid) {
      this.hideAndroid = JSON.parse(localStorage.hideAndroid)
    }
  },
  methods: {
    openURL,
    hideAndroidHand: function () {
      this.hideAndroid = true
      localStorage.hideAndroid = JSON.stringify(this.hideAndroid)
    },
    hideAlert: function () {
      this.visibleAlert = false
      localStorage.visibleAlert = JSON.stringify(this.visibleAlert)
    },
    hideAlertTransc: function () {
      this.visibleAlertTransc = false
      localStorage.visibleAlertTransc = JSON.stringify(this.visibleAlertTransc)
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
  font-size: 25px;
  margin-top: 20px;
  margin-left: 5px;
}

@import url('../statics/fonts.css');

</style>
