# **Home Automation**

This page shall document and present the home automation I am running.
Feel free to contact me with detailed questions.



# Server

Server
Lenovo ThinkCentre M93p Tiny Mini PC
(i5 4570T 2.9 GHz, 8GB, 256GB Samsung SSD, HD Graphics 4600, WLAN)

Running Debian and Docker Images
* Home Assistant - homeassistant/home-assistant:stable
* Unify Controller - jacobalberty/unifi:latest
* Portainer - portainer/portainer
* Grafana - grafana/grafana:latest
* Influx - influxdb:latest

# Home Assistant

Home Assistant is used as a Visualization and Automation Tool. https://www.home-assistant.io/
### General Setup
Screenshots
### Automations 



**Theme:**
[https://community.home-assistant.io/t/clear-theme/100464](https://community.home-assistant.io/t/clear-theme/100464)

**Additional enhancements used:**
| description | links| 
|--|--|
| Media Player Card | https://github.com/kalkih/mini-media-player |
| HACS |https://github.com/hacs/integration|
| Custom Header | https://github.com/maykar/custom-header |

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



# Network
Ubiquiti Unifi Security Gateway

Ubiquiti Unifi 8 Port Switch, POE

Ubiquiti Unifi Access Points, 3x

[https://www.ui.com/](https://www.ui.com/)

The Unifi Controller is running as a docker container.

# Other Components
A quick overview of some other devices and compontents that are integrated into the overall solution.

### Alpha Innotect Heatpump
[LWAV82R1/3-HSV9M1/3](https://www.alpha-innotec.de/endkunde/produkte/waermepumpen-produktkatalog/produktkatalog/detailseite/lwav82r13-hsv9m13.html) 
This also has a webserver/http interface. Integrated into Home Assistant via [https://github.com/Bouni/Home-Assistant-Luxtronik](https://github.com/Bouni/Home-Assistant-Luxtronik) 
It provides access to lots of data from the heatpump. Also controlling it would be possible, but I don't have the need to adapt anything regularly. 

### Zehnder Q350 
A [automated ventilation](https://www.zehnder-systems.de/l%C3%BCftungsger%C3%A4te-zehnder-comfounit/komfort-l%C3%BCftungsger%C3%A4te-mit-w%C3%A4rmer%C3%BCckgewinnung-zentral/komfort-l%C3%BCftungsger%C3%A4te-bis-800-m%C2%B3h/zehnder-comfoair-q350-tr) system that provides fresh air. No need to open windows to get fresh air into the house. Detecting air quality by CO2 sensor and triggering the different levels of ventilation.
One sensor in the living room, one sensor in the master bedroom.
Integration via KNX into Home Assistant.
Ventilation is lowered while away to save power and avoiding lowering the humidity unnecessarily. 

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

# Links

Following online resource were quite helpful for me:
https://community.home-assistant.io/
https://knx-user-forum.de



If you found this helpful, feel free to buy me a coffee:
buymeacoff.ee/t2JeMGFmx

