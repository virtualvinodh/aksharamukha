(Get-Content .\aksharamukha-front\src\layouts\default.vue).replace('fonts.css', 'fontsdocker.css') | Set-Content .\aksharamukha-front\src\layouts\default.vue

(Get-Content .\aksharamukha-front\src\mixins\ScriptMixin.js).replace('https://aksharamukha.appspot.com/api/', 'http://localhost:8085/api') | Set-Content .\aksharamukha-front\src\mixins\ScriptMixin.js

python .\dockerfonts.py

cd .\aksharamukha-fonts

docker build -t virtualvinodh/aksharamukha-fonts .

cd ..\aksharamukha-front

quasar build

cd .\dist

docker build -t virtualvinodh/aksharamukha-front .

cd ..\..\aksharamukha-back

docker build -t virtualvinodh.com/aksharamukha-back .

docker push virtualvinodh/aksharamukha-fonts
docker push virtualvinodh/aksharamukha-front
docker push virtualvinodh/aksharamukha-back

cd ..

(Get-Content .\aksharamukha-front\src\layouts\default.vue).replace('fontsdocker.css', 'fonts.css') | Set-Content .\aksharamukha-front\src\layouts\default.vue





