Aksharamukha aims to provide transliteration a.k.a script conversion between various scripts within the Indic cultural sphere.  These include historic scripts, contemporary Brahmi-derived/inspired scripts, scripts invented for minority Indian languages, scripts that have co-existed with Indic scripts (like Avestan) or linguistically related scripts like Old Persian. It also specifically provides lossless transliteration between the main Indian scripts (along with Sinhala).

Apart from the simple mapping of characters, Askharamukha also attempts to implement various script/language-specific orthographic conventions (where known) such as vowel lengths, gemination and nasalization. It also provides several customization options to fine-tune and get the desired orthography.

Aksharamukha as of now supports 85 scripts and 8 romanization methods.

The scripts supported are:

*Ahom, Ariyaka, Assamese, Avestan, Balinese, Batak Karo, Batak Mandailing, Batak Pakpak, Batak Toba, Batak Simalungun, Bengali, Brahmi, Bhaiksuki, Buginese (Lontara), Buhid, Burmese (Myanmar), Chakma, Cham, Devanagari, Dogra, Gondi (Gunjala), Gondi (Masaram), Grantha, Grantha (Pandya), Gujarati, Hanunoo, Javanese, Kaithi, Kannada, Khamti Shan, Kharoshthi, Khmer (Cambodian), Khojki, Khom Thai, Khudawadi, Lao, Lao (Pali), Lepcha, Limbu, Malayalam, Mahajani, Marchen, Meetei Mayek (Manipuri), Modi, Mon, Mro, Multani, Newa (Nepal Bhasa), Old Persian, Oriya, PhagsPa, Punjabi (Gurmukhi), Ranjana (Lantsa), Rejang, Rohingya (Hanifi), Santali (Ol Chiki), Saurashtra, Siddham, Shan, Sharada, Sinhala, Sora Sompeng, Soyombo, Sundanese, Syloti Nagari, Tagbanwa, Tagalog, Tai Laing, Tai Tham (Lanna), Takri, Tamil, Tamil (Extended), Tamil Brahmi, Telugu, Thaana (Dhivehi), Thai, Tibetan, Tirhuta (Maithili), Urdu, Vatteluttu, Wancho, Warang Citi, Zanabazar Square, Cyrillic (Russian), IPA,*

The Romanization Formats supported are:

*Harvard-Kyoto, ITRANS, Velthuis, IAST, ISO, Titus*

## Usage and Examples

Please find the usage instructions [here](http://aksharamukha.appspot.com/#/python).

## Online Version

The package as an online tool is available [here](http://aksharamukha.appspot.com/).

## JSON Resources
You can find the overall mapping as a JSON file [here](https://github.com/virtualvinodh/aksharamukha/tree/master/aksharamukha-back/resources/script_mapping). Those characters that have approximate mappings to the generic Indic scheme are marked with 'ʽ' (U+02BD). For instance, Thaana (Dhivehi) does not have /kha/, which has therefore been approximated to /kaʽ/. You may want to remove the character as part of post-processing. Similarly with Phags-Pa, /Ṿ/ was extraneously added to differentiate between vowels, vowel-signs and aspirate-markers. You have to remove that character as well after the mapping has been done.

## Contact

If you have any questions please head to [Github](https://github.com/virtualvinodh/aksharamukha) or mail vinodh@virtualvinodh.com