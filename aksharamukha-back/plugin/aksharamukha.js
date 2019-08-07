window.addEventListener('load', appendTool)

var origText = [];
var origBody = '';

var counter = 0

function appendTool() {
  var d1 = document.body;

  if (counter == 0 ) {
    origBody = d1.innerHTML;
  }

  d1.insertAdjacentHTML('afterbegin', `
      <div id="navbar" class="sticky">
      <div class="logo-aksharamukha"/>
        <a href="http://aksharamukha.appspot.com">
          <img src="icon.png" width="30px" >
        </a>
      </div>
      <div class="selection">
        <select name="cars" id="aksharamukhaselect">
          <option value="Tamil">Tamil</option>
          <option value="Telugu">Telugu</option>
          <option value="Tibetan">Tibetan</option>
          <option value="Devanagari">Devanagari</option>
          <option value="Grantha">Grantha</option>
          <option value="Kannada">Kannada</option>
          <option value="Javanese">Javanese</option>
          <option value="Kaithi">Kaithi</option>
          <option value="PhagsPa">Phags Pa</option>
         </select>
        </div>
    </div>
  `);

  var newStyle = document.createElement('style');
  newStyle.appendChild(document.createTextNode(`
    .logo-aksharamukha {
      float:left;
      padding-right:5px;
    }

    .selection {
      margin-top: 5px;
    }

    #navbar {
      float: right;
      position: -webkit-sticky;
      position: sticky;
      top: 20px;
      // border: 1px solid black;
      width: 130px;
    }

    #navbar a {
     text-decoration: none;
    }

    @import url('https://fonts.googleapis.com/css?family=Mukta+Malar&subset=latin-ext,tamil');

    .footer-img {
      height: 20px;
    }
    .footer-quote {
      font-size: 12px;
    }
    .page {
      margin-left: 10px;
    }
    .footer-quote {
      text-align: right;
      float:center;
    }
    .quotef {
      float: center;
    }
    .demo1 {
        color: white;
        background-color: #424242;
        text-shadow: 0px 1px 0px rgba(0,0,0,.5);
    }
    .social {
      text-align: center;
    }
    .q-body-1 {
      line-height: 1.75em;
    }
    @font-face {
      font-family: 'Noto Sans Tamil';
      src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansTamil/NotoSansTamil-Regular.otf')
    }
    @font-face {
      font-family: 'Noto Sans Saurashtra';
      src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansSaurashtra/NotoSansSaurashtra-Regular.otf')
    }
    @font-face {
      font-family: 'Noto Serif Bali';
      src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSerifBalinese/NotoSerifBalinese-Regular.otf')
    }
    @font-face {
      font-family: 'e-Grantamil';
      src: url('../statics/e-Grantamil.ttf')
    }
    @font-face {
      font-family: 'Noto Sans Javanese';
      src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansJavanese/NotoSansJavanese-Regular.otf')
    }
    @font-face {
      font-family: 'Noto Sans Khojki';
      src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansKhojki/NotoSansKhojki-Regular.otf')
    }
    @font-face {
      font-family: 'Noto Sans Avestan';
      src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansAvestan/NotoSansAvestan-Regular.otf')
    }
    @font-face {
      font-family: 'Noto Sans Buginese';
      src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansBuginese/NotoSansBuginese-Regular.otf')
    }
    @font-face {
      font-family: 'Noto Sans Tagalog';
      src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansTagalog/NotoSansTagalog-Regular.otf')
    }
    @font-face {
      font-family: 'Noto Sans Malayalam';
      src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansMalayalam/NotoSansMalayalam-Regular.otf')
    }
    @font-face {
      font-family: 'Noto Sans Tagbanwa';
      src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansTagbanwa/NotoSansTagbanwa-Regular.otf')
    }
    @font-face {
      font-family: 'Noto Sans Sundanese';
      src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansSundanese/NotoSansSundanese-Regular.otf')
    }
    @font-face {
      font-family: 'Noto Sans Cham';
      src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansCham/NotoSansCham-Regular.otf')
    }
    @font-face {
      font-family: 'Noto Sans Chakma';
      src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansChakma/NotoSansChakma-Regular.otf')
    }
    @font-face {
      font-family: 'Noto Sans Telugu';
      src: url('../statics/Lohit-Telugu.ttf')
    }
    @font-face {
      font-family: 'Noto Sans Batak';
      src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansBatak/NotoSansBatak-Regular.otf')
    }
    @font-face {
      font-family: 'Noto Sans Lepcha';
      src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansLepcha/NotoSansLepcha-Regular.otf')
    }
    @font-face {
      font-family: 'Noto Sans Limbu';
      src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansLimbu/NotoSansLimbu-Regular.otf')
    }
    @font-face {
      font-family: 'Noto Sans Meetei Mayek';
      src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansMeeteiMayek/NotoSansMeeteiMayek-Regular.otf')
    }
    @font-face {
      font-family: 'Noto Sans Nastaliq Urdu';
      src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoNastaliqUrdu/NotoNastaliqUrdu-Regular.otf')
    }
    @font-face {
      font-family: 'Noto Serif Gujarati';
      src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSerifGujarati/NotoSerifGujarati-Regular.otf')
    }
    @font-face {
      font-family: 'Noto Sans Khmer';
      src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSerifKhmer/NotoSerifKhmer-Regular.otf')
    }
    @font-face {
      font-family: 'Noto Sans OldPersian';
      src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansOldPersian/NotoSansOldPersian-Regular.otf')
    }
    @font-face {
      font-family: 'Noto Sans Sinhala';
      src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansSinhala/NotoSansSinhala-Regular.otf')
    }
    @font-face {
      font-family: 'Noto Sans Kannada';
      src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansKannada/NotoSansKannada-Regular.otf')
    }
    @font-face {
      font-family: 'Noto Sans Tai Tham';
      src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/unhinted/NotoSansTaiTham-Regular.ttf')
    }
    @font-face {
      font-family: 'Noto Sans Grantha2';
      src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansGrantha/NotoSansGrantha-Regular.otf')
    }
    @font-face {
      font-family: 'Muktamsiddham';
      src: url('../statics/Muktamsiddham.otf')
    }
    @font-face {
      font-family: 'MuktamsiddhamG';
      src: url('../statics/MuktamsiddhamG.ttf')
    }
    @font-face {
      font-family: 'ApDevaSiddham';
      src: url('../statics/ApDevaSiddham.ttf')
    }
    @font-face {
      font-family: 'Nepal2';
      src: url('../statics/Nepal-lipi2.woff')
    }
    @font-face {
      font-family: 'BabelStoneZanabazar';
      src: url('../statics/BabelStoneZanabazar.woff')
    }
    @font-face {
      font-family: 'Adinatha Tamil Brahmi';
      src: url('../statics/AdinathaTamilBrahmi2.otf')
    }
    @font-face {
      font-family: 'Kharoshthi Ka';
      src: url('../statics/ka-khar.otf')
    }
    @font-face {
      font-family: 'Meera';
      src: url('../statics/Meera-Regular.ttf')
    }
    @font-face {
      font-family: 'Lao Pali';
      src: url('../statics/Lanexang_Mon4.otf')
    }
    @font-face {
      font-family: 'MithilaUni';
      src: url('../statics/MithilaUni.ttf')
    }
    @font-face {
      font-family: 'e-Vatteluttu';
      src: url('../statics/e-VatteluttuOT.ttf')
    }
    @font-face {
      font-family: 'e-Pandya';
      src: url('../statics/e-Pandya.ttf')
    }
    @font-face {
      font-family: 'JMYZK--LZT Lantsa';
      src: url('../statics/JMYZK--LZT.ttf')
    }
    @font-face {
      font-family: 'JMYZK--WDT Wartu';
      src: url('../statics/JMYZK--WDT.ttf')
    }
    @font-face {
      font-family: 'Lamphun';
      src: url('../statics/Hariphunchai.otf')
    }
    @font-face {
      font-family: 'Tibetan Dbu Med';
      src: url('../statics/Qomolangma-Betsu.ttf')
    }
    @font-face {
      font-family: 'AnnaPurna';
      src: url('../statics/AnnapurnaSIL-TT-Regular.ttf')
    }
    @font-face {
      font-family: 'Noto Sans Modi';
      src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansModi/NotoSansModi-Regular.otf')
    }
    @font-face {
      font-family: 'Noto Sans Multani';
      src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansMultani/NotoSansMultani-Regular.otf')
    }
    @font-face {
      font-family: 'Noto Sans SoraSompeng';
      src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansSoraSompeng/NotoSansSoraSompeng-Regular.otf')
    }
    @font-face {
      font-family: 'Noto Sans Mahajani';
      src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansMahajani/NotoSansMahajani-Regular.otf')
    }
    @font-face {
      font-family: 'Noto Sans Kaithi';
      src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansKaithi/NotoSansKaithi-Regular.otf')
    }
    @font-face {
      font-family: 'Noto Sans Tirhuta';
      src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansTirhuta/NotoSansTirhuta-Regular.otf')
    }
    @font-face {
      font-family: 'Noto Sans Takri';
      src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansTakri/NotoSansTakri-Regular.otf')
    }
    @font-face {
      font-family: 'Noto Sans SylotiNagri';
      src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansSylotiNagri/NotoSansSylotiNagri-Regular.otf')
    }
    @font-face {
      font-family: 'Noto Sans Newa';
      src: url('../statics/NotoSansNewa-Regular_New.otf')
    }
    @font-face {
      font-family: 'Noto Sans Sharada';
      src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansSharada/NotoSansSharada-Regular.otf')
    }
    @font-face {
      font-family: 'Noto Sans Bhaiksuki';
      src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansBhaiksuki/NotoSansBhaiksuki-Regular.otf')
    }
    @font-face {
      font-family: 'Noto Sans Khudawadi';
      src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansKhudawadi/NotoSansKhudawadi-Regular.otf')
    }
    @font-face {
      font-family: 'Noto Serif Ahom';
      src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSerifAhom/NotoSerifAhom-Regular.otf')
    }
    @font-face {
      font-family: 'Noto Sans Siddham';
      src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansSiddham/NotoSansSiddham-Regular.otf')
    }
    @font-face {
      font-family: 'Noto Sans Brahmi';
      src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansBrahmi/NotoSansBrahmi-Regular.otf')
    }
    @font-face {
      font-family: 'Noto Sans Ol Chiki';
      src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansOlChiki/NotoSansOlChiki-Regular.otf')
    }
    @font-face {
      font-family: 'Noto Sans Rejang';
      src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansRejang/NotoSansRejang-Regular.otf')
    }
    @font-face {
      font-family: 'Noto Sans Buhid';
      src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansBuhid/NotoSansBuhid-Regular.otf')
    }
    @font-face {
      font-family: 'Noto Sans Hanunoo';
      src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansHanunoo/NotoSansHanunoo-Regular.otf')
    }
    @font-face {
      font-family: 'Noto Sans WarangCiti';
      src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansWarangCiti/NotoSansWarangCiti-Regular.otf')
    }
    @font-face {
      font-family: 'Noto Sans PhagsPa';
      src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansPhagsPa/NotoSansPhagsPa-Regular.otf')
    }
    @font-face {
      font-family: 'Noto Sans Kharoshthi';
      src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansKharoshthi/NotoSansKharoshthi-Regular.otf')
    }
    @font-face {
      font-family: 'RanjanaUnicode';
      src: url('../statics/RanjanaUNICODE1.0.ttf')

    }
    @font-face {
      font-family: 'Noto Sans Brahmi';
      src: url('https://cdn.jsdelivr.net/gh/googlei18n/noto-fonts/phaseIII_only/unhinted/otf/NotoSansBrahmi/NotoSansBrahmi-Regular.otf')
    }
    .title-ka {
      font-family: "Kharoshthi Ka";
      font-size: 30px;
      margin-top: 25px;
      margin-left: 5px;
    }
    .tamilold {
      font-family: "Mukta Malar Regular";
      font-feature-settings: "ss04", "kern";
    }
    .tamil {
      font-family: "Noto Sans Tamil"
    }
    .tibetandbumed {
      font-family: "Tibetan Dbu Med";
      line-height: 2.3em;
    }
    .buhid {
      font-family: "Noto Sans Buhid"
    }
    .rejang {
      font-family: "Noto Sans Rejang"
    }
    .hanunoo {
      font-family: "Noto Sans Hanunoo"
    }
    .saurashtra {
      font-family: "Noto Sans Saurashtra"
    }
    .sorasompeng {
      font-family: "Noto Sans SoraSompeng"
    }
    .warangciti {
      font-family: "Noto Sans WarangCiti"
    }
    .balinese {
      font-family: "Noto Serif Bali"
    }
    .kannada {
      font-family: "Noto Sans Kannada"
    }
    .javanese {
      font-family: "Noto Sans Javanese", "Javanese Text";
    }
    .avestan {
      font-family: "Noto Sans Avestan";
      direction: rtl;
    }
    .buginese {
      font-family: "Noto Sans Buginese"
    }
    .sinhala {
      font-family: "Noto Sans Sinhala"
    }
    .tagalog {
      font-family: "Noto Sans Tagalog"
    }
    .tagbanwa {
      font-family: "Noto Sans Tagbanwa";
      writing-mode: bt-lr;

    }
    .sundanese {
      font-family: "Noto Sans Sundanese"
    }
    .cham {
      font-family: "Noto Sans Cham"
    }
    .malayalam {
      font-family: "Noto Sans Malayalam"
    }
    .malayalamold {
      font-family: "Meera";
      font-size:130%;
      line-height:125%;

    }
    .chakma {
      font-family: "Noto Sans Chakma"
    }
    .lepcha {
      font-family: "Noto Sans Lepcha"
    }
    .limbu {
      font-family: "Noto Sans Limbu"
    }
    .batakkaro {
      font-family: "Noto Sans Batak"
    }
    .batakmanda {
      font-family: "Noto Sans Batak"
    }
    .batakpakpak {
      font-family: "Noto Sans Batak"
    }
    .bataksima {
      font-family: "Noto Sans Batak"
    }
    .bataktoba {
      font-family: "Noto Sans Batak"
    }
    .telugu {
      font-family: "Noto Sans Telugu"
    }
    .khmer {
      font-family: "Noto Sans Khmer"
    }
    .meeteimayek {
      font-family: "Noto Sans Meetei Mayek"
    }
    .tolongsiki {
      font-family: "kellytolong"
    }
    .tamilbrahmi {
      font-family: "Adinatha Tamil Brahmi"
    }
    .phagspa {
      font-family: "Microsoft PhagsPa", "Noto Sans PhagsPa";
      writing-mode: vertical-lr;
      line-height: 1.8em;
    }
    .urdu {
      font-family: "Noto Sans Nastaliq Urdu";
      direction: rtl;
    }
    .kaithi {
      font-family: "Noto Sans Kaithi";
    }
    .gujarati {
      font-family: "Noto Serif Gujarati";
    }
    .modi {
      font-family: "Noto Sans Modi";
    }
    .multani {
      font-family: "Noto Sans Multani";
    }
    .ahom {
      font-family: "Noto Serif Ahom";
    }
    .tirhuta {
      font-family: "MithilaUni";
    }
    .oldpersian {
      font-family: "Noto Sans OldPersian";
    }
    .takri {
      font-family: "Noto Sans Takri";
    }
    .taitham {
      font-family: "Lamphun";
      font-size: 175%;
    }
    .sylotinagri {
      font-family: "Noto Sans SylotiNagri"
    }
    .granthagrantamil {
      font-family: "e-Grantamil";
      font-size: 110%;
      line-height: 1.5em;
    }
    .tamilgrantha {
      font-family: "e-Grantamil";
      font-size: 110%;
      line-height: 1.5em;
    }
    .siddhammukta {
      font-size: 120%;
      font-family: Muktamsiddham
    }
    .siddham {
      font-size: 100%;
      font-family: "Noto Sans Siddham"
    }
    .grantha {
      font-family: "Noto Sans Grantha2";
      line-height: 2em;
    }
    .kharoshthi {
       font-family: "Segoe UI Historic", "Noto Sans Kharoshthi";
      direction: rtl;
    }
    .thaana {
      direction: rtl;
    }
    .tibetan {
    }
    .zanabazarsquare {
      font-family: "BabelStoneZanabazar";
      line-height: 3em;
    }
    .newa {
      font-family: "Noto Sans Newa"
    }
    .sharada {
      font-family: "Noto Sans Sharada"
    }
    .mahajani {
      font-family: "Noto Sans Mahajani"
    }
    .multani {
      font-family: "Noto Sans Multani"
    }
    .bhaiksuki {
      font-family: "Noto Sans Bhaiksuki"
    }
    .khojki {
      font-family: "Noto Sans Khojki"
    }
    .khudawadi {
      font-family: "Noto Sans Khudawadi"
    }
    .granthapandya {
      font-family: "e-Pandya"
    }
    .vatteluttu {
      font-family: "e-Vatteluttu"
    }
    .brahmi {
      font-family: "Segoe UI Historic", "Noto Sans Brahmi"
    }
    .siddhamap {
      font-family: "ApDevaSiddham"
    }
    .limbudeva {
      font-family: "AnnaPurna"
    }
    .laopali {
      font-family: "Lao Pali"
    }
    .nepaldevafont {
      font-family: "Nepal2"
    }
    .santali {
      font-family: "Noto Sans Ol Chiki"
    }
    .ranjana {
      font-family: "RanjanaUnicode"
    }
    .ranjanalantsa {
      font-family: "JMYZK--LZT Lantsa"
    }
    .ranjanawartu {
      font-family: "JMYZK--WDT Wartu"
    }
  `));

  document.head.appendChild(newStyle);

  document.getElementById('aksharamukhaselect').addEventListener('change', transliterate);

// Storing original content
  var d1 = document.getElementsByClassName('trans-devanagari');
  console.log(d1.length)
  for (var i=0; i<d1.length; i++) {
    origText.push(d1[i].innerHTML)
  }

  counter += 1
}

var targetOld = ""
var target = ""

function transliterate() {
  targetOld = target

  var sel = document.getElementById('aksharamukhaselect')
  target = sel.options[sel.selectedIndex].value

  var d1 = document.getElementsByClassName('trans-devanagari');

  for (var i=0; i<d1.length; i++) {
    getResult(d1[i], i, target);
  }
}

function transliterateAll() {
  xhttp = new XMLHttpRequest();
  var sel = document.getElementById('aksharamukhaselect')
  target = sel.options[sel.selectedIndex].value

  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.body.innerHTML = this.responseText;
      appendTool()

      sel = document.getElementById('aksharamukhaselect')

      for(var i, j = 0; i = sel.options[j]; j++) {
          if(i.value == target) {
            sel.options[j].selected="selected"
          }
      }
    }
  }

  xhttp.open("POST", "http://localhost:8085/api/plugin", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send("source=Devanagari&target="+ target + "&text=" + origBody);
}

function getResult(el, i, target) {
  xhttp = new XMLHttpRequest();

  var text = el.textContent;

  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      el.innerHTML = this.responseText;
      console.log(targetOld)
      console.log(target)
      if (targetOld != "" ) {
        el.classList.remove(targetOld.toLowerCase())
      }
      el.classList.add(target.toLowerCase())
    }
  };

  xhttp.open("POST", "http://localhost:8085/api/plugin", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send("source=Devanagari&target="+ target + "&text=" + origText[i]);
}