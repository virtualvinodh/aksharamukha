<template>
  <q-card inline class="cards q-ma-sm non-selectable">
    <q-card-title>
      <div :class="script2.toLowerCase()">{{text2}}</div>
    </q-card-title>
    <q-card-main align="center">
      <font size="7"><div :class="script1.toLowerCase()">{{text1}}</div></font>
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
  width:200px;
}
.tamil {
  font-size: 100%;
}
</style>
