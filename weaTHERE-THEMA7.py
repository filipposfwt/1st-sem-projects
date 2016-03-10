import urllib2
import json
#api key
locu_api = '07e71a4d1fc5d0fb773e4bbf5780e4d1'
print ("Please give the coords of the area you want:")
lon=raw_input("x:")
lat=raw_input("y:")
url='http://api.openweathermap.org/data/2.5/weather?lat='+lat+'&lon='+lon+'&appid='+locu_api
json_obj=urllib2.urlopen(url)
data= json.load(json_obj)

temper_K=data['main']['temp']
weather= data['weather'][0]['main']
#temperature in Json file is given in Kelvin degrees
temper_C=temper_K-273.15

if (temper_C>20):
    print ('nice...')
elif(temper_C<5):
    print ('brrrr')

if (weather=='Rain'):
    print ('im singing in the rain!')
