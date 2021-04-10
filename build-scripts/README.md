http://aksharamukha.appspot.com

Aksharamukha aims to provide transliteration a.k.a script conversion between various scripts within the Indic cultural sphere.  Apart from the simple mapping of characters, Askharamukha also attempts to implement various script/language-specific orthographic conventions (where known) such as vowel lengths, gemination and nasalization. It also provides several customization options to fine-tune and get the desired orthography.

It is a total rewrite of the PHP-based version available [here](https://launchpad.net/aksharamukha) and [here](https://github.com/nareshv/aksharamukha).

Aksharamukha as of now supports 85 scripts and 8 romanization methods.

Ahom, Ariyaka, Assamese, Avestan, Balinese, Batak Karo, Batak Mandailing, Batak Pakpak, Batak Toba, Batak Simalungun, Bengali, Brahmi, Bhaiksuki, Buginese (Lontara), Buhid, Burmese (Myanmar), Chakma, Cham, Devanagari, Dogra, Gondi (Gunjala), Gondi (Masaram), Grantha, Grantha (Pandya), Gujarati, Hanunoo, Javanese, Kaithi, Kannada, Khamti Shan, Kharoshthi, Khmer (Cambodian), Khojki, Khom Thai, Khudawadi, Lao, Lao (Pali), Lepcha, Limbu, Malayalam, Mahajani, Marchen, Meetei Mayek (Manipuri), Modi, Mon, Mro, Multani, Newa (Nepal Bhasa), Old Persian, Oriya, PhagsPa, Punjabi (Gurmukhi), Ranjana (Lantsa), Rejang, Rohingya (Hanifi), Santali (Ol Chiki), Saurashtra, Siddham, Shan, Sharada, Sinhala, Sora Sompeng, Soyombo, Sundanese, Syloti Nagari, Tagbanwa, Tagalog, Tai Laing, Tai Tham (Lanna), Takri, Tamil, Tamil (Extended), Tamil Brahmi, Telugu, Thaana (Dhivehi), Thai, Tibetan, Tirhuta (Maithili), Urdu, Vatteluttu, Wancho, Warang Citi, Zanabazar Square, Cyrillic (Russian), IPA,

The Romanization Formats supported are:

Harvard-Kyoto, ITRANS, Velthuis, IAST, IAST (Pāḷi), ISO, Titus, Roman (Readable)

## Docker
You can use the docker-compose.yaml file to orchestrate the containers. It will start the necessary containers for the frontend/backend and, also, bind the webapp to localhost:12345. This would be easiest way to run the app locally.

## Front End
The front end is written using Quasar and Vue. Use _npm install_ to install all the dependencies and then use _quasar dev_ to start the front end. Also, please point the api to localhost at mixins/ScriptMixin.js.

## Back End
The back end is written in Python 3 with Flask. After installing all the necessary libraries, use _python3 main.py_ to intialize the backend server.

## Python Package
Aksharamukha is also available as a [Python package](https://pypi.org/project/aksharamukha/).

Use the following command to install the package.

```pip install aksharamukha```

You can read the usage instructions [here](http://aksharamukha.appspot.com/#/python)

## Rest API

There is a REST API for reasonable public consumption. You can read about it [here](http://aksharamukha.appspot.com/#/web-api)

## JSON Resources
Frequently used script resources have been made available as JSON files under aksharamukha-back/resources.

You can find the overall mapping as a JSON file [here](https://github.com/virtualvinodh/aksharamukha/tree/master/aksharamukha-back/resources/script_mapping). Those characters that have approximate mappings to the generic Indic scheme are marked with 'ʽ' (U+02BD). For instance, Thaana (Dhivehi) does not have /kha/, which has therefore been approximated to /kaʽ/. You may want to remove the character as part of post-processing. Similarly with Phags-Pa, /Ṿ/ was extraneously added to differentiate between vowels, vowel-signs and aspirate-markers. You have to remove that character as well after the mapping has been done.

The Script Matrix data is available [here](https://github.com/virtualvinodh/aksharamukha/tree/master/aksharamukha-back/resources/script_matrix). The file suffix indicates the guiding romanization and the how the characters have been divided into chunks. For instance, << script_matrix_IAST5.json >> indicates that the guiding script is IAST and the characters have been divided into chunks of 5.

The syllabary for each script can be found [here](https://github.com/virtualvinodh/aksharamukha/tree/master/aksharamukha-back/resources/syllabary). The file includes the list of vowels, consonants and the complete consonant-vowel compounds for each script.

The list of all possible Sanskrit (and Pali) conjuncts for the scripts can be found [here](https://github.com/virtualvinodh/aksharamukha/tree/master/aksharamukha-back/resources/conjuncts1) and [here](https://github.com/virtualvinodh/aksharamukha/tree/master/aksharamukha-back/resources/conjuncts2). The conjuncts have been split based on the number of consonants in the conjuncts. (The folder had to be split due to Google App Engine limitations). The suffix indicates the appended vowel. For instance, << conjuncts_Gujarati_o.json >> indicated all the possible Gujarati conjuncts that occurs with the vowel /o/.

The project is released under GNU AGPL 3.0 License