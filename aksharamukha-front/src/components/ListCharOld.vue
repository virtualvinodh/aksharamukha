<template>
  <div class="row">
    <div v-for="(char, index) in chars2" :key="char+index" class="col-xs-2 col-lg-1 q-mb-lg">
      <span :class="script2.toLowerCase()"> {{char}} </span> <br/>
      <span :class="checkDiacritics(chars1[index]) ? 'text-blue-4' : ''">
        <span :class="script1.toLowerCase()">
          <span class="letter" :class="charsIr[index] !== chars[index] ? 'text-red-2' : ''"> {{chars1[index]}}
          </span>
        </span>
      </span>
    </div>
  </div>
</template>

<script>
import {ScriptMixin} from '../mixins/ScriptMixin'

export default {
  // name: 'ComponentName',
  props: ['chars', 'script1', 'script2'],
  mixins: [ScriptMixin],
  created: function () {
    this.compoundsGen()
  },
  watch: {
    script2: async function () {
      this.chars2 = ['...']
      this.chars2 = await this.convertAsync('HK', this.script2, JSON.stringify(this.chars), true, [], [])
    },
    script1: async function () {
      this.$q.loading.show({
        delay: 400 // ms
      })

      this.chars1 = ['...']
      this.chars1 = await this.convertAsync('HK', this.script1, JSON.stringify(this.chars), true, [], [])
      if (this.script1 === 'Urdu' || this.script1 === 'Thaana') {
        this.chars1 = JSON.parse(this.chars1.replace(/،/g, ','))
      }
      this.charsIr = await this.convertAsync(this.script1, 'HK', JSON.stringify(this.chars1), false, [], [])

      this.$q.loading.hide()
    }
  },
  data () {
    return {
      chars1: ['...'],
      chars2: ['...'],
      charsIr: ['...']
    }
  },
  methods: {
    compoundsGen: async function () {
      this.$q.loading.show({
        delay: 400 // ms
      })

      this.chars1 = await this.convertAsync('HK', this.script1, JSON.stringify(this.chars), true, [], [])
      if (this.script1 === 'Urdu' || this.script1 === 'Thaana') {
        this.chars1 = JSON.parse(this.chars1.replace(/،/g, ','))
      }
      this.chars2 = await this.convertAsync('HK', this.script2, JSON.stringify(this.chars), true, [], [])
      this.charsIr = await this.convertAsync(this.script1, 'HK', JSON.stringify(this.chars1), true, [], [])

      this.$q.loading.hide()
    }
  }
}
</script>

<style>
.letter {
  font-size: 25px;
}
.block {
  display:inline-block;
}
</style>
