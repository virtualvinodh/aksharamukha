<template>
  <div>
  <div v-for="script in scriptsIndic" :key="script.value">
    <div class="row q-ma-md">
      <div class="col-xs-2 col-lg-2 q-mr-lg">
        <span><router-link :to="'/describe/' + script.value">{{script.label}}</router-link>
        </span>
      </div>
      <div v-for="(char, index) in chars1[script.value]" :key="char+index" class="col-xs-9 col-lg-9 q-mb-lg" >
          <span :class="script.value.toLowerCase()">
          <span :class="{'letter': true, 'text-red-4': charsIr[script.value][index] !== chars2[index], 'text-blue-4': checkDiacritics(chars1[script.value][index])}">
            {{chars1[script.value][index]}}
          </span>
            <q-tooltip v-html="getDescription(script, false)" v-show="desc === 'tooltip'"></q-tooltip>
            </span>
            <span v-if="charsIr[script.value][index] !== chars2[index]">
              ( <transliterate :text="charsIr[script.value][index]" src="HK" :tgt="script2" :sourcePreserve="true" :postOptions="[]">
        </transliterate> )
            </span>
      </div>
    </div>
    <transition
  appear
  enter-active-class="animated fadeIn"
  leave-active-class="animated fadeOut"
>
    <div class="q-body-1" v-html="getDescription(script, false)" v-show="desc === 'textblock'"></div>
    </transition>
  </div>
</div>
</template>

<script>
const rp = require('request-promise')

import {ScriptMixin} from '../mixins/ScriptMixin'
import Transliterate from '../components/Transliterate'
import {QTooltip} from 'quasar'

export default {
  // name: 'ComponentName',
  props: ['chars', 'script1', 'script2', 'sourcePreserve', 'desc'],
  components: {
    Transliterate,
    QTooltip
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
  mounted: function () {
    /* var dhis = this
    this.scriptsIndic.forEach(function (script) {
      dhis.scriptDesc(script)
    })
    console.log(this.scriptDescription) */
  },
  data () {
    return {
      chars1: {},
      chars2: ['...'],
      charsIr: {},
      scriptDescription: {}
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
    },
    scriptDesc: function (script) {
      // let scriptNew = script.value.split(/(?=[A-Z])/).join(' ')

      //
      var url = 'https://cors-escape.herokuapp.com/http://scriptsource.org/cms/scripts/page.php?item_id=script_detail&key=Zanb'

      rp(url)
        .then(function (html) {
          var parser = new DOMParser()
          var htmlDoc = parser.parseFromString(html, 'text/html')
          console.log(htmlDoc.getElementsByClassName('contentBody')[0].innerText.split('\n')[0])
        })
        .catch(function (err) {
          console.log(err)
        })

      /* var url = 'https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=true&explaintext&origin=*&redirects=1&titles=' + scriptNew + '_script'

      var dhis = this

      this.wikipediaCall.get(url)
        .then(function (response) {
          var resp = Object.keys(response.data.query.pages)[0]
          if (resp !== '-1') {
            dhis.scriptDescription[script.value] = response.data.query.pages[Object.keys(response.data.query.pages)[0]].extract
          } else {
            dhis.scriptDescription[script.value] = 'Page no found'
          }
        })
        .catch(function (error) {
          console.log(error)
        }) */
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
