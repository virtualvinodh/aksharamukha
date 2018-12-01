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
  props: ['chars', 'script1', 'script2', 'chars1', 'chars2'],
  mixins: [ScriptMixin],
  created: function () {
    this.compoundsGen()
  },
  data () {
    return {
    }
  },
  methods: {
    compoundsGen: async function () {
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
