# Start the first process
/sbin/apcupsd
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start apcupsd: $status"
  exit $status
fi

echo "Waiting... for apcupsd to get ready"
sleep 5

# Start the second process (this is a blocking script...)
/usr/local/bin/apcupsd2mqtt 