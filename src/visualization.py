from src.Entities.labyrinth import Labyrinth
from src.Entities.labyrinth import Cell
from src.Labyrinth_generation.general_generation_methods import update_cells

def write_svg(labyrinth, filename):
    aspect_ratio = labyrinth.width_ / labyrinth.height_
    padding = 10
    height = 500
    width = int(height * aspect_ratio)
    # Scaling factors mapping maze coordinates to image coordinates
    scy, scx = height / labyrinth.height_, width / labyrinth.width_
    def write_wall(ww_f, ww_x1, ww_y1, ww_x2, ww_y2):
        """Write a single wall to the SVG image file handle f."""

        print('<line x1="{}" y1="{}" x2="{}" y2="{}"/>'
              .format(ww_x1, ww_y1, ww_x2, ww_y2), file=ww_f)

    # Write the SVG image file for maze
    with open(filename, 'w') as f:
        # SVG preamble and styles.
        print('<?xml version="1.0" encoding="utf-8"?>', file=f)
        print('<svg xmlns="http://www.w3.org/2000/svg"', file=f)
        print('    xmlns:xlink="http://www.w3.org/1999/xlink"', file=f)
        print('    width="{:d}" height="{:d}" viewBox="{} {} {} {}">'
              .format(width + 2 * padding, height + 2 * padding,
                      -padding, -padding, width + 2 * padding, height + 2 * padding),
              file=f)
        print('<defs>\n<style type="text/css"><![CDATA[', file=f)
        print('line {', file=f)
        print('    stroke: #000000;\n    stroke-linecap: square;', file=f)
        print('    stroke-width: 5;\n}', file=f)
        print(']]></style>\n</defs>', file=f)
        # Draw the "South" and "East" walls of each cell, if present (these
        # are the "North" and "West" walls of a neighbouring cell in
        # general, of course).
        for x in range(labyrinth.width_):
            for y in range(labyrinth.height_):
                if self.cell_at(x, y).walls['S']:
                    x1, y1, x2, y2 = x * scx, (y + 1) * scy, (x + 1) * scx, (y + 1) * scy
                    write_wall(f, x1, y1, x2, y2)
                if self.cell_at(x, y).walls['E']:
                    x1, y1, x2, y2 = (x + 1) * scx, y * scy, (x + 1) * scx, (y + 1) * scy
                    write_wall(f, x1, y1, x2, y2)
        # Draw the North and West maze border, which won't have been drawn
        # by the procedure above.
        print('<line x1="0" y1="0" x2="{}" y2="0"/>'.format(width), file=f)
        print('<line x1="0" y1="0" x2="0" y2="{}"/>'.format(height), file=f)
        print('</svg>', file=f)