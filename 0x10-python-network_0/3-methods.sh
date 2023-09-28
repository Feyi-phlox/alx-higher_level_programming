#!/bin/bash
# script sends OPTIONS request to a URL and displays the allowed HTTP methods
curl -s -I -X OPTIONS "$1"
