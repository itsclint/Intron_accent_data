#!/usr/bin/env zsh

#output directory
outputdir=../audio


# downloads audio files from the links in the nassvid.txt file
youtube-dl -o ${outputdir}/"%(title)s.%(ext)s" -x --audio-format wav  -a, --batch-file "nassvid.txt"
