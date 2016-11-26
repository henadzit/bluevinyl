#!/bin/sh

LOG_FILE=/home/pi/main.log
BLUEAGENT_LOG=/home/pi/blueagent.log

echo "Started $(date)" >> $LOG_FILE

sleep 30 && pulseaudio --start

echo "Loading PA modules" >> $LOG_FILE

pacmd load-module module-ladspa-sink sink_name=bluevinyl master=alsa_output.usb-0d8c_C-Media_USB_Headphone_Set-00-Set.analog-stereo plugin=vynil_1905 label=vynil control=1940,33,0,0.5,0.5

pacmd load-module module-ladspa-sink sink_name=bluevinyl_valve master=alsa_output.usb-0d8c_C-Media_USB_Headphone_Set-00-Set.analog-stereo plugin=valve_1209 label=valve control=1,1
pacmd load-module module-ladspa-sink sink_name=bluevinyl_valve master=alsa_output.usb-0d8c_C-Media_USB_Headphone_Set-00-Set.analog-stereo plugin=valve_1209 label=valve control=1,1


# echo "Starting blueagent" >> $LOG_FILE
# /home/pi/blueagent5.py >> $BLUEAGENT_LOG  &

echo "Script finished" >> $LOG_FILE
