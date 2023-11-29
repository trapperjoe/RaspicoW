# RaspicoW
Send data from one Raspberry Pico to another by use of REYAX RYLR998 UARTs. 
There are two boards. One sender board and one receier board. Each board has two modules on it: One Raspberry Pico and one REYAX RYLR998 UART.
On both board the two modules are connected in exactly the same way (pls. refer to the "Drawing.JPG" file). 
The only difference is in the software. The sender will run stand-alone, while the receiver is waiting to receive some data and will then display them on the screen. 

On the receiver board the following files should be placed in the main directory: 
UART_check.py
INIT_Receiver.py 
RUN_Receiver.py

On the sender board the following files should be placed in the main directory: 
UART_check.py
Z_Numbers.txt
RUN_Sender.py - This one should be renamed to main.py once all initial tests are successfully completed. Then it can rund as a stand-alone device. 

In this exercise we will experience how data can be transported from one Raspberry Pico to another Raspberry Pico. Data will be sent across 
via two REYAX RYLR998 UART modules, by use of the LoraWAN protocol. One board is configured as the "sender" and the other as the "receiver". 

The LoraWAN transfer protocol allows for much greater distances compared to Bluetooth or WiFi. This is very useful for IoT projects. 
There are some limitations with bandwidth, so large data files cannot be sent over. But for small data amounts (like for sensors) Lora is very well suited. 

In this example there are no sensors. All data is taken from a local text file (Z_Numbers.txt), which contains an indexed list of random 2-digits integer numbers. 
These records will be sent over the LoraWAN channel line by line, until all lines are transfered. Then the sender program just terminates. 

Programs are kept very short and simple, such that also beginners will quickly unerstand and can start experimenting without running into too many troubles. 

Here are the recommended steps to follow: 
1. Place two Raspberry Picos (I use Raspberry Pico W, but a normal Pico should also work...) on two seperate bread boards together with one REYAX RYLR998 UART, each.
2. Load Micropython on both Pico boards. More information can be found on the https://micropython.org/ web site.  
3. Connect all jumper cables (as illustrated in the drawing - see "Drawing.JPG" file).
4. Load the following programs on the receiver board: UART_check.py, INIT_receiver.py and RUN_receiver.py.
5. Load the following programs on the  sender  board: UART_check.py, RUN_sender.py and Z_Numbers.txt.
6. Test sender and receiver boards by entering simple AT commands on each board (make use of the UART_check.py program for that).
7. On the receiver board start first the INIT_receiver.py program and once successfully finished, run the RUN_receiver.py program.
8. Leave the receiver board alone. It will continue running and will wait until it receives some data from the sender board. 
9. On the sender board save the RUN_sender.py program as "main.py" on the Pico. It will automatically execute once re-connected.
10. Now, disconnect the sender board and let it run autonomously (without computer), by simply connecting it to a power source (USB hub).
11. Wait a few seconds....
12. The sender should now propagate 5 bytes of data every few seconds. This will continue until the last line of the text file has been processed. 
13. On the sender board a quick LED flashing light indicates, that the sending process is ongoing. The receiver should now show the data received.

14. Have fun!!
15. Good luck.

One last hint: The programming of the internal LED is differnet for a Pico and a Pico W. 
For the Pico the initializaton is:    led_onboard = Pin(25, Pin.OUT)
For the Pico W  the initializaton is: led_onboard = Pin("LED", Pin.OUT)
Therfore a small adjustment in the code might be necessary if you run a normal Raspberry Pico device and not a Raspberry Pico W.





   
