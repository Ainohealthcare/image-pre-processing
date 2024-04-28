import os
from PIL import Image

imagedir = os.path.join(os.getcwd(), 'images')
outputdir = os.path.join(os.getcwd(), 'output')

OUT_SIZE = 512
MIN_RATIO = 0.8
MAX_RATIO = 1.25

def image_filter(f):
  (width, height) = f.size
  return (width >= OUT_SIZE) and (height >= OUT_SIZE) and (width >= MIN_RATIO * height) and (width <= MAX_RATIO * height)

if not os.path.exists(outputdir):
  os.mkdir(outputdir)

for filename in os.listdir(imagedir):
  with Image.open(os.path.join(imagedir, filename), 'r') as f:
    if image_filter(f):
      f_resized = f.resize((OUT_SIZE, OUT_SIZE))
      f_resized.save(os.path.join(outputdir, filename), 'JPEG')

# tests
for filename in os.listdir(outputdir):
  with Image.open(os.path.join(outputdir, filename), 'r') as f:
      assert f.width == OUT_SIZE and f.height == OUT_SIZE