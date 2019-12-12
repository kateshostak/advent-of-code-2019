import pdb
import itertools

INPUTS = []
OUTPUTS = []


class Memmory():
    OPCODE_TO_FUNC = {
            99: 'halt_',
            1: 'add_',
            2: 'mult_', 3: 'store_input',
            4: 'print_output',
            5: 'jump_if_true',
            6: 'jump_if_false',
            7: 'less_than',
            8: 'equals'
            }

    def __init__(self, arr):
        self.position = 0
        self.prog = list(arr)

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
        else:
            return self.prog[i]

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
        inpt = INPUTS.pop(0)
        ind = self.prog[self.position + 1]
        self.prog[ind] = int(inpt)
        self.position += 2
        return False

    def print_output(self, modes):
        i = self.get_value(self.position + 1, modes)
        OUTPUTS.append(i)
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

def find_res(n, arr, comp):
    for i in range(100):
        for j in range(100):
            arr[1] = i
            arr[2] = j
            res = comp.compute(arr)[0]
            if res == n:
                return i, j
    return -1, -1


def calculate_signal(mycomp, arr):
    max_output_signal = 0
    max_setting = []
    for setting in itertools.permutations([0, 1, 2, 3, 4], 5):
        output_signal = 0
        input_signal = 0
        for position in setting:
            INPUTS.append(position)
            INPUTS.append(input_signal)
            mycomp = Memmory(arr)
            mycomp.compute()
            input_signal = OUTPUTS.pop(0)
        output_signal = input_signal
        if output_signal > max_output_signal:
            max_output_signal = output_signal
            max_setting = setting
    print(max_setting)
    return max_output_signal


def day_7_part_1(mycomp, arr):
    return calculate_signal(mycomp, arr)


def get_input_prog():
    with open('13.txt') as f:
        prog = f.read().strip().split(',')
        arr = [int(elem) for elem in prog]
    return arr


def day_7_part_2(arr):
    max_output = 0
    output = 0
    for setting in itertools.permutations(range(5, 10), 5):
        amplifiers = make_amplifier_arr(5, arr)
        to_exit = 'Pause'
        first_input = [True]*5
        while to_exit != 'Stop':
            for i in range(5):
                inp = first_input[i]
                comp = amplifiers[i]
                if inp:
                    INPUTS.append(setting[i])
                    first_input[i] = False
                    if i == 0:
                        input_signal = 0
                        INPUTS.append(input_signal)
                    else:
                        output = OUTPUTS.pop(0)
                        INPUTS.append(output)
                else:
                    if not len(OUTPUTS):
                        to_exit = 'Stop'
                        purge_inputs()
                        break
                    else:
                        output = OUTPUTS.pop(0)
                        INPUTS.append(output)
                print(f'setting::{setting}, i::{i}, input::{INPUTS}, outputs::{OUTPUTS}')
                comp.compute()
        if output > max_output:
            max_setting = setting
            max_output = output

    return max_setting,  max_output

def purge_inputs():
    while len(INPUTS):
        INPUTS.pop(0)

def make_amplifier_arr(n, arr):
    return [Memmory(arr) for i in range(n)]


def main():
    arr = get_input_prog()
    #arr = [3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26, 27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99, 0, 0, 5]
    print(day_7_part_2(arr))


if __name__ == '__main__':
    main()
