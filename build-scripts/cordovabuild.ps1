(Get-Content ..\aksharamukha-front\src\statics\fonts.css).replace('http://localhost:9899/aksharamukha-fonts.css', 'https://cdn.jsdelivr.net/gh/virtualvinodh/aksharamukha-fonts/aksharamukha-fonts.css') | Set-Content ..\aksharamukha-front\src\statics\fonts.css

(Get-Content ..\aksharamukha-front\src\mixins\ScriptMixin.js).replace('http://localhost:8085/api/', 'https://aksharamukha.appspot.com/api/') | Set-Content ..\aksharamukha-front\src\mixins\ScriptMixin.js

cd ..\aksharamukha-front

quasar build -m cordova -T android

cd src-cordova

cordova run android

# cordova build android --release