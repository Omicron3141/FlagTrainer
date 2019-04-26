from PIL import Image
import os
from resizeimage import resizeimage


rawFolder = "raw"
processedFolder = "processed"

size = [384, 256]


for fn in os.listdir(rawFolder):
	if fn.endswith(".png"):
		name = os.path.join(rawFolder, fn)
		with open(name, 'r+b') as f:
			with Image.open(f) as image:
				print fn
				if image.size[0] >= size[0] and image.size[1] > size[1]:
					cover = resizeimage.resize_contain(image, size)
					new_im = Image.new("RGB", (size[0], size[1]))
					new_im.paste(cover)
					new_im.save(os.path.join(processedFolder, fn), image.format)