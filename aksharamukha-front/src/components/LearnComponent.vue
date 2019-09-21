<template>
      <span v-if="letters1.length > 0">
        <h5 class="q-ma-md"> {{letters1.length}} characters</h5>
      <span v-if="displaytype === 'showall'">
        <span v-for="(vowel, index) in letters1" :key="vowel+'k1'">
           <component  :script1="script1" :text1="vowel" :script2="script2" :text2="letters2[index]"
             :is="'LearncardTeach'" :ref="'letter1' + index"> </component >
        </span>
      </span>

      <span v-if="displaytype === 'flipcard'">
        <span v-for="(vowel, index) in letters1" :key="vowel+'k2'">
           <component  :script1="script1" :text1="vowel" :script2="script2" :text2="letters2[index]"
             :is="'flipcard'" :ref="'letter2' + index"> </component >
        </span>
      </span>

      <span v-if="displaytype === 'flashcard'">
        <transition
           leave-active-class="animated pulse"
           mode="out-in"
        >
          <component :script1="script1" :text1="letters1[letterindexProper]" :script2="script2" :text2="letters2[letterindexProper]"
             :is="$q.platform.is.mobile ? 'FlashcardMobile' : 'FlashcardDesktop'" :ref="'vowel3' + letterindex" @forward="$emit('forward')"
             @back="$emit('back')" :key="'letter3' + letterindex"> </component>
        </transition>
      </span>
      </span>
</template>

<script>
import {QCard, QCardTitle, QCardMain, QCardMedia, QCardActions} from 'quasar'
import LearncardTeach from '../components/LearncardTeach'
import Flipcard from '../components/Flipcard'
import FlashcardDesktop from '../components/FlashcardDesktop'
import FlashcardMobile from '../components/FlashcardMobile'

export default {
  // name: 'ComponentName',
  props: ['letters1', 'letters2', 'script1', 'script2', 'letterindex', 'displaytype'],
  components: {
    QCard,
    QCardTitle,
    QCardMain,
    QCardMedia,
    Flipcard,
    QCardActions,
    FlashcardDesktop,
    FlashcardMobile,
    LearncardTeach
  },
  data () {
    return {
    }
  },
  computed: {
    letterindexProper: function () {
      if (this.letterindex < 0) {
        return (this.letters1.length + (this.letterindex % this.letters1.length)) % this.letters1.length
      } else {
        return this.letterindex % this.letters1.length
      }
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
.cards {
  width: 60vw;
}
</style>
