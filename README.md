# RaspicoW
Transfer of Data using  REYAX RYLR998 UART with Raspberry Pico W 
In this section we will experiment with two Raspberry Pico W boards which will send data across via REYAX RYLR998 UARTs. 
The Lora transfer protocol, which is supported by the two RYLR998 UARTs allows for much greater distances to be covered than WiFi. 
There are some limitations as of data transfer rates, but for small amouts of date (like sensors) Lora is very well suited. 

In this example no sensor is used, but it is read from a text file with random two-digits integer numbers ranging from 0 to 99. 
The program is kept very simple, such that beginners can start experimenting without a lot of effort.  

Here are the steps to follow: 
1. Purchase 2 Raspberry Picos (I use Raspberry Pico W, but normal Pico should also work...) and two REYAX RYLR998 UART boards.
2. Load Micropython and Thonny on both Pico boards
3. Connect jumper cable (see drawing)
4. Load the following programs on the receiver board: UART_check.py, INIT_receiver.py and RUN_receiver.py
5. Load the following programs on the  sender  board: UART_check.py, RUN_sender.py and Z_Numbers.txt
6. Test Sender and receiver boards by sending simple AT commands on each board (you can use of the UART_check.py program for that)
7. On the receiver board start first the INIT_receiver.py program and afterwards  that start RUN_receiver.py.
8. Wait a few seconds.....
9. On the sender board make a copy of the RUN_sender.py program and call it main.py. Store it on the sender board. 
8. Now, disconnect the sender board and let it run autonomously (without computer), by simply connecting it to a USB cable with power adaptor.
10. Wait a few seconds....
11. The sender should now propagate 5 bytes of data every few seconds to the receiver. This will continue 100 times, until the end of the text file.

12. Have fun!!
13.   
