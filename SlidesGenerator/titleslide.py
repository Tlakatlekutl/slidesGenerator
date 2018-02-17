from PIL import ImageDraw
import random
from .baseslide import BaseSlide
from .config import DEFAULT_SLIDE_HIGHT, DEFAULT_SLIDE_WiDTH
from .blocks import TitleBlock, TitleTextBlock

class TitleSlide(BaseSlide):
    def modify(self, d):
        x = DEFAULT_SLIDE_WiDTH
        y = DEFAULT_SLIDE_HIGHT

        title = TitleBlock(0, x*0.3, 0, y/10)
        title.add(d)

        text = TitleTextBlock(0, x/3, y/2, y*0.6)
        text.add(d)
        