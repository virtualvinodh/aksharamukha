<template>
  <vue-flip :active-click="true" width="140px" height="120px" transition="2s" class="q-ma-sm flip cursor-pointer">
        <div slot="front">
          <q-card inline class="cards">
            <q-card-main align="center" :style="script1 === 'tamil' ? 'tamil' : ''">
              <font size="7"><span :class="script1.toLowerCase()">{{text1}}</span></font>
            </q-card-main>
          </q-card>
        </div>
        <div slot="back">
          <q-card inline class="cards" color="tertiary">
            <q-card-main align="center" :style="script2 === 'tamil' ? 'tamil' : ''">
              <font size="7"><span :class="script2.toLowerCase()">{{text2}}</span></font>
            </q-card-main>
          </q-card>
        </div>
  </vue-flip>
</template>

<script>
import VueFlip from 'vue-flip'
import {QCard, QCardTitle, QCardMain, QCardMedia, QCardActions} from 'quasar'
import Transliterate from '../components/Transliterate'

export default {
  // name: 'ComponentName',
  props: ['text1', 'text2', 'script1', 'script2'],
  components: {
    VueFlip,
    QCard,
    QCardTitle,
    QCardMain,
    QCardMedia,
    QCardActions,
    Transliterate
  },
  methods: {
  },
  data () {
    return {
    }
  }
}
</script>

<style scoped>
.cards {
  width:140px;
  height:120px;
}
.flip {
  display: inline-block;
}
.tamil {
  font-size:75%;
}
</style>
