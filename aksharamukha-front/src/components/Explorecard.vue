<template>
  <q-card inline class="cards non-selectable cursor-pointer" flat @mouseover.native="hovering" @mouseleave.native="nothovering">
    <q-card-title align="center">
      <small><span>{{getScriptObject(script1).label}}</span></small>
    </q-card-title>
    <transition
   enter-active-class="animated fadeIn"
   mode="out-in"
    >
    <q-card-main align="center" :key="text1"  :style="{zoom: zoomfactor}" @click.native="clicked">
      <font size="7"><span :class="script1.toLowerCase()">{{text1}}</span></font>
    </q-card-main>
      </transition>
  </q-card>
</template>

<script>
import {QCard, QCardTitle, QCardMain, QCardMedia, QCardActions} from 'quasar'
import { ScriptMixin } from '../mixins/ScriptMixin'

export default {
  // name: 'ComponentName',
  props: ['text1', 'script1'],
  mixins: [ScriptMixin],
  components: {
    QCard,
    QCardTitle,
    QCardMain,
    QCardMedia,
    QCardActions
  },
  data () {
    return {
      zoomfactor: 1,
      hoveringInd: false
    }
  },
  methods: {
    clicked: function () {
      this.$emit('click')
    },
    hovering: function () {
      this.zoomfactor = 1.3
      this.hoveringInd = true
    },
    nothovering: function () {
      this.zoomfactor = 1
      this.hoveringInd = false
    }
  }
}
</script>

<style scoped>
.cards {
  width:170px;
  height:160px;
}
.tamil {
  font-size: 100%;
}
 a, a:hover, a:focus, a:active {
  text-decoration: none;
  color: inherit;
 }
</style>
