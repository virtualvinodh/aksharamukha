<template>
  <q-page padding>
  <q-field
  icon="cloud"
  label="Count"
  helper="Enter the number of letters that you want to test"
  :count="3"
>
  <q-input suffix="letters" v-model="countTotal" @input="reset"/>
</q-field> <br/>
<p class="q-body-1 q-ma-md"> Fill in the equivalent Tamil letters </p>
  <transition
   enter-active-class="animated fadeIn"
   leave-active-class="animated fadeOut"
   mode="out-in"
    >
    <span :key="resetV">
      <q-card v-for="(i,index) in randomList" :key="i" inline class="cards q-ma-sm"
       :text-color="colors(index)">
        <q-card-title>
          <q-input placeholder="answer" ref="'q' + i" v-model="answers['q' + index]"></q-input>
        </q-card-title>
        <q-card-main align="center">
          <font size="7"><component :text="compounds[i]" spelling="late" :is="script"></component></font>
        </q-card-main>
        <transition
           enter-active-class="animated fadeIn"
           leave-active-class="animated fadeOut"
           mode="out-in">
        <q-card-actions align="around" horizontal v-show="selections">
          <q-btn-toggle
                toggle-color="faded"
                v-model="options"
                @input="answers['q' + index] = options"
                text-color="black"
                :options="[
                {label: compounds[randomOptions[index][0]], value: compounds[randomOptions[index][0]]},
                {label: compounds[randomOptions[index][1]], value: compounds[randomOptions[index][1]]},
                {label: compounds[randomOptions[index][2]], value: compounds[randomOptions[index][2]]}
                ]"
              flat
              dense
              size="11px"
              />
        </q-card-actions>
        </transition>
      </q-card>
    </span>
  </transition> <br/>
  <q-toggle v-model="selections" icon="settings"
      label="Multiple Choice" left-label class="q-mt-md" />
  <q-btn label = "Verify answers" class="q-ma-lg" color="faded" @click="verify"></q-btn>
  <q-btn label = "Show answers" class="q-ma-lg" color="faded" @click="show"></q-btn>
  <q-btn label = "Play again" class="q-ma-lg" color="faded" @click="reset"></q-btn>
  Result : {{correct}} / {{countTotal}}
  <br/>
  </q-page>
</template>

<script>
import {QCard, QCardTitle, QCardMain, QCardMedia, QCardActions, QField, QInput, QBtnToggle, QToggle} from 'quasar'
import Brahmi from '../components/Brahmi'
import Controls from '../components/Controls'
import BrahmiE from '../components/BrahmiE'
import Vatteluttu from '../components/Vatteluttu'
var _ = require('underscore')

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
    QField,
    QInput,
    QBtnToggle,
    QToggle,
    Controls
  },
  props: ['script'],
  mounted: function () {
    this.randomListGen()
  },
  computed: {
    compounds: function () {
      var compounds = []
      var short = ['ெ', 'ொ']
      for (let i = 0; i < this.consonants.length; i++) {
        for (let j = 0; j < this.vowelSigns.length; j++) {
          if (this.script === 'vatteluttu') {
            if (!this.grantha.includes(this.consonants[i]) || !short.includes(this.vowelSigns[j])) {
              compounds.push(this.consonants[i] + this.vowelSigns[j])
            }
          } else {
            compounds.push(this.consonants[i] + this.vowelSigns[j])
          }
        }
      }

      compounds.push('ஶ்ரீ')

      compounds = compounds.concat(this.vowels)
      compounds = compounds.concat(this.consonants)

      return compounds
    },
    correct: function () {
      var count = 0
      for (let i = 0; i < this.results.length; i++) {
        if (this.results[i]) {
          count++
        }
      }
      return count
    }
  },
  data () {
    return {
      countTotal: 12,
      options: [],
      answers: {},
      results: [],
      randomList: [],
      randomListOld: [],
      randomOptions: [],
      resetV: true,
      selections: false,
      vowels: ['அ', 'ஆ', 'இ', 'ஈ', 'உ', 'ஊ', 'எ', 'ஏ', 'ஐ', 'ஒ', 'ஓ', 'ஔ', 'ஃ'],
      consonants: ['க', 'ங', 'ச', 'ஞ', 'ட', 'ண', 'த', 'ந',
        'ப', 'ம', 'ய', 'ர', 'ல', 'வ', 'ழ', 'ள', 'ற', 'ன', 'ஜ', 'ஷ', 'ஸ', 'ஹ'],
      vowelSigns: ['ா', 'ி', 'ீ', 'ு', 'ூ', 'ெ', 'ே', 'ை', 'ொ', 'ோ', 'ௌ', '்'],
      grantha: ['ஜ', 'ஷ', 'ஸ', 'ஹ', 'ஶ']
    }
  },
  methods: {
    getRandomInt: function (min, max) {
      return Math.floor(Math.random() * (max - min + 1)) + min
    },
    getRandomCompound: function () {
      return this.getRandomInt(0, this.compounds.length - 1)
    },
    randomListGen: function () {
      this.randomListOld = this.randomList.slice()
      this.randomList = []
      while (this.randomList.length < this.countTotal) {
        let random = this.getRandomCompound()
        if (!this.randomList.includes(random) && !this.randomListOld.includes(random)) {
          this.randomList.push(random)
          let sign = this.getRandomInt(0, 1) === 0 ? 1 : -1
          let options = [random, this.getRandomCompound(), random + (sign * this.getRandomInt(1, 5))]
          this.randomOptions.push(this.shuffle(this.shuffle(options)))
        }
      }
    },
    verify: function () {
      this.results = []
      for (let i = 0; i < this.countTotal; i++) {
        if (typeof this.answers['q' + i] === 'undefined') {
          this.answers['q' + i] = ''
        }
        if (this.answers['q' + i] === 'ஸ்ரீ') {
          this.answers['q' + i] = 'ஶ்ரீ'
        }
        this.results.push(this.answers['q' + i].trim() === this.compounds[this.randomList[i]])
      }
    },
    colors: function (index) {
      if (typeof this.results[index] === 'undefined') {
        return ''
      } else if (this.results[index]) {
        return 'green-3'
      } else {
        return 'red-3'
      }
    },
    reset: function () {
      this.results = []
      this.answers = []
      this.resetV = !this.resetV
      this.randomListGen()
    },
    show: function () {
      this.results = []
      for (let i = 0; i < this.countTotal; i++) {
        this.answers['q' + i] = this.compounds[this.randomList[i]]
      }
    },
    shuffle: function (arr) {
      return _.shuffle(arr)
    }
  }
}
</script>

<style scoped>
.cards {
  width:140px;
}

</style>
