<template>
  <q-card inline class="non-selectable cursor-pointer" @mouseover.native="hovering" @mouseleave.native="nothovering" :class="$q.platform.is.mobile ? 'cards-mobile' : 'cards-desk'">
    <q-card-title align="center" v-if="!hidetitle">
      <small><span>{{getScriptObject(script1).label}}</span></small>
    </q-card-title>
    <q-card-title align="center" v-else>
      <small><span>&nbsp;</span></small>
    </q-card-title>
    <transition
   enter-active-class="animated fadeIn"
   mode="out-in"
    >
    <q-card-main align="center" :key="text1"  :style="{zoom: zoomfactor, 'margin-top': !hidetitle ? '' : '5px'}" @click.native="clicked">
      <span class="text-red-4" v-if="approx"><font size="6"><span :class="script1.toLowerCase()">{{text1}}</span></font></span>
      <div class="text-grey-6" v-if="approx"> {{text2}} </div>

      <span v-else><font size="6"><span :class="script1.toLowerCase()">{{text1}}</span></font></span>

    </q-card-main>
      </transition>
  </q-card>
</template>

<script>
import {QCard, QCardTitle, QCardMain, QCardMedia, QCardActions} from 'quasar'
import { ScriptMixin } from '../mixins/ScriptMixin'

export default {
  // name: 'ComponentName',
  props: ['text1', 'script1', 'hidetitle', 'approx', 'text2'],
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
  width:130px;
  height:150px;
}
.cards-mobile {
  width:130px;
  height:150px;
}
.tamil {
  font-size: 100%;
}
 a, a:hover, a:focus, a:active {
  text-decoration: none;
  color: inherit;
 }
</style>
