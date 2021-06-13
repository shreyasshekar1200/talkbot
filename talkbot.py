import speech_recognition as sr
from chatterbot import ChatBot
import pyttsx3
from chatterbot.trainers import ChatterBotCorpusTrainer
bot = ChatBot('talkbot')
bot.set_trainer(ChatterBotCorpusTrainer)
# bot.train('chatterbot.corpus.english')


while(True):
    r = sr.Recognizer()
    print("please talk")
    mic = sr.Microphone()
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.record(source, duration=3)
        print("recognise")
        guess = r.recognize_google(audio)
        print(guess)

    message = guess
    if((message == 'bye') or (message == 'Bye')):
        reply = 'Nice to talk to you.'
        print('{} : {}'.format(bot.name, reply))
        break
    else:
        con = pyttsx3.init()
        print(type(message))
        print(message)
        reply = bot.get_response(message)
        con.say(reply)
        con.runAndWait()
        print('{} : {}'.format(bot.name, reply))
