# Start the first process
echo "Starting apcupsd"
/sbin/apcupsd
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start apcupsd: $status"
  exit $status
fi

echo "Waiting... for apcupsd to get ready"
sleep 10


# Start the second process (this is a blocking script...)
echo "Starting Python infinite loop to mqtt"
python3 apcupsd2mqtt.py