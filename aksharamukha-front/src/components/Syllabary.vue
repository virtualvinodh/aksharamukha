<template>
      <span>
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
        <br/><br/><br/><br/>
      </span>
    </span>
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
  props: ['script1', 'script2'],
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
    script1: function () {
      this.compoundsGen()
    },
    script2: function () {
      this.compoundsGen()
    }
  },
  mounted: function () {
    this.compoundsGen()
  },
  methods: {
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
    }
  }
}
</script>
