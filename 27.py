from Comp import Memmory
from Comp import get_input_prog
from prog import Prog
from point import point

def store_input(INPUTS):
    return INPUTS.pop(0)


def print_output(i, OUTPUTS):
    OUTPUTS.append(i)

class Canvas():
    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows

    def build_cnavas(self, arr):
       pass

    def draw_tile(self):
        pass

    def draw_canvas(self):
        for tile in self.canvas:
            pass

def build_canvas(INPUTS):
    canvas  = {}
    count = 0
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    for i in range(0, len(INPUTS)-3, 3):
        tile = INPUTS[i:i+3]
        x = tile[0]
        y = tile[1]
        type_ = tile[2]
        tile_point = point(x, y)
        canvas[tile_point] = type_
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y

    return canvas, max_x, max_y

def main():
    arr = get_input_prog('26.txt')
    prog = Prog(arr)

    INPUTS = []
    OUTPUTS = []
    prog.set_value(0, 2)
    intcode = Memmory(prog, input, print_output, INPUTS, OUTPUTS)

    to_exit = 'Resume'
    while to_exit != 'Stop':
        to_exit = intcode.compute()
        if to_exit == 'Input':
            canvas, columns, rows = build_canvas(OUTPUTS)
            print(columns, rows)

if __name__ == '__main__':
    main()
