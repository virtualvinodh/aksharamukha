<template>
  <q-page padding>
    <h5> Internal Documentation </h5> <br/><br/>
    <p class="q-body-1"> Listed below are the script identifiers and various flags that you can use for advanced transliteration in the Web API and the Python pip package.</p>

    <h5> Script Identifiers </h5>
    <br/>
    <table class="q-body-1">
      <tr>
        <td><b>Script Name</b></td>
        <td><b>Script Identifier</b></td>
      </tr>
    <tr v-for="script in scriptsOutput" :key="script.value">
      <td>{{script.label}}</td>
      <td><i>{{script.value}}</i></td>
    </tr>
    </table>

    <h5> Post Options </h5>
    <div v-for="key in Object.keys(postOptionsGroup)" :key="key + 'post'">
      <h6> {{getScriptObject(key).label}} </h6> <br/>
      <div>
        <table class="q-body-1">
          <tr v-for="opt in postOptionsGroup[key]" :key="opt.value + opt.key">
            <td v-html="opt.label"></td>
            <td><i>{{opt.value}}</i></td>
          </tr>
        </table>
      </div>
    </div>

    <h5> Pre Options </h5>

    <div v-for="key in Object.keys(preOptionsGroup)" :key="key+'pre'">
      <h6> {{getScriptObject(key).label}} </h6> <br/>
      <div>
        <table class="q-body-1">
          <tr v-for="opt in preOptionsGroup[key]" :key="opt.value + opt.key">
            <td v-html="opt.label"></td>
            <td><i>{{opt.value}}</i></td>
          </tr>
        </table>
      </div>
    </div>

  </q-page>
</template>

<script>
import { QTooltip, QPageSticky } from 'quasar'
import { ScriptMixin } from '../mixins/ScriptMixin'

export default {
  // name: 'PageName',
  mixins: [ScriptMixin],
  components: {
    QTooltip,
    QPageSticky
  },
  data () {
    return {
    }
  }
}
</script>

<style scoped>
h6 {
  margin-bottom: -10px;
}
h5 {
  margin-bottom: -10px;
}
table, td {
  border: 0.5px solid;
  border-collapse: collapse;
}
td {
  padding: 10px;
}
</style>
