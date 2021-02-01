#!/bin/bash

if [[ $1 = "stop" ]] || [[ $1 = 'k' ]] ;
then
    killall -9 dico.py
    echo Stoped
elif [[ $1 = "restart" ]] || [[ $1 = 'r' ]]
then
    killall -9 dico.py
    ./dico.py &>/dev/null &
    echo Restarted $(pidof dico.py)
elif [[ $1 = 'start' ]] || [[ $1 = 's' ]]
then
    ./dico.py &>/dev/null &
    echo Started $(pidof dico.py)
else
    echo "Usage: "
    echo "       run_in_background.sh r/restart  ----------   to restart the bot"
    echo "       run_in_background.sh s/start    ----------   to start the bot"
    echo "       run_in_background.sh k/stop     ----------   to stop the bot"
fi
