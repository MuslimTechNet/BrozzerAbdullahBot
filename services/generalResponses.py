from random import randint
from linereader import copen
from responseConstants import constants

# Submission Response
def taqiyaPostResponse():
    return "Sniff, sniff... I smell Taqiya\n\n"

# Both Submission and Comment Responses
def takbirResponse():
    return "#الله اكبر  ALLAHU AKBAR!!!!\n\n"
def staffGorillaResponse():
    return "[You called me?](https://imgur.com/T60vscc)\n\n"

# Comment Responses
def goodBotResponse():
    return "Good Human. " + get_random_dua() + "\n\n"
def badBotResponse():
    return "[Behave yourself!](https://i.ytimg.com/vi/oL15on_OyBA/hqdefault.jpg)\n\n"
def taqiyaResponse():
    return  "This brozzer/sizter is using taqqiya, 100% true taqqiya master\n\n"
def jazakallahResponse():
    return "وأنتم فجزاكم الله خيرا Wa antum, fa jazakumullahu khairan\n\n"
def infoResponse():
    return constants.info
def get_random_dua():
    openfile = copen("./constants/dua.txt")
    lines = openfile.count('\n') + 1
    dua = openfile.getline(randint(1,lines))
    return dua