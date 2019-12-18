import time
import pdb
from Comp import Memmory
from Comp import get_input_prog
from prog import Prog
from point import point


def store_input(INPUTS):
    return INPUTS.pop(0)


def print_output(i, OUTPUTS):
    OUTPUTS.append(i)


class Canvas():
    TILES = {
            0: ' ',
            1: '.',
            2: '#',
            3: '=',
            4: '*'
            }

    def __init__(self, arr):
        self.canvas = self.build_canvas(arr)
        self.columns = max(self.canvas)[0]
        self.rows = max(self.canvas, key=lambda elem: elem[1])[1]
        self.field = self.make_field()
        self.update_field(self.canvas)

    def build_canvas(self, arr):
        canvas = {}
        for i in range(0, len(arr), 3):
            tile = arr[i:i+3]
            x = tile[0]
            y = tile[1]
            type_ = tile[2]
            tile_point = point(x, y)
            if x < 0:
                canvas[tile_point] = type_
            else:
                canvas[tile_point] = Canvas.TILES[type_]
        return canvas

    def make_field(self):
        field = [[0 for _ in range(self.columns + 1)] for _ in range(self.rows + 2)]
        return field

    def update_field(self, canvas):
        for tile in canvas:
            self.field[tile.y][tile.x] = canvas[tile]

    def draw_field(self):
        for i in range(self.rows + 2):
            for j in range(self.columns + 1):
                if j == self.columns:
                    print(self.field[i][j])
                else:
                    print(self.field[i][j], end='')

    def draw_canvas(self, arr):
        canvas = self.build_canvas(arr)
        self.update_field(canvas)
        self.draw_field()

def main():
    arr = get_input_prog('26.txt')
    prog = Prog(arr)

    INPUTS = []
    OUTPUTS = []
    prog.set_value(0, 2)
    intcode = Memmory(prog, input, print_output, INPUTS, OUTPUTS)

    to_exit = 'Resume'
    canvas = None
    i = 0
    while to_exit != 'Stop':

        to_exit = intcode.compute()

        if to_exit == 'Input':
            if not canvas:
                canvas = Canvas(OUTPUTS)
                canvas.draw_field()
            else:
                canvas.draw_canvas(OUTPUTS)
        #print('\r', flush=True)
            #time.sleep(0.1)

if __name__ == '__main__':
    main()
