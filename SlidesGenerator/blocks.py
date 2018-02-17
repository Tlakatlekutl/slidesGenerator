from .config import *
import random
from PIL import ImageFont
from .textgenerator import text_gen

class BaseBlock():
    color = None
    min_w = 10
    max_w = DEFAULT_SLIDE_WiDTH
    min_h = 10
    max_h = DEFAULT_SLIDE_HIGHT

    def __init__(self, X0, X1, Y0, Y1):
        self.X = random.randint(X0, int(X1))
        self.Y = random.randint(Y0, int(Y1))

    def add(self, d):
        x0 = int(self.X)
        y0 = int(self.Y)
        min_w = int(self.min_w)
        min_h = int(self.min_h)
        max_w = int(self.max_w)
        max_h = int(self.max_h)
        
        x1 = min(x0 + random.randint(min_w, max_w), DEFAULT_SLIDE_WiDTH)
        y1 = min(y0 + random.randint(min_h, max_h), DEFAULT_SLIDE_HIGHT)
        
        d.rectangle([(x0, y0), (x1, y1)], fill=self.color)


class BaseTextBlock():
    color = TEXT_COLOR
    font_name = "arial.ttf"
    font_size = 15

    def __init__(self, X0, X1, Y0, Y1):
        self.X = random.randint(X0, int(X1))
        self.Y = random.randint(Y0, int(Y1))

    def add(self, d):
        x0 = int(self.X)
        y0 = int(self.Y)
        
        #font = ImageFont.truetype(self.font_name, self.font_size)
        font = ImageFont.truetype(self.font_name, self.font_size)

        text = self.get_text()

        if random.choice([True, False]):
            text = translit(text, 'ru')
        
        input_text = text.split()
        output_text = ''
        for w in input_text:
            (len_x, len_y) = d.textsize(output_text + w + ' ', font=font)

            if x0 + len_x < DEFAULT_SLIDE_WiDTH:
                output_text += (w + ' ')
            else:
                output_text += ('\n' + w+ ' ')

        d.text((x0, y0), output_text, font=font, fill=self.color)

    def get_text(self):
        return 'default_text'


class TitleBlock(BaseTextBlock):
    font_size=52
    def get_text(self):
        return text_gen()
    

class TitleTextBlock(BaseTextBlock):
    font_size=28
    def get_text(self):
        return text_gen(random.randint(1, 4))


class SubtitleTextBlock(BaseTextBlock):
    font_size=28
    def get_text(self):
        return text_gen()
    

class ContentTextBlock(BaseTextBlock):
    font_size=18
    def get_text(self):
        return text_gen(random.randint(8, 12))
    
    



