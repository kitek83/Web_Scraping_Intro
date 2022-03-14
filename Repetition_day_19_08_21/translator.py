from googletrans import Translator

translator = Translator()

query = '2nd officer SDPO find work'
translate0 = translator.translate(query, src='en', dest='en')
translate1 = translator.translate(query, src='en', dest='de')
translate2 = translator.translate(query, src='en', dest='pl')
print(f'{translate1.origin}({translate1.src})-->{translate1.text}({translate1.dest})')
print()
print(f'{translate1.text} ({translate1.dest})')
print('--------------------')

translates = [translate0,translate1, translate2]
for translate in translates:
    print(f'{translate.text} ({translate.dest})')

print('===================')
print(translate2.text)