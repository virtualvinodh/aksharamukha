(Get-Content ..\aksharamukha-front\src\statics\fonts.css).replace('https://cdn.jsdelivr.net/gh/virtualvinodh/aksharamukha-fonts/aksharamukha-fonts.css', 'http://localhost:9899/aksharamukha-docker-fonts.css') | Set-Content ..\aksharamukha-front\src\statics\fonts.css

(Get-Content ..\aksharamukha-front\src\mixins\ScriptMixin.js).replace('https://aksharamukha.appspot.com/api/', 'http://localhost:8085/api/') | Set-Content ..\aksharamukha-front\src\mixins\ScriptMixin.js

# python .\dockerfonts.py

Get-ChildItem ..\..\aksharamukha-fonts *.ttf | Copy-Item -Destination ..\..\aksharamukha-docker-fonts -Force -PassThru
Get-ChildItem ..\..\aksharamukha-fonts *.otf | Copy-Item -Destination ..\..\aksharamukha-docker-fonts -Force -PassThru
Get-ChildItem ..\..\aksharamukha-notomirror *.ttf | Copy-Item -Destination ..\..\aksharamukha-docker-fonts -Force -PassThru
Get-ChildItem ..\..\aksharamukha-notomirror *.otf | Copy-Item -Destination ..\..\aksharamukha-docker-fonts -Force -PassThru

cd ..\..\aksharamukha-docker-fonts

docker build --no-cache -t virtualvinodh/aksharamukha-fonts .

cd ..\aksharamukha\aksharamukha-front

npx quasar build

cd .\dist

docker build --no-cache -t virtualvinodh/aksharamukha-front .

cd ..\..\aksharamukha-back

docker build --no-cache -t virtualvinodh/aksharamukha-back .

docker push virtualvinodh/aksharamukha-fonts
docker push virtualvinodh/aksharamukha-front
docker push virtualvinodh/aksharamukha-back

(Get-Content ..\aksharamukha-front\src\statics\fonts.css).replace('http://localhost:9899/aksharamukha-docker-fonts.css', 'https://cdn.jsdelivr.net/gh/virtualvinodh/aksharamukha-fonts/aksharamukha-fonts.css') | Set-Content ..\aksharamukha-front\src\statics\fonts.css

cd ..\build-scripts