var outputClassOld

if (typeof outputClass !== 'undefined') {
  outputClassOld = outputClass
} else {
  outputClassOld = ''
}

var source = pars.source
var target = pars.target
var nativize = pars.nativize
var postOptionsList = pars.postOptionsList
var preOptionsList = pars.preOptionsList
var outputClass = pars.outputClass

var scriptsLTR = ['Urdu', 'Thaana', 'HanifiRohingya']

if (document.readyState == 'complete') {
  setTimeout(function() {
    performTransliteration()
  }, 2500);
};

function performTransliteration() {
  if (document.getElementById('aksharamukha-text') == null) {
    var texts = []
    addBanner()
    originalDoc(document.getElementById('aksharamukha-text'))
    console.log('first time')
  } else {
    document.getElementById('akshsrctgt').innerHTML =  source + ` to ` + target
    console.log('not first time')
  }

  translit(document.getElementById('aksharamukha-text'))
}

function originalDoc (element) {
  var nodes = document.createTreeWalker(element, NodeFilter.SHOW_TEXT, null, null);
  texts = []
  nodeList = []
  while (node = nodes.nextNode()) {
    var text = node.nodeValue;
    if (text.trim() != '') {
      texts.push(text)
      // node.nodeValue = await transliterateReq(text)
    }
  }
}

async function translit( element ){
  textsTran = await transliterateReq(JSON.stringify(texts), target)

    if (scriptsLTR.includes(target)) {
      textsTran = textsTran.replace(/،/g, ',')
    }

    if (target == "IPA") {
      textsTran = textsTran.replace(/"̆/g, '')
    }

  try {
    textsTran = JSON.parse(textsTran)
  } catch(e) {
    console.log(textsTran)
    console.log(e)

    textsTran = textsTran
  }


  var i = 0

  var nodes = document.createTreeWalker(element, NodeFilter.SHOW_TEXT, null, null);

  console.log(texts.length)
  console.log(textsTran.length)

  while (node = nodes.nextNode()) {
    var text = node.nodeValue;
    if (text.trim() != '') {
      node.nodeValue = textsTran[i]
      if (node.parentNode.classList.length > 0 && outputClassOld !== '' ) {
        node.parentNode.classList.remove(outputClassOld)
      }
      node.parentNode.classList.add(outputClass)
      i = i + 1
    }
  }

  console.log(i)

  // document.body.className += " " + outputClass
}

function transliterateReq(text) {
  var xhttp = new XMLHttpRequest();

  return new Promise(function (resolve, reject) {

  xhttp.open("POST", "https://aksharamukha-plugin.appspot.com/api/plugin", true)
  xhttp.setRequestHeader("Content-type", "application/json")

  var data = JSON.stringify({"source": source, "target": target, "nativize": nativize, 'postOptions': postOptionsList, 'preOptions': preOptionsList,'text': text});

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

function addBanner() {

        var div = document.createElement("span");
        div.id = "aksharamukha-text";

        // Move the body's children into this wrapper
        while (document.body.firstChild)
        {
            div.appendChild(document.body.firstChild);
        }

        // Append the wrapper to the body
        document.body.appendChild(div);

  document.body.insertAdjacentHTML('afterbegin', `
      <div id="aksharamukha-navbar" class="sticky">
      <div class="aksharamukha-logosec">
      <div class="logo-aksharamukha"/>
        <a href="http://aksharamukha.appspot.com" target="_blank">
          <img src="`+ chrome.runtime.getURL('48.png') + `" width="20px" >
        </a> Website is being transliterated from <span id="akshsrctgt">` + source + ` to ` + target + `</span>. This may take a few seconds.
      </div>
      </div>
  `);

  var newStyle = document.createElement('style');
  newStyle.appendChild(document.createTextNode(`

    #aksharamukha-navbar {
      text-align: center;
      font-family: calibri;
      position: -webkit-sticky;
      position: sticky;
      top: 0px;
      width: 100%;
      padding: 10px 10px 10px 10px;
      background: #CDCDCD;
      z-index: 1000;
      font-size: 15px;
      opacity:0.7;
    }

    }
  `));

  document.head.appendChild(newStyle);

}

// Todo save original content


