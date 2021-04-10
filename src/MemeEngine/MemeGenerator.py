from PIL import Image, ImageDraw, ImageFont
from random import randint
import os

class MemeGenerator:
    def __init__(self, output_dir):
        self.output_dir = output_dir
        try:
            os.mkdir(output_dir)
        except OSError:
            print ("Creation of the directory %s failed" % output_dir)
        else:
            print ("Successfully created the directory %s " % output_dir)

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Create a meme With a Text

        Arguments:
            img_path {str} -- the file location for the input image.
            out_path {str} -- the desired location for the output image.
            width {int} -- The pixel width value. Default=None.
        Returns:
            str -- the file path to the output image.
        """
        img = Image.open(img_path)

        if width is not None:
            ratio = width/float(img.size[0])
            height = int(ratio*float(img.size[1]))
            img = img.resize((width, height), Image.NEAREST)

        if text is not None and author is not None:
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype(font='./_data/fonts/LilitaOne-Regular.ttf', size=20)
            draw.text((randint(0,width), randint(0,height)), f'"{text}" - {author}', font=font, fill='white')
        
        out_path = self.output_dir + '/img' + str(randint(0, 1000000000)) + '.jpg'
        img.save(out_path)
        return out_path