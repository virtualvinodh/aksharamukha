// require ./ScriptMixin.js

// Author: Vinodh Rajan vinodh@virtualvinodh.com
// Website: http://www.virtualvinodh.com
// Plugin: Web plugin for http://www.aksharamukha.appspot.com

// Global Data
var apiURL = "https://aksharamukha-plugin.appspot.com/api/plugin"

var navbarOld = ''
var origText = [];
var nodesListAll = []
var counter = 0
var targetOld = ""
var target = ""
var postOptionsList = []
var preOptionsList = []
var postOptionsListOld = []

var preservePrevious = false

var changeURLParams = false

var optionsHide = true

var scripts = ScriptMixin.data().scriptsIndic;
var postOptions = ScriptMixin.data().postOptionsGroup;

var scriptsLTR = ['Urdu', 'Thaana', 'HanifiRohingya']

scriptList = []
ScriptMixin.data().scriptsIndic.forEach(function(e) {
  scriptList.push(e.value)
})

scriptList.push('RussianCyrillic')
scriptList.push('ISO')
scriptList.push('IAST')
scriptList.push('IASTPali')
scriptList.push('RomanReadable')
scriptList.push('IPA')
scriptList.push('Original')

var myTags = document.getElementsByTagName("script");
var src = myTags[myTags.length-1].src;

if (src.includes('changeurl')) {
  changeURLParams = unescape(src).split("changeurl=")[1].split("&")[0] == '1';
}

if (src.includes('prelist')) {
  var preList = unescape(src).split("prelist=")[1].split("&")[0];
  console.log(preList)
  if (preList === 'majorindic') {
    scriptList = ['ISO', 'IAST', 'IPA', 'RomanReadable', 'RussianCyrillic', 'Assamese', 'Bengali', 'Devanagari', 'Grantha', 'Gujarati', 'Gurmukhi', 'Kannada', 'Malayalam', 'Oriya', 'Sharada', 'Tamil', 'TamilExtended', 'Telugu', 'Urdu']
  } else if (preList == 'majorall') {
    scriptList = ['ISO', 'IAST', 'IPA', 'RomanReadable', 'RussianCyrillic', 'Assamese', 'Bengali', 'Burmese', 'Devanagari', 'Grantha', 'Gujarati', 'Gurmukhi', 'Kannada', 'Khmer', 'Malayalam', 'Oriya', 'Sharada', 'Sinhala', 'Tamil', 'TamilExtended', 'Telugu', 'Thai', 'Tibetan', 'Urdu']
  } else if (preList == 'sansktradall') {
    scriptList = ['ISO', 'IAST', 'IPA', 'RomanReadable', 'RussianCyrillic', 'Assamese', 'Balinese', 'Bengali', 'Brahmi', 'Bhaikshuki', 'Burmese', 'Devanagari', 'Dogra', 'Grantha', 'GranthaPandya', 'Gujarati', 'Gurmukhi', 'Javanese', 'Kannada', 'Kharoshthi', 'KhomThai', 'Khmer', 'Malayalam', 'Mongolian', 'Newa', 'Oriya', 'PhagsPa', 'Ranjana', 'Saurashtra', 'Siddham', 'Sharada', 'Sinhala', 'Soyombo', 'TaiTham', 'Takri', 'Tamil', 'TamilExtended', 'Telugu', 'Thai', 'Tibetan', 'Tirhuta', 'Urdu', 'ZanabazarSquare']
  } else if (preList == 'sanskall') {
    scriptList = ['ISO', 'IAST', 'IPA', 'RomanReadable', 'RussianCyrillic', 'Ariyaka', 'Assamese', 'Balinese', 'Bengali', 'Brahmi', 'Bhaikshuki', 'Burmese', 'Chakma', 'Devanagari', 'Dogra', 'GunjalaGondi', 'MasaramGondi', 'Grantha', 'GranthaPandya', 'Gujarati', 'Gurmukhi', 'Javanese', 'Kaithi', 'Kannada', 'Kharoshthi', 'KhomThai', 'Khmer', 'Khudawadi', 'LaoPali', 'Malayalam', 'Mongolian', 'Modi', 'Newa', 'Oriya', 'PhagsPa', 'Ranjana', 'Santali', 'Saurashtra', 'Siddham', 'Sharada', 'Sinhala', 'Soyombo', 'TaiTham', 'Takri', 'Tamil', 'TamilExtended', 'Telugu', 'Thai', 'Tibetan', 'Tirhuta', 'Urdu', 'ZanabazarSquare']
  }
  scriptList.push('Original')
}

if (src.includes('scriptlist')) {
  scriptList = unescape(src).split("scriptlist=")[1].split("&")[0].split(',');
  scriptList.push('Original')
}

var sourceURL = 'autodetect'

if (src.includes('source')) {
  sourceURL = unescape(src).split("source=")[1].split("&")[0];
}

var classURL = 'aksharamukha-text'
if (src.includes('class')) {
  classURL = unescape(src).split("class=")[1].split("&")[0];
}

var preOptionsURL = ''
if (src.includes('preoptions')) {
  preOptionsURL = unescape(src).split("preoptions=")[1].split("&")[0].split(',');
}

async function translit( element, ind, source, targetOld, target){

outputClassOld = ScriptMixin.methods.getOutputClass(targetOld, postOptionsListOld, JSON.stringify(nodesListAll[ind]))
outputClass = ScriptMixin.methods.getOutputClass(target, postOptionsList, JSON.stringify(nodesListAll[ind]))

if (target != 'Original') {
  textsTran = await transliterateReq(source, target, !preservePrevious, JSON.stringify(nodesListAll[ind]), postOptionsList, preOptionsList)
  var textsTranOrig = textsTran
  try {
    if (scriptsLTR.includes(target)) {
      textsTran = textsTran.replace(/،/g, ',')
    }

    if (target == "IPA") {
      textsTran = textsTran.replace(/"̆/g, '')
    }

    textsTran = JSON.parse(textsTran)
  } catch (e) {
    console.log(e)
    console.log(textsTranOrig)
    // console.log(typeof textsTran)
    textsTran = textsTran
  }
} else {
  textsTran = nodesListAll[ind]
}

  var nodes = document.createTreeWalker(element, NodeFilter.SHOW_TEXT, null, null);
  var i = 0
  while (node = nodes.nextNode()) {
    if (node.nodeValue.trim() != '') {
      node.nodeValue = textsTran[i]
      if (node.parentNode.classList.length > 0 && outputClassOld !== '' ) {
        node.parentNode.classList.remove(outputClassOld)
      }
      node.parentNode.classList.add(outputClass)
      i += 1
    }
  }

}

function transliterateReq(source, target, nativize, text, postOptions, preOptions) {
  var xhttp = new XMLHttpRequest();

  return new Promise(function (resolve, reject) {

  xhttp.open("POST", apiURL, true)
  xhttp.setRequestHeader("Content-type", "application/json")

  var data = JSON.stringify({"source": source, "target": target, "nativize": nativize, 'postOptions': postOptions, 'text': text, 'preOptions': preOptions});

  xhttp.send(data);

      // Setup our listener to process compeleted requests
      xhttp.onreadystatechange = function () {

        // Only run if the request is complete
        if (xhttp.readyState !== 4) return;

        // Process the response
        if (xhttp.status >= 200 && xhttp.status < 300) {
          // If successful
          resolve(xhttp.responseText);
        } else {
          // If failed
          reject({
            status: xhttp.status,
            statusText: xhttp.statusText
          });
        }
      };
    });
}

function optionsOutput (outputScript) {
  if (typeof postOptions[outputScript] !== 'undefined') {
    var checkbox = ''

    if (optionsHide) {
      checkbox = '<span id="aksharamukha-options"><div id="options" class="aksharamukha-hidedown">';
    } else {
      checkbox = '<span id="aksharamukha-options"><div id="options" class="aksharamukha-showup">';
    }

    postOptions[outputScript].forEach(function(option) {
      checkbox += '<input type="checkbox" name="aksharamukha-optionpost" value="' + option.value + '"><small>' + option.label + '</small><br>';
    })

    return checkbox + '</div></span>'
  } else {
    return ''
  }
}

function appendTool() {
  if (counter == 0 ) {
    var transContent2 = document.getElementsByClassName(classURL)

    if (transContent2.length == 0) {
        var div = document.createElement("span");
        div.className = "aksharamukha-text " + "inputscript-" + sourceURL + " preoptions-" + preOptionsURL;

        // Move the body's children into this wrapper
        while (document.body.firstChild)
        {
            div.appendChild(document.body.firstChild);
        }

        // Append the wrapper to the body
        document.body.appendChild(div);
    }

    origBody = document.body.innerHTML;

  }

// Selection Items

var selectInit = '<span class="aksharamukha-selection"><select name="scriptinput" id="aksharamukhaselect" placeholder="Select output script"/>'
var selectEnd = '</select></span>'///</datalist></span>'
var selectMid = '' // '<datalist id="script-list">'

selectMid += '<option value="Original"> Original script </option>'
if (scriptList.includes("IAST")) {
  selectMid += '<option value="IAST">IAST</option>'
}
if (scriptList.includes("IASTPali")) {
  selectMid += '<option value="IASTPali">IAST (Pali)</option>'
}
if (scriptList.includes("ISO")) {
  selectMid += '<option value="ISO">ISO</option>'
}
if (scriptList.includes("RomanReadable")) {
  selectMid += '<option value="RomanReadable">Readable Roman</option>'
}
if (scriptList.includes("IPA")) {
  selectMid += '<option value="IPA">IPA</option>'
}
if (scriptList.includes("RussianCyrillic")) {
  selectMid += '<option value="RussianCyrillic">Cyrillic (Russian)</option>'
}

//var preservebutton = '<input type="checkbox" name="preserve" id="aksharamukha-preserve"/> Preserve source </input>'

scripts.forEach(function(script) {
  if (scriptList.includes(script.value)) {
    selectMid += '<option value="' + script.value + '">' + script.label + "</option>";
  }
});

  var widthNavBar = '';

  document.body.insertAdjacentHTML('afterbegin', `
      <div id="aksharamukha-navbar" class="sticky aksharamukha-printhide">
      <div class="aksharamukha-logosec">
          <span class="aksharamukha-name"><small>Select script</small>&nbsp;&nbsp;&nbsp;<button id="aksharamukha-pluginhidebutton"><small>Hide</small></button>
      </div>
      <div id="aksharamukha-minlogo">
      <small><a href="http://aksharamukha.appspot.com" class="aksharamukha-hyperlink" target="_blank"><img src="https://cdn.jsdelivr.net/gh/virtualvinodh/aksharamukha/aksharamukha-web-plugin/icon.png" width="20px"/></a>&nbsp;<sup><button id="aksharamukha-minlogobutton"><small>Show</small></button></sup>
      </div>
` + selectInit + selectMid + selectEnd + `
  `);

    var newDivLogo = document.createElement("div")
    newDivLogo.id = "aksharamukha-branding1"
    var navbar = document.getElementById('aksharamukha-navbar')
    navbar.appendChild(newDivLogo)

    document.getElementById('aksharamukha-branding1').innerHTML = '<a href="http://aksharamukha.appspot.com" class="aksharamukha-hyperlink" target="_blank"><img src="https://cdn.jsdelivr.net/gh/virtualvinodh/aksharamukha/aksharamukha-web-plugin/icon.png" width="15px"/> <small><sup>Aksharamukha</sup></small></a>'

  var newStyle = document.createElement('style');
  newStyle.appendChild(document.createTextNode(`
    .logo-aksharamukha {
      padding-right:5px;
    }

    #aksharamukha-minlogo {
      display: none;
    }

    .aksharamukha-logosec {
      margin-bottom: 5px;
    }

    .aksharamukha-selection {
      margin-top: 5px;
    }

    .aksharamukha-name {
      font-style: italic;
    }

    #aksharamukha-more {
      margin-top:6px;
      margin-bottom: 0px;
    }

    .aksharamukha-hidedown {
      display: none;
    }

    .aksharamukha-showup {
      display: all;
    }

    #aksharamukhaselect {
      font-family: calibri;
      width:140px;
    }

    #aksharamukha-preserve {
      margin-top:10px;
      margin-bottom: 10px;
    }

    #aksharamukha-navbar {
      float: right;
      font-family: calibri;
      position: -webkit-sticky;
      position: sticky;
      top: 20px;
      // border: 1px solid black;
      padding: 5px 5px 2px 5px;
      border-radius: 5px;
      background: #CDCDCD;
      z-index: 1000;
    }

    @media print
    {
      .aksharamukha-printhide
      {
          display: none !important;
      }
    }

    @media only screen and (max-device-width: 760px) {
    }

    .aksharamukha-printhide {

    }

    #aksharamukha-navbar a {
     text-decoration: none;
    }

    #aksharamukha-loading {
      margin-top:8px;
      margin-bottom:5px;
    }

    a.aksharamukha-hyperlink:link {
      text-decoration: none;
      color:black;
    }

    a.aksharamukha-hyperlink:visited {
      text-decoration: none;
      color:black;
    }

    a.aksharamukha-hyperlink:hover {
      text-decoration: underline;
      color:black;
    }

    a.aksharamukha-hyperlink:active {
      text-decoration: underline;
      color:black;
    }

    #aksharamukha-branding1 {
      margin-top: 8px;
      font-size: 90%
    }

    #aksharamukha-branding {
      font-size: 90%;
    }

    #akshmukha-text {

    }
  `));

  document.head.appendChild(newStyle);

  var link = document.createElement("link");

  link.type = "text/css";
  link.rel = "stylesheet";
  link.href = 'https://cdn.jsdelivr.net/gh/virtualvinodh/aksharamukha/aksharamukha-front/src/statics/fonts.css'

  document.head.appendChild(link)

  document.getElementById('aksharamukhaselect').addEventListener('input', transliterate)
  document.getElementById('aksharamukha-minlogobutton').addEventListener('click', showPlugin)
  document.getElementById('aksharamukha-pluginhidebutton').addEventListener('click', hidePlugin)


  // Storing original content
  var transContent = document.getElementsByClassName(classURL)
  var texts = []
  for (var i=0; i<transContent.length; i++) {
    origText.push(transContent[i].innerHTML)

    var nodes = document.createTreeWalker(transContent[i], NodeFilter.SHOW_TEXT, null, null);
    texts = []
    while (node = nodes.nextNode()) {
      if (node.nodeValue.trim() != '') {
        texts.push(node.nodeValue)
      }
    }
    nodesListAll.push(texts)
  }

  counter += 1

  navbarOld = document.getElementById('aksharamukha-navbar').innerHTML

  // Restore values
  var sel = document.getElementById('aksharamukhaselect')

  if(window.location.search.indexOf('akshrmkh') > -1) {
    var targetUrl = window.location.search.split('=')[window.location.search.split('=').length - 1]
    sel.value = targetUrl
    transliterate()
  } else if (window.localStorage.getItem('target')) {
    sel.value = window.localStorage.getItem('target')
  }

  if (window.localStorage.getItem('target')) {
    transliterate()
    hidePlugin()
  }

  if (window.localStorage.getItem('hidePlugin') === 'true') {
    hidePlugin()
  }

  if( /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) {
    hidePlugin()
  }

  console.log('here once')
}

async function transliterate(event) {
  if (typeof event !== 'undefined' && event.target.id == 'aksharamukha-preserve') {
    preservePrevious = event.target.checked
    console.log(event.target.checked)
    console.log(preservePrevious)
    window.localStorage.setItem('preservePrevious', preservePrevious)
  }

  var sel = document.getElementById('aksharamukhaselect')
  target = sel.value

  if (changeURLParams) {
    var url = window.location.href;
    var refresh
    if (url.indexOf('?') > -1) {
      if (window.location.search.indexOf('akshrmkh') > -1) {
        var oldPar = window.location.search.split('=')[window.location.search.split('=').length - 1]
        console.log(window.location.search)
        var newPath = window.location.search.replace('akshrmkh='+oldPar, 'akshrmkh='+target)
        refresh = window.location.protocol + "//" + window.location.host + window.location.pathname +  newPath;
      } else {
        refresh = window.location.protocol + "//" + window.location.host + window.location.pathname +  window.location.search + '&akshrmkh=' + target;
      }
    }
    else {
      refresh = window.location.protocol + "//" + window.location.host + window.location.pathname + '?akshrmkh=' + target;
    }

    window.history.pushState({ path: refresh }, '', refresh);
  }

  if (scriptList.includes(target)) {
    var postOptionsChecked = []
    var postOptions = document.getElementsByName('aksharamukha-optionpost')

    postOptionsList = []

    // console.log(targetOld)
    // console.log(target)

    if (window.localStorage.getItem('postOptionsChecked' + sel.value)) {
      var storepostOptionsChecked= window.localStorage.getItem('postOptionsChecked' + sel.value).split(',').map( x => JSON.parse(x))
      var storepostOptionsList= window.localStorage.getItem('postOptionsList' + sel.value).split(',')

      if (window.localStorage.getItem('postOptionsList' + sel.value) != '') {
        postOptionsChecked = storepostOptionsChecked
        postOptionsList = storepostOptionsList
      }
    }

    if (targetOld == target) {
      postOptionsList = []
      postOptionsChecked = []

      postOptions.forEach(function (postOption) {
        postOptionsChecked.push(postOption.checked)

        if (postOption.checked) {
          postOptionsList.push(postOption.value)
        }
      })
    }

    var navbar = document.getElementById('aksharamukha-navbar')
    var moreButton = ''

    if (optionsOutput(target) != '' || addPreserveSource(target) != '') {
      navbar.innerHTML = navbarOld

      if (optionsHide) {
        moreButton = '<button id="aksharamukha-more"><small>More options</small></button>'
      } else {
        moreButton = '<button id="aksharamukha-more"><small>Hide options</small></button>'
      }

      navbar.innerHTML = navbarOld + moreButton + "" + addPreserveSource(target) + optionsOutput(target, '')

      document.getElementById('aksharamukha-more').addEventListener('click', optionsToggle)


      if (addPreserveSource(target) !== '') {
        document.getElementById('aksharamukha-preserve').checked = JSON.parse(window.localStorage.getItem('preservePrevious'))
        document.getElementById('aksharamukha-preserve').addEventListener('change', transliterate)
      }

      sel = document.getElementById('aksharamukhaselect')
      sel.value = target

    } else {
      navbar.innerHTML = navbarOld
    }

    var newDivLoad = document.createElement("div")
    newDivLoad.id = "aksharamukha-loading"
    navbar.appendChild(newDivLoad)

    document.getElementById('aksharamukha-branding1').innerHTML = ''
    var branding1 = document.getElementById('aksharamukha-branding1')
    branding1.id = 'aksharamukha-branding2'

    var newDivLogo = document.createElement("div")
    newDivLogo.id = "aksharamukha-branding"
    var navbar = document.getElementById('aksharamukha-navbar')
    navbar.appendChild(newDivLogo)

    document.getElementById('aksharamukha-branding').innerHTML = '<a href="http://aksharamukha.appspot.com" class="aksharamukha-hyperlink" target="_blank"><img src="https://cdn.jsdelivr.net/gh/virtualvinodh/aksharamukha/aksharamukha-web-plugin/icon.png" width="15px"/> <small><sup>Aksharamukha </sup></small></a>'

    document.getElementById('aksharamukhaselect').addEventListener('input', transliterate)
    document.getElementById('aksharamukha-minlogobutton').addEventListener('click', showPlugin)
    document.getElementById('aksharamukha-pluginhidebutton').addEventListener('click', hidePlugin)

    postOptions.forEach(function (postOption, index) {
      postOption.checked = postOptionsChecked[index]
      postOption.addEventListener('change', transliterate)
    })

    window.localStorage.setItem('target', target)
    window.localStorage.setItem('postOptionsChecked'+target, postOptionsChecked)
    window.localStorage.setItem('postOptionsList'+target, postOptionsList)

    var transContent = document.getElementsByClassName(classURL)

    document.getElementById('aksharamukhaselect').value = target

    if (window.localStorage.getItem('preservePrevious')) {
      preservePrevious = JSON.parse(window.localStorage.getItem('preservePrevious'))
    }

    for (var i=0; i<transContent.length; i++) {
      var source = ''
      transContent[i].classList.forEach(function (clas) {
        if (clas.includes('inputscript')) {
          source = clas.split('-')[1]
        }
        if (clas.includes('preoptions') && clas.split('-')[1] != '') {

          preOptionsList = clas.split('-')[1].split(',')
        }
      })

      if (source == '') {
        source = 'autodetect'
      }

      if (sourceURL !== 'autodetect') {
        source = sourceURL
      }

      if (preOptionsURL !== '') {
        preOptionsList = preOptionsURL
      }


      if (targetOld != "" ) {
        // console.log('removing')
        // console.log(ScriptMixin.methods.getOutputClass(targetOld, postOptionsList))
        //transContent[i].classList.remove(ScriptMixin.methods.getOutputClass(targetOld, postOptionsListOld))
      }

      //transContent[i].classList.add(ScriptMixin.methods.getOutputClass(target, postOptionsList))

      document.getElementById('aksharamukha-loading').innerHTML = '<img src="https://cdn.jsdelivr.net/gh/virtualvinodh/aksharamukha/aksharamukha-web-plugin/loading.gif" width="70px" />'

      await translit(transContent[i], i, source, targetOld, target)

      document.getElementById('aksharamukha-loading').innerHTML = ''

      //getResult(transContent[i], i, source, targetOld)
    }
    targetOld = target
    postOptionsListOld = postOptionsList
  }
}

function hidePlugin() {
  document.getElementsByClassName('aksharamukha-name')[0].style.display = 'none'
  document.getElementsByClassName('aksharamukha-selection')[0].style.display = 'none'
  if (document.getElementById('aksharamukha-more')) {
    document.getElementById('aksharamukha-more').style.display = 'none'
  }
  if (document.getElementById('aksharamukha-branding')) {
    document.getElementById('aksharamukha-branding').style.display = 'none'
  }
  if (document.getElementById('aksharamukha-branding1')) {
    document.getElementById('aksharamukha-branding1').style.display = 'none'
  }
  if (document.getElementById('aksharamukha-options')) {
    document.getElementById('aksharamukha-options').style.display = 'none'
  }
  if (document.getElementById('aksharamukha-preservebut')) {
    document.getElementById('aksharamukha-preservebut').style.display = 'none'
  }
  document.getElementById('aksharamukha-minlogo').style.display = 'block'

  window.localStorage.setItem('hidePlugin', 'true')
}

function showPlugin() {
  document.getElementsByClassName('aksharamukha-name')[0].style.display = ''
  document.getElementsByClassName('aksharamukha-selection')[0].style.display = ''
  if (document.getElementById('aksharamukha-more')) {
    document.getElementById('aksharamukha-more').style.display = ''
  }
  if (document.getElementById('aksharamukha-branding')) {
    document.getElementById('aksharamukha-branding').style.display = ''
  }
  if (document.getElementById('aksharamukha-branding1')) {
    document.getElementById('aksharamukha-branding1').style.display = ''
  }
  if (document.getElementById('aksharamukha-options')) {
    document.getElementById('aksharamukha-options').style.display = ''
  }
  if (document.getElementById('aksharamukha-preservebut')) {
    document.getElementById('aksharamukha-preservebut').style.display = ''
  }
  document.getElementById('aksharamukha-minlogo').style.display = 'none'

  window.localStorage.setItem('hidePlugin', 'false')
}

function optionsToggle() {
  var el = document.getElementById('options')
  var elpre = document.getElementById('aksharamukha-preservebut')

  var button = document.getElementById('aksharamukha-more')
  optionsHide = !optionsHide

  if (button.innerHTML == '<small>More options</small>') {
      if (el != null) {
        el.classList = ['aksharamukha-showup']
      }
      if (elpre != null) {
        elpre.classList = ['aksharamukha-showup']
      }

      button.innerHTML = '<small>Hide options</small>'
  } else {
    if (el != null) {
      el.classList = ['aksharamukha-hidedown']
    }
    if (elpre != null) {
      elpre.classList = ['aksharamukha-hidedown']
    }

    button.innerHTML = '<small>More options</small>'
  }
}

function addPreserveSource(target) {
  var explO = ScriptMixin.data().preserveSourceExampleOut[target]

  if (typeof explO !== 'undefined' && target !== 'Original') {
    var expl = '<small>' + explO + '</small>'

    var cls = optionsHide ? '"aksharamukha-hidedown"' : '"aksharamukha-showup"'

    var button = '<span id = "aksharamukha-preservebut" class=' + cls + '><div><input type="checkbox" name="preserve" id="aksharamukha-preserve"/> <small>Preserve source<br/> ' + expl + '</small><hr/></div></span>'

    return  button

  } else {
    return ''
  }
}

window.addEventListener('load', appendTool)

console.log('Aksharamukha plugin is loaded')

