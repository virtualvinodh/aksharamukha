<template>
  <q-page padding>
  <h4> Learn </h4>
<div class="row q-mt-sm">
<span class="q-mt-md"> I would like to learn</span>
       <q-select
        filter
        inset
        lable="front"
        autofocus-filter
        filter-placeholder="search"
        placeholder="My Script"
        v-model="script1"
        v-on="{input: $q.platform.is.mobile ? updateLazy : compoundsGen}"
        class="q-ma-sm col-md-2"
        :options="scriptsIndic"
      />
<span class="q-ml-md q-mt-md">through </span>
       <q-select
        filter
        inset
        autofocus-filter
        filter-placeholder="search"
        placeholder="Help Script"
        v-model="script2"
        v-on="{input: $q.platform.is.mobile ? updateLazy : compoundsGen}"
        class="q-ma-sm col-md-2"
        :options="scriptsOutput"
      />   <q-spinner-comment color="dark" :size="30" v-show="loading"/>
</div>
<div class="q-mt-md q-mb-md">
    <q-btn-toggle
      class="q-ml-md"
      v-model="displaytype"
      toggle-color="dark"
      :options="[
        {label: 'Flash Cards', value: 'flashcard'},
        {label: 'Quick Overview', value: 'flipcard'},
        {label: 'Show All', value: 'showall'}
      ]"
      @input="autoflip"
    />
</div>

<q-tabs color="tertiary" no-pane-border animated swipeable inverted position="top" class="q-mt-lg q-mb-md" v-model="currentab">
  <!-- Tabs - notice slot="title" -->
  <q-tab default slot="title" name="tab-1" label="Vowels" class="print-hide"/> <br/>
  <q-tab slot="title" name="tab-2" label="consonants" class="print-hide"/>
  <q-tab slot="title" name="tab-3" label="Compounds" class="print-hide"/>
  <q-tab slot="title" name="tab-4" label="conjuncts" class="print-hide"/>
  <q-tab slot="title" name="tab-5" label="Words" class="print-hide"/>

  <q-tab-pane name="tab-1">
    <learn-component :letters1="vowels1" :letters2="vowels2" :script1="script1" :script2="script2" :letterindex="indexes['tab-1']"
     :displaytype="displaytype" @forward="indexes['tab-1'] += 1" @back="indexes['tab-1'] -= 1">
    </learn-component>
  </q-tab-pane>
  <q-tab-pane name="tab-2">
    <learn-component :letters1="consonants1" :letters2="consonants2" :script1="script1" :script2="script2" :letterindex="indexes['tab-2']"
     :displaytype="displaytype" @forward="indexes['tab-2'] += 1" @back="indexes['tab-2'] -= 1">
    </learn-component>
  </q-tab-pane>
  <q-tab-pane name="tab-3">
      <div class="q-mb-md">
        <q-chip v-for="(con, index) in consonants1" :key="con" :class="script1.toLowerCase()" class="q-ma-xs cursor-pointer"
        @click="setConselect(index)" dense :color="consselect == index ? 'dark': ''"> <font size="4">{{con}}</font></q-chip>
      </div>
      <div class="q-mt-md q-mb-md">
        <q-chip v-for="(con,index) in vowels1.slice(1).concat(['✕'])" :key="con" :class="script1.toLowerCase()" dense class="q-ma-xs cursor-pointer"
         @click="setVowselect(index)" :color="vowselect == index ? 'dark': ''">
         <font size="4">{{con}}</font> </q-chip>
      </div>
    <learn-component :letters1="currentcompund1" :letters2="currentcompund2" :script1="script1" :script2="script2" :letterindex="indexes['tab-3']"
     :displaytype="displaytype" @forward="indexes['tab-3'] += 1" @back="indexes['tab-3'] -= 1">
    </learn-component>

  </q-tab-pane>
  <q-tab-pane name="tab-4">
    <!-- <q-btn-toggle
      class="q-ml-md"
      v-model="conjunctsselected"
      toggle-color="dark"
      :options="[
        {label: 'double', value: '2S'},
        {label: 'triple', value: '3S'},
        {label: 'final', value: '1S'},
      ]"
    /> -->
        <div>
        <q-chip v-for="(con, index) in consonants1" :key="con" :class="script1.toLowerCase()" class="q-ma-xs cursor-pointer"
        @click="setConjselect(index)" dense :color="conjselect == index ? 'dark': ''"> <font size="4">{{con}}</font></q-chip>
      </div>
    <learn-component :letters1="conjunctsList1R[conjselect]" :letters2="conjunctsList2R[conjselect]" :script1="script1" :script2="script2" :letterindex="indexes['tab-4']"
     :displaytype="displaytype" @forward="indexes['tab-4'] += 1" @back="indexes['tab-4'] -= 1">
    </learn-component>
  </q-tab-pane>
  <q-tab-pane name="tab-5">
    <q-btn-toggle
      class="q-ml-md"
      v-model="wordtype"
      toggle-color="dark"
      :options="[
        {label: 'Simple', value: 'simple'},
        {label: 'Intermediate', value: 'medium'},
        {label: 'Complex', value: 'complex'}
      ]"
    />
    <q-btn class="q-ma-md" label="Generate new words"></q-btn>

    <learn-component :letters1="wordlists1Simple" :letters2="wordlists1Simple" :script1="script1" :script2="script2" :letterindex="indexes['tab-4']"
     :displaytype="displaytype" @forward="indexes['tab-4'] += 1" @back="indexes['tab-4'] -= 1">
    </learn-component>

  </q-tab-pane>
</q-tabs>
  </q-page>
</template>

<style scoped>
h4 {
  margin-top: -30px;
  margin-bottom: 10px;
}
h5 {
  margin-top: -5px;
  margin-bottom: 10px;
}
</style>

<script>
import Transliterate from '../components/Transliterate'
import {ScriptMixin} from '../mixins/ScriptMixin'
import LearnComponent from '../components/LearnComponent'
import simple from '../statics/words_simple.json'
import medium from '../statics/words_medium.json'
import complex from '../statics/words_compl.json'

var _ = require('underscore')

import {QPageSticky, QSelect, QSpinnerComment, QTabs, QTab, QTabPane, QRouteTab, QBtnToggle, QToggle, QChip} from 'quasar'

export default {
  name: 'PageIndex',
  mixins: [ScriptMixin],
  components: {
    QPageSticky,
    QChip,
    Transliterate,
    QSpinnerComment,
    QSelect,
    QTabs,
    QTab,
    LearnComponent,
    QTabPane,
    QRouteTab,
    QBtnToggle,
    QToggle
  },
  data () {
    return {
      options: {script: 'Devanagari', sourcePreserve: false},
      dash: _,
      wordtype: 'simple',
      simpleWords: simple,
      mediumWords: medium,
      complexWords: complex,
      simpleWords1: [],
      mediumWords1: [],
      complexWords1: [],
      simpleWords2: [],
      mediumWords2: [],
      complexWords2: [],
      consselect: 0,
      conjselect: 0,
      vowselect: -1,
      currentab: '',
      currentcompund1: [],
      currentcompund2: [],
      displaytype: 'flashcard',
      indexes: {'tab-1': 0, 'tab-2': 0, 'tab-3': 0, 'tab-4': 0},
      text: '',
      fullpage: true,
      dhis2: this,
      script1: 'Grantha',
      script2: 'IAST',
      vowels1: ['...'],
      vowels2: ['...'],
      consonants1: ['...'],
      consonants2: ['...'],
      compounds1: ['...'],
      compounds2: ['...'],
      conjuncts1: [],
      conjuncts2S1: [],
      conjuncts2S2: [],
      conjuncts3S1: [],
      conjuncts3S2: [],
      conjuncts4S1: [],
      conjuncts4S2: [],
      conjuncts5S1: [],
      conjuncts5S2: [],
      conjuncts1S1: [],
      conjuncts1S2: [],
      vowelOptions: [],
      conjunctsselected: '2S',
      vowel: 'a',
      loading: false,
      postOptionCon: ['SinhalaConjuncts', 'ChakmaEnableAllConjuncts'],
      wordlist1: [],
      wordlist2: [],
      flip: false
    }
  },
  watch: {
    options: function () {
      this.compoundsGen()
    },
    compounds1: function () {
      if (this.consselect !== -1) {
        console.log('I am here')
        this.currentcompund1 = this.compounds1Chunk[this.consselect].slice(0, this.vowels1.length)
      }
      if (this.vowsselect !== -1) {
        this.currentcompund1 = this.compounds1Chunk[this.vowselect].slice(0, this.vowels1.length)
      }
    },
    compounds2: function () {
      if (this.consselect !== -1) {
        this.currentcompund2 = this.compounds2Chunk[this.consselect].slice(0, this.vowels1.length)
      }
      if (this.vowsselect !== -1) {
        this.currentcompund2 = this.compounds2Chunk[this.vowselect].slice(0, this.vowels1.length)
      }
    },
    currentab: function () {
      if (this.consselect === 0 && this.currentab === 'tab-3') {
        this.currentcompund1 = this.compounds1Chunk[0].slice(0, this.vowels1.length)
        this.currentcompund2 = this.compounds2Chunk[0].slice(0, this.vowels1.length)
      }
    }
  },
  mounted: function () {
    // this.script1 = this.scriptRandom().value
    // this.compoundsGen()
    // console.log(this.vowels1)

    var dhis = this

    window.addEventListener('keydown', function (event) {
      if (event.key === 'ArrowLeft') {
        dhis.indexes[dhis.currentab] -= 1
      } else if (event.key === 'ArrowRight') {
        dhis.indexes[dhis.currentab] += 1
      }
    })

    this.compoundsGen()
  },
  computed: {
    wordlists1Simple: function () {
      var random = []

      var dhis = this

      while (random.length < 11) {
        var min = 0
        var max = this.simpleWords.length
        var rand = Math.random() * (max - min) + min
        if (!random.includes[rand]) {
          random.push(rand)
        }
      }

      random = random.map(x => Math.floor(x))

      var words = []

      random.forEach(function (index) {
        words.push(dhis.wordlist1[index])
      })

      return words
    },
    conjunctsList1: function () {
      var conjunctsAll = []
      var dhis = this
      this.compounds1ChunkV[this.vowels1.length - 1].forEach(function (cons1) {
        var conjC = []
        dhis.consonants1.forEach(function (cons2) {
          conjC.push(cons1 + cons2)
        })
        conjunctsAll.push(conjC)
      })

      return conjunctsAll
    },
    conjunctsList2: function () {
      var conjunctsAll = []
      var dhis = this
      this.compounds2ChunkV[this.vowels1.length - 1].forEach(function (cons1) {
        var conjC = []
        dhis.consonants2.forEach(function (cons2) {
          conjC.push(cons1 + cons2)
        })
        conjunctsAll.push(conjC)
      })

      return conjunctsAll
    },
    conjunctsList1R: function () {
      var dhis = this

      var conjChunks = []

      for (var i = 0; i < this.consonants1.length; i++) {
        var conjR = []
        dhis.conjunctsList1.forEach(function (letters) {
          conjR.push(letters[i])
        })
        conjChunks.push(conjR)
      }
      return conjChunks
    },
    conjunctsList2R: function () {
      var dhis = this

      var conjChunks = []

      for (var i = 0; i < this.consonants1.length; i++) {
        var conjR = []
        dhis.conjunctsList2.forEach(function (letters) {
          conjR.push(letters[i])
        })
        conjChunks.push(conjR)
      }
      return conjChunks
    },
    compounds1Chunk: function () {
      console.log(this.vowels1)
      console.log(this.vowels1.length)

      return this.dash.chunk(this.compounds1, this.vowels1.length + 1)
    },
    compounds2Chunk: function () {
      return this.dash.chunk(this.compounds2, this.vowels1.length + 1)
    },
    compounds1ChunkV: function () {
      var vowelChunks = []
      var dhis = this
      for (var i = 0; i < this.vowels1.length; i++) {
        var vowelC = []
        dhis.compounds1Chunk.forEach(function (letters) {
          vowelC.push(letters[i])
        })
        vowelChunks.push(vowelC)
      }
      return vowelChunks
    },
    compounds2ChunkV: function () {
      var vowelChunks = []
      var dhis = this
      for (var i = 0; i < this.vowels2.length; i++) {
        var vowelC = []
        dhis.compounds2Chunk.forEach(function (letters) {
          vowelC.push(letters[i])
        })
        vowelChunks.push(vowelC)
      }
      return vowelChunks
    },
    conjunsel: function () {
      var conj = [this['conjuncts' + this.conjunctsselected + '1'], this['conjuncts' + this.conjunctsselected + '2']]
      return conj
    },
    consoptions: function () {
      var options = []
      var dhis = this

      this.consonants1.forEach(function (cons, index) {
        options.push({
          label: '<span class="' + dhis.script1.toLowerCase() + '">' + cons + '</span>',
          // sublabel: '<span class="' + dhis.script2.toLowerCase() + '">' + dhis.consonants2[index] + '</span>',
          value: cons
        })
      })
      return options
    }
  },
  methods: {
    sleep: function (ms) {
      return new Promise(resolve => setTimeout(resolve, ms))
    },
    setConjselect: function (index) {
      this.conjselect = index
    },
    setConselect: function (index) {
      this.currentcompund1 = this.compounds1Chunk[index].slice(0, this.vowels1.length)
      this.currentcompund2 = this.compounds2Chunk[index].slice(0, this.vowels1.length)

      this.consselect = index
      this.vowselect = -1
    },
    setVowselect: function (index) {
      this.currentcompund1 = this.compounds1ChunkV[index]
      this.currentcompund2 = this.compounds2ChunkV[index]

      this.vowselect = index
      this.consselect = -1
    },
    autoflip: async function () {
      if (this.displaytype === 'flipcard') {
        var i
        await this.sleep(2000)
        if (this.currentab === 'tab-1') {
          for (i = 0; i < this.vowels1.length; i++) {
            this.$refs['vowel2' + i][0].$el.click()
            await this.sleep(5000)
            this.$refs['vowel2' + i][0].$el.click()
            await this.sleep(2000)
          }
        }
        if (this.currentab === 'tab-2') {
          for (i = 0; i < this.consonants1.length; i++) {
            this.$refs['consonant2' + i][0].$el.click()
            await this.sleep(5000)
            this.$refs['consonant2' + i][0].$el.click()
            await this.sleep(2000)
          }
        }
      }
    },
    updateLazy: function () {
      this.vowels1 = ['...']
      this.vowels2 = ['...']
      this.consonants1 = ['...']
      this.consonants2 = ['...']
      this.compounds1 = ['...']
      this.compounds2 = ['...']

      this.compoundsGen()
    },
    compoundsGen: async function () {
      this.loading = true
      var data = {
        script1: this.script1,
        script2: this.script2
      }
      var dhis = this
      this.apiCall.post('/syllabary', data)
        .then(function (response) {
          // console.log(response.data)
          dhis.vowels1 = response.data['vowelsScript1']
          dhis.vowels2 = response.data['vowelsScript2']
          dhis.consonants1 = response.data['consonantsScript1']
          dhis.consonants2 = response.data['consonantsScript2']
          dhis.compounds1 = response.data['compoundsScript1']
          dhis.compounds2 = response.data['compoundsScript2']
          dhis.loading = false
          // console.log(dhis.compounds1)
          // console.log(dhis.compounds2)
        })
        .catch(function (error) {
          console.log(error)
        })

      data = {
        vowel: this.vowel,
        script1: this.script1,
        script2: this.script2,
        postoptions: this.postOptionCon
      }

      this.apiCall.post('/conjuncts', data)
        .then(function (response) {
          for (var key in response.data) {
            dhis[key] = response.data[key]
          }
          dhis.loading = false
        })
        .catch(function (error) {
          console.log(error)
        })

      data = {
        source: 'Devanagari',
        target: this.script1,
        text: JSON.stringify(this.simpleWords),
        nativize: false,
        postOptions: this.postOptionCon,
        preOptions: []
      }

      // console.log('Calling with this options')
      // console.log(this.postOptions)
      this.apiCall.post('/convert', data)
        .then(function (response) {
          dhis.wordlist1 = response.data
          dhis.loading = false
        })
        .catch(function (error) {
          console.log(error)
        })

      data = {
        source: 'Devanagari',
        target: this.script2,
        text: JSON.stringify(this.simpleWords),
        nativize: false,
        postOptions: this.postOptionCon,
        preOptions: []
      }

      // console.log('Calling with this options')
      // console.log(this.postOptions)
      this.apiCall.post('/convert', data)
        .then(function (response) {
          dhis.wordlist2 = response.data
          dhis.loading = false
        })
        .catch(function (error) {
          console.log(error)
        })
    }
  }
}
</script>
