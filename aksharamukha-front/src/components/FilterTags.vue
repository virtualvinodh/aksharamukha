<template>
  <div>
      <i>Usage:</i>
      <q-btn rounded flat dense v-for="tag in tagsUsageM" :key="tag + 'v'" @click="tagClick(tag)">
        <q-chip :color="tagsActiveL.includes(tag) ? 'green-3' : 'red-3'" dense tag>
          {{tag}}
        </q-chip>
      </q-btn>
      |
      <q-btn rounded flat dense v-for="tag in tagsUsageS" :key="tag + 'v'" @click="tagClick(tag)">
        <q-chip :color="tagsActiveL.includes(tag) ? 'green-3' : 'red-3'" dense tag>
          {{tag}}
        </q-chip>
      </q-btn> <br/>
      <i>Region:</i>
      <q-btn rounded flat dense v-for="tag in tagsRegionM1" :key="tag + 'v'" @click="tagClick(tag)">
        <q-chip :color="tagsActiveL.includes(tag) ? 'green-3' : 'red-3'" dense tag>
          {{tag}}
        </q-chip>
      </q-btn>
      |
      <q-btn rounded flat dense v-for="tag in tagsRegionS1" :key="tag + 'v'" @click="tagClick(tag)">
        <q-chip :color="tagsActiveL.includes(tag) ? 'green-3' : 'red-3'" dense tag>
          {{tag}}
        </q-chip>
      </q-btn> <br/>
      <q-btn rounded flat dense v-for="tag in tagsRegionM2" :key="tag + 'v'" @click="tagClick(tag)">
        <q-chip :color="tagsActiveL.includes(tag) ? 'green-3' : 'red-3'" dense tag>
          {{tag}}
        </q-chip>
      </q-btn>
      |
      <q-btn rounded flat dense v-for="tag in tagsRegionS2" :key="tag + 'v'" @click="tagClick(tag)">
        <q-chip :color="tagsActiveL.includes(tag) ? 'green-3' : 'red-3'" dense tag>
          {{tag}}
        </q-chip>
      </q-btn> <br/>
      <i>Derivation:</i>
      <q-btn rounded flat dense v-for="tag in tagsDerivationM" :key="tag + 'v'" @click="tagClick(tag)">
        <q-chip :color="tagsActiveL.includes(tag) ? 'green-3' : 'red-3'" dense tag>
          {{tag}}
        </q-chip>
      </q-btn><br/>
      <i>Language Capability:</i>
      <q-btn rounded flat dense v-for="tag in tagsLanguageM" :key="tag + 'v'" @click="tagClick(tag)">
        <q-chip :color="tagsActiveL.includes(tag) ? 'green-3' : 'red-3'" dense tag>
          {{tag}}
        </q-chip>
      </q-btn>
  </div>
</template>

<script>
import {ScriptMixin} from '../mixins/ScriptMixin'
import { QBtn, QChip } from 'quasar'

export default {
  // name: 'ComponentName',
  props: ['tagsActive'],
  mixins: [ScriptMixin],
  components: {
    QChip,
    QBtn
  },
  data () {
    return {
      tagsActiveL: []
    }
  },
  methods: {
    tagClick: function (tag) {
      var dhis = this

      if (tag === 'Living') {
        this.tagsActiveL.push('Living: Major', 'Living: Minor')
      }

      if (tag.includes('Living:')) {
        this.tagsActiveL = this.tagsActiveL.filter(tag => tag !== 'Living')
      }

      if (tag === 'Extinct') {
        this.tagsActiveL.push('Extinct: Ancient', 'Extinct: Medieval', 'Extinct: Pre-Modern')
      }

      if (tag.includes('Extinct:')) {
        this.tagsActiveL = this.tagsActiveL.filter(tag => tag !== 'Extinct')
      }

      if (tag === 'South East Asian') {
        this.tagsActiveL = this.tagsActiveL.concat(this.tagsRegionS2)
      }

      if (tag.includes('South East Asian:')) {
        this.tagsActiveL = this.tagsActiveL.filter(tag => tag !== 'South East Asian')
      }

      if (tag.includes('Extinct:')) {
        this.tagsActiveL = this.tagsActiveL.filter(tag => tag !== 'Extinct')
      }

      if (tag === 'Indic') {
        this.tagsActiveL = this.tagsActiveL.concat(this.tagsRegionS1)
      }

      if (tag.includes('-Indic') || tag.includes(' Indic')) {
        this.tagsActiveL = this.tagsActiveL.filter(tag => tag !== 'Indic')
      }

      if (!this.tagsActiveL.includes(tag)) {
        this.tagsActiveL.push(tag)
      } else {
        this.tagsActiveL = this.tagsActiveL.filter(function (value, index, arr) { return value !== tag })
        if (tag === 'Living') {
          this.tagsActiveL = this.tagsActiveL.filter(tag => !tag.includes('Living:'))
        }
        if (tag === 'Extinct') {
          this.tagsActiveL = this.tagsActiveL.filter(tag => !tag.includes('Extinct:'))
        }
        if (tag === 'Indic') {
          this.tagsActiveL = this.tagsActiveL.filter(tag => !dhis.tagsRegionS1.includes(tag))
        }
        if (tag === 'South East Asian') {
          this.tagsActiveL = this.tagsActiveL.filter(tag => !dhis.tagsRegionS2.includes(tag))
        }
      }
      this.$emit('input', this.tagsActiveL)
    }
  }
}
</script>

<style scoped>
</style>
