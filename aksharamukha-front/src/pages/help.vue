<template>
  <q-page padding>
    <div class="q-display-1 q-mt-lg q-mb-md">Help</div>
    <h5> Default Conversion </h5>
    <div class="q-body-1">Aksharamukha automatically applies (if necessary) certain nativization conventions to the output text.  This is to be in line with the linguistic/orthographic conventions of the output script. For the nativization conventions of each script, refer to the individual script page.</div>
    <h5>Preserve Source</h5>
    <div class="q-body-1">Since the output text is by default processed for nativization conventions, there may be a need to accurately preserve the source text.  This option facilitates lossless reverse transliteration (as much as possible) by preserving the source text. This is usually done by skipping nativization conventions, using historical (or obsolete) characters, and various diacritics [such as caret (^), apostrophe (ʼ) ] to preserve the source.</div>
    <h5> Rosetta Stone </h5>
    <div class="q-body-1">This allows your to enter a phrase in one script and render it in all of the other scripts supported by Aksharamukha. You probably want to write your name and render it in different scripts. In that case,  you should approximate your name to Indic phonology and give it as input in one of the romanization formats or as an Indic script. For instance, John Smith would have to become 'jAn smit' (Harvard-Kyoto Romanization) and Jane has to become 'jen' (HK). Please have look <a href="https://www.sanskrit-trikashaivism.com/en/learning-sanskrit-pronunciation-1-1/456">here</a>, <a href="http://www.sanskritsounds.com/about-sanskrit/46/index.html">here</a> and <a href="http://www.visiblemantra.org/pronunciation.html">here</a>. They might help in the approximation.</div>
    <h5> Fonts </h5>
    <div class="q-body-1">Aksharamukha uses web fonts to display the text in the target script, particularly for minority scripts. Hence, there may be a slight delay until the font is downloaded to have a legible text in the target script. Most fonts are used from Google's Noto Fonts project. This can be accessed from <a href="https://github.com/googlei18n/noto-fonts">Github</a>. For others, refers to the statics folder of Aksharamukha's source code in Github. </div>
    <h5> Input Method Editor (IME) </h5>
    <div class="q-body-1">Aksharamukha can be used as an online IME for inputting in various scripts. But it was not designed to be so. You may choose any one of the <router-link to="/roman">romanization</router-link> formats and use it get a text in a desired script. It should work by and large as expected. But please note that Aksharamukha tries to be 'intelligent', which can be helpful or annoying depending on how you look at it. So, it is suggested you turn on the 'preserve source' options, if you do intend to use it as an IME.</div>

  </q-page>
</template>

<script>
export default {
  // name: 'PageName',
}
</script>

<style scoped>
.q-body-1 {
  line-height: 1.75em;
  font-color: red;
}
h5 {
  margin-bottom: 10px;
}
</style>
