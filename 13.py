import pdb
import itertools

INPUTS = []
OUTPUTS = []


class Memmory():
    OPCODE_TO_STEP = {
            99: 1,
            1: 4,
            2: 4,
            3: 2,
            4: 2,
            5: 0,
            6: 0,
            7: 4,
            8: 4
            }

    OPCODE_TO_FUNC = {
            99: 'halt_',
            1: 'add_',
            2: 'mult_',
            3: 'store_input',
            4: 'print_output',
            5: 'jump_if_true',
            6: 'jump_if_false',
            7: 'less_than',
            8: 'equals'
            }

    def compute(self, arr):
        self.position = 0
        self.prog = arr.copy()
        to_exit = False
        while not to_exit:
            params = self.prog[self.position]
            modes = params//100
            opcode = params % 100
            to_exit = self.execute(opcode, modes)
            self.position += self.step(opcode)
        return self.prog

    def execute(self, opcode, modes):
        func = Memmory.OPCODE_TO_FUNC[opcode]
        return self.__getattribute__(func)(modes)

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
        return False

    def mult_(self, modes):
        i = self.get_value(self.position + 1, modes % 10)
        j = self.get_value(self.position + 2, modes//10)
        k = self.prog[self.position + 3]
        self.prog[k] = i*j
        return False

    def store_input(self, modes):
        #inpt = input('Type input here: ')
        inpt = INPUTS.pop(0)
        ind = self.prog[self.position + 1]
        self.prog[ind] = int(inpt)
        return False

    def print_output(self, modes):
        i = self.get_value(self.position + 1, modes)
        #print(i)
        OUTPUTS.append(i)
        return False

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
        if i < j:
            self.prog[k] = 1
        else:
            self.prog[k] = 0

    def equals(self, modes):
        i = self.get_value(self.position + 1, modes % 10)
        j = self.get_value(self.position + 2, modes//10)
        k = self.prog[self.position + 3]
        if i == j:
            self.prog[k] = 1
        else:
            self.prog[k] = 0


def find_res(n, arr, comp):
    for i in range(100):
        for j in range(100):
            arr[1] = i
            arr[2] = j
            res = comp.compute(arr)[0]
            if res == n:
                return i, j
    return -1, -1


def calculate_signal(mycomp, prog):
    max_output_signal = 0
    max_setting = []
    for setting in itertools.permutations([0, 1, 2, 3, 4], 5):
        output_signal = 0
        input_signal = 0
        for position in setting:
            INPUTS.append(position)
            INPUTS.append(input_signal)
            mycomp.compute(prog)
            input_signal = OUTPUTS.pop(0)
        output_signal = input_signal
        if output_signal > max_output_signal:
            max_output_signal = output_signal
            max_setting = setting
    print(max_setting)
    return max_output_signal

def day_7_part_1(mycomp, arr):
    return calculate_signal(mycomp, arr)

def main():
    arr = []
    with open('13.txt') as f:
        prog = f.read().strip().split(',')
        for elem in prog:
            arr.append(int(elem))
    mycomp = Memmory()
    print(day_7_part_1(mycomp, arr))

if __name__ == '__main__':
    main()
