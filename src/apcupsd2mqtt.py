#!/usr/bin/env python3                                                                                  my.py                                                                                                      #!/usr/bin/env python3
import subprocess
import time
import paho.mqtt.client as mqtt
import json
import os

# ----- USER CONFIG -----

# MQTT CONFIG
MQTT_BROKER =  os.environ.get('MQTT_BROKER')
MQTT_PORT = os.environ.get('MQTT_PORT')
MQTT_TOPIC_PREFIX =  os.environ.get('MQTT_TOPIC_PREFIX')
MQTT_KEEPALIVE_INTERVAL = int( os.environ.get('MQTT_KEEPALIVE_INTERVAL') )

# OTHER CONFIG
POLLING_INTERVAL = 15

# ----- END CONFIG -----

mc = mqtt.Client()
mc.connect(MQTT_BROKER, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)

while True:
    # Fetch the apcupsd status output
    OUTPUT = subprocess.run(['apcaccess'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()

    #create a dictionary from teh output of the apcaccess command
    d = dict()
    for item in OUTPUT.splitlines():
        s = item.split(":")
        k = s[0].strip()
        v = s[1].strip()
        d[k] = v

    #do some adjustment to get numeric data

    d["LINEVnum"] = float( d["LINEV"].split(" ")[0] )
    d["LOADPCTnum"] = float( d["LOADPCT"].split(" ")[0] )
    d["BCHARGEnum"] = float( d["BCHARGE"].split(" ")[0] )
    d["TIMELEFTnum"]  = float( d["TIMELEFT"].split(" ")[0] )
    d["BATTVNum"] = float( d["BATTV"].split(" ")[0] )
    d["NOMPOWERnum"] = float( d["NOMPOWER"].split(" ")[0] )
    d["WATTnum"]  = (float(d["LOADPCTnum"]) / 100.0) * int(d["NOMPOWERnum"])

    #serialize the dictionary as a JSON
    jsonPayload = json.dumps(d, indent=2)
    
    # Publish message to MQTT Topic 
    mc.publish(MQTT_TOPIC_PREFIX + "/data", jsonPayload)

    #mqtt client loop (multithread in python is miserable)
    mc.loop()

    time.sleep(POLLING_INTERVAL)