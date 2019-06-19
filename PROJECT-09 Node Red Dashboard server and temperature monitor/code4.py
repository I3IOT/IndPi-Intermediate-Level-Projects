import Adafruit_DHT    
sensor=Adafruit_DHT.DHT11 
import paho.mqtt.client as mq 
x=mq.Client() 
x.connect('iot.eclipse.org') 
gpio=7  
humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)  
if humidity is not None and temperature is not None: 
  print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)) 
  x.publish('K12-System-temp','temperature') 
  x.publish('K12-System-humi','humidity') 
  x.disconnect() 
else: 
  print('Failed to get reading. Try again!') 
