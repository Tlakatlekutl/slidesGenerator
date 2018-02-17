import os
from .config import *
from PIL import Image, ImageDraw


class BaseSlide():
    ext = DEFAULT_EXTENTION
    dir = '.'

    def create(self, name, show=False):
        im = Image.new(DEFAULT_IMAGE_MODE, (DEFAULT_SLIDE_WiDTH,
                                            DEFAULT_SLIDE_HIGHT), DEFAULT_IMAGE_BACKGROUND)
        d = ImageDraw.Draw(im)                                    
        self.modify(d)
        del d

        im.save(os.path.join(self.dir, str(name) + self.ext))
        if show:
            im.show()
        del im

    def set_directory(self, dir):
        self.dir = dir

    def modify(self, im):
        return im
