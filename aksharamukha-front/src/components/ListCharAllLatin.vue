<template>
  <div>
  <div class="row q-ma-md">
      <div class="col-xs-2 col-lg-1 q-mr-xl">
        {{script2}}
      </div>
    <div v-for="(char, index) in chars2" :key="char+index" class="col-xs-2 col-lg-1">
          <span :class="script2.toLowerCase()"> {{char}} </span>
    </div>
  </div>
      <hr/>
  <div v-for="script in scriptsRomanization" :key="script.value">
    <div class="row q-ma-md">
      <div class="col-xs-2 col-lg-1 q-mr-xl">
        {{script.label}}
      </div>
      <div v-for="(char, index) in chars1[script.value]" :key="char+index" class="col-xs-2 col-lg-1 q-mb-lg" >
        {{chars1[script.value][index]}}
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
      chars1: {'HK': ['...']},
      chars2: ['...']
    }
  },
  methods: {
    compoundsGen: async function () {
      this.$q.loading.show({
        delay: 400 // ms
      })
      this.chars2 = await this.convertAsync('HK', this.script2, JSON.stringify(this.chars), true, [], [])
      var scriptsV = this.scriptsRomanization.map(x => x.value)
      var chars1 = await this.convertLoopTgtAsync('HK', scriptsV, JSON.stringify(this.chars), true, [], [])
      for (var script in chars1) {
        if (script === 'Velthuis') {
          chars1[script] = chars1[script].replace('""', '"\\"')
        }
        this.$set(this.chars1, script, JSON.parse(chars1[script]))
      }
      this.$q.loading.hide()
    }
  }
}
</script>

<style>
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
