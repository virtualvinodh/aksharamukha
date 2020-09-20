(Get-Content .\aksharamukha-front\src\layouts\default.vue).replace('fontsdocker.css', 'fonts.css') | Set-Content .\aksharamukha-front\src\layouts\default.vue

(Get-Content .\aksharamukha-front\src\mixins\ScriptMixin.js).replace('http://localhost:8085/api', 'https://aksharamukha.appspot.com/api/') | Set-Content .\aksharamukha-front\src\mixins\ScriptMixin.js

cd ./aksharamukha-front

quasar build -m cordova -T android

cd src-cordova

cordova run android

# cordova build android --release