import requests
import json
from pprint import pprint
import datetime
import time
import os
import winsound
import pyttsx3

age = 45
district_id = 506
while True:
    
    Vaccine_found = False
    

    day = datetime.date.today().day
    month = datetime.date.today().month
    year = datetime.date.today().year


    # dd/mm/YY

    d1 = str(day) + "-0" + str(month) + "-" + str(year)
    d2 = str(day+1) + "-0" + str(month) + "-" + str(year)
    d3 = str(day+2) + "-0" + str(month) + "-" + str(year)
    d4 = str(day+3) + "-0" + str(month) + "-" + str(year)
    d5 = str(day+4) + "-0" + str(month) + "-" + str(year)

    
    print(d1)
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36' , 'accept': 'application/json', 'Accept-Language': 'en_IN' }
        a = requests.get("http://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id="+str(district_id)+"&date="+d1, headers=headers).json()

        # b = json.load(a)

        for center in a['centers']:
            for sessions in center['sessions']:
                if sessions['available_capacity'] > 0:
                    if sessions['min_age_limit'] == age:
                        print(center)
                        Vaccine_found = True
                        engine = pyttsx3.init()
                        engine.say("Vaccine is avaliable at " + str(center['name']))
                        engine.runAndWait()
        time.sleep(2)
        print(d2)
    except:
        pass


    
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36' , 'accept': 'application/json', 'Accept-Language': 'en_IN' }
        B= requests.get("http://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id="+str(district_id)+"&date="+d2, headers=headers).json()

        # b = json.load(a)

        for center in B['centers']:
            for sessions in center['sessions']:
                if sessions['available_capacity'] > 0:
                    if sessions['min_age_limit'] == age:
                        print(center)
                        Vaccine_found = True
                        engine = pyttsx3.init()
                        engine.say("Vaccine is avaliable at " + str(center['name']))
                        engine.runAndWait()

        time.sleep(2)
        print(d3)

    except:
        pass

    
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36' , 'accept': 'application/json', 'Accept-Language': 'en_IN' }
        C= requests.get("http://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id="+str(district_id)+"&date="+d3, headers=headers).json()

        # b = json.load(a)

        for center in C['centers']:
            for sessions in center['sessions']:
                if sessions['available_capacity'] > 0:
                    if sessions['min_age_limit'] == age:
                        print(center)
                        Vaccine_found = True
                        engine = pyttsx3.init()
                        engine.say("Vaccine is avaliable at " + str(center['name']))
                        engine.runAndWait()

        time.sleep(2)
        print(d4)
    except:
        pass
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36' , 'accept': 'application/json', 'Accept-Language': 'en_IN' }
        D= requests.get("http://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id="+str(district_id)+"&date="+d4, headers=headers).json()

        # b = json.load(a)

        for center in D['centers']:
            for sessions in center['sessions']:
                if sessions['available_capacity'] > 0:
                    if sessions['min_age_limit'] == age:
                        print(center)
                        Vaccine_found = True
                        engine = pyttsx3.init()
                        engine.say("Vaccine is avaliable at " + str(center['name']))
                        engine.runAndWait()

        time.sleep(2)
        print(d5)
    except:
        pass
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36' , 'accept': 'application/json', 'Accept-Language': 'en_IN' }
        E= requests.get("http://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id="+str(district_id)+"&date="+d5, headers=headers).json()

        # b = json.load(a)

        for center in E['centers']:
            for sessions in center['sessions']:
                if sessions['available_capacity'] > 0:
                    if sessions['min_age_limit'] == age:
                        print(center)
                        Vaccine_found = True
                        engine = pyttsx3.init()
                        engine.say("Vaccine is avaliable at " + str(center['name']))
                        engine.runAndWait()
    
    except:
        pass
    
    if Vaccine_found:
        winsound.Beep(800, 3000)
    else:
        time.sleep(30)
    os.system('cls')




