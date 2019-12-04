// Copyright 2017 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

'use strict';
// Add a listener to create the initial context menu items,
// context menu items only need to be created at runtime.onInstalled
chrome.runtime.onInstalled.addListener(function() {
chrome.storage.local.get(['source', 'target', 'nativize',
 'postOptionsList', 'preOptionsList'], function(para) {
    chrome.contextMenus.create({
      id: 'transliterate',
      title: 'Convert text',
      type: 'normal',
      contexts: ['selection'],
    });
    chrome.contextMenus.create({
      id: 'transliteratesite',
      title: 'Convert site',
      type: 'normal',
      contexts: ['page'],
    });
    chrome.contextMenus.create({
      id: 'transliteratestop',
      title: 'Stop conversion',
      type: 'normal',
      contexts: ['page'],
    });
  })
});

chrome.contextMenus.onClicked.addListener(function(item, tab) {
  if (item.menuItemId == 'transliterate') {
    chrome.storage.local.get(['source', 'target', 'nativize',
     'postOptionsList', 'preOptionsList'], function(para) {
      if (typeof para.target === 'undefined') {
        para.target = 'ISO'
      }

      let url = 'https://aksharamukha.appspot.com/converter' +'?text=' + item.selectionText + '&target=' + para.target;
      chrome.tabs.create({url: url, index: tab.index + 1});
    })
  } else if (item.menuItemId == 'transliteratesite') {
    chrome.storage.local.set({ current: tab.id })
    convertSite()
  } else {
    chrome.storage.local.set({ current: null })

    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
        chrome.tabs.update(tabs[0].id, {url: tabs[0].url});
    });
  }
});

chrome.tabs.onUpdated.addListener(function(tabId,changeInfo,tab){
  chrome.storage.local.get(['current'], function (result) {
    if (tabId == result.current && changeInfo.status === 'complete') {
      convertSite()
    }
  })
});

function convertSite() {
    chrome.tabs.insertCSS({
      file: "fonts.css"
    });

    chrome.storage.local.get(['source', 'target', 'nativize',
     'postOptionsList', 'preOptionsList'], function(para) {

        if (typeof para.target == 'undefined') {
          para.target = 'ISO'
        }

        if (typeof para.source == 'undefined') {
          para.source = 'autodetect'
        }

        if (typeof para.nativize == 'undefined') {
          para.nativize = true
        }

        if (typeof para.postOptionsList == 'undefined') {
          para.postOptionsList = []
        }

        if (typeof para.preOptionsList == 'undefined') {
          para.preOptionsList = []
        }

        var outputClass = ScriptMixin.methods.getOutputClass(para.target, para.postOptionsList)

        var parameters = {source: para.source, target: para.target, nativize: para.nativize, postOptionsList: para.postOptionsList, preOptionsList: para.preOptionsList, outputClass: outputClass}

        chrome.tabs.executeScript({
            code: 'var pars =' + JSON.stringify(parameters)
          });

        chrome.tabs.executeScript({
            file: 'inject.js'
          });
    })
}

