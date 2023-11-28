# RaspicoW
Transfer of Data using  REYAX RYLR998 UART with Raspberry Pico W 
In this section we will experiment with two Raspberry Pico W boards which will send data across via REYAX RYLR998 UARTs. 
The Lora transfer protocol, which is supported by the two RYLR998 UARTs allows for much greater distances to be covered than WiFi. 
There are some limitations as of data transfer rates, but for small amouts of date (like sensors) Lora is very well suited. 

In this example no sensor is used, but it is read from a text file with random two-digits integer numbers ranging from 0 to 99. 
The program is kept very simple, such that beginners can start experimenting without a lot of effort.  


