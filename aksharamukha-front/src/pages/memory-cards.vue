<template>
  <q-page padding>
  <q-field
  icon="cloud"
  label="Count"
  helper="Enter the number of letters that you want to test"
  :count="3"
>
  <q-input suffix="letters" v-model="countTotal" @input="resetSoft"/>
</q-field>
<span class="q-mt-md"> Script: </span>
       <q-select
        filter
        inset
        lable="front"
        autofocus-filter
        filter-placeholder="search"
        placeholder="Input Script"
        v-model="script"
        @input="resetHard"
        class="q-ma-sm col-md-3"
        :options="scripts"
      />
  <p class="q-body-1 q-ma-md">Find matching cards. Click on the cards to flip them. <q-spinner-comment color="dark" :size="30" v-show="loading"/> </p>
  <transition
   enter-active-class="animated fadeIn"
   leave-active-class="animated fadeOut"
   mode="out-in"
    >
    <span :key="resetV">
    <transition-group
    name="flip-list"
    >
      <flipcard-memory v-for="(i,index) in randomList" :key="index" inline class="cards q-ma-sm" :ref="'q' + index"
        @click.native="select(index, i)"
        :text="compoundsF[i]" :script="script" >
      </flipcard-memory>
    </transition-group>
    </span>
  </transition>
  <br/>
  <q-btn label = "Play again" class="q-ma-lg" color="faded" @click="resetSoft"></q-btn>
  <br/>
  </q-page>
</template>

<script>
import {QCard, QCardTitle, QCardMain, QCardMedia, QCardActions, QField, QInput, QBtnToggle, QToggle, Notify, QSelect, QSpinnerComment} from 'quasar'
import FlipcardMemory from '../components/FlipcardMemory'
import {ScriptMixin} from '../mixins/ScriptMixin'
var _ = require('underscore')

export default {
  // name: 'PageName',
  components: {
    QCard,
    QCardTitle,
    QCardMain,
    QCardMedia,
    QCardActions,
    QField,
    QInput,
    QBtnToggle,
    QToggle,
    FlipcardMemory,
    QSpinnerComment,
    QSelect
  },
  plugins: [Notify],
  mixins: [ScriptMixin],
  mounted: function () {
    this.script = this.scriptRandom().value
    this.compoundsGen()
  },
  data () {
    return {
      countTotal: 9,
      script: '',
      autoclick: false,
      selected: ['', ''],
      matched: [],
      randomList: [],
      randomListOld: [],
      resetV: true,
      compoundsF: '',
      compoundsT: '',
      loading: true
    }
  },
  methods: {
    getRandomInt: function (min, max) {
      return Math.floor(Math.random() * (max - min + 1)) + min
    },
    getRandomCompound: function () {
      return this.getRandomInt(0, this.compoundsF.length - 1)
    },
    randomListGen: function () {
      this.randomListOld = this.randomList.slice()
      this.randomList = []
      while (this.randomList.length < this.countTotal) {
        let random = this.getRandomCompound()
        if (!this.randomList.includes(random) && !this.randomListOld.includes(random)) {
          this.randomList.push(random)
        }
      }
      this.randomList = this.randomList.concat(this.randomList)
      this.randomList = this.shuffle(this.shuffle(this.randomList))
    },
    compoundsGen: async function () {
      var compounds = this.compounds
      this.loading = true

      compounds = JSON.stringify(compounds)

      this.compoundsF = await this.convertAsync('HK', this.script, compounds, false, [], [])
      this.compoundsF = this.replaceCommaJSON(this.script, this.compoundsF)

      // console.log(this.compoundsF)
      this.compoundsF = _.uniq(this.compoundsF)
      // console.log(this.compoundsF)

      this.compoundsT = await this.convertAsync(this.script, 'IAST', JSON.stringify(this.compoundsF), true, [], [])

      this.randomListGen()

      this.loading = false
    },
    verify: function () {
    },
    resetHard: function () {
      this.resetV = !this.resetV
      this.selected = ['', '']
      this.matched = []
      this.autoclick = false
      this.compoundsGen()
    },
    resetSoft: function () {
      this.resetV = !this.resetV
      this.matched = []
      this.selected = ['', '']
      this.autoclick = false
      this.randomListGen()
    },
    shuffleCard: function () {
      this.randomList = this.shuffle(this.randomList)
    },
    show: function () {
      this.$refs.q1[0].$el.click()
      console.log(this.$refs.q1)
    },
    select: function (index, compound) {
      if (!this.autoclick) {
        if (index === this.selected[0] || this.matched.includes(index)) {
          this.$refs['q' + index][0].$el.click()
        } else if (this.selected[0] === '') {
          this.selected[0] = index
          this.selected[1] = compound
          console.log(index + 'clicked')
        } else {
          if (compound === this.selected[1]) {
            var dis = this
            this.$q.notify({
              type: 'positive',
              message: 'Matched ' + dis.compoundsT[compound] + ' !',
              position: 'center',
              timeout: 1000
            })

            this.matched.push(index)
            this.matched.push(this.selected[0])

            this.selected[0] = ''
            this.selected[1] = ''
          } else {
            console.log(index + 'clicked')

            this.$q.notify({
              type: 'negative',
              message: 'Not a match',
              position: 'center',
              timeout: 250
            })

            var dhis = this

            setTimeout(function () {
              dhis.autoclick = true
              dhis.$refs['q' + index][0].$el.click()
              dhis.$refs['q' + dhis.selected[0]][0].$el.click()

              dhis.selected[0] = ''
              dhis.selected[1] = ''

              dhis.autoclick = false
            }, 2000)
          }
        }
      }
    },
    shuffle: function (arr) {
      return _.shuffle(arr)
    }
  }
}
</script>

<style>
.cards {
  width: 100px;
}
.flip-list-move {
  transition: transform 1s;
}

</style>
