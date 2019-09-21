<template>
  <div>
  <q-card inline class="cards4 q-ma-sm non-selectable" color="dark">
  <q-btn flat round dense icon="arrow back" @click="$emit('back')"/>
    <q-card-main align="center">
      <div :class="script2.toLowerCase()" class="text text-grey-5">{{text2}}</div>
    </q-card-main>
    <hr/>
    <q-card-main align="center">
     <div :class="script1.toLowerCase()" class="text">{{text1}}</div>
    </q-card-main>
    <div class="arrowbottom"> <q-btn flat round dense icon="arrow forward"  @click="$emit('forward')"/> </div>
  </q-card>
</div>
</template>

<script>
import {QCard, QCardTitle, QCardMain, QCardMedia, QCardActions} from 'quasar'

export default {
  // name: 'ComponentName',
  props: ['text1', 'script1', 'script2', 'text2'],
  components: {
    QCard,
    QCardTitle,
    QCardMain,
    QCardMedia,
    QCardActions
  },
  data () {
    return {
    }
  },
  methods: {
  }
}
</script>

<style scoped>
.arrowbottom {
  text-align: right;
}
.text {
  font-size: 11vh;
}
.cards4 {
  width: 60vw;
}
</style>
