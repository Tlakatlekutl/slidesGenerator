from .baseslide import BaseSlide
from .config import DEFAULT_SLIDE_HIGHT, DEFAULT_SLIDE_WiDTH
from .blocks import SubtitleTextBlock, ContentTextBlock

class ContenTextSlide(BaseSlide):
    def modify(self, d):
        x = DEFAULT_SLIDE_WiDTH
        y = DEFAULT_SLIDE_HIGHT

        title = SubtitleTextBlock(0, x*0.3, 0, y*0.2)
        title.add(d)

        text = ContentTextBlock(0, x/3, y*0.3, y*0.3)
        text.add(d)



class ContenTextTwoSlide(BaseSlide):
    def modify(self, d):
        x = DEFAULT_SLIDE_WiDTH
        y = DEFAULT_SLIDE_HIGHT

        title = SubtitleTextBlock(0, x*0.3, 0, y*0.2)
        title.add(d)

        text = ContentTextBlock(0, x/3, y*0.3, y*0.3)
        text.add(d)
        text2 = ContentTextBlock(0, x/3, y*0.6, y*0.8)
        text2.add(d)