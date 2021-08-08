(Get-Content ..\aksharamukha-front\src\statics\fonts.css).replace('http://localhost:9899/aksharamukha-fonts.css', 'https://cdn.jsdelivr.net/gh/virtualvinodh/aksharamukha-fonts/aksharamukha-fonts.css') | Set-Content ..\aksharamukha-front\src\statics\fonts.css

(Get-Content ..\aksharamukha-front\src\mixins\ScriptMixin.js).replace('http://localhost:8085/api/', 'https://aksharamukha.appspot.com/api/') | Set-Content ..\aksharamukha-front\src\mixins\ScriptMixin.js

cd ..\aksharamukha-front

quasar build

cd ..\aksharamukha-back

gcloud app deploy --project=aksharamukha --quiet

cd ..\aksharamukha-web-plugin-api

gcloud app deploy --project=aksharamukha-plugin --quiet

cd ..\build-scripts


