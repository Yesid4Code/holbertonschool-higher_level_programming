#!/bin/bash
# Script that displays the body of the response of a request.
curl -sX POST -d "email=hr@holbertonschool.com&subje
ct=I will always be here for PLD" "$1"
