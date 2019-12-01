var texts = []

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

originalDoc(document.body)

async function translit( element , target){
  console.log(texts)
  console.log(JSON.stringify(texts).length)

  textsTran = await transliterateReq(JSON.stringify(texts), target)

  textsTran = JSON.parse(textsTran)

  var i = 0
  var nodes = document.createTreeWalker(element, NodeFilter.SHOW_TEXT, null, null);
  while (node = nodes.nextNode()) {
    var text = node.nodeValue;
    if (text.trim() != '') {
      node.nodeValue = textsTran[i]
      i = i + 1
    }
  }

}

function transliterateReq(text, target) {
  var xhttp = new XMLHttpRequest();

  return new Promise(function (resolve, reject) {

  xhttp.open("POST", "http://localhost:8085/api/plugin", true)
  xhttp.setRequestHeader("Content-type", "application/json")


  var data = JSON.stringify({"source": "Devanagari", "target": target, "nativize": true, 'postOptions': [], 'text': text});

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

translit(document.body, 'Kannada');
