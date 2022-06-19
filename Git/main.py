from greetings import greets
from translate import Translator

translator = Translator(to_lang='pt')

for g in greets:
    print(translator.translate(g).title()+ "!!!")



print("hello")
