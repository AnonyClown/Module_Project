#!/bin/sh

echo "Starting crawler..."

CONTAINER_ALREADY_STARTED="CONTAINER_ALREADY_STARTED_PLACEHOLDER"
if [ ! -e $CONTAINER_ALREADY_STARTED ]; then
    touch $CONTAINER_ALREADY_STARTED
    echo "-- First container startup --"
	echo "if"
        mysql/main.py
else
    echo "-- Not first container startup --"
	echo "else"
fi
