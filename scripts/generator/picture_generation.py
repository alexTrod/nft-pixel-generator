from PIL import Image
import random

class GenImage:

    filename = "generated_image"
    def __init__(self, *size):
        self.h, self.w = size

    def generates(self):
        # creates new image
        img = Image.new('RGB', (self.h, self.w))
        # add random pixels in the imge
        for pixel_h in range(self.h):
            for pixel_w in range(self.w):
                random_color_r = random.randint(0,255)
                random_color_g = random.randint(0,255)
                random_color_b = random.randint(0,255)

                img.putpixel((pixel_h,pixel_w), (random_color_r,random_color_g,random_color_b))

        random_nonce = random.randint(0, 100)
        img.save(f'{self.filename}_{random_nonce}.png')

        return img