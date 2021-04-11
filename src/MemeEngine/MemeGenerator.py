"""MemeGenerator package."""
from PIL import Image, ImageDraw, ImageFont, UnidentifiedImageError
from random import randint
import os
import textwrap


class MemeGenerator:
    """MemeGenerator class for meme creation."""

    def __init__(self, output_dir):
        """Instanciate a MemeGenerator."""
        self.output_dir = output_dir
        try:
            os.mkdir(output_dir)
        except OSError:
            print("Creation of the directory %s failed, \
                  maybe was already present" % output_dir)
        else:
            print("Successfully created the directory %s " % output_dir)

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Create a meme With a Text.

        Arguments:
            img_path {str} -- the file location for the input image.
            text {str} -- the text for the quote.
            author {str} -- the fauthor for the quote.
            out_path {str} -- the desired location for the output image.
            width {int} -- The pixel width value. Default=None.
        Returns:
            str -- the file path to the output image.
        """
        try:
            img = Image.open(img_path)
        except UnidentifiedImageError:
            print("make_meme cannot open image")
            return False
        if width is not None:
            ratio = width/float(img.size[0])
            height = int(ratio*float(img.size[1]))
            img = img.resize((width, height), Image.NEAREST)

        if text is not None and author is not None:
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype(font='./_data/fonts/' +
                                      'LilitaOne-Regular.ttf',
                                      size=20)
            text = f'"{text}" - \n {author}'
            if len(text) > 30:
                lines = textwrap.wrap(text, width=40)
                y_text = 20
                for line in lines:
                    width, height = font.getsize(line)
                    draw.text((30, y_text), line,
                              font=font, fill='white')
                    y_text += height
            else:
                draw.text((randint(0, abs(width-200)),
                          randint(0, abs(height-100))),
                          text, font=font, fill='white')

        out_path = self.output_dir + '/img' + \
            str(randint(0, 1000000000)) + '.jpg'
        img.save(out_path)
        return out_path
