from collections import Counter
from PIL import Image

def crop(img, x, y, width, height):
    left = x
    top  = y
    right = x + width
    bottom = y + height
    
    return img.crop((left, top, right, bottom))

image = Image.open('broken_qr.png')
image_size = image.size
kernel_size = 5 # 5x5 px

for h in range(image_size[1]):
    for w in range(image_size[0]):
        cropped_img = crop(
            image,
            w*kernel_size,
            h*kernel_size,
            kernel_size,
            kernel_size
        )        

        most_common_pixel = Counter(
            cropped_img.getdata()
        ).most_common(1)[0][0]
        
        fill = Image.new('1', [kernel_size]*2, most_common_pixel)
        image.paste(fill, (w*kernel_size, h*kernel_size))

image.save('fixed_qr.png')