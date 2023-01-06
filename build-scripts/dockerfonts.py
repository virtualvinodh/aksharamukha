import re

fontscss_aksharamukha = open("../../aksharamukha-fonts/aksharamukha-fonts.css", "r")
fontscss_noto = open("../../aksharamukha-notomirror/aksharamukha-notomirror.css", "r")

content_aksharamukha = fontscss_aksharamukha.read()
content_noto = fontscss_noto.read()

content = content_aksharamukha + content_noto

fonts_aksharamukha = list(map(lambda x: x.replace('\'', ''), re.findall(r'(?<=url\().*(?=\))', content_aksharamukha)))
fonts_noto = list(map(lambda x: x.replace('\'', ''), re.findall(r'(?<=url\().*(?=\))', content_noto)))

fonts = fonts_aksharamukha + fonts_noto

print('Starting font replacement')

for i, font in enumerate(fonts[:]):
  fontparts = font.split('/')
  url = '/'.join(fontparts[:-1])
  content = content.replace(url, 'http://localhost:9899')

content = content.replace("@import url('http://localhost:9899/aksharamukha-notomirror.css');", '').strip()

with open('../../aksharamukha-docker-fonts/aksharamukha-docker-fonts.css', 'w') as f:
    f.write(content)

fontscss_aksharamukha.close()
fontscss_noto.close()

print('Font replacement complete')