curl -X POST "https://platform.bodygram.com/api/orgs/${ORG_ID}/scans" \
--header "Content-Type: text/plain" \
--header "Authorization: ${API_KEY}" \
--data "{
  \"customScanId\": \"myFirstScan\",
  \"photoScan\": {
    \"age\": 29,
    \"weight\": 54000,
    \"height\": 1640,
    \"gender\": \"female\",
    \"frontPhoto\": \"${FRONT_PHOTO_BASE64}\",
    \"rightPhoto\": \"${RIGHT_PHOTO_BASE64}\"
  }
}"