#!/bin/bash
# This script takes a URL, sends a request to it, and displays the size of the response body in bytes
curl -s -o /dev/null -w "%{size_download}\n" "$1"
