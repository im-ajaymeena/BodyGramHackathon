#!/bin/bash

# Set the environment variables
export ORG_ID="org_2iYS3txeV95Z5efZF1nGmK"
export API_KEY="kCCyePRUJ1tylALFoXOuxZqIj94fGqnsuLc3LwgMnfy"
RIGHT_PHOTO_BASE64="$(base64 -i right.jpg)"
FRONT_PHOTO_BASE64="$(base64 -i front.jpg)"

curl -X POST "https://platform.bodygram.com/api/orgs/${ORG_ID}/scans" \
--header "Content-Type: text/plain" \
--header "Authorization: ${API_KEY}" \
--data @data.txt