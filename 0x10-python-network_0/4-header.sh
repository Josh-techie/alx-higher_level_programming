#!/bin/bash
# This script sends a GET request to a URL and displays the body of the response

url="$1"
# -H adds a custom header to the request
# -s makes curl operate in silent mode
# -L follows redirects if any
curl -s -H "X-School-User-Id: 98" -v "$url"
