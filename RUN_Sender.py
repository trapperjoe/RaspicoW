# Module: RUN_Sender.py
# Run this proram on the sender board after you have started the Receiver.
# All parameter should be set correctly within this program.
#
# Most parameters are left as their default values, but some needed to be changed: 
# 
# BAND=866200000 - Band adapted to comply with European legislation.
# Please check what Band is allowed in your location. 
# ADDRESS=11 - Needs to be different from receiver address.
# NETWORKID=18 - Needs to match the NETWORKID of the respective sender.
#
#
#
#
# Import libraries
from machine import UART, Pin
import utime


# Function: Send AT-Command and receive replies
def sendCmdAT (at_cmd):
    char = ''
    dataString = ''
    uart0.write(at_cmd + '\r\n')
    utime.sleep(2)
    while (char is not None):
        char = uart0.read(1)
        try:
            dataString += char.decode('utf-8')
        except: pass
    # print (dataString)
    return dataString

def lora_init():
    cmd = 'AT'
    print("Command: ", cmd, '\t', "Response: ", sendCmdAT(cmd))
    utime.sleep(1)  
    print("Command: ", cmd, '\t', "Response: ", sendCmdAT(cmd))
    cmd = 'AT+RESET'
    print("Command: ", cmd, '\t', "Response: ", sendCmdAT(cmd))
    cmd = 'AT+IPR=115200'
    print("Command: ", cmd, '\t', "Response: ", sendCmdAT(cmd))
    cmd = 'AT+BAND=866200000'
    print("Command: ", cmd, '\t', "Response: ", sendCmdAT(cmd))
    cmd = 'AT+NETWORKID=18'
    print("Command: ", cmd, '\t', "Response: ", sendCmdAT(cmd))
    cmd = 'AT+ADDRESS=11'
    print("Command: ", cmd, '\t', "Response: ", sendCmdAT(cmd))



# Main program
# Initialize Onboard-LED
led_onboard = Pin("LED", Pin.OUT)

# Blink LED three times to indicate that the program is running
i = 0
while i < 3:
    led_onboard.on()
    utime.sleep_ms(300)
    led_onboard.off()
    utime.sleep_ms(300)
    i = i+1

# Initialize UART
uart0 = UART(0, 115200)
print("UART0 = ", uart0) # Sender

# Initialize RYLR998 Module as Sender (Network = 18, Address = 11)
lora_init()

# Open file with random variables
DateiZ = open('Z_Numbers.txt', 'r')
     
counter = 0
for line in DateiZ:
    index = line[0:2]
    znum = line[3:5]
    ##print("index = ", index)
    ##print("znum  = ", znum)
    
# Compose and send message of 5 bytes
    cmd = 'AT+SEND=37,'
    cmd = cmd + '5' + ',' + index + '\t' + znum
     
    #print("Command: ", cmd, '\n', "Response: ", sendCmdAT(cmd))
    led_onboard.on()
    sendCmdAT(cmd)     
    led_onboard.off()
    utime.sleep(2)
      
# Check if data was sent
    cmd = 'AT+SEND?'
    print("Command: ", cmd, '\n', "Response: ", sendCmdAT(cmd))
    utime.sleep(1)
    print("*******************************************************")
    print()
    counter += 1
  
# Terminate program and close file
DateiZ.close()
    
    
    
    
    
    
    
