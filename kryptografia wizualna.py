import random
from PIL import Image


def generate_shares(image_path):
    image = Image.open(image_path).convert('1')
    width, height = image.size
    width = width
    share1 = Image.new('1', (width * 2, height))
    share2 = Image.new('1', (width * 2, height))

    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            if pixel:
                if random.randint(0, 1):
                    share1.putpixel((2 * x, y), 1)
                    share1.putpixel((2 * x + 1, y), 0)

                    share2.putpixel((2 * x, y), 0)
                    share2.putpixel((2 * x + 1, y), 1)
                else:
                    share1.putpixel((2 * x, y), 0)
                    share1.putpixel((2 * x + 1, y), 1)

                    share2.putpixel((2 * x, y), 1)
                    share2.putpixel((2 * x + 1, y), 0)
            else:
                if random.randint(0, 1):
                    share1.putpixel((2 * x, y), 1)
                    share1.putpixel((2 * x + 1, y), 0)

                    share2.putpixel((2 * x, y), 1)
                    share2.putpixel((2 * x + 1, y), 0)
                else:
                    share1.putpixel((2 * x, y), 0)
                    share1.putpixel((2 * x + 1, y), 1)

                    share2.putpixel((2 * x, y), 0)
                    share2.putpixel((2 * x + 1, y), 1)

    return share1, share2


def combine_shares(share1, share2):
    width, height = share1.size

    combined_image = Image.new('1', (width, height))

    for x in range(width):
        for y in range(height):
            pixel1 = share1.getpixel((x, y))
            pixel2 = share2.getpixel((x, y))

            combined_image.putpixel((x, y), pixel1 ^ pixel2)

    return combined_image


input_image_path = 'obrazek.png'

share1, share2 = generate_shares(input_image_path)

share1.save('share1.bmp')
share2.save('share2.bmp')

combined_image = combine_shares(share1, share2)

combined_image.save('combined_image.bmp')
