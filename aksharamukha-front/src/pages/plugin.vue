<template>
  <q-page padding>
  If you would like to integrate Aksharamukha as a plugin in your website, contact vinodh@virtualvinodh.com.
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
