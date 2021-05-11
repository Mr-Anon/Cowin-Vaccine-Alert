import requests
import json
from pprint import pprint
import datetime
import time
import os
import winsound
import pyttsx3

age = 18
district_id = 506
while True:
    
    Vaccine_found = False
    

    day = datetime.date.today().day
    month = datetime.date.today().month
    year = datetime.date.today().year


    # dd/mm/YY

    d1 = str(day) + "-0" + str(month) + "-" + str(year)

    print("Searching Vaccine")
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36' , 'accept': 'application/json', 'Accept-Language': 'en_IN' }
        a = requests.get("http://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id="+str(district_id)+"&date="+d1, headers=headers).json()

        # b = json.load(a)

        for center in a['centers']:
            for session in center['sessions']:
                if session['available_capacity'] > 0:
                    if session['min_age_limit'] == age:
                        pprint(session['date'])
                        pprint(center['name'])
                        pprint(session['available_capacity'])
                        pprint(center['pincode'])
                        pprint(center)
                        Vaccine_found = True
                        engine = pyttsx3.init()
                        engine.say("Vaccine is available at " + str(center['name']))
                        engine.runAndWait()
                
        time.sleep(1)
    except Exception as e:
        print("ERROR: ", e)
        pass
    
    if Vaccine_found:
        winsound.Beep(800, 6000)
    else:
        print("No Vaccine Found")
        time.sleep(6)
        os.system('cls')
