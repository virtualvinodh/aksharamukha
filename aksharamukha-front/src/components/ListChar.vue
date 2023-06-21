<template>
  <div class="row">
    <div v-for="(char, index) in chars2" :key="char+index" class="col-xs-2 col-lg-1 q-mb-lg">
      <span :class="getOutputClass(script2, [], char)"> {{char}} </span> <br/>
      <span :class="checkDiacritics(chars1[index]) ? 'text-blue-4' : ''">
        <span :class="getOutputClass(script1, [], chars1[index])">
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
  props: ['chars', 'script1', 'script2', 'chars1', 'chars2', 'charsIr'],
  mixins: [ScriptMixin],
  created: function () {
    this.compoundsGen()
  },
  data () {
    return {
    }
  },
  methods: {
  }
}
</script>

<style scoped>
.letter {
  font-size: 25px;
}
.block {
  display:inline-block;
}
</style>
