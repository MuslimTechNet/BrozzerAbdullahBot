import requests
import json

def getQuranVerse(searchObj,ayah_ar):
    if (int(searchObj.group(1)) > 114): #If surah number > 114 return Invalid Surah since only 114 Surah in Quran
        return ("Invalid Surah")
    metaData = requests.get(url = f'http://api.alquran.cloud/ayah/{searchObj.group(1)}:1') #To check the number of verses in the Surah
    end = int(json.loads(metaData.text)['data']['surah']['numberOfAyahs'])
    start = 1
    ayah_ar = ayah_ar + json.loads(metaData.text)['data']['surah']['name'] + " : " + json.loads(metaData.text)['data']['surah']['englishName'] + " : " + json.loads(metaData.text)['data']['surah']['englishNameTranslation'] + "\n\n|Verse|Ayah|Translation Saheeh International|\n|:-|:-|:-|\n"
    ayah_end = "\n\n"

    if(searchObj.group(3)): #If command is in -quran 1:5-7 format, the other section covers -quran 1:5 format
        start = int(searchObj.group(2))
        end = int(searchObj.group(3))
    
        if (end-start > 9):
            end = start + 9
            ayah_end = "\n\n(Truncated - max 10 Aayat)\n\n"

        for x in range (start,end+1):
            msg = requests.get(url = f'http://api.alquran.cloud/ayah/{searchObj.group(1)}:{str(x)}/en.sahih')
            msg_ar = requests.get(url = f'http://api.alquran.cloud/ayah/{searchObj.group(1)}:{str(x)}')
            response_text = json.loads(msg.text)
            response_text_ar = json.loads(msg_ar.text)
            ayah_ar = ayah_ar + "|" + searchObj.group(1) + ":" + str(x) + "|" + response_text_ar['data']['text'] + "|" +  response_text['data']['text'] + "|\n"
        return ayah_ar + ayah_end
        
    else:  #If command is in -quran 1:5-7 format,
        print (searchObj.group(0))
        msg = requests.get(url = f'http://api.alquran.cloud/ayah/{searchObj.group(1)}:{searchObj.group(2)}/en.sahih')
        msg_ar = requests.get(url = f'http://api.alquran.cloud/ayah/{searchObj.group(1)}:{searchObj.group(2)}')
        response_text = json.loads(msg.text)
        response_text_ar = json.loads(msg_ar.text)
        ayah_ar = ayah_ar + "|" + searchObj.group(1) + ":" + searchObj.group(2) + "|" + response_text_ar['data']['text'] + "|" +  response_text['data']['text'] + "|\n"
        return ayah_ar + ayah_end