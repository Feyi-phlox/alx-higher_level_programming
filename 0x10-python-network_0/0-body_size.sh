#!/bin/bash
# This script sends a request to a URL and displays the size
curl -sI "$1" | grep -i 'content-length' | awk '{print $2}'
