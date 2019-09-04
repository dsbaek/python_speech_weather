import speech_recognition as sr
from time import sleep
from pyowm import OWM
#import pygal                                                       
#bar_chart = pygal.Bar()
#bar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])  # Add some values
#bar_chart.render_to_file('bar_chart.svg') 


r = sr.Recognizer()
mic = sr.Microphone()


API_key = '(your key)'
owm = OWM(API_key)


while True:
    print('어디의 날씨가 궁굼 하세요? ')
    with mic as source:
        audio = r.listen(source)

    talk = r.recognize_google(audio, language = 'en')


    if talk == '감사합니다':
        print('네 알겠습니다.')
    else:
        print(talk,'의 날씨 정보')
        obs = owm.weather_at_place(talk)
        w = obs.get_weather()
        l = obs.get_location()
        temp = w.get_temperature
        rain = w.get_rain()
        print(l.get_name()+':', w.get_status()+',', temp(unit='celsius')['temp'], '˚C')

        if w.get_status() == 'Rain':
            print('현재',  l.get_name()+'은 ' '비가 옵니다. 우산을 챙겨 가세요')
        """print('강수확율:' , rain , '%')
        if rain   > 50:
            print('우산을 챙겨 가세요')
        """
    sleep(1)
    
    

