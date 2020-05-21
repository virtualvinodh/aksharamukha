// require ./ScriptMixin.js

// Author: Vinodh Rajan vinodh@virtualvinodh.com
// Website: http://www.virtualvinodh.com
// Plugin: Web plugin for http://www.aksharamukha.appspot.com

// Global Data
var apiURL = "https://aksharamukha.appspot.com/api/plugin"

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

var optionsHide = true

var scripts = ScriptMixin.data().scriptsIndic;
var postOptions = ScriptMixin.data().postOptionsGroup;

var scriptsLTR = ['Urdu', 'Thaana', 'HanifiRohingya']

scriptList = []
ScriptMixin.data().scriptsIndic.forEach(function(e) {
  scriptList.push(e.value)
})

scriptList.push('ISO')
scriptList.push('IAST')
scriptList.push('IASTPali')
scriptList.push('RomanReadable')
scriptList.push('IPA')
scriptList.push('Original')

var myTags = document.getElementsByTagName("script");
var src = myTags[myTags.length-1].src;

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

outputClassOld = ScriptMixin.methods.getOutputClass(targetOld, postOptionsListOld)
outputClass = ScriptMixin.methods.getOutputClass(target, postOptionsList)

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
      checkbox = '<br/><span id="options" class="aksharamukha-hidedown">';
    } else {
      checkbox = '<br/><span id="options" class="aksharamukha-showup">';
    }

    postOptions[outputScript].forEach(function(option) {
      checkbox += '<input type="checkbox" name="aksharamukha-optionpost" value="' + option.value + '">' + option.label + '<br>';
    })

    return checkbox + '</span>'
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

var preservebutton = '<input type="checkbox" name="preserve" id="aksharamukha-preserve"/> Preserve source </input>'

scripts.forEach(function(script) {
  if (scriptList.includes(script.value)) {
    selectMid += '<option value="' + script.value + '">' + script.label + "</option>";
  }
});

  document.body.insertAdjacentHTML('afterbegin', `
      <div id="aksharamukha-navbar" class="sticky">
      <div class="aksharamukha-logosec">
      <div class="logo-aksharamukha"/>
        <a href="http://aksharamukha.appspot.com">
          <img src="https://raw.githubusercontent.com/virtualvinodh/aksharamukha/master/aksharamukha-front/src/statics/icons/favicon-32x32.png" width="20px" >
        </a> <span class="aksharamukha-name">Aksharamukha</span>
      </div>
      </div>
` + selectInit + selectMid + selectEnd + preservebutton + `
  `);

  var newStyle = document.createElement('style');
  newStyle.appendChild(document.createTextNode(`
    .logo-aksharamukha {
      padding-right:5px;
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
      margin-top:2px;
      margin-bottom: 5px;
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
      width: 150px;
      padding: 5px 5px 5px 5px;
      background: #CDCDCD;
      z-index: 1000;
    }

    #aksharamukha-navbar a {
     text-decoration: none;
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
  document.getElementById('aksharamukha-preserve').addEventListener('change', transliterate)

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

  if (window.localStorage.getItem('target')) {
    sel.value = window.localStorage.getItem('target')
  }

  if (window.localStorage.getItem('preservePrevious')) {
    document.getElementById('aksharamukha-preserve').checked = JSON.parse(window.localStorage.getItem('preservePrevious'))
  }

  if (window.localStorage.getItem('target')) {
    transliterate()
  }

}

async function transliterate() {
  var sel = document.getElementById('aksharamukhaselect')
  target = sel.value

  if (scriptList.includes(target)) {
    preservePrevious = document.getElementById('aksharamukha-preserve').checked

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

    if (optionsOutput(target) != '' ) {
      navbar.innerHTML = navbarOld

      if (optionsHide) {
        moreButton = '<br/><button id="aksharamukha-more">Show options</button>'
      } else {
        moreButton = '<br/><button id="aksharamukha-more">Hide options</button>'
      }

      navbar.innerHTML = navbarOld + moreButton + optionsOutput(target, '')

      document.getElementById('aksharamukha-more').addEventListener('click', optionsToggle)

      sel = document.getElementById('aksharamukhaselect')
      sel.value = target

    } else {
      navbar.innerHTML = navbarOld
    }

    document.getElementById('aksharamukha-preserve').checked = preservePrevious

    document.getElementById('aksharamukhaselect').addEventListener('input', transliterate)
    document.getElementById('aksharamukha-preserve').addEventListener('change', transliterate)

    postOptions.forEach(function (postOption, index) {
      postOption.checked = postOptionsChecked[index]
      postOption.addEventListener('change', transliterate)
    })

    window.localStorage.setItem('target', target)
    window.localStorage.setItem('preservePrevious', preservePrevious)
    window.localStorage.setItem('postOptionsChecked'+target, postOptionsChecked)
    window.localStorage.setItem('postOptionsList'+target, postOptionsList)

    var transContent = document.getElementsByClassName(classURL)

    document.getElementById('aksharamukhaselect').value = target

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

      await translit(transContent[i], i, source, targetOld, target)

      //getResult(transContent[i], i, source, targetOld)
    }
    targetOld = target
    postOptionsListOld = postOptionsList
  }
}

function optionsToggle() {
  var el = document.getElementById('options')
  var button = document.getElementById('aksharamukha-more')
  optionsHide = !optionsHide

  if (button.innerHTML == 'Show options') {
      el.classList = ['aksharamukha-showup']
      button.innerHTML = 'Hide options'
  } else {
    el.classList = ['aksharamukha-hidedown']
    button.innerHTML = 'Show options'
  }
}

window.addEventListener('load', appendTool)

console.log('Aksharamukha plugin is loaded')


