#!/bin/bash
# Script that displays all HTTP methods the sever will accept.
curl -sI "$1" | grep Allow: | cut -d " " -f1 --complement
