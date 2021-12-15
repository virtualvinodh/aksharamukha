<template>
  <q-card class="cursor-pointer" @mouseover.native="hovering" @mouseleave.native="nothovering" :class="$q.platform.is.mobile ? 'cards-mobile' : 'cards-desk'">
    <q-card-title align="left" v-if="!hidetitle">
      <small><span>{{getScriptObject(script1).label}}</span></small>
    </q-card-title>
    <q-card-title align="left" v-else>
      <small><span>&nbsp;</span></small>
    </q-card-title>
    <transition
   enter-active-class="animated fadeIn"
   mode="out-in"
    >
    <q-card-main align="left" :key="text1"  :style="{zoom: zoomfactor, 'margin-top': !hidetitle ? '' : '5px'}" @click.native="clicked">
      <div class="text-red-4" v-if="approx && highapprox"><font size="5"><div :class="script1.toLowerCase()">{{text1}}</div></font></div>
      <div class="text-grey-6" v-if="approx && highapprox"> <br/> {{text2}} </div>
      <div v-else><font size="5"><div :class="script1.toLowerCase()">{{text1}}</div></font></div>
    </q-card-main>
      </transition>
  </q-card>
</template>

<script>
import {QCard, QCardTitle, QCardMain, QCardMedia, QCardActions} from 'quasar'
import { ScriptMixin } from '../mixins/ScriptMixin'

export default {
  // name: 'ComponentName',
  props: ['text1', 'script1', 'hidetitle', 'approx', 'text2', 'highapprox'],
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
.cards-desk {
}
.cards-mobile {
}
.tamil {
  font-size: 100%;
}
 a, a:hover, a:focus, a:active {
  text-decoration: none;
  color: inherit;
 }
</style>
