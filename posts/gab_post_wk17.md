### Connecting an ESP8266 to a Pi Over WiFi: A Few Options

Ok so I got to read my Grove GSR sensor with the ESP and send data to a web page via my local network. Now, the challenge is to send that data to a web page that can be accessed by another computer or microcontroller on a different home network.
There seems to be a couple options:

*1. IoT Platform*  
The first one is to use some sort of API/IoT platform like Pushing Box, Blynk or IFTTT. [Here's a list](https://geekflare.com/iot-platform-tools/#anchor-node-red) of such platforms.

*2. From scratch*
Another option is to build our own server from scratch with something like node.js. This seems to be Tim Ingoe's preferred method (in Making Things Talk chap 3). Perhaps more complex but we also would have more control.

Something we can do as well is to turn one of the ESP8266 into its own server that other devices can access (explanation [here](https://lastminuteengineers.com/creating-esp8266-web-server-arduino-ide/)). It still doesn't solve the problem of inter-home communication but perhaps something to look into.
