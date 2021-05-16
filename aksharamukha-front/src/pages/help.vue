<template>
  <q-page padding>
    <div class="q-display-1 q-mt-lg q-mb-md">Help</div>
    <h5> Default Conversion </h5>
    <div class="q-body-1">Aksharamukha automatically applies (if necessary) certain nativization conventions to the output text.  This is to be in line with the linguistic/orthographic conventions of the output script. For the nativization conventions of each script, refer to the individual script page.</div>
    <h5>Preserve Source</h5>
    <div class="q-body-1">Since the output text is by default processed for nativization conventions, there may be a need to accurately preserve the source text.  This option facilitates lossless reverse transliteration (as much as possible) by preserving the source text. This is usually done by skipping nativization conventions, using historical (or obsolete) characters, and various diacritics [such as caret (^), apostrophe (ʼ) ] to preserve the source.</div>
    <h5>How do I transliterate my name? </h5>
    <div class="q-body-1">This allows your to enter a phrase in one script and render it in all of the other scripts supported by Aksharamukha. You probably want to write your name and render it in different scripts. In that case,  you should approximate your name to Indic phonology and give it as input in one of the romanization formats or as an Indic script. For instance, John Smith would have to become 'jAn smit' (Harvard-Kyoto Romanization) and Jane has to become 'jen' (HK). Please have look <a href="https://www.sanskrit-trikashaivism.com/en/learning-sanskrit-pronunciation-1-1/456">here</a>, <a href="http://www.sanskritsounds.com/about-sanskrit/46/index.html">here</a> and <a href="http://www.visiblemantra.org/pronunciation.html">here</a>. They might help in the approximation.</div>
    <h5> How do I learn more about the scripts listed? </h5>
    <div class="q-body-1"> <a href="http://scriptsource.org">Script Source</a> is a good place to start. You can also try <a href="omniglot.com">Omniglot</a>, <a href="http://www.ancientscripts.com/">Ancient Scripts</a>, Ishida's <a href="https://r12a.github.io/doclist">script notes</a> and as always our good old friend <a href="https://en.wikipedia.org/wiki/Category:Writing_systems">Wikipedia</a>. The <a href="http://www.unicode.org/L2/">Unicode proposals</a> for many of the minority and historical scripts is also a good way to learn about them.</div>
    <h5> Fonts </h5>
    <div class="q-body-1">Aksharamukha uses web fonts to display the text in the target script, particularly for minority scripts. Hence, there may be a slight delay until the font is downloaded to have a legible text in the target script. Most fonts are used from Google's Noto Fonts project. This can be accessed from <a href="https://github.com/googlei18n/noto-fonts">Github</a>. For others, refers to the individual script description page. </div>
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
