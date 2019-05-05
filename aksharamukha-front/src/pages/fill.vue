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
<span class="q-mt-md"> Front: </span>
       <q-select
        filter
        inset
        lable="front"
        autofocus-filter
        filter-placeholder="search"
        placeholder="Input Script"
        v-model="script1"
        class="q-ma-sm col-md-3"
        :options="scriptsOutput"
      />
<span class="q-ml-md q-mt-md"> Back: </span>
       <q-select
        filter
        inset
        autofocus-filter
        filter-placeholder="search"
        placeholder="Input Script"
        v-model="script2"
        class="q-ma-sm col-md-3"
        :options="scriptsOutput"
      />
<q-btn class="q-ml-md q-mt-md" @click="reset"> Play </q-btn>
      <!-- <q-toggle color="dark" v-model="conjunctsShow" label="Include conjuncts" class="q-ml-sm q-mb-sm q-mt-sm"/> -->

</div>
<p class="q-body-1 q-mt-md"> Fill in the equivalent of {{script1}} letters in {{script2}} <q-spinner-comment color="dark" :size="30" v-show="loading"/></p>
  <transition
   enter-active-class="animated fadeIn"
   leave-active-class="animated fadeOut"
   mode="out-in"
    >
    <span :key="resetV">
      <q-card v-for="(i,index) in randomList" :key="i" inline class="cards q-ma-sm"
       :text-color="colors(index)">
        <q-input class="q-ml-xl q-mr-xl" placeholder="answer" ref="'q' + i" v-model="answers['q' + index]" :class="script2.toLowerCase()"></q-input>
        <q-card-main align="center">
          <font size="7"><span :class="script1.toLowerCase()">{{compounds1[i]}}</span></font>
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
                {label: compounds2[randomOptions[index][0]], value: compounds2[randomOptions[index][0]]},
                {label: compounds2[randomOptions[index][1]], value: compounds2[randomOptions[index][1]]},
                {label: compounds2[randomOptions[index][2]], value: compounds2[randomOptions[index][2]]}
                ]"
              flat
              dense
              size="11px"
              :class="script2.toLowerCase()"
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
  <q-btn label = "Play again" class="q-ma-lg" color="faded" @click="resetSoft"></q-btn>
  Result : {{correct}} / {{countTotal}}
  <br/>
  </q-page>
</template>

<script>
import {QCard, QCardTitle, QCardMain, QCardMedia, QCardActions, QField, QInput, QBtnToggle, QToggle, QSelect, QSpinnerComment} from 'quasar'
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
  mixins: [ScriptMixin],
  mounted: function () {
    // this.script1 = this.scriptRandom().value
    // this.script2 = this.scriptRandom().value
    // this.compoundsGen()
  },
  computed: {
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
      script1: '',
      script2: '',
      compounds1: '',
      compounds2: '',
      options: [],
      answers: {},
      results: [],
      randomList: [],
      randomListOld: [],
      randomOptions: [],
      common: [],
      loading: false,
      resetV: true,
      selections: true
    }
  },
  methods: {
    getRandomInt: function (min, max) {
      return Math.floor(Math.random() * (max - min + 1)) + min
    },
    getRandomCompound: function () {
      return this.getRandomInt(0, this.compounds1.length - 1)
    },
    randomListGen: function () {
      this.randomListOld = this.randomList.slice()
      this.randomList = []
      this.randomOptions = []
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
    compoundsGen: async function () {
      this.loading = true

      var data = {
        // letters: this.compounds,
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

      /* compounds = JSON.stringify(compounds)

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

      this.common = _.intersection(compounds1Hk, compounds2Hk)
      console.log(this.common)
      console.log(this.common.length)

      this.compounds1 = await this.convertAsync('HK', this.script1, JSON.stringify(this.common), false, [], [])
      this.compounds1 = this.replaceCommaJSON(this.script1, this.compounds1)

      this.compounds2 = await this.convertAsync('HK', this.script2, JSON.stringify(this.common), false, [], [])
      this.compounds2 = this.replaceCommaJSON(this.script2, this.compounds2)

      this.randomListGen()

      this.$q.loading.hide() */
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
        this.results.push(this.answers['q' + i].trim() === this.compounds2[this.randomList[i]])
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
      if (this.script1 !== '' && this.script2 !== '') {
        this.results = []
        this.answers = []
        this.resetV = !this.resetV
        this.compoundsGen()
      }
    },
    resetSoft: function () {
      this.results = []
      this.answers = []
      this.resetV = !this.resetV
      this.randomListGen()
    },
    show: function () {
      this.results = []
      for (let i = 0; i < this.countTotal; i++) {
        this.answers['q' + i] = this.compounds2[this.randomList[i]]
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
.q-card-title {
  width:20px;
}
</style>
