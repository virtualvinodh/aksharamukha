var pythonRuntime;
var loaded;

languagePluginLoader.then(() => {
  // pyodide is now ready to use...
  pyodide.loadPackage('micropip').then(() => {
  // micropip is now available
    pythonRuntime = pyodide.runPython(`
  import micropip
  micropip.install('aksharamukha')
  'loaded'
      `);
  });

  document.body.innerHTML += 'Python loaded'
});

if (pythonRuntime === 'loaded') {
  var buddha = pyodide.runPython('from aksharamukha import transliterate\ntransliterate.process("HK", "Telugu", "zuddho bhagavato")')
}

alert(buddha)



