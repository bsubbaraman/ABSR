## Week 11

### Writing
Started a rough outline and an even rougher first draft [here](https://docs.google.com/document/d/1DP4beTx_-u9Q00OJScsCfrmkAIwGsHkycZZqXyLownU/edit#). I'm pretty excited to start writing. 

I'll share a reading list/early bib soon, or perhaps we can have a shared Zotero collection?

### Making
This week my objective was to have a microcontroller send and receive data over wifi and it looks like it'd be really complicated to do that without an ESP8266 board. The bad news is therefore that I couldn't work on it this week, the good news is that *they're coming*, after many customs delays, so that I'll be able to work on it starting Monday.

In the meantime, here's my plan of action for hardware:

#### Sending sensor data over wifi

implementing a few options: port forwarding (as in [this tutorial](https://www.circuitbasics.com/how-to-set-up-a-web-server-using-arduino-and-esp8266-01/)), [sensor hub](https://auth0.com/blog/javascript-for-microcontrollers-and-iot-part-2/) (looks really cool, need to look into more), [implement a web server on the microcontroller](https://www.r-bloggers.com/2020/02/alternatives-for-retrieving-sensor-data-from-arduino-compatible-microcontrollers-into-r/) using R and serve the data in a format like HTML, JSON or CSV.

**Materials**
microcontroller
sensor (ultrasound is the best I got right now)
ESP-01 or ESP-12E
resistors (1k, for pull up and down)
breadboard, jumper wires

**Steps**
1. Connect sensor and microncontroller. Ensure continous [data collection](https://www.creativebloq.com/how-to/create-an-app-that-collects-sensor-data).
2. Connect ESP-12E to the microcontroller
3. Program the ESP-12E
4. Connect microcontroller to home wifi
5. Then port forward
  
Tada! Your data is sent to a web page. Or do where do we want to send it?

#### Miniaturizing the sensor and the mc
For the **microcontroller** maybe an [ATtiny85](https://www.microchip.com/wwwproducts/en/ATtiny85)?
For the sensor... dunno yet.

#### Making the circuit
Once we have our mini parts, we'll have to make a mini circuit (maybe design and outsource the production, to ensure reliability).

#### CADing the shell
1. Ask Scott Rivers for Rhino license.
2. Start CADing a bracelet
3. Depending on the material, we can either use silicon molding or 3D printing to create it. 
  3.1. Hire Joshua as consultant.




