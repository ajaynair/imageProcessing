# Heavily inspired from stackoverflow answers
# <this script> DIR 

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import re
import sys
import os

if len(sys.argv) <= 1:
  print('<this script> DIR')
  print('DIR: Directory with images')
  exit(1)

dir = sys.argv[1]

os.mkdir('hasText')
os.mkdir('hasNoText')

i = 0
for filename in os.listdir(dir): 
  print(i)
  i = i + 1

  print('Processing: ' + filename)

  try:
    filepath = os.path.join(dir, filename)
    text = str(pytesseract.image_to_string(Image.open(filepath)))
    if any(c.isalnum() for c in text):
      os.rename(filepath, os.path.join('hasText', filename))
    else:
      os.rename(filepath, os.path.join('hasNoText', filename))
  except Exception:
    pass
