#!/usr/bin/env python

import inkex

from lxml import etree

def draw_dot(r, cx, cy, width, fill, parent):
    style = { 'stroke': 'none', 'fill': fill }
    dot_attribs = {'style': str(inkex.styles.Style(style)),
                    'cx':str(cx), 'cy':str(cy), 
                    'r':str(r)}
    etree.SubElement(parent, 'circle', dot_attribs )


class DotGrid(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)
        self.arg_parser.add_argument("--dot_diameter",
                        action="store", type=float, 
                        dest="dot_diameter", default=0.3,
                        help="Dot diameter")
        self.arg_parser.add_argument("--row_spacing",
                        action="store", type=float, 
                        dest="row_spacing", default=5.0,
                        help="Row spacing")
        self.arg_parser.add_argument("--col_spacing",
                        action="store", type=float, 
                        dest="col_spacing", default=5.0,
                        help="Col spacing")
        self.arg_parser.add_argument("--num_rows",
                        action="store", type=int, 
                        dest="num_rows", default=20,
                        help="Number of columns")
        self.arg_parser.add_argument("--num_cols",
                        action="store", type=int, 
                        dest="num_cols", default=20,
                        help="Number of columns")


    def effect(self):
        grid = etree.SubElement(self.svg.get_current_layer(), 'g')
        for row in range(0,self.options.num_rows):
            for col in range(0,self.options.num_cols):
                draw_dot(self.options.dot_diameter/2,
                                col*self.options.col_spacing,
                                row*self.options.row_spacing,
                                0,'rgb(100, 100, 100)' ,
                                grid)
        

        
if __name__ == '__main__':
    dot_grid = DotGrid()
    dot_grid.run()



