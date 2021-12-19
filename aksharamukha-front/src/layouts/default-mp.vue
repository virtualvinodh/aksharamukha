<template>
  <q-layout view="hHr Lpr fFf">
    <q-page-container class="page">
      <router-view/>
    </q-page-container>

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
