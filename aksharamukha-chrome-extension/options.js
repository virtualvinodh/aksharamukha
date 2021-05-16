// Copyright 2017 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

var scripts = ScriptMixin.data().scriptsIndic;
var postOptions = ScriptMixin.data().postOptionsGroup;
var preOptions = ScriptMixin.data().preOptionsGroup;
var preserveSourceDetails = ScriptMixin.data().preserveSourceExampleOut

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

// Selection Items

var selectInit = '<span class="aksharamukha-selection1">Input script: <select name="scriptinput" id="aksharamukhaselect1" placeholder="Select output script"/>'
var selectEnd = '</select></span>'
var selectMid = ''

selectMid1 = '<option value="autodetect" selected> Autodetect </option>'
selectMid2 = '<option value="original" selected> Original script </option>'

selectMid += '<option value="IAST">IAST</option>'
selectMid += '<option value="IASTPali">IAST (Pali)</option>'
selectMid += '<option value="ISO">ISO</option>'
selectMid += '<option value="RomanReadable">Readable Roman</option>'
selectMid += '<option value="IPA">IPA</option>'

scripts.forEach(function(script) {
  selectMid += '<option value="' + script.value + '">' + script.label + "</option>"
})

 moreButton1 = '<br/><div id="options1"</div>'

document.body.innerHTML += selectInit + selectMid1 + selectMid + selectEnd + '<br/>' + moreButton1

var preservebutton = '<span id="aksharamukha-preserve-block"><input type="checkbox" name="preservesrc" id="aksharamukha-preserve"/> Preserve source </input></span><div id="aksharamukha-preserve-ex">Options:</div>'

var selectInit2 = '<br/><span class="aksharamukha-selection2">Output script: <select name="scriptoutput" id="aksharamukhaselect2" placeholder="Select output script"/>'
var moreButton2 = '<div id="options2"></div>'

document.body.innerHTML += selectInit2 + selectMid2 + selectMid + selectEnd + '<br/><br/>' + preservebutton + '<br/>' + moreButton2

document.body.innerHTML += '<br/><button id="settings">Save settings</button> <br/>'

document.body.innerHTML += '<br/><button id="convertsite">Convert site</button>'
document.body.innerHTML += ' <button id="stopconv"">Stop conversion</button> '


document.getElementById('aksharamukhaselect1').addEventListener('input', addOptionsIn)
document.getElementById('aksharamukhaselect2').addEventListener('input', addOptionsOut)

document.getElementById('convertsite').addEventListener('click', convertsite)
document.getElementById('settings').addEventListener('click', savePars)
document.getElementById('stopconv').addEventListener('click', stopconversion)


chrome.storage.local.get(['source', 'target', 'nativize',
 'postOptionsList', 'preOptionsList'], function(para) {
    if(typeof para.source == 'undefined') {
      para.source = 'autodetect'
    }

    if (typeof para.target == 'undefined') {
      para.target = 'original'
    }

    if (typeof para.nativize == 'undefined') {
      para.nativize = true
    }

    document.getElementById('aksharamukhaselect1').value = para.source
    document.getElementById('aksharamukhaselect2').value = para.target
    document.getElementById('aksharamukha-preserve').checked = !para.nativize

    addOptionsOut(para.target)
    addOptionsIn(para.source)

    var preOptionsEl = document.getElementsByName('aksharamukha-optionpre')

    preOptionsEl.forEach(function (stopt) {
      if (para.preOptionsList.includes(stopt.value)) {
        stopt.checked = true
      }
    })

    var postOptionsEl = document.getElementsByName('aksharamukha-optionpost')

    postOptionsEl.forEach(function (stopt) {
      if (para.postOptionsList.includes(stopt.value)) {
        stopt.checked = true
      }
    })
 })

function stopconversion() {
  chrome.storage.local.set({ current: null })
  chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {

     // since only one tab should be active and in the current window at once
     // the return variable should only have one entry
     chrome.tabs.update(tabs[0].id, {url: tabs[0].url});

     window.close()

  });
}

function savePars() {
  source = document.getElementById('aksharamukhaselect1').value
  target = document.getElementById('aksharamukhaselect2').value
  nativize = !document.getElementById('aksharamukha-preserve').checked

  var postOptionsEl = document.getElementsByName('aksharamukha-optionpost')
  postOptionsList = []

  postOptionsEl.forEach(function(opt) {
    if (opt.checked) {
      postOptionsList.push(opt.value)
    }
  })

  var preOptionsEl = document.getElementsByName('aksharamukha-optionpre')
  preOptionsList = []

  preOptionsEl.forEach(function(opt) {
    if (opt.checked) {
      preOptionsList.push(opt.value)
    }
  })

  outputClass = ScriptMixin.methods.getOutputClass(target, postOptionsList)

  chrome.storage.local.set({ source: source })
  chrome.storage.local.set({ target: target })
  chrome.storage.local.set({ nativize: nativize })
  chrome.storage.local.set({ postOptionsList: postOptionsList })
  chrome.storage.local.set({ preOptionsList: preOptionsList })

  window.close()
}


function convertsite() {

source = document.getElementById('aksharamukhaselect1').value
target = document.getElementById('aksharamukhaselect2').value
nativize = !document.getElementById('aksharamukha-preserve').checked

var postOptionsEl = document.getElementsByName('aksharamukha-optionpost')
postOptionsList = []

postOptionsEl.forEach(function(opt) {
  if (opt.checked) {
    postOptionsList.push(opt.value)
  }
})

var preOptionsEl = document.getElementsByName('aksharamukha-optionpre')
preOptionsList = []

preOptionsEl.forEach(function(opt) {
  if (opt.checked) {
    preOptionsList.push(opt.value)
  }
})

outputClass = ScriptMixin.methods.getOutputClass(target, postOptionsList)

chrome.tabs.insertCSS({
  file: "fonts.css"
});

chrome.storage.local.set({ source: source })
chrome.storage.local.set({ target: target })
chrome.storage.local.set({ nativize: nativize })
chrome.storage.local.set({ postOptionsList: postOptionsList })
chrome.storage.local.set({ preOptionsList: preOptionsList })

parameters = {source: source, target: target, nativize: nativize, postOptionsList: postOptionsList, preOptionsList: preOptionsList, outputClass: outputClass}

chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {

     // since only one tab should be active and in the current window at once
     // the return variable should only have one entry
     var activeTab = tabs[0];
     var activeTabId = activeTab.id; // or do whatever you need

      chrome.storage.local.set({ current: activeTabId })
  });

chrome.tabs.executeScript({
    code: 'var pars =' + JSON.stringify(parameters)
  });

chrome.tabs.executeScript({
    file: 'inject.js'
  });

window.close()
}

function addOptionsOut () {
  var script = document.getElementById('aksharamukhaselect2').value
  document.getElementById('options2').innerHTML = optionsOutput(script)

  if(typeof preserveSourceDetails[script] === 'undefined') {
    document.getElementById('aksharamukha-preserve-block').style.display = 'none'
    document.getElementById('aksharamukha-preserve-ex').style.display = 'none'

  } else {
    document.getElementById('aksharamukha-preserve-block').style.display = 'block'
    document.getElementById('aksharamukha-preserve-ex').style.display = 'block'
    document.getElementById('aksharamukha-preserve-ex').innerHTML = '<small>' + preserveSourceDetails[script] + '</small>'
  }

}

function optionsOutput (inputScript) {
  var checkbox = '<small>'

  if (typeof postOptions[inputScript] !== 'undefined') {
    postOptions[inputScript].forEach(function(option) {
      checkbox += '<input type="checkbox" name="aksharamukha-optionpost" value="' + option.value + '">' + option.label + '<br>';
    })
    return checkbox + '</small></span>'
  } else {
    return ''
  }
}


function addOptionsIn () {
  var script = document.getElementById('aksharamukhaselect1').value
  document.getElementById('options1').innerHTML = optionsInput(script)
}

function optionsInput (inputScript) {
  var checkbox = '<small>'

  if (typeof preOptions[inputScript] !== 'undefined') {
    preOptions[inputScript].forEach(function(option) {
      checkbox += '<input type="checkbox" name="aksharamukha-optionpre" value="' + option.value + '">' + option.label + '<br>';
    })
    return checkbox + '</span>'
  } else {
    return ''
  }
}
