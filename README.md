http://aksharamukha.appspot.com

Aksharamukha aims to provide script conversion between various scripts within the Indic cultural sphere.  Apart from the simple mapping of characters, Askharamukha also attempts to implement various script/language-specific orthographic conventions (where known) such as vowel lengths, gemination and nasalization. It also provides several customization options to fine-tune and get the desired orthography.

It is basically totally rewrite of the PHP-based version available [here](https://launchpad.net/aksharamukha) and [here](https://github.com/nareshv/aksharamukha).

Aksharamukha as of now supports 66 scripts and 8 romanization methods.

## Front End
The front end is written using Quasar and Vue. Use _npm install_ to install all the dependencies and then use _quasar dev_ to start the front end. Also, please point the api to localhost at mixins/ScriptMixin.js.

## Back End
The back end is written in Python 3 with Flask. After installing all the libraries, use _python3 main.py_ to intialize the backend server.