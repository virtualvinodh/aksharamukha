<template>
  <q-card inline class="cards q-ma-sm non-selectable">
    <q-card-main align="center">
      <font size="5"><span :class="script2.toLowerCase()" class="text-grey-5">{{text2}}</span></font>
    </q-card-main>
    <hr/>
    <q-card-main align="center">
      <font size="5"><span :class="script1.toLowerCase()" class="text-grey-10">{{text1}}</span></font>
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
}
.tamil {
  font-size: 100%;
}
</style>
