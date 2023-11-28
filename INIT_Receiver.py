# Module: INIT_Receiver.py
# Run this proram on the receiver board before RUN_Receiver to make sure all
# parameters are set correctly.
#
# This program first initializes the serial interface UART0 on the Pico.
# The next ation is to set some basic parameters on the REYAX RYLR998 UART Module
# so it will to act as a receiver.
#
# Most parameters are left as their default values, but some needed to be changed: 
# 
# BAND=866200000 - Band adapted to comply with European legislation.
# Please check what Band is allowed in your location. 
# ADDRESS=37 - Needs to be different from sender address.
# NETWORKID=18 - Needs to match the NETWORKID of the respective sender.
#
#
#
#
# Load libraries
from machine import UART
import utime

# Initialise UART0
# UART0, TX=GPIO0 (Pin 1), RX=GPIO1 (Pin 2)

uart0 = UART(0, 115200)
print(uart0)

# Send AT-Commands and receive messages back
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
    if at_cmd + '\r\n' == dataString: return 'TX und RX sind vertauscht.'
    return dataString


# Initialize RYLR998 Module as Receiver (Network = 18, Address = 37)
def init_998():
    sendCmdAT('AT')
    sendCmdAT('AT+RESET')
    sendCmdAT('AT+IPR=115200')
    sendCmdAT('AT+BAND=866200000')
    sendCmdAT('AT+NETWORKID=18')
    sendCmdAT('AT+ADDRESS=37')
    return
   
# Read all critical configuration data from RYLR998 Module and print them on screen
def display_998():
    print("AT-Response",   sendCmdAT('AT'))
    print("Baud rate = ",  sendCmdAT('AT+IPR?'))
    print("Band    = ",  sendCmdAT('AT+BAND?'))
    print("Adress  = ",  sendCmdAT('AT+ADDRESS?'))
    print("NetworkID = ", sendCmdAT('AT+NETWORKID?'))
    return
   

# Main program
# Initialize Module and show status
print("=============== Initialize ===================")
init_998()
print("***************   Status     *****************")
display_998()
