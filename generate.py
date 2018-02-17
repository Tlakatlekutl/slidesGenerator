#!/usr/bin/python3

from SlidesGenerator.titleslide import TitleSlide
from SlidesGenerator.contentslide import ContenTextSlide


import argparse

parser = argparse.ArgumentParser(description='Generate random slides')

parser.add_argument('--type', type=str, help='Set slides type', default='title')
parser.add_argument('-n', type=int, help='Generated slides count', default=1) 
parser.add_argument('-s', type=int, help='start from', default=1)
parser.add_argument('--show', help='Show slides after creating', type=bool, nargs='?',
                        const=True, default=False)
parser.add_argument('--dir', help='Output files', type=str, default=".")


args = vars(parser.parse_args())

gen_type = args['type']
if gen_type == 'title':
    slide = TitleSlide()
elif gen_type == 'content':
    slide = ContenTextSlide()
    

slide.set_directory(args['dir'])

for i in range(args['s'], args['n']+1):
    slide.create(i, show=args['show'])
   
    