#!/bin/bash
# Script that sends a JSON POST request to a URL
curl -sX POST -H "Content-Type: application/json" --data @"$2" "$1"
