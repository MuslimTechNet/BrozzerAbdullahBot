import requests
import json

def getQuranVerse(searchObj):
    if(searchObj.group(3)):
        print (searchObj.group(0))
        # print (searchObj.group(1))
        
        start = int(searchObj.group(2))
        end = int(searchObj.group(3))

        ayah_end = ""

        if (end-start > 9):
            end = start + 9
            ayah_end = "(Truncated - max 10 Aayat)\n\n"

        # print (start)
        # print (end)

        ayah_ar = ""

        for x in range (start,end+1):

            msg = requests.get(url = f'http://api.alquran.cloud/ayah/{searchObj.group(1)}:{str(x)}/en.sahih')
            msg_ar = requests.get(url = f'http://api.alquran.cloud/ayah/{searchObj.group(1)}:{str(x)}')
            response_text = json.loads(msg.text)
            response_text_ar = json.loads(msg_ar.text)
            ayah_ar = ayah_ar + "Qur'an " + searchObj.group(1) + ":" + str(x) + "\n\n> " + response_text_ar['data']['text'] + "\n\n> " +  response_text['data']['text'] + "\n\n"
            # print(ayah_ar)
        return ayah_ar + ayah_end
    else:
        print (searchObj.group(0))
        # print (searchObj.group(1))
        # print (searchObj.group(2))
        msg = requests.get(url = f'http://api.alquran.cloud/ayah/{searchObj.group(1)}:{searchObj.group(2)}/en.sahih')
        msg_ar = requests.get(url = f'http://api.alquran.cloud/ayah/{searchObj.group(1)}:{searchObj.group(2)}')
        response_text = json.loads(msg.text)
        response_text_ar = json.loads(msg_ar.text)
        ayah_ar = "Qur'an " + searchObj.group(1) + ":" + searchObj.group(2) + "\n\n> " + response_text_ar['data']['text'] + "\n\n> " + response_text['data']['text'] + "\n\n"
        print(ayah_ar)
        return ayah_ar
