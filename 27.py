import pdb
import sys
from Comp import Memmory
from Comp import get_input_prog
from prog import Prog
from point import point


def store_input(INPUTS):
    if INPUTS:
        return INPUTS.pop(0)
    else:
        return 0

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


def handle_input(INPUTS):
    if INPUTS:
        return INPUTS.pop(0)
    else:
        inpt = sys.stdin.readline().strip()
        if not inpt:
            tmp_input.append(0)
            return 0
        i = 0
        while i < len(inpt):
            if inpt[i] == '-':
                tmp_input.append(-1)
                i += 1
                INPUTS.append(-1)
            else:
                tmp_input.append(int(inpt[i]))
                INPUTS.append(int(inpt[i]))
            i += 1
        return INPUTS.pop(0)

def purge_inputs(inputs):
    while inputs:
        inputs.pop(0)

def get_max_score(name):
    with open(name, 'r') as f:
        return int(f.readline().strip())

def get_best_seq(name):
    seq = []
    with open(name, 'r') as f:
        inpt = f.read().strip()
        i = 0
        while i < len(inpt):
            if inpt[i] == '-':
                seq.append(-1)
                i += 1
            else:
                seq.append(int(inpt[i]))
            i += 1
    return seq

tmp_input = get_best_seq('bestseq.txt')

def main():
    arr = get_input_prog('26.txt')
    canvas = None
    max_score = get_max_score('maxscore.txt')
    INPUTS = get_best_seq('bestseq.txt')
    OUTPUTS = []
    score = 0
    score_arr = []
    to_exit = 'Resume'
    prog = Prog(arr)
    prog.set_value(0, 2)
    intcode = Memmory(prog, handle_input, print_output, INPUTS, OUTPUTS)
    while to_exit != 'Stop':
        to_exit = intcode.compute()
        if len(OUTPUTS) > 2282:
            if len(OUTPUTS)%3 == 0:
                canvas = Canvas(OUTPUTS)
                score = canvas.canvas[point(-1,0)]
                score_arr.append(score)
                print(score)
                if score >= 10200:
                    canvas.draw_field()
    score = max(score_arr)
    if score >= max_score:

        print(f'max_score::{max_score}')
        max_score = score
        with open('maxscore.txt', 'w') as f:
            f.write(f'{max_score}')
        with open('seq.txt', 'w') as f:
            f.write(f'{score}::')
            for elem in tmp_input:
                f.write(str(elem))
        with open('progstate.txt', 'w') as f:
            for key, value in prog.prog.items():
                f.write(f'{elem},')
        with open('out.txt', 'w') as f:
            for elem in OUTPUTS:
                f.write(f'{elem},')

if __name__ == '__main__':
    main()
