http://aksharamukha.appspot.com

Aksharamukha aims to provide transliteration a.k.a script conversion between various scripts within the Indic cultural sphere.  Apart from the simple mapping of characters, Aksharamukha also attempts to implement various script/language-specific orthographic conventions (where known) such as vowel lengths, gemination and nasalization. It also provides several customization options to fine-tune and get the desired orthography.

It is a total rewrite of the PHP-based version available [here](https://launchpad.net/aksharamukha) and [here](https://github.com/nareshv/aksharamukha).

Aksharamukha as of now supports 120 scripts and 21 romanization methods. The scripts supported are:

*Ahom, Arabic, Ariyaka, Assamese, Avestan, Balinese, Batak Karo, Batak Mandailing, Batak Pakpak, Batak Simalungun, Batak Toba, Bengali (Bangla), Bhaiksuki, Brahmi, Buginese (Lontara), Buhid, Burmese (Myanmar), Chakma, Cham, Cyrillic (Russian), Devanagari, Dogra, Elymaic, Ethiopic (Abjad), Gondi (Gunjala), Gondi (Masaram), Grantha, Grantha (Pandya), Gujarati, Hanunoo, Hatran, Hebrew, Hebrew (Judeo-Arabic), Imperial Aramaic, Inscriptional Pahlavi, Inscriptional Parthian, Japanese (Hiragana), Japanese (Katakana), Javanese, Kaithi, Kannada, Kawi, Khamti Shan, Kharoshthi, Khmer (Cambodian), Khojki, Khom Thai, Khudawadi, Lao, Lao (Pali), Lepcha, Limbu, Mahajani, Makasar, Malayalam, Manichaean, Marchen, Meetei Mayek (Manipuri), Modi, Mon, Mongolian (Ali Gali), Mro, Multani, Nabataean, Nandinagari, Newa (Nepal Bhasa), Old North Arabian, Old Persian, Old Sogdian, Old South Arabian, Oriya (Odia), Pallava, Palmyrene, Persian, PhagsPa, Phoenician, Psalter Pahlavi, Punjabi (Gurmukhi), Ranjana (Lantsa), Rejang, Rohingya (Hanifi), Roman (IPA Indic), Samaritan, Santali (Ol Chiki), Saurashtra, Shahmukhi, Shan, Sharada, Siddham, Sinhala, Sogdian, Sora Sompeng, Soyombo, Sundanese, Syloti Nagari, Syriac (Eastern), Syriac (Estrangela), Syriac (Western), Tagalog, Tagbanwa, Tai Laing, Takri, Tamil, Tamil (Extended), Tamil Brahmi, Telugu, Thaana (Dhivehi), Thai, Tham (Lanna), Tham (Lao), Tham (Tai Khuen), Tham (Tai Lue), Tibetan, Tirhuta (Maithili), Ugaritic, Urdu, Vatteluttu, Wancho, Warang Citi, Zanabazar Square*

The Indic Romanization Formats supported are: *Harvard-Kyoto, ITRANS, Velthuis, IAST, IAST (Pāḷi), ISO, ISO (Pāḷi), Titus, SLP1, WX, Roman (Readable), Roman (Colloquial)* . The Semitic Romanization Formats supported are: *Semitic (Aksharamukha), Semitic Typeable (Aksharamukha), ISO 259 Hebrew, SBL Hebrew, ISO 233 Arabic, DMG Persian*

## Docker
You can use the docker-compose.yaml file to orchestrate the containers. It will start the necessary containers for the frontend/backend and, also, bind the webapp to localhost:12345. This would be easiest way to run the app locally. It also pulls a third container that serves the fonts locally. Without this, you would need an internet connection to load the web fonts.

1. Install [Docker Desktop](https://docs.docker.com/get-docker/)
2. To build and start all docker containers, run `docker compose up` inside this project's root folder. This will use the configuration given in `docker-compose.yaml`
3. To load the frontend, point your browser at the port displayed in Docker desktop. (`http://localhost:12345`)

## Front End
The front end is written using Quasar and Vue. Use _npm install_ to install all the dependencies and then use _quasar dev_ to start the front end. Also, please point the api to localhost at mixins/ScriptMixin.js.

1. Install a node.js version supported by quasar. As of May 2021, we recommend the current LTS v14. For example, on OSX you can use [homebrew](https://brew.sh/) and run `brew install node@14`
2. Install [Quasar-cli](https://quasar.dev/quasar-cli/installation) e.g. by `npm install -g @quasar/cli`
3. Comment out line 9 in `quasar.conf.js` to disable importing the analytics plugin which will casue the build to fail
4. Comment out `import keys from '../keys.js'` in `src/pages/index.vue`. Add below that line:

```
// sets empty API key for Google's OCR API to build the project without using that service
var keys = {}
keys['api_key'] = ''
```

5. Run `quasar dev` and point your browser at the address specied in the output of the `quasar dev` command.

## Back End
The back end is written in Python 3 with Flask. After installing all the necessary libraries, use _python3 main.py_ to intialize the backend server.

## Python Package
Aksharamukha is also available as a [Python package](https://pypi.org/project/aksharamukha/). There is a separate repository for it [https://github.com/virtualvinodh/aksharamukha-python](https://github.com/virtualvinodh/aksharamukha-python).

## Rest API
There is a REST API for reasonable public consumption. You can read about it [here](http://aksharamukha.appspot.com/#/web-api)

## Chrome Extension
The source code for [Aksharamukha Chrome Extension](https://chrome.google.com/webstore/detail/aksharamukha-script-conve/nahdihjmpjlifenlocchbokbnpoifpho?hl=en) can be found [here](https://github.com/virtualvinodh/aksharamukha-extension).

## Web Plugin
The source code for the Web Plugin can be found [here](https://github.com/virtualvinodh/aksharamukha-extension). Please, do not use the files linked here. They are for legacy purposes, so that any sites that load the old plugins from here do not break.

## JSON Resources
Frequently used script resources have been made available as JSON files under aksharamukha-back/resources.

You can find the overall mapping as a JSON file [here](https://github.com/virtualvinodh/aksharamukha/tree/master/aksharamukha-back/resources/script_mapping). Those characters that have approximate mappings to the generic Indic scheme are marked with 'ʽ' (U+02BD). For instance, Thaana (Dhivehi) does not have /kha/, which has therefore been approximated to /kaʽ/. You may want to remove the character as part of post-processing. Similarly with Phags-Pa, /Ṿ/ was extraneously added to differentiate between vowels, vowel-signs and aspirate-markers. You have to remove that character as well after the mapping has been done.

The Script Matrix data is available [here](https://github.com/virtualvinodh/aksharamukha/tree/master/aksharamukha-back/resources/script_matrix). The file suffix indicates the guiding romanization and the how the characters have been divided into chunks. For instance, << script_matrix_IAST5.json >> indicates that the guiding script is IAST and the characters have been divided into chunks of 5.

The syllabary for each script can be found [here](https://github.com/virtualvinodh/aksharamukha/tree/master/aksharamukha-back/resources/syllabary). The file includes the list of vowels, consonants and the complete consonant-vowel compounds for each script.

The list of all possible Sanskrit (and Pali) conjuncts for the scripts can be found [here](https://github.com/virtualvinodh/aksharamukha/tree/master/aksharamukha-back/resources/conjuncts1) and [here](https://github.com/virtualvinodh/aksharamukha/tree/master/aksharamukha-back/resources/conjuncts2). The conjuncts have been split based on the number of consonants in the conjuncts. (The folder had to be split due to Google App Engine limitations). The suffix indicates the appended vowel. For instance, << conjuncts_Gujarati_o.json >> indicated all the possible Gujarati conjuncts that occurs with the vowel /o/.

The project is released under GNU AGPL 3.0 License
