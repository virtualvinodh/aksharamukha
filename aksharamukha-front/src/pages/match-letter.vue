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
<div class="row q-mt-sm">
<span class="q-mt-md"> Deck 1: </span>
       <q-select
        filter
        inset
        lable="front"
        autofocus-filter
        filter-placeholder="search"
        placeholder="Input Script"
        v-model="script1"
        @input="reset"
        class="q-ma-sm col-md-3"
        :options="scriptsOutput"
      />
<span class="q-ml-md q-mt-md"> Deck 2: </span>
       <q-select
        filter
        inset
        autofocus-filter
        filter-placeholder="search"
        placeholder="Input Script"
        v-model="script2"
        @input="reset"
        class="q-ma-sm col-md-3"
        :options="scriptsOutput"
      />

      <!-- <q-toggle color="dark" v-model="conjunctsShow" label="Include conjuncts" class="q-ml-sm q-mb-sm q-mt-sm"/> -->

</div>
  <p class="q-body-1 q-ma-md"> Click a card in one deck and then click a card on the other deck to find a match <q-spinner-comment color="dark" :size="30" v-show="loading"/> </p>
  <transition
   enter-active-class="animated fadeIn"
   leave-active-class="animated fadeOut"
   mode="out-in"
    >
    <span :key="resetV">
    <transition-group
    name="flip-list"
    >
      <q-card v-for="(i,index) in randomList" :key="i" inline class="cards q-ma-sm"
       @click.native="select(parseInt(index), 1)" :color="typeof colors1[index] === 'undefined' ? '' : colors1[index]">
        <q-card-main align="center">
          <font size="6"><span :class="script1.toLowerCase()">{{compounds1[i]}}</span></font>
        </q-card-main>
      </q-card>
    </transition-group>
    </span>
  </transition>
  <hr/>
  <transition
   enter-active-class="animated fadeIn"
   leave-active-class="animated fadeOut"
   mode="out-in"
    >
    <span :key="resetV">
  <transition-group
    name="flip-list"
    >
      <q-card v-for="(i,index) in randomList2" :key="i" inline class="cards q-ma-sm"
       @click.native="select(parseInt(index), 2)" :color="typeof colors2[index] === 'undefined' ? '' : colors2[index]">
        <q-card-main align="center">
          <font size="6"><span :class="script2.toLowerCase()"> {{compounds2[i]}} </span></font>
        </q-card-main>
      </q-card>
    </transition-group>
    </span>
  </transition>
  <br/>
  <q-btn label = "Shuffle" class="q-ma-lg" color="faded" @click="shuffleCard"
          :class="{disabled:!isEmpty(colors1) && !isEmpty(colors2)}"></q-btn>
  <q-btn label = "Show answers" class="q-ma-lg" color="faded" @click="show"></q-btn>
  <q-btn label = "Play again" class="q-ma-lg" color="faded" @click="resetSoft"></q-btn>
  <br/>
  </q-page>
</template>

<script>
import {QCard, QCardTitle, QCardMain, QCardMedia, QCardActions, QField, QInput, QBtnToggle, QToggle, Notify, QSelect, QSpinnerComment} from 'quasar'
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
    QSpinnerComment,
    QSelect
  },
  plugins: [Notify],
  mixins: [ScriptMixin],
  mounted: function () {
    this.script1 = this.scriptRandom().value
    this.script2 = this.scriptRandom().value
    this.compoundsGen()
  },
  computed: {
  },
  data () {
    return {
      countTotal: 12,
      script1: 'Gujarati',
      script2: 'Saurashtra',
      answers: {},
      colors1: {},
      colors2: {},
      selected1: ['', ''],
      selected2: ['', ''],
      randomList: [],
      randomList2: [],
      randomListOld: [],
      resetV: true,
      compounds1: [],
      loading: true,
      compounds2: []
    }
  },
  methods: {
    getRandomCompound: function () {
      return this.getRandomInt(0, this.compounds1.length - 1)
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
      this.randomList2 = this.shuffle(this.randomList)
    },
    compoundsGen: async function () {
      this.loading = true

      var data = {
        letters: this.compounds,
        script1: this.script1,
        script2: this.script2
      }

      var dhis = this

      this.apiCall.post('/commonletters', data)
        .then(function (response) {
          dhis.compounds1 = response.data['script1']
          dhis.compounds2 = response.data['script2']

          dhis.randomListGen()

          dhis.loading = false
        })
        .catch(function (error) {
          console.log(error)
        })

      /* var compounds = this.compounds

      compounds = JSON.stringify(compounds)

      this.compounds1 = await this.convertAsync('HK', this.script1, compounds, false, [], [])
      this.compounds1 = this.replaceCommaJSON(this.script1, this.compounds1)
      this.compounds1 = _.uniq(this.compounds1)

      this.compounds2 = await this.convertAsync('HK', this.script2, compounds, false, [], [])
      this.compounds2 = this.replaceCommaJSON(this.script2, this.compounds2)
      this.compounds2 = _.uniq(this.compounds2)

      var compounds1Hk = await this.convertAsync(this.script1, 'HK', JSON.stringify(this.compounds1), false, [], [])
      var compounds2Hk = await this.convertAsync(this.script2, 'HK', JSON.stringify(this.compounds2), false, [], [])

      console.log(compounds1Hk)
      console.log(compounds2Hk)

      var common = _.intersection(compounds1Hk, compounds2Hk)
      console.log(common)
      console.log(common.length)

      this.compounds1 = await this.convertAsync('HK', this.script1, JSON.stringify(common), false, [], [])
      this.compounds1 = this.replaceCommaJSON(this.script1, this.compounds1)

      this.compounds2 = await this.convertAsync('HK', this.script2, JSON.stringify(common), false, [], [])
      this.compounds2 = this.replaceCommaJSON(this.script2, this.compounds2)

      this.randomListGen() */
    },
    verify: function () {
    },
    reset: function () {
      this.results = []
      this.answers = []
      this.colors1 = {}
      this.colors2 = {}
      this.resetV = !this.resetV
      this.compoundsGen()
    },
    resetSoft: function () {
      this.results = []
      this.answers = []
      this.colors1 = {}
      this.colors2 = {}
      this.resetV = !this.resetV
      this.randomListGen()
    },
    shuffleCard: function () {
      if (this.isEmpty(this.colors1)) {
        this.randomList = this.shuffle(this.randomList)
      }
      if (this.isEmpty(this.colors2)) {
        this.randomList2 = this.shuffle(this.randomList)
      }
    },
    show: function () {
      this.$set(this, 'colors1', [])
      this.$set(this, 'colors2', [])
      this.randomList2 = this.randomList.slice()
    },
    isEmpty: function (obj) {
      return Object.keys(obj).length === 0 && obj.constructor === Object
    },
    select: function (index, script) {
      if (this['colors' + script][this['selected' + script][0]] !== 'dark') {
        this.$set(this['colors' + script], this['selected' + script][0], '')
      }

      this['selected' + script][0] = index
      this['selected' + script][1] = true

      this.$set(this, 'selected' + script, this['selected' + script])

      if (this['colors' + script][index] !== 'dark') {
        this.$set(this['colors' + script], index, 'light')
      }
      if (script === 1) {
        if (this.compounds[this.randomList[index]] === this.compounds[this.randomList2[this['selected2'][0]]]) {
          this.$set(this['colors' + script], index, 'dark')
          this.$set(this['colors' + 2], this['selected2'][0], 'dark')

          this.$q.notify({
            type: 'positive',
            message: 'Match!',
            position: 'center',
            timeout: 250
          })
        }
      } else {
        if (this.compounds[this.randomList2[index]] === this.compounds[this.randomList[this['selected1'][0]]]) {
          this.$set(this['colors' + script], index, 'dark')
          this.$set(this['colors' + 1], this['selected1'][0], 'dark')

          this.$q.notify({
            type: 'positive',
            message: 'Match!',
            position: 'center',
            timeout: 250
          })
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
