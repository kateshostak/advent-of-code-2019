import pdb
from collections import namedtuple
from Comp import Memmory
from Comp import get_input_prog
from prog import Prog
from point import point

def store_input(INPUTS):
    return INPUTS.pop(0)


def print_output(i, OUTPUTS):
    OUTPUTS.append(i)


class Robot():
    DIRECTIONS = ['up', 'rigth', 'down', 'left']
    def __init__(self, start):
        self.painting = {}
        self.position = point(*start)
        self.painting[self.position] = 0
        self.direction = 0

    def paint(self, color):
        self.painting[self.position] = color

    def step(self, turn):
        self.change_direction(turn)
        direction = Robot.DIRECTIONS[self.direction]
        if direction == 'up':
            self.step_up()
        elif direction == 'down':
            self.step_down()
        elif direction == 'rigth':
            self.step_right()
        elif direction == 'left':
            self.step_left()

    def change_direction(self, turn):
        if turn == 1:
            self.direction += 1
        else:
            self.direction -= 1
        self.direction %= len(Robot.DIRECTIONS)

    def step_up(self):
        y = self.position.y + 1
        x = self.position.x
        self.position = point(x, y)

    def step_down(self):
        y = self.position.y - 1
        x = self.position.x
        self.position = point(x, y)

    def step_right(self):
        x = self.position.x + 1
        y = self.position.y
        self.position = point(x, y)

    def step_left(self):
        x = self.position.x - 1
        y = self.position.y
        self.position = point(x, y)

    def get_color(self):
        if self.position in self.painting:
            return self.painting[self.position]
        else:
            return 0

def main():
    INPUTS = []
    OUTPUTS = []
    arr = get_input_prog('22.txt')
    prog = Prog(arr)
    intcode = Memmory(prog, store_input, print_output, INPUTS, OUTPUTS)
    start = [0, 0]
    robot = Robot(start)
    to_exit = 'Pause'
    while to_exit != 'Stop':
        current_color = robot.get_color()
        INPUTS.append(current_color)
        to_exit = intcode.compute()
        if OUTPUTS:
            color = OUTPUTS.pop(0)
        else:
            break
        to_exit = intcode.compute()
        direction = OUTPUTS.pop(0)
        robot.paint(color)
        robot.step(direction)

    print(len(robot.painting))
if __name__ == '__main__':
    main()
