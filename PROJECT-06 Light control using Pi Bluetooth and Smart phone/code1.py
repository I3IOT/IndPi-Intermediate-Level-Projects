import RPi.GPIO as GPIO        #calling for header file which helps in using GPIOs of PI 
LED1=4 
LED2=17 
LED3=27 
GPIO.setmode(GPIO.BCM)     #programming the GPIO by BCM pin numbers. (like PIN40 as GPIO21) 
GPIO.setwarnings(False) 
GPIO.setup(LED1,GPIO.OUT)   
GPIO.setup(LED2,GPIO.OUT)   
GPIO.setup(LED3,GPIO.OUT) 
GPIO.output(LED1,0) 
GPIO.output(LED2,0) 
GPIO.output(LED3,0) 
server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM ) 
port = 1 
server_socket.bind(("",port)) 
server_socket.listen(1) 
client_socket,address = server_socket.accept() 
print "Accepted connection from ",address 
while 1: 
  data = client_socket.recv(1024) 
  print "Received: %s" % data 
  If (data == "10"):    #if '10' is sent from the Android App, turn OFF the LED 
    print ("GPIO 4 LOW, LED OFF") 
    GPIO.output(LED,0) 
  if (data == "11"):    #if '11' is sent from the Android App, turn ON the LED 
    print ("GPIO 4 HIGH, LED ON") 
    GPIO.output(LED,1) 
  if (data == "20"):    #if '20' is sent from the Android App, turn OFF the LED 
    print ("GPIO 17 LOW, LED OFF") 
    GPIO.output(LED,0) 
  if (data == "21"):    #if '21' is sent from the Android App, turn ON the LED 
    print ("GPIO 17 HIGH, LED ON") 
    GPIO.output(LED,1) 
  if (data == "30"):    #if '30' is sent from the Android App, turn OFF the LED 
    print ("GPIO 27 LOW, LED OFF") 
    GPIO.output(LED,0) 
  if (data == "31"):    #if '31' is sent from the Android App, turn ON the LED 
    print ("GPIO 27 HIGH, LED ON") 
    GPIO.output(LED,1) 
  if (data == "q"): 
    print ("Quit") 
    break 
client_socket.close() 
server_socket.close()

