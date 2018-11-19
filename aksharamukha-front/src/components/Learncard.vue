<template>
  <q-card inline class="cards q-ma-sm non-selectable">
    <q-card-title>
      <span :class="script2.toLowerCase()">{{text2}}</span>
    </q-card-title>
    <q-card-main align="center">
      <font size="7"><span :class="script1.toLowerCase()">{{text1}}</span></font>
    </q-card-main>
  </q-card>
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
.cards {
  width:140px;
  height:170px;
}
.tamil {
  font-size: 100%;
}
</style>
