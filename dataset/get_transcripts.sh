#!/usr/bin/env bash

SECONDS=0

#.txt file containing video IDs
File=Vid_Ids.txt
ids=$(cat $File)

# create output folder
mkdir -p transcript
cd transcript

# get transcript for each video and save it in the output dir as a WebVTT file
for id in $ids
do
   youtube_transcript_api "$id" ... --languages en --format webvtt > "$id".vtt
done

ELAPSED="$(($SECONDS / 3600))hrs $((($SECONDS / 60) % 60))min $(($SECONDS % 60))sec"

echo "Done! Elapsed time: $ELAPSED"



