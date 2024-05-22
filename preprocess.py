import os
from PIL import Image

image_dir = os.path.join(os.getcwd(), 'output')
output_dir = os.path.join(os.getcwd(), 'processed_output')

OUT_SIZE = 512

def image_filter(f):
  (width, height) = f.size
  return (width >= OUT_SIZE) and (height >= OUT_SIZE) 

def image_process(f):
  return f.crop(calc_center(f.size)).resize((OUT_SIZE, OUT_SIZE))

# return area of processed image
def calc_center(size):
  (width, height) = size
  if (width > height):
    left = (width - height) / 2
    right = (width + height) / 2
    return (left, 0, right, height)
  else:
    top = (height - width) / 2
    bottom = (height + width) / 2
    return (0, top, width, bottom)

# create output folder
if not os.path.exists(output_dir):
  os.mkdir(output_dir)

# process image 
for filename in os.listdir(image_dir):
  file_path = os.path.join(image_dir, filename)
  try:
    with Image.open(file_path, 'r') as f:
      if image_filter(f):
        f_resized = image_process(f)
        # Convert to RGB if not already in RGB
        if f_resized.mode != 'RGB':
          f_resized = f_resized.convert('RGB')
        f_resized.save(os.path.join(output_dir, filename), 'JPEG')
  except Exception as e:
      print(f"Error processing {filename}: {e}")
  

# tests
for filename in os.listdir(output_dir):
  with Image.open(os.path.join(output_dir, filename), 'r') as f:
      assert f.width == OUT_SIZE and f.height == OUT_SIZE