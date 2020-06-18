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
  <div v-for="script in scriptsIndic" :key="script.value" v-if="filterscripts.includes(script.value)">
    <div class="row q-ma-md">
      <div class="col-xs-2 col-lg-1 q-mr-xl">
        <router-link :to="'/describe/' + script.value">{{script.label}}</router-link>
      </div>
      <div v-for="(char, index) in chars1[script.value]" :key="char+index" class="col-xs-2 col-lg-1 q-mb-lg" >
          <span :class="script.value.toLowerCase()">
          <span :class="{'letter': true, 'text-red-2': charsIr[script.value][index] !== chars[index], 'text-blue-4': checkDiacritics(chars1[script.value][index])}">
            {{chars1[script.value][index]}}
          </span> </span>
      </div>
    </div>
  </div>
  <br/><br/>
</div>
</template>

<script>
import {ScriptMixin} from '../mixins/ScriptMixin'

export default {
  // name: 'ComponentName',
  props: ['chars', 'chars1', 'chars2', 'charsIr', 'script2', 'filterscripts'],
  mixins: [ScriptMixin],
  created: function () {
    this.compoundsGen()
    console.log(this.filterscripts)
  },
  data () {
    return {
    }
  },
  methods: {
    compoundsGen: async function () {
      /*
      this.chars2 = await this.convertAsync('HK', this.script2, JSON.stringify(this.chars), true, [], [])
      var charsIr = await this.convertLoopSrcAsync(scriptsV, 'HK', JSON.stringify(this.chars1), true, [], [])
      for (script in charsIr) {
        this.$set(this.charsIr, script, charsIr[script])
      }
      this.$q.loading.hide()
      */
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
