## Week 12

### thoughts
It's the end of the quarter! We all successfully survived and are ready to enter 2021, year of the Metal Ox according to the Chinese zodiac, which meaning I'm still trying to figure out. We're also exiting the rule of stern Saturn and entering forward-thinking Aquarius, so hopefully universal income can become a plausible political project.

After talking to Blair and meeting with Daniela this week, I've precised some of my thinking about how to frame this project so that it appears like a relevant contribution.

A few scattered thoughts:
**Focus on the design intervention**
The rest will flow from there. It shouldn't be a heavy historical contribution (which, according to Daniela, wouldn't even be considered by the DIS community) but a design one with a solid historical and critical *framing.* The [Pataphysical Software](https://doi-org.offcampus.lib.washington.edu/10.1145/3357236.3395526) paper might be a good inspiration in this regard.

**Methodological contribution**
Weaving the design inquiry with an autoethnography isn't something new. Audrey calls it "first-person research method" (autobiographical design being a big one - see [this workshop](http://clab.iat.sfu.ca/pubs/Lucero-DesignForOne-DIS2019.pdf) from last year's DIS). But our intervention is a little different in that it deals with the body -- something that is inherently biographical, so to speak.

Very plainly, the soma-narratives are doing two things:
1. Propose a more expressive way of representing biosensing data;
2. Propose a more "embodied" (?) way of engaging with text

In this regard, the choice of text is very important, and there might an occasion of weaving in the historical portion there. I've said this before but I think the story of the Gilbreths is an interesting one of scientific contribution co-opted by a capitalist agenda, which potentially all work within HCI is subject too (ours included). Where's the line between a shiny new gadget and a critical intervention? That in and of itself is an interesting research question.

Finally, the intimacy part of the project is relevant to the exploration of body and text but we need to think more about how it fits with the other parts. Perhaps because the experience of the body is inherently intimate and therefore autobiographical? Maybe that's the link.

**Build it fast, think after**
Enough said.

### stuff

**Resources**
[wristband podometer tutorial](https://www.instructables.com/How-to-Make-a-Wristband-Pedometer/) - very basic
[Arduino sport watch tutorial](https://www.instructables.com/DIY-Arduino-Watch-Sport-20/) - a lot more detailed! Very useful.
I also had an old Jawbone Up24 (used to be the Cadillac of sensing tech, now a failed startup) and found this [greaaat video](https://www.youtube.com/watch?v=sRjHAGsl6ws) from the [EEV blog](https://www.eevblog.com/) that takes one apart. Very useful to see how they sandwiched the wiring between the PCB and MC to make everything compact.

Based on the sport watch tutorial, here's a tentative outline of what needs to happen:

**Materials**
- battery 3.7v-240mA
- microcontroller
- ESP32
- sensor
- straps
- shell
- maybe a switch
- PCB

**Steps**

PROTOTYPE A
For a quick and dirty prototype

1. Connect all your components: sensor + mc + ESP
2. Send data over wifi (program the mc + ESP)
4. Process data
5. Send the txt file via email? (for now, until we get a mini printer)

PROTOTYPE B
Still breadboarding

1. Figure out the sensor situation. If it's GSR, then we need to think of a GSR that wouldn't necessarily need to be attached to your fingers because that might be distracting. Heart rate might be easier? GSR is just more fun/relevant to the project I find.
2. Connect all your components: sensor + mc + ESP
3. Send data over wifi (program the mc + ESP)
4. Process data
5. Send the txt to a printer that will print it

PROTOTYPE C
From breadboard to protoboard

1. 





