<template>
  <div>
  <div class="row q-ma-md">
      <div class="col-xs-2 col-lg-1 q-mr-xl">
        {{script2}}
      </div>
    <div v-for="(char, index) in chars2" :key="char+index" class="col-xs-2 col-lg-1">
          {{char}}
    </div>
  </div>
      <hr/>
  <div v-for="script in scriptsIndic" :key="script.value">
    <div class="row q-ma-md">
      <div class="col-xs-2 col-lg-1 q-mr-xl">
        {{script.label}}
      </div>
      <div v-for="(char, index) in chars1[script.value]" :key="char+index" class="col-xs-2 col-lg-1 q-mb-lg" >
          <span :class="script.value.toLowerCase()">
          <span :class="{'letter': true, 'text-red-2': charsIr[script.value][index] !== chars[index], 'text-blue-4': checkDiacritics(chars1[script.value][index])}">
            {{chars1[script.value][index]}}
          </span> </span>
      </div>
    </div>
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
      this.chars2 = await this.convertAsync('HK', this.script2, JSON.stringify(this.chars), true, [], [])
    },
    script1: async function () {
      this.chars1 = await this.convertAsync('HK', this.script1, JSON.stringify(this.chars), true, [], [])
      this.charsIr = await this.convertAsync(this.script1, 'HK', JSON.stringify(this.chars1), false, [], [])
    }
  },
  data () {
    return {
      chars1: {'Avestan': ['...']},
      chars2: ['...'],
      charsIr: {'Avestan': ['...']}
    }
  },
  methods: {
    compoundsGen: async function () {
      this.$q.loading.show({
        delay: 400 // ms
      })
      this.chars2 = await this.convertAsync('HK', this.script2, JSON.stringify(this.chars), true, [], [])
      var scriptsV = this.scriptsIndic.map(x => x.value)
      var chars1 = await this.convertLoopTgtAsync('HK', scriptsV, JSON.stringify(this.chars), true, [], [])
      for (var script in chars1) {
        if (script === 'Urdu' || script === 'Thaana') {
          chars1[script] = chars1[script].replace(/،/g, ',')
        }
        this.$set(this.chars1, script, JSON.parse(chars1[script]))
      }
      var charsIr = await this.convertLoopSrcAsync(scriptsV, 'HK', JSON.stringify(this.chars1), true, [], [])
      for (script in charsIr) {
        this.$set(this.charsIr, script, charsIr[script])
      }
      this.$q.loading.hide()
    }
  }
}
</script>

<style scoped>
.row {
}
.letter {
  font-size: 25px;
}
.col-lg-1 {
  border-left: 0px solid black;
  text-align: center;
}
.block {
  display:inline-block;
}
</style>
