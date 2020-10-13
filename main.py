import sys
from PIL import Image
from itertools import product
from constants import *

def main(filename):
    im = Image.open(filename)
    # get file size
    mx, my  = im.size

    # create html file
    with open('output/index.html', mode='w') as htmlf:
        # write html head tags
        for line in HTML_FORMAT_FIRST:
            htmlf.write(line)

        # write <p> blocks
        for x, y in product(range(0, mx, BIT_SIZE), range(0, my, BIT_SIZE)):
            write_data = DIV_FORMAT.format(x, y)
            htmlf.write(write_data)

        # write html tail tag
        for line in HTML_FORMAT_SECOND:
            htmlf.write(line)

    # create base css file
    with open('output/base.css', mode='w') as basef:
        basef.write(RESET_CSS)
        p_size = BIT_SIZE - SKIP_SIZE
        basef.write(BASE_STYLE.format(p_size, p_size))
        basef.write(BASE_P_STYLE.format(mx, my))

    # create css file
    with open('output/style.css', mode='w') as cssf:
        # check image per bits
        for x, y in product(range(0, mx - BIT_SIZE, BIT_SIZE), range(0, my - BIT_SIZE, BIT_SIZE)):
            r, g, b = 0, 0, 0

            # summarize near bits
            for nx, ny in product(range(BIT_SIZE), range(BIT_SIZE)):
                nr, ng, nb = im.getpixel((x+nx, y+ny))
                r, b, g = r + nr, b + nb, g + ng

            # calc RGB average
            r, g, b = r // (BIT_SIZE ** 2), g // (BIT_SIZE ** 2) , b // (BIT_SIZE ** 2)

            write_data = STYLE_FORMAT.format(x, y, RGB_FORMAT.format(r,g,b), x, y)
            cssf.write(write_data)


if __name__ == "__main__":
    filename = sys.argv[1]

    if len(sys.argv) > 2:
        BIT_SIZE = int(sys.argv[2])
    if len(sys.argv) > 3:
        SKIP_SIZE = int(sys.argv[3])

    main(filename)