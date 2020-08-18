#!/bin/bash
# Script that displays the body of the response of a request changing the HEADER.
curl -sH "X-HolbertonSchool-User-Id: 98" "$1"
