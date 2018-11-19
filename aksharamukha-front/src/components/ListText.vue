<template>
  <div>
  <div v-for="script in scriptsIndic" :key="script.value">
    <div class="row q-ma-md">
      <div class="col-xs-2 col-lg-2 q-mr-lg">
        {{script.label}}
      </div>
      <div v-for="(char, index) in chars1[script.value]" :key="char+index" class="col-xs-9 col-lg-9 q-mb-lg" >
          <span :class="script.value.toLowerCase()">
          <span :class="{'letter': true, 'text-red-4': charsIr[script.value][index] !== chars2[index], 'text-blue-4': checkDiacritics(chars1[script.value][index])}">
            {{chars1[script.value][index]}}
          </span> </span>
            <span v-if="charsIr[script.value][index] !== chars2[index]">
              ( <transliterate :text="charsIr[script.value][index]" src="HK" :tgt="script2" :sourcePreserve="true" :postOptions="[]">
        </transliterate> )
            </span>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import {ScriptMixin} from '../mixins/ScriptMixin'
import Transliterate from '../components/Transliterate'

export default {
  // name: 'ComponentName',
  props: ['chars', 'script1', 'script2', 'sourcePreserve'],
  components: {
    Transliterate
  },
  mixins: [ScriptMixin],
  created: function () {
    this.compoundsGen()
  },
  watch: {
    chars: function () {
      this.compoundsGen()
    }
  },
  data () {
    return {
      chars1: {},
      chars2: ['...'],
      charsIr: {}
    }
  },
  methods: {
    compoundsGen: async function () {
      if (this.chars.length === 0) {
        return
      }
      this.chars2 = await this.convertAsync(this.script2, 'HK', JSON.stringify(this.chars), true, [], [])
      var scriptsV = this.scriptsIndic.map(x => x.value)
      var chars1 = await this.convertLoopTgtAsync(this.script2, scriptsV, JSON.stringify(this.chars), this.sourcePreserve, [], [])
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

      this.$emit('loaded')
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
