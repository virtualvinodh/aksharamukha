<template>
  <q-card inline class="cards2 q-ma-sm non-selectable" color="dark">
    <q-card-main align="center">
      <font size="6"><div :class="script2.toLowerCase()" class="text-grey-5">{{text2}}</div></font>
    </q-card-main>
    <hr/>
    <q-card-main align="center">
      <font size="6"><div :class="script1.toLowerCase()">{{text1}}</div></font>
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
.cards2 {
  width:155px;
}
</style>
