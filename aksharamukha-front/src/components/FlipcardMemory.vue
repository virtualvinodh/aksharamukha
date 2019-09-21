<template>
  <vue-flip :active-click="true" width="140px" height="120px" transition="2s" class="q-ma-sm flip cursor-pointer">
        <div slot="front">
          <q-card inline class="cards" color="tertiary">
            <q-card-main>
              <font size="7"><span :class="script.toLowerCase()">.</span></font>
            </q-card-main>
          </q-card>
        </div>
        <div slot="back">
          <q-card inline class="cards">
            <q-card-main align="center">
              <font size="7"><span :class="script.toLowerCase()">{{text}}</span></font>
            </q-card-main>
          </q-card>
        </div>
  </vue-flip>
</template>

<script>
import VueFlip from 'vue-flip'
import {QCard, QCardTitle, QCardMain, QCardMedia, QCardActions} from 'quasar'

export default {
  // name: 'ComponentName',
  props: ['text', 'script'],
  components: {
    VueFlip,
    QCard,
    QCardTitle,
    QCardMain,
    QCardMedia,
    QCardActions
  },
  data () {
    return {}
  }
}
</script>

<style scoped>
.cards {
  width:140px;
}
.flip {
  display: inline-block;
}
</style>
