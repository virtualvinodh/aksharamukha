import re
import requests

fontscss = open("./aksharamukha-front/src/statics/fonts.css", "r")

content = fontscss.read()

fonts = list(map(lambda x: x.replace('\'', ''), re.findall(r'(?<=url\().*(?=\))', content)))

print('Starting font replacement')

for i, font in enumerate(fonts[:]):
  fontparts = font.split('/')
  url = '/'.join(fontparts[:-1])
  content = content.replace(url, 'http://localhost:9899')

  filename = fontparts[-1]

  print('Downloading ' + filename + ' ' + str(i+1))

  r = requests.get(font)

  with open('./aksharamukha-fonts/' + filename, 'wb') as f:
    f.write(r.content)

with open('./aksharamukha-front/src/statics/fontsdocker.css', 'w') as f:
    f.write(content)

fontscss.close()

print('Font replacement complete')