# RaspicoW
Data transfer using REYAX RYLR998 UARTs with Raspberry Picos running Micropython. 
There are two boards. One sender board and one receier board. 
Both boards have the exact same hardware (One Pico and one RYLR998 Module) and also identical jumper cable connections. 
The only difference is in the software. The sender will run stand-alone, while the receiver is waiting to receive some data and display them on the screen. 

In this section we will learn how data can be transported from one Raspberry Pico to another Raspberry Pico. Data will be sent across 
via two REYAX RYLR998 UART modules, which can be used for a LoraWAN P2P connection. One is configured as sender and the other as receiver. 

The LoraWAN transfer protocol allows for much greater distances compared to Bluetooth or WiFi. 
Although there are some limitations for the data transfer rates, but for small data amounts (like for sensors) Lora is very well suited. 

In this exercise no sensor is used, all data is rather extracted from a text file, which contains 100 lines of random numbers between 00 and 99. 
These data lines will be sent over the LoraWAN channel....

All programs are kept very short and simple, such that beginners can start experimenting without running into too many troubles. 

Here are the steps recommended to follow: 
1. Place two Raspberry Picos (I use Raspberry Pico W, but a normal Pico should also work...) on two seperate bread boards together with one REYAX RYLR998 UART, each.
2. Load Micropython and the Thonny IDE on both Pico boards.
3. Connect all jumper cables (as illustrated in the drawing - see *.JPG file).
4. Load the following programs on the receiver board: UART_check.py, INIT_receiver.py and RUN_receiver.py.
5. Load the following programs on the  sender  board: UART_check.py, RUN_sender.py and Z_Numbers.txt.
6. Test sender and receiver boards by entering simple AT commands on each board (make use of the UART_check.py program for that).
7. On the receiver board start first the INIT_receiver.py program and afterwards start RUN_receiver.py.
8. Leave the receiver board alone. It will continue running and wait until it receives some data from the sender board. 
9. On the sender board save the RUN_sender.py program as "main.py" on the Pico. This way t will automatically execute when connected to a power bank (like USB hub).   
8. Now, disconnect the sender board and let it run autonomously (without computer), by simply connecting it to a power source (USB hub).
10. Wait a few seconds....
11. The sender should now propagate 5 bytes of data every few seconds to the receiver. This will continue 100 times, until the end of the text file.
12. A quick LED flash light indicates that the sending process is ongoing. 

13. Have fun!!
14. Good luck.
   
