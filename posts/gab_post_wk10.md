## Week 10 explorations

### Some stuff
<img src="images/generic supplies.jpg" width="60%">  
<img src="images/ultrasound_IIR.jpeg" width="60%">

Last week, I tried to make [this circuit](http://www.chris3000.com/wp-content/uploads/2010/02/Gsr02.jpg) but didn't have the necessary [op amps](https://www.digchip.com/datasheets/parts/datasheet/041/OP471A.php). Then I tried to have two microcontrollers talk to one another but needed WiFi-enabled microcontrollers (such as AF's [feather Huzzah](https://www.adafruit.com/product/2821) – out of stock).

Since I only have a bunch of generic parts, my option were limited. I found [a paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4179033/) that also uses a generic (40 kHz) ultrasound sensor to create a breath sensor. They use an IIR filter afterwards to isolate the breathing. I might be able to replicate the system in hacky way to have a decent enough breath sensor that's not in your face.  

[![A dc motor controlled with a generic ultrasound sensor](https://i.vimeocdn.com/video/1006982921_130x73.jpg)](https://vimeo.com/486495941)  Video of me controlling a dc motor with the ultrasound sensor. First step.
[![Overview of FIR and IIR filters](https://i.ytimg.com/vi/9yNQBWKRSs4/hq720.jpg?sqp=-oaymwEZCOgCEMoBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLAMomTOyT7Qdd3PeEGB1ZH9SRF9Jw)](https://www.youtube.com/watch?v=9yNQBWKRSs4)  
About IIR filters.

### Some thoughts



