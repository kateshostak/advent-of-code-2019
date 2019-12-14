import pdb
import itertools

INPUTS = []
OUTPUTS = []

def store_input(i):
    return INPUTS.pop(0)

def print_output(i):
    OUTPUTS.append(i)

class Memmory():
    OPCODE_TO_FUNC = {
            99: 'halt_',
            1: 'add_',
            2: 'mult_', 3: 'store_input',
            4: 'print_output',
            5: 'jump_if_true',
            6: 'jump_if_false',
            7: 'less_than',
            8: 'equals',
            9: 'change_base'
            }

    def __init__(self, arr, inpt, outpt):
        self.position = 0
        self.base = 0
        self.prog = list(arr)
        self.print_ = outpt
        self.input_ = inpt

    def compute(self):
        to_exit = False
        while not to_exit:
            params = self.prog[self.position]
            modes = params//100
            opcode = params % 100
            to_exit = self.execute(opcode, modes)
        if opcode == 99:
            return 'Stop'
        elif opcode == 4:
            return 'Pause'

    def execute(self, opcode, modes):
        func = Memmory.OPCODE_TO_FUNC[opcode]
        return getattr(self, func)(modes)

    def step(self, opcode):
        return Memmory.OPCODE_TO_STEP[opcode]

    def get_value(self, i, mode):
        if mode == 0:
            ind = self.prog[i]
            return self.prog[ind]
        elif mode == 1:
            return self.prog[i]
        elif mode == 2:
            ind = self.prog[i] + self.base
            return self.prog[ind]

    def halt_(self, modes):
        return True

    def add_(self, modes):
        i = self.get_value(self.position + 1, modes % 10)
        j = self.get_value(self.position + 2, modes//10)
        k = self.prog[self.position + 3]
        self.prog[k] = i + j
        self.position += 4
        return False

    def mult_(self, modes):
        i = self.get_value(self.position + 1, modes % 10)
        j = self.get_value(self.position + 2, modes//10)
        k = self.prog[self.position + 3]
        self.prog[k] = i*j
        self.position += 4
        return False

    def store_input(self, modes):
        inpt = self.input_()
        ind = self.prog[self.position + 1]
        self.prog[ind] = int(inpt)
        self.position += 2
        return False

    def print_output(self, modes):
        i = self.get_value(self.position + 1, modes)
        self.print_(i)
        self.position += 2
        return True

    def jump_if_true(self, modes):
        i = self.get_value(self.position + 1, modes % 10)
        j = self.get_value(self.position + 2, modes//10)
        if i:
            self.position = j
        else:
            self.position += 3
        return False

    def jump_if_false(self, modes):
        i = self.get_value(self.position + 1, modes % 10)
        j = self.get_value(self.position + 2, modes//10)
        if not i:
            self.position = j
        else:
            self.position += 3
        return False

    def less_than(self, modes):
        i = self.get_value(self.position + 1, modes % 10)
        j = self.get_value(self.position + 2, modes//10)
        k = self.prog[self.position + 3]
        self.position += 4
        if i < j:
            self.prog[k] = 1
        else:
            self.prog[k] = 0
        return False

    def equals(self, modes):
        i = self.get_value(self.position + 1, modes % 10)
        j = self.get_value(self.position + 2, modes//10)
        k = self.prog[self.position + 3]
        self.position += 4
        if i == j:
            self.prog[k] = 1
        else:
            self.prog[k] = 0

        return False

    def change_base(self, modes):
        i = self.get_value(self.position + 1,modes)
        self.base += i
        return False


def get_input_prog():
    with open('17.txt') as f:
        prog = f.read().strip().split(',')
        arr = [int(elem) for elem in prog]
    return arr


def main():
    arr = [3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26, 27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99, 0, 0, 5]
    arr = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
    arr = [1102,34915192,34915192,7,4,7,99,0]
    #arr = [104,1125899906842624,99]
    #arr = get_input_prog()
    inpt = input
    outpt = print
    mycomp = Memmory(arr, inpt, outpt)
    mycomp.compute()


if __name__ == '__main__':
    main()
