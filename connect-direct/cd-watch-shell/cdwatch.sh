#!/bin/bash

#set +vx
# Connect:Director Monitor

#    echo "Usage: cdwatch.sh"
#    echo "Usage: cdwatch.sh <interval in seconds> <iterations> <server port> <client port>"


INTERVAL=${1:-30}
ITER=${2:-1}
SERVER_PORT="${4:-1363}"
CLIENT_PORT="${5:-1364}"
LOGFILE=cdwatch-`date +%F-%H%M`.log

CNT=0

echo "=================================================" >> $LOGFILE

while [ $CNT -lt $ITER ]; do
    CNT=`expr $CNT + 1`
    echo "------------------ $CNT - [`date +%F_%H:%M:%S`] ------------------" >> $LOGFILE
    if [ -x /usr/bin/top ]; then
        top -b -d 0 -n 1 | head -n 40 >> $LOGFILE
        echo >> $LOGFILE
    else 
        vmstat -w >> $LOGFILE 2>/dev/null
        if [ $? -ne 0]; then
            vmstat >> $LOGFILE
        fi
        echo >> $LOGFILE
    fi

    ps_output=$(ps -ef | grep -v grep)

    # Define the process
    strings=("ndmsmgr" "ndmumgr" "ndmcmgr" "cdpmgr" "cdstatm")

    for str in "${strings[@]}"; do
        count=$(echo "$ps_output" | grep -c "$str")
        #ps -ef | grep ndmsmgr | grep " -p " | grep -v grep | head >> $LOGFILE

        echo "$str count:  $count" >> $LOGFILE

        if [ $count -gt 0 ]; then
            echo "$str list head:" >> $LOGFILE
            ps -efl | grep "$str" | grep -v grep | head -n5  >> $LOGFILE
        fi
        echo "" >> $LOGFILE
    done


    netstat_output=$(netstat -an)

    # Define the process
    strings=("ESTABLISHED" "TIME_WAIT" "CLOSE_WAIT" "SYN_RCVD")

    total=$(echo "$netstat_output" | grep -c ":${SERVER_PORT} ")
    echo "server sockets total count: $total" >> $LOGFILE
    for str in "${strings[@]}"; do
        count=$(echo "$netstat_output" | grep ":${SERVER_PORT} " | grep -c "$str")

        echo "     $str count:  $count" >> $LOGFILE
    done
    echo "" >> $LOGFILE

    total=$(echo "$netstat_output" | grep -c ":${CLIENT_PORT} ")
    echo "client sockets total count: $total" >> $LOGFILE
    for str in "${strings[@]}"; do
        count=$(echo "$netstat_output" | grep ":${CLIENT_PORT} " | grep -c "$str")

        echo "     $str count:  $count" >> $LOGFILE
    done
    echo "" >> $LOGFILE

    sleep $INTERVAL
done
