#!/bin/bash

# This script required face-recognition python library
# You can run pip install face-recognition
# Run it as <thisScript> <directoryWithImages>

function setup {
  mkdir withFace
  mkdir withoutFace  
}

function imageHasFace () {
  face_detection --cpus -1 $1 | grep "."
}

setup

for FILE in "$1"/*; do 
  imageHasFace $FILE; 
  if [ $? -eq 1 ] 
  then
    mv $FILE withoutFace/  
  else
    mv $FILE withFace/
  fi
done

