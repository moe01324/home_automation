# **Home Automation**

This page shall document and present the home automation I am running.
Feel free to contact me with detailed questions.

# Server

Server
Lenovo ThinkCentre M93p Tiny Mini PC
(i5 4570T 2.9 GHz, 8GB, 256GB Samsung SSD, HD Graphics 4600, WLAN)

Running Debian and Docker Images
* Home Assistant - homeassistant/home-assistant:stable
* Unifi Controller - jacobalberty/unifi:latest
* Portainer - portainer/portainer
* Grafana - grafana/grafana:latest
* Influx - influxdb:latest

## Home Assistant
The "brain" of the home automation.

## Unifi Controller
Gives an nice UI to manage everything network related. Though I have to admit a little bit unstable when adding new stuff or making major changes. If everything runs, it runs flawless.
Also provides the VPN endpoint to connect from the outside.

## Portainer 
To manage the docker containers via a web UI.

## Grafana/Influx
For long term storage and visualisation of some data.
Is then shown within the HA user interface.

## Keepass
https://keepass.info/
To manage all the passwords. 

# Home Assistant

Home Assistant is used as a Visualization and Automation Tool. https://www.home-assistant.io/
## General Setup

Please mind that I adapt (play around) with the system all the time -> Most probably the screenshots do NOT match the config provided here.

### Screenshots Desktop

<img src="https://github.com/moe01324/home_automation/blob/master/pics/screens/screen1.png" width="800px" /> 

<img src="https://github.com/moe01324/home_automation/blob/master/pics/screens/screen1dark.png" width="800px" /> 

<img src="https://github.com/moe01324/home_automation/blob/master/pics/screens/screen2.png" width="800px" /> 

<img src="https://github.com/moe01324/home_automation/blob/master/pics/screens/screen3.png" width="800px" /> 

<img src="https://github.com/moe01324/home_automation/blob/master/pics/screens/screen4.png" width="800px" /> 

<img src="https://github.com/moe01324/home_automation/blob/master/pics/screens/screen5.png" width="800px" /> 

<img src="https://github.com/moe01324/home_automation/blob/master/pics/screens/screen6.png" width="800px" /> 

### Screenshots Mobile

Screenshots from my android mobile.

<img src="https://github.com/moe01324/home_automation/blob/master/pics/mobile/mobile1.jpg" height="500px" />      <img src="https://github.com/moe01324/home_automation/blob/master/pics/mobile/mobile2.jpg" height="500px" />

<img src="https://github.com/moe01324/home_automation/blob/master/pics/mobile/mobile3.jpg" height="500px" />      <img src="https://github.com/moe01324/home_automation/blob/master/pics/mobile/mobile4.jpg" height="500px" />

<img src="https://github.com/moe01324/home_automation/blob/master/pics/mobile/mobile5.jpg" height="500px" />      <img src="https://github.com/moe01324/home_automation/blob/master/pics/mobile/mobil6.jpg" height="500px" />

<img src="https://github.com/moe01324/home_automation/blob/master/pics/mobile/mobile7.jpg" height="500px" />      <img src="https://github.com/moe01324/home_automation/blob/master/pics/mobile/mobile8.jpg" height="500px" />

<img src="https://github.com/moe01324/home_automation/blob/master/pics/mobile/dark.jpg" height="500px" /> 


## Automations 

In my opinion a smart home is only really smart if most of the actions and adaptions happen automatically. Doing something via a stupid app is not smart.

* Coffee Machine
My coffee machine (https://xenia.coffee/) needs around 12-15 minutes to fully heat up. Therefore it gets switched on automatically in the morning. 6am during the week. 7am on the weekends. Runs for half an hour.

* Window Blinds
Rather complex setup...
Trying to allow to use as much sun energy during the colder months, and try to avoid heating the house up during the warmer months.
In addition some comfort features like closing the blinds in the bath at night.

* Lights 
All main lights are controlled via KNX motion detectors. Usually I dont need to use any light switches.

* Garden Irrigation
Can be scheduled via HA UI.

**Additional enhancements used:**
| description | links| 
|--|--|
| Media Player Card | https://github.com/kalkih/mini-media-player |
| HACS |https://github.com/hacs/integration|
| Custom Header | https://github.com/maykar/custom-header |
| Luxtronik Integration | https://github.com/Bouni/Home-Assistant-Luxtronik |

## Telegram Integration
A Telegram Bot is integrated into HA. Allows to send me notifications. E.g. if I leave the house and windows are still open. In case the smoke detectors are alarming etc.
Also I can send commands to the HA. Start the coffee machine if I am on my way back home.

<img src="https://github.com/moe01324/home_automation/blob/master/pics/mobile/telegram.jpg" height="500px" /> 

# KNX
Following KNX devices are used withing this installation.
Some of the automation logic is directly on the devices, others is supported by automations within Home Assistant.

| Device | Link | Image |
|--|--|--|
| MDT Glastaster II Smart BE-GT2TW.01 | https://www.mdt.de/Glastaster_Smart.html |  |
| MDT Jalousieaktoren | https://www.mdt.de/Jalousieaktoren.html |  |
| MDT Glastaster II Smart BE-GT2TW.01 | https://www.mdt.de/Glastaster_Smart.html |  |
| MDT CO2 Sensor | https://www.mdt.de/CO2_Sensor.html |  |
| MDT IP Router | https://www.mdt.de/Interfaces.html |  |
| MDT Presence Detector| https://www.mdt.de/Praesenzmelder.html |  |
| MDT Binary Input | https://www.mdt.de/Binaereingaenge.html |  |
| MDT Weather Station| https://www.mdt.de/Praesenzmelder.html |  |
| MDT Stromversorgung 640mA | https://www.mdt.de/Interfaces.html |  |
| ComfoConnect KNX C | https://www.zehnder-systems.de/produkte-und-systeme/komfortable-wohnraumlueftung/zehnder-comfoconnect-knx-c |  |

## KNX Switches
I really like the fully customizable MDT Glastaster.

Pretty default switch that controls lights and the coffee machine in the kitchen/dinner area.
<img src="https://github.com/moe01324/home_automation/blob/master/pics/misc/switch1.jpg" height="500px" />

Second page of the kitchen/dinner area. Controlling window blinds and showing the outside temperature.
<img src="https://github.com/moe01324/home_automation/blob/master/pics/misc/switch1.jpg" height="500px" />

Switch at the main door. Top left shows if any windows/doors are open. 
<img src="https://github.com/moe01324/home_automation/blob/master/pics/misc/switch1.jpg" height="500px" />

# Network
Using Ubiquitu Unifi components. Good performance/price point in my opinion.
[https://www.ui.com/](https://www.ui.com/)

Ubiquiti Unifi Security Gateway

2x Ubiquiti Unifi 8 Port Switch, POE

3x Ubiquiti Unifi Access Points

The Unifi Controller is running as a docker container.

# Other Components
A quick overview of some other devices and compontents that are integrated into the overall solution.

### Distribution Box
Houses all the fuses and KNX components.

<img src="https://github.com/moe01324/home_automation/blob/master/pics/misc/elektro.jpg" height="500px" />

### Alpha Innotect Heatpump
[LWAV82R1/3-HSV9M1/3](https://www.alpha-innotec.de/endkunde/produkte/waermepumpen-produktkatalog/produktkatalog/detailseite/lwav82r13-hsv9m13.html) 
This also has a webserver/http interface. Integrated into Home Assistant via [https://github.com/Bouni/Home-Assistant-Luxtronik](https://github.com/Bouni/Home-Assistant-Luxtronik) 
It provides access to lots of data from the heatpump. Also controlling it would be possible, but I don't have the need to adapt anything regularly. 


<img src="https://github.com/moe01324/home_automation/blob/master/pics/misc/wp.jpg" height="500px" />

### Zehnder Q350 
A [automated ventilation](https://www.zehnder-systems.de/l%C3%BCftungsger%C3%A4te-zehnder-comfounit/komfort-l%C3%BCftungsger%C3%A4te-mit-w%C3%A4rmer%C3%BCckgewinnung-zentral/komfort-l%C3%BCftungsger%C3%A4te-bis-800-m%C2%B3h/zehnder-comfoair-q350-tr) system that provides fresh air. No need to open windows to get fresh air into the house. Detecting air quality by CO2 sensor and triggering the different levels of ventilation.
One sensor in the living room, one sensor in the master bedroom.
Integration via KNX into Home Assistant.
Ventilation is lowered while away to save power and avoiding lowering the humidity unnecessarily. 

<img src="https://github.com/moe01324/home_automation/blob/master/pics/misc/kwl.jpg" height="500px" />

### Nuki Smartlock
An add-on [smart lock](https://nuki.io) to the front door. Bluethooth controlled (optional WIFI bridge available) and battery powered. Also comes with a keypad that is mounted outside the door.
No need to take a key with you any more. In addition I can provided temporary access by giving out temporary keycodes.
Works flawless. 
Integrated into Home Assistant (unfortunately the API does not provide a userID for an Unlock right now, [feature request](https://developer.nuki.io/t/add-user-to-bridge-http-api-notifications/151/10) is raised with Nuki. 

### Sonos One
One in the kitchen, one in the office. Just for some background music.
Integrated into Homeassistant.

### Alarm System
Presence/motion detectors and window sensors are used to detect any movement if the house is set to "away mode". 

### Garden Irrigation

A Raspberry Pi connect to some relays that are controlling Rainbird water valves.
Integrated into Homeassistant for automation and control.

<img src="https://github.com/moe01324/home_automation/blob/master/pics/misc/irrig1.jpg" height="500px" />

<img src="https://github.com/moe01324/home_automation/blob/master/pics/misc/irrig2.jpg" height="500px" />

<img src="https://github.com/moe01324/home_automation/blob/master/pics/misc/irrig3.jpg" height="500px" />

# Links

Following online resource were quite helpful for me:
https://community.home-assistant.io/
https://knx-user-forum.de



If you found this helpful, feel free to buy me a coffee:
https://www.buymeacoffee.com/t2JeMGFmx

