# APC USP daemon 2 MQTT

With this Container you will be able to grab the status of your APC UPS over USB and send to an MQTT Server

I startd this repo merging many other samples out (see credit).

I'll not provide an extensive set of instructions BTW you can simply take this repo, build your container and execute it!

The overall idea is to start the apcupsd with a startup script (under src folder), then the script start the python infinite loop.

The Python code requires some environment variable to connect to the right MQTT Broker and the right topic:

    # MQTT CONFIG
    MQTT_BROKER =  os.environ.get('MQTT_BROKER')
    MQTT_PORT = os.environ.get('MQTT_PORT')
    MQTT_TOPIC_PREFIX =  os.environ.get('MQTT_TOPIC_PREFIX')
    MQTT_KEEPALIVE_INTERVAL = int( os.environ.get('MQTT_KEEPALIVE_INTERVAL') )

Polling interval right now is hardcoded to 15 seconds.

    # OTHER CONFIG
    POLLING_INTERVAL = 15

# Execute
To exeute, the easiesst and less safe way to do is starting with privileges:

    docker run -it  --privileged --device /dev/usb/hiddev0 -v /var/run/dbus/system_bus_socket:/var/run/dbus/system_bus_socket apcd2mqtt

Don't know why just sharing the right device (i was searching with lsusb to find your UPS in your USB Bus) wasn't working.


# credit

As base Docker i'm using this: https://github.com/gregewing/apcupsd

I've just start a different script instead of running directly the apcups daemon:

CMD ["/sbin/apcupsd", "-b"]

The shell script was more or less copied from: https://github.com/hobbyquaker/apcupsd2mqtt

Python script inspiration came from : https://github.com/vandenberghev/apcupsd2mqtt/blob/master/apcupsd2mqtt.py