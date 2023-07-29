import bluetooth
import RPi.GPIO as GPIO
led=12

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(led,GPIO.OUT)
GPIO.output(led,0)

server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

port=1

server_socket.bind(('',1))
server_socket.listen(1)


client_socket,address = server_socket.accept()
print("Accepted connection from"+str(address))
while 1:

    data = client_socket.recv(1024)
    print("Received:%s"%data)

    if(data == "0"):
        print("LED OFF")
        GPIO.output(led,0)
    if(data == "1"):
        print("LED ON")
        GPIO.output(led,1)
    if(data == "q"):
        print("Quit")
        break

client_socket.close()
server_socket.close()
GPIO.cleanup()
