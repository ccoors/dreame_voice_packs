# Steps to build

1. Run `./generate_glados.py`, this generates missing files in `original/`
2. Normalize the files and export as ogg (with ffmpeg or Audacity macros)
3. Run something like `for x in original/*.ogg; do oggdec $x -o x && oggenc x -o $(echo $x | sed -e 's/original/16k/') -b 100 --resample 16000; done`
4. Run `cd 16k && tar czf ../glados-en-16k.tar.gz *.ogg`
