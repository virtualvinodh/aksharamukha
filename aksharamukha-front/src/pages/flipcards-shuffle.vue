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

<q-btn class="q-ml-md q-mt-md" @click="resetHard"> Play </q-btn>

      <!-- <q-toggle color="dark" v-model="conjunctsShow" label="Include conjuncts" class="q-ml-sm q-mb-sm q-mt-sm"/> -->

</div>
    <q-btn label = "Shuffle" class="q-ma-md" color="faded" @click="shuffleCard"></q-btn>
    <q-btn label = "New Set" class="q-ma-md" color="faded" @click="resetSoft"></q-btn>
    <br/>
    <p class="q-body-1 q-ma-md">Guess a character of the card and then click on the card to check your answer <q-spinner-comment color="dark" :size="30" v-show="loading"/> </p>
  <transition
   enter-active-class="animated fadeIn"
   leave-active-class="animated fadeOut"
   mode="out-in"
    >
    <span :key="resetV">
    <transition-group
    name="flip-list"
    >
      <flipcard v-for="i in randomList" :key="i" inline class="cards q-ma-sm"
       :text1="compounds1[i]" :text2="compounds2[i]" :script1="script1" :script2="script2">
      </flipcard>
    </transition-group>
    </span>
  </transition>
  </q-page>
</template>

<script>
import {QCard, QCardTitle, QCardMain, QCardMedia, QCardActions, QField, QInput, QBtnToggle, QToggle, Notify, QBtn, QSelect, QSpinnerComment} from 'quasar'
import Flipcard from '../components/Flipcard'
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
    QBtn,
    Flipcard,
    QSpinnerComment,
    QSelect
  },
  plugins: [Notify],
  mixins: [ScriptMixin],
  created: function () {
    // this.script1 = this.scriptRandom().value
    // this.script2 = this.scriptRandom().value
    // this.compoundsGen()
  },
  data () {
    return {
      countTotal: 18,
      conjunctsShow: false,
      script1: '',
      script2: '',
      compounds1: '',
      compounds2: '',
      randomList: [],
      randomListOld: [],
      resetV: true,
      loading: false
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

      this.loading = true

      compounds = JSON.stringify(compounds)
      // console.log(compounds)

      this.compounds1 = await this.convertAsync('HK', this.script1, compounds, false, [], [])
      this.compounds1 = this.replaceCommaJSON(this.script1, this.compounds1)

      // console.log('Before filtering' + this.compounds1.length)

      this.compounds1 = _.uniq(this.compounds1)
      // console.log('After filtering' + this.compounds1.length)

      // console.log('here')
      // console.log(this.compounds1)

      // this.compounds1 = await this.convertAsync('HK', this.script1, JSON.stringify(this.compounds1), true, [], [])
      // this.compounds1 = this.replaceCommaJSON(this.script1, this.compounds1)

      this.compounds2 = await this.convertAsync(this.script1, this.script2, JSON.stringify(this.compounds1), true, [], [])
      this.compounds2 = this.replaceCommaJSON(this.script2, this.compounds2)

      this.randomListGen()

      this.loading = false */
    },
    verify: function () {
    },
    resetHard: function () {
      if (this.script1 !== '' && this.script2 !== '') {
        this.resetV = !this.resetV
        this.compoundsGen()
      }
    },
    resetSoft: function () {
      this.resetV = !this.resetV
      this.randomListGen()
    },
    shuffleCard: function () {
      this.randomList = this.shuffle(this.randomList)
    },
    shuffle: function (arr) {
      return _.shuffle(arr)
    }
  }
}
</script>

<style scoped>
.cards {
  width: 100px;
}
.flip-list-move {
  transition: transform 1s;
}

</style>
