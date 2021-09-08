#!/usr/bin/env bash

set -euo pipefail

mkdir -p original

while IFS=";" read -r file line; do
  file=$(sed -e 's/^"//' -e 's/"$//' <<<"$file")
  line=$(sed -e 's/^"//' -e 's/"$//' <<<"$line")
  file=${file%.*}
  echo $file
  echo $line
  if [ "$file" = "0" ] || [ "$file" = "200" ]; then
    continue
  fi
  if [ ! -e original/${file}.wav ]; then
    echo "Missing wav"
    curl -L --retry 30 --get --fail --data-urlencode "text=$line" -o original/${file}.wav "https://glados.c-net.org/generate"
  fi
done < ../sound_list.csv
