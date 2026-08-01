#!/bin/bash
# This script sends a GET request to a URL, follows redirects, and displays the body only if the final response is a 200 status code
curl -s -L -o /tmp/response_body -w "%{http_code}" "$1" | grep -q "^200$" && cat /tmp/response_body
