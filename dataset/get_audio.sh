#!/usr/bin/env zsh

SECONDS=0

#output directory
outputdir=../audio


# downloads audio files from the links in the nassvid.txt file
youtube-dl -o ${outputdir}/"%(title)s.%(ext)s" -x --audio-format wav  -a, --batch-file "nassvid.txt"

ELAPSED="$(($SECONDS / 3600))hrs $((($SECONDS / 60) % 60))min $(($SECONDS % 60))sec"

echo "Done! Elapsed time: $ELAPSED"
