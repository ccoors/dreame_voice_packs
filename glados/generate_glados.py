#!/usr/bin/env python3

import csv
import os

if not os.path.isdir("original"):
    os.mkdir("original")

with open("../sound_list.csv") as csvfile:
    reader = csv.reader(csvfile, quotechar='"')
    for row in reader:
        print(f"{row[0]}: {row[1]}")
        if row[0] in ("0.ogg", "200.ogg"):
            continue
        base, ext = os.path.splitext(row[0])
        if not os.path.exists(os.path.join("original", f"{base}.wav")):
            print("Missing file")
            cmd = f'curl -L --retry 30 --get --fail --data-urlencode "text={row[1]}" -o original/{base}.wav "https://glados.c-net.org/generate"'
            print(f"Running curl: {cmd}")
            os.system(cmd)
