#!/usr/bin/env bash
###
# Run from npm generate-api
###

Tempdir=$(mktemp -d)
Url="0.0.0.0:8000/openapi.json"

echo "Tempdir: $Tempdir"

if wget -q "${Url}" -O "${Tempdir}"/openapi.json;
then
    echo "Successfully downloaded openapi.json"
else
    echo "Failed to download openapi.json. Is the fastapi backend running?"
    exit 1
fi

docker run --rm --user=$(stat -c "%u:%g" $Tempdir) \
  -v "${Tempdir}":/local openapitools/openapi-generator-cli  generate \
  --type-mappings=Datetime=Date \
  -i /local/openapi.json \
  -g typescript-axios \
  -o /local/out/

rm -rf src/api/
mv -f "${Tempdir}"/out/ frontend/src/api/
rm -rf "${Tempdir}"
