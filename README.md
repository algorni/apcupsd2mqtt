# APC USP 2 MQTT

# Execute
docker run -it  --privileged --device /dev/usb/hiddev0 -v /var/run/dbus/system_bus_socket:/var/run/dbus/system_bus_socket apcd2mqtt



# credit

As base Docker i'm using this: https://github.com/gregewing/apcupsd

I've just start a different script instead of running directly the apcups daemon:

CMD ["/sbin/apcupsd", "-b"]

The shell script was more or less copied from: https://github.com/hobbyquaker/apcupsd2mqtt

Python script inspiration came from : https://github.com/vandenberghev/apcupsd2mqtt/blob/master/apcupsd2mqtt.py