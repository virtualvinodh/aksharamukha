<template>
  <q-page padding class="book-content q-mt-lg">
    <div class="print-hide">
      <q-page-sticky position="top-right">
        <controls v-model="options" :minimizeO="true"> </controls>
      </q-page-sticky>
    </div>
      <transliterate :text="text" src="Devanagari" :tgt="options.script" :sourcePreserve="options.sourcePreserve" :postOptions="options.postOptions">
      </transliterate>
  </q-page>
</template>

<style>
</style>

<script>
import Transliterate from '../components/Transliterate'
import Controls from '../components/Controls'
import {QPageSticky, QInnerLoading, QSpinnerComment} from 'quasar'

export default {
  components: {
    Controls,
    QPageSticky,
    Transliterate,
    QInnerLoading,
    QSpinnerComment
  },
  data () {
    return {
      options: {script: 'IAST', sourcePreserve: false},
      text: '. . .',
      name: this.$route.params.text,
      loading: true
    }
  },
  watch: {
    '$route' (to, from) {
      this.name = to.params.text
      this.text = '. . .'
      this.renderPage()
    }
  },
  mounted: function () {
    this.renderPage()
  },
  methods: {
    renderPage: function () {
      this.loading = true
      var dhis = this
      this['old'] = Date.now()
      this.$axios.get('../statics/' + this.name + '.html', {})
        .then(function (response) {
          dhis.text = response.data
          dhis.loading = false
        })
        .catch(function (error) {
          console.log(error)
        })
    }
  }
}
</script>
