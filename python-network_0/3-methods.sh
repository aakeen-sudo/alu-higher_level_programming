#!/bin/bash
# This script sends an OPTIONS request to a URL and displays all HTTP methods the server accepts
curl -s -X OPTIONS -D - "$1" -o /dev/null | grep -i "^Allow:" | cut -d' ' -f2-
