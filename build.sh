#!/bin/bash -eu

end=$((SECONDS+300))
# keep pinging until sql is setup. Max timeout is 300 seconds.
while [ $SECONDS -lt $end ]; do
    ping -c 3 db
    rc=$?
    if [[ $rc -eq 2 ]] ; then
        echo "We connected to our db!"
        break
    fi
done
pip install -r requirements.txt
