# Module: RUN_Receiver.py
# Run this proram on the receiver board after INIT_Receiver.py
#
#
# Include libraries
from machine import UART
import utime
import array

# Initialize UART0 with 115200 Baud
# UART0, TX=GPIO0 (Pin 1), RX=GPIO1 (Pin 2)
uart0 = UART(0, 115200)
print(uart0)

print('Waiting for data ...')

# Initialize variables
counter = 0
line= '______________________________________________________________'

# Loop
while True:
    utime.sleep(1)
    char = uart0.read()
    if char is not None: # as long as there is data continue reading...
        try:
            line = char.decode()
            print("Received: ", '\t', counter, '\t', line[10:18])
            # Separation via tabs ('\t') helps with analysing the data later
            counter += 1
            
        except: print(char)

                