#!/bin/bash
# This script sends a GET request to a URL and displays the body of the response only if the status code is 200
curl -s -o /tmp/response_body -w "%{http_code}" "$1" | grep -q "^200$" && cat /tmp/response_body
