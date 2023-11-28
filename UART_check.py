# Module: UART_check.py
# Run this proram to check hardware and jumper cables connected correctly
# Can be used for both Sender and Receiver board.
#
#
#
#
# Import libraries
from machine import UART
import utime

# Initialise: UART
# UART 0, TX=GPIO0 (Pin 1), RX=GPIO1 (Pin 2)
# UART 1, TX=GPIO4 (Pin 6), RX=GPIO5 (Pin 7)
uart0 = UART(0, 115200)
#print(uart0)

# Send AT-Commands and receive replies
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
    if at_cmd + '\r\n' == dataString: return 'TX and RX possibly not crossed.'
    return dataString

# Main program
# Enter AT-Command and send it to UART
while (True):
    cmd = input('AT-Command: ')
    print(sendCmdAT(cmd))
    