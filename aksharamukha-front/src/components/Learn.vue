<template>
  <div>
    <q-page-sticky position="top-right" :offset="[18,18]">
      <q-toggle v-model="flip" icon="copy" color="faded"
        label="As flipcards" left-label class="q-ml-sm q-mb-md print-hide" @input="notification"></q-toggle>
        <br/>

    </q-page-sticky>
    <font size="6">
      <component :text="script === 'vatteluttu' ? 'வட்டெழுத்து' : 'தமிழ் பிராமி'"
        spelling="late" :is="script" class="cards q-ma-sm"></component>
    </font> <br/>

    <transition
      enter-active-class="animated fadeIn"
      leave-active-class="animated fadeOut"
      mode="out-in"
    >
      <span :key="flip">
        <component v-for="vowel in vowels" :key="vowel" :script1="script" script2="tamil" :text="vowel" class="q-ma-sm"
                     :is="flip ? 'flipcard' : 'learncard' ">
        </component>

        <br/>

        <component :script1="script" script2="tamil" text="ஃ" class="q-ma-sm"
                     :is="flip ? 'flipcard' : 'learncard' ">
        </component>

        <br/>

        <component v-for="consonant in consonants" :key="consonant" :script1="script" script2="tamil" :text="consonant" class="q-ma-sm"
                     :is="flip ? 'flipcard' : 'learncard' " :grantha="grantha.includes(consonant)">
        </component>

        <br/>

          <div v-if="script === 'vatteluttu'">
          <q-card color="faded" class="q-ma-sm">
            <q-card-title>
              Pallava Letters
            </q-card-title>
            <q-card-main>
              Vatteluttu frequently adopted Pallava letters to denote such sounds.
            </q-card-main>
          </q-card>
        </div>

        <br/>

        <span v-for="consonant in consonants" :key="consonant + '2'" v-if="script !== 'vatteluttu' || consonant !== 'த⁴'">
          <component v-for="vowelSign in vowelSigns" :key="vowelSign + '2'" :script1="script" script2="tamil" :text="consonant + vowelSign" class="q-ma-sm"
                     :is="flip ? 'flipcard' : 'learncard' " :grantha="grantha.includes(consonant)">
          </component>
          <br/>
        </span>

        <br/>

        <component :script1="script" script2="tamil" text="ஶ்ரீ" class="q-ma-sm"
                     :is="flip ? 'flipcard' : 'learncard' " :grantha="true">
        </component>
     </span>
  </transition>
 </div>
</template>

<script>
import {QCard, QCardTitle, QCardMain, QCardMedia, QCardActions, QToggle, QPageSticky, Notify} from 'quasar'
import Brahmi from '../components/Brahmi'
import BrahmiE from '../components/BrahmiE'
import Vatteluttu from '../components/Vatteluttu'
import VueFlip from 'vue-flip'
import Learncard from '../components/Learncard'
import Flipcard from '../components/Flipcard'

export default {
  // name: 'PageName',
  components: {
    QCard,
    QCardTitle,
    QCardMain,
    QCardMedia,
    QCardActions,
    Brahmi,
    BrahmiE,
    Vatteluttu,
    VueFlip,
    QToggle,
    Learncard,
    Flipcard,
    QPageSticky
  },
  props: ['script'],
  plugins: [Notify],
  data () {
    return {
      vowels: ['அ', 'ஆ', 'இ', 'ஈ', 'உ', 'ஊ', 'எ', 'ஏ', 'ஐ', 'ஒ', 'ஓ', 'ஔ'],
      consonants: ['க', 'ங', 'ச', 'ஞ', 'ட', 'ண', 'த', 'ந',
        'ப', 'ம', 'ய', 'ர', 'ல', 'வ', 'ழ', 'ள', 'ற', 'ன', 'ஜ', 'ஷ', 'ஸ', 'ஹ', 'ஶ', 'த⁴'],
      vowelSigns: ['ா', 'ி', 'ீ', 'ு', 'ூ', 'ெ', 'ே', 'ை', 'ொ', 'ோ', 'ௌ', '்'],
      grantha: ['ஜ', 'ஷ', 'ஸ', 'ஹ', 'ஶ'],
      short: ['ெ', 'ொ'],
      flip: false
    }
  },
  methods: {
    notification: function () {
      if (this.flip) {
        this.$q.notify({
          type: 'info',
          message: 'Click on a card to flip it over',
          color: 'positive',
          position: 'top-right',
          timeout: 5000
        })
      }
    }
  }
}
</script>

<style scoped>
.cards {
  width:140px;
  height:170px;
}
</style>
