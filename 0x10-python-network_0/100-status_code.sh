#!/bin/bash
# Script that displays the status code of the response
curl -sw "%{http_code}" -o /dev/null "$1"
