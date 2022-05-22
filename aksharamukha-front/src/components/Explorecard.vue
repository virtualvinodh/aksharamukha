<template>
  <q-card inline class="non-selectable cursor-pointer" :class="$q.platform.is.mobile ? 'cards-mobile' : 'cards-desk'" @click.native="clicked">
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
    <q-card-main align="center" :key="text1"  :style="{zoom: zoomfactor, 'margin-top': !hidetitle ? '' : '5px'}">
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

</style>
