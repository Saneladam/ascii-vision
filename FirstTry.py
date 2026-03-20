#!/usr/bin/env python3

# =============================================================================
# Authors:      Román García Guill
# Contact:      romangarciaguill@gmail.com
# Created:      Wed 18. Mar 2026
#
# Purpose:      Get an Image and create an Ascii from it
# =============================================================================

import sys
from pathlib import Path

import numpy as np
from PIL import Image

factor = 10

img = Image.open(Path(sys.argv[1]))
img = img.convert('L')
width, height = img.size
img = img.resize((width//factor, height//(2*factor)))
width, height = img.size

img = np.array(img)

ascii_chars = ('$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,"^`\'. ')

maximum = 0
for i in range(height):
    row = []
    for j in range(width):
        rel_shiny = len(ascii_chars) - 1 - int(img[i,j] / 255 * (len(ascii_chars) - 1))
        character = ascii_chars[rel_shiny]
        row.append(character)
    print("".join(row))

def main() -> None:
    pass

if __name__ == "__main__":
    main()

