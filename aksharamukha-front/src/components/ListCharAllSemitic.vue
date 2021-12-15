<template>
  <div>
  <div class="row q-ma-md">
      <div class="col-xs-2 col-lg-1 q-mr-xl">
        {{script2}}
      </div>
    <div v-for="(char, index) in chars2" :key="char+index" class="col-xs-2 col-lg-1" v-if="index >= from && index <=to">
          {{char}}
    </div>
  </div>
  <div class="row q-ma-md">
      <div class="col-xs-2 col-lg-1 q-mr-xl q-mt-md">
        {{script1}} (Phonetic)
      </div>
    <div v-for="(char, index) in chars1['script2']" :key="char+index" :class="'col-xs-2 col-lg-1 q-mt-md ' + script1.toLowerCase()" v-if="index >= from && index <=to">
          <span :class="{'letter': true, 'text-red-2': chars1['script2R'][index] !== chars2[index]}"> {{char}} </span>
    </div>
  </div>
    <div class="row q-ma-md">
      <div class="col-xs-2 col-lg-1 q-mr-xl q-mt-md">
        {{script1}} (Genealogical)
      </div>
    <div v-for="(char, index) in chars1['script2G']" :key="char+index" :class="'col-xs-2 col-lg-1 q-mt-md ' + script1.toLowerCase()" v-if="index >= from && index <=to">
        <span :class="{'letter': true, 'text-red-2': chars1['script2GR'][index] !== chars2[index]}"> {{char}} </span>    </div>
  </div>
      <hr/>
  <!-- add hebrew to the list -->
  <div v-for="script in scriptSemiticSortedHebr" :key="script.value" v-if="script.value !== 'Latn' && filterscripts.includes(script.value)">
    <div class="row q-ma-md">
      <div class="col-xs-2 col-lg-1 q-mr-xl">
        <router-link :to="'/describesemitic/' + script.value" v-if="script.value !== 'Hebr'">{{script.label}}</router-link>
        <router-link :to="'/describe/Hebrew'" v-if="script.value === 'Hebr'">{{script.label}}</router-link>
      </div>
      <div v-for="(char, index) in chars1[script.value]" :key="char+index" class="col-xs-2 col-lg-1 q-mb-lg" v-if="index >= from && index <=to">
          <span :class="script.value.toLowerCase()">
          <span :class="{'letter': true, 'text-red-2': chars1[script.value+'R'][index] !== chars2[index]}">
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
  props: ['chars', 'chars1', 'chars2', 'charsIr', 'script2', 'filterscripts', 'script1', 'from', 'to'],
  mixins: [ScriptMixin],
  created: function () {
    this.compoundsGen()
    // console.log(this.filterscripts)
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
