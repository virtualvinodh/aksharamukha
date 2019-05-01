<template>
  <q-page padding>
  <!-- Batak add vowel signs -->
  <!-- Add Sinhala pre-nsalized signs -->
<div class="row q-mt-sm">
<span class="q-mt-md"> Main: </span>
       <q-select
        filter
        inset
        lable="front"
        autofocus-filter
        filter-placeholder="search"
        placeholder="Input Script"
        v-model="script1"
        @input="compoundsGen"
        class="q-ma-sm col-md-3"
        :options="scriptsIndic"
      />
<span class="q-ml-md q-mt-md"> Guide: </span>
       <q-select
        filter
        inset
        autofocus-filter
        filter-placeholder="search"
        placeholder="Input Script"
        v-model="script2"
        @input="compoundsGen"
        class="q-ma-sm col-md-3"
        :options="scriptsOutput"
      />
      <!-- <q-toggle color="dark" v-model="conjunctsShow" label="Include conjuncts" class="q-ml-sm q-mb-sm q-mt-sm"/> -->

</div>
      <div class="q-mt-lg">Select a script to view its syllabary</div>

      <h5> Vowels <q-spinner-comment color="dark" :size="30" v-show="loading"/> </h5>
      <span v-for="(vowel, index) in vowels1" :key="vowel+index+'k'">
         <learncard :script1="script1" :text1="vowel" :script2="script2" :text2="vowels2[index]"> </learncard>
      </span>
      <h5> Consonants </h5>
      <span v-for="(consonant, index) in consonants1" :key="consonant+index+'k1'">
         <learncard :script1="script1" :text1="consonant" :script2="script2" :text2="consonants2[index]"> </learncard>
      </span>
      <h5> Compounds </h5>
      <span v-for="(compound, index) in compounds1" :key="compound+index+'k2'" v-if="!compound.includes('&')">
         <learncard :script1="script1" :text1="compound" :script2="script2" :text2="compounds2[index]"> </learncard>
      </span>
      <span v-else>
        <br/>
      </span>
  </q-page>
</template>

<style>
</style>

<script>
import Learncard from '../components/Learncard'
import Transliterate from '../components/Transliterate'
import {ScriptMixin} from '../mixins/ScriptMixin'
import {QPageSticky, QSelect, QSpinnerComment} from 'quasar'

export default {
  name: 'PageIndex',
  mixins: [ScriptMixin],
  components: {
    QPageSticky,
    Transliterate,
    Learncard,
    QSpinnerComment,
    QSelect
  },
  data () {
    return {
      options: {script: 'Devanagari', sourcePreserve: false},
      text: '',
      script1: '',
      script2: 'IAST',
      vowels1: ['...'],
      vowels2: ['...'],
      consonants1: ['...'],
      consonants2: ['...'],
      compounds1: ['...'],
      compounds2: ['...'],
      loading: false
    }
  },
  watch: {
    options: function () {
      this.compoundsGen()
    }
  },
  mounted: function () {
    // this.script1 = this.scriptRandom().value
    // this.compoundsGen()
    // console.log(this.vowels1)
  },
  methods: {
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

      /* if (this.script1 !== 'Tamil') {
        this.vowels1 = await this.convertAsync('HK', this.script1, JSON.stringify(this.vowelsAll), true, ['RemoveDiacritics'], [])
      } else {
        this.vowels1 = await this.convertAsync('HK', this.script1, JSON.stringify(this.vowelsAll), true, ['RemoveDiacriticsTamil'], [])
      }

      this.vowels1 = this.replaceCommaJSON(this.script1, this.vowels1)

      var vowels1HK = await this.convertAsync(this.script1, 'HK', JSON.stringify(this.vowels1), true, [], [])
      var vowelsAllL = _.intersection(this.vowelsAll, vowels1HK)

      if (this.script1 !== 'Tamil') {
        this.vowels1 = await this.convertAsync('HK', this.script1, JSON.stringify(vowelsAllL), true, ['RemoveDiacritics'], [])
      } else {
        vowelsAllL = _.difference(vowelsAllL, ['aE', 'aO'])
        this.vowels1 = await this.convertAsync('HK', this.script1, JSON.stringify(vowelsAllL), true, ['RemoveDiacriticsTamil'], [])
      }

      this.vowels1 = this.replaceCommaJSON(this.script1, this.vowels1)

      this.vowels1 = _.uniq(this.vowels1)

      // var vowruHK = await this.convertAsync(this.script1, 'HK', JSON.stringify(vowru), true, [], [])
      // this.vowels1 = _.difference(this.vowels1, vowru)

      // minux ru rU lu lU

      this.vowels2 = await this.convertAsync(this.script1, this.script2, JSON.stringify(this.vowels1), true, [], [])
      this.vowels2 = this.replaceCommaJSON(this.script2, this.vowels2)

      if (this.script1 === 'Sinhala') {
        this.consonantsAll = this.consonantsAll.concat(['n*g', 'n*j', 'n*D', 'n*d', 'm*b'])
      } else {
        this.consonantsAll = _.difference(this.consonantsAll, ['n*g', 'n*j', 'n*D', 'n*d', 'm*b'])
      }

      this.consonants1 = await this.convertAsync('HK', this.script1, JSON.stringify(this.consonantsAll.map(x => x + 'a')), true, ['RemoveDiacritics'], [])
      this.consonants1 = this.replaceCommaJSON(this.script1, this.consonants1)

      this.consonants1 = _.uniq(this.consonants1)
      this.consonants2 = await this.convertAsync(this.script1, this.script2, JSON.stringify(this.consonants1), true, [], [])
      this.consonants2 = this.replaceCommaJSON(this.script2, this.consonants2)

      var compounds = []

      var vowelsLocal = vowelsAllL.slice(1)

      if (this.script1 === 'BatakSima') {
        vowelsLocal.push('e')
        vowelsLocal.push('o')
        vowelsLocal.push('au')
      }

      if (this.script1 === 'BatakManda') {
        vowelsLocal.push('e')
        vowelsLocal.push('o')
      }

      if (this.script1 === 'BatakPakpak') {
        vowelsLocal.push('e')
        vowelsLocal.push('aE')
        vowelsLocal.push('o')
      }

      if (this.script1 === 'BatakToba') {
        vowelsLocal.push('e')
        vowelsLocal.push('o')
      }

      if (this.script1 === 'BatakKaro') {
        vowelsLocal.push('e')
        vowelsLocal.push('aE')
        vowelsLocal.push('o')
        vowelsLocal.push('aO')
      }

      for (let i = 0; i < this.consonantsAll.length; i++) {
        for (let j = 0; j < vowelsLocal.length; j++) {
          compounds.push(this.consonantsAll[i] + vowelsLocal[j])
        }
        compounds.push(this.consonantsAll[i])
        compounds.push('&' + this.consonantsAll[i])
      }

      console.log(compounds)

      this.compounds1 = await this.convertAsync('HK', this.script1, JSON.stringify(compounds), true, ['RemoveDiacritics'], [])
      this.compounds1 = this.replaceCommaJSON(this.script1, this.compounds1)

      this.compounds1 = _.uniq(this.compounds1)
      this.compounds1 = _.difference(this.compounds1, this.consonants1)
      this.compounds2 = await this.convertAsync(this.script1, this.script2, JSON.stringify(this.compounds1), true, [], [])
      this.compounds2 = this.replaceCommaJSON(this.script2, this.compounds2) */
    }
  }
}
</script>
