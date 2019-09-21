<template>
  <div>
          <q-card inline class="cards3" color="tertiary">
          <q-btn flat round dense icon="arrow back" @click="$emit('back')"/>
            <q-card-main align="center" :style="script1 === 'tamil' ? 'tamil' : ''">
              <div :class="script1.toLowerCase()" class="text">{{text1}}</div>
            </q-card-main>
          </q-card>
          <q-card inline class="cards3" color="tertiary text-grey-5">
            <q-card-main align="center" :style="script2 === 'tamil' ? 'tamil' : ''">
              <div :class="script2.toLowerCase()" class="text">{{text2}}</div>
            </q-card-main>
          </q-card>
          <div class="arrowbottom"> <q-btn flat round dense icon="arrow forward"  @click="$emit('forward')"/> </div>

  </div>
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
.arrowbottom {
  text-align: right;
  margin-top: -40px;
  color:white;
}
.text {
  font-size: 10vw;
}
.cards3 {
  width: 50%;
  height: 40vh;
}
.grantha {
  margin-top: -80px;
}
.flip {
  display: inline-block;
}
</style>
